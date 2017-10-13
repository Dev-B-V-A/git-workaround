#! usr/bin/env python
import os
from subprocess import check_output 
from subprocess import call 
import argparse

def call_cmd (cmd):
    call (cmd)

def get_clone_dst_path ():
    return './dest'

def get_clone_addr ():
  parser = argparse.ArgumentParser (description="Clone git-repository")
  parser.add_argument ('--src', dest='src_clone', help='address git repository for cloning')
  result_parse_args = parser.parse_args ()
  return result_parse_args.src_clone

def init_workspace_dir ():
    clone_cmd = [ 'git', 'clone', get_clone_addr ()]
    call_cmd (clone_cmd)

def main ():
    init_workspace_dir ()

if __name__ == '__main__':
    main ()
