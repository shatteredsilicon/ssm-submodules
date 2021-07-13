#!/usr/bin/env python

import argparse
import configparser
import os
import sys
from subprocess import check_output, check_call, call, CalledProcessError


DEFAULT_BRANCH = 'main' # we can rewrite it in config
CONFIG_NAME = '.gitmodules-new'


config = configparser.ConfigParser()
config.read(CONFIG_NAME)


def get_list_of_submodules(c):
    submodules = []
    for s in config.sections():
        submodules_name = s.split('"')[1]
        submodules_info = dict(config.items(s))
        submodules_info['name'] = submodules_name
        submodules.append(submodules_info)
    return submodules




def switch_or_create_branch(path, branch):
    cur_branch = check_output(["git", "symbolic-ref", "--short", "HEAD"],
                                cwd=path)
    cur_branch = cur_branch.decode().strip()
    if cur_branch != branch:
        branches = check_output(["git", "show-ref", "--heads"], cwd=path)
        branches = [line.split("/")[-1]
                    for line in branches.decode().strip().split("\n")]
        if branch in branches:
            print(f"  Switch to branch: {branch} (from {cur_branch})")
        else:
            print(f"  Switch and create branch: {branch} (from {cur_branch}")
            check_call(["git", "checkout", "-b", branch,
                        "origin/" + branch], cwd=path)

def main():
    parser = argparse.ArgumentParser()

    rootdir = check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').strip()
    submodules = get_list_of_submodules(config)
    

    init = True
    build_client = False

    for submodule in submodules:
        path = os.path.join(rootdir, submodule["path"])
        if init:
            if not os.path.exists(os.path.join(rootdir, path)):
                check_call(['git', 'clone', '--depth', '3', '--no-single-branch', submodule["url"], path])
            else:
                print('Path for {} already exist'.format(submodule["name"]))
        call(["git", "pull", "--ff-only"], cwd=path)
        switch_or_create_branch(path, submodule['branch'])
        if submodule.get('default_branch', DEFAULT_BRANCH) != submodule['branch'] and submodule['component'] == 'client':
            build_client = True

    if not build_client:
        print('It don\'t need to rebuild client. We\'ll use dev-latest ')
    

main()