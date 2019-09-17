#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Micropy-Stubs
Copyright (c) 2019 Braden Mars

Module for creating/updating stub package git branches.

"""


import subprocess as sp
from datetime import datetime
from pathlib import Path


def execute(cmd, **kwargs):
    check = kwargs.pop('check', True)
    if not kwargs.get('shell', None):
        cmd = cmd.split()
    proc = sp.run(cmd, capture_output=True, check=check, **kwargs)
    return proc


def get_change_count(root_path):
    _cmd = (f"git diff --cached --numstat {root_path} | wc -l")
    result = execute(_cmd, text=True, shell=True).stdout
    count = int(result.strip())
    return count


def branch_exists(ref_path):
    _cmd = f"git show-ref -q --heads '{ref_path}'"
    result = execute(_cmd, check=False, shell=True).returncode
    return not result


def create_package_branch(root_path, ref_path):
    _cmd = ("true | git mktree | xargs git commit-tree"
            f" | xargs git branch {ref_path}")
    execute(_cmd, shell=True)
    print("Creating new Stub Branch...")
    commit_msg = "chore({}): New Stub Branch"
    return update_package_branch(root_path, ref_path, commit_msg=commit_msg)


def update_package_branch(root_path, ref_path, commit_msg=None):
    now = datetime.now().strftime("%m/%d/%y")
    commit_msg = commit_msg or "chore({}): Package Updates"
    commit_msg = commit_msg.format(now)
    _cmd = (f"git commit-tree -p {ref_path} -m '{commit_msg}' "
            f"master:{root_path} | xargs git update-ref "
            f"refs/heads/{ref_path}"
            )
    try:
        execute(_cmd, shell=True)
    except sp.CalledProcessError as e:
        print("Failed to update package branch!")
        print(e)
        return None


def create_or_update_package_branch(root_path, name):
    ref_path = f"pkg/{name}"
    if Path(root_path).is_absolute():
        root_path = root_path.relative_to(Path.cwd())
    print(f"\nCREATING PACKAGE BRANCH: {root_path} - {ref_path}")
    if not branch_exists(ref_path):
        return create_package_branch(root_path, ref_path)
    print("Branch already exists, checking for changes...")
    if get_change_count(root_path):
        return update_package_branch(root_path, ref_path)
    print("Pushing branch...")
    execute(f"git push origin {ref_path}:{ref_path}", shell=True)
    print("No changes found, skipping...")
