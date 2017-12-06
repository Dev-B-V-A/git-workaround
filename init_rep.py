#! /usr/bin/env python
import os
from subprocess import check_output 
from subprocess import call 
import argparse

def call_cmd (cmd):
    call (cmd)

def get_clone_rep_name (src_str):
    return src_str[src_str.rfind('/') + 1: src_str.find('.git')]

def call_clone (args):
    cmd = ['git', 'clone']
    cmd += args
    call_cmd (cmd)

def get_clone_addr ():
  parser = argparse.ArgumentParser (description="Clone git-repository")
  parser.add_argument ('--src', dest='src_clone', help='address git repository for cloning')
  result_parse_args = parser.parse_args ()
  return result_parse_args.src_clone

def init_workspace_dir ():
#    address = get_clone_addr ()
    address = 'https://github.com/Dev-B-V-A/Python.git'
    clone_args = [ address ]
    call_clone (clone_args)
    return address

def get_mirror_dir_name (git_rep_path):
    return os.path.basename(git_rep_path) + '_MIR'

def create_mirror_rep (git_rep_path):
    clone_mir_args = [ '--mirror', git_rep_path, get_mirror_dir_name (git_rep_path)]
    call_clone (clone_mir_args)
    
def create_clone_by_mirror (git_mirror_path, clone_name):
    clone_args = [ git_mirror_path, clone_name ]
    call_clone (clone_args)

def create_md (git_mirror_path):
    clone_md_args = [ git_mirror_path, './md']
    call_clone (clone_md_args)

def create_test_md (mir_path):
    clone_test_args = [ mir_path, './test_md']
    call_clone (clone_test_args)

def add_remote_branches (test_md_path, address):
    remote_test_cmd = ['git', 'remote', 'add', 'test_md', test_md_path]
    remote_server_cmd = ['git', 'remote', 'add', 'server', address]
    call_cmd (remote_test_cmd)
    call_cmd (remote_server_cmd)
    call_cmd (['git', 'fetch', 'test_md'])
    call_cmd (['git', 'fetch', 'server'])

def configure_md (address):
    md_path = os.getcwd () + '/md'
    os.chdir (md_path)
    test_md_path = md_path + '/../test_md'
    add_remote_branches (test_md_path, address)

def main ():
    rep_address = init_workspace_dir ()
    rep_name = get_clone_rep_name (rep_address)
    rep_path = os.getcwd () + '/' + rep_name
    mir_path = os.getcwd () + '/' + get_mirror_dir_name (rep_path)
    create_mirror_rep (rep_path)
    create_md (mir_path)
    create_test_md (mir_path)
    configure_md (rep_address)

if __name__ == '__main__':
    main ()
