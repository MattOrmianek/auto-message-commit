import sys
from pydriller import Repository
import os
import subprocess

def fix_formatting(message):
    return message.replace('\\n', " \n ")

def create_commit_message():
    git_status = "auto"
    #get git status
    #get git diff
    #get git log

    response_from_git_status = subprocess.Popen(["git", "status"],stdout=subprocess.PIPE)
    git_status = fix_formatting(str(response_from_git_status.communicate()[0])[1:])

    response_from_git_diff = subprocess.Popen(["git", "diff"],stdout=subprocess.PIPE)
    git_diff = fix_formatting(str(response_from_git_diff.communicate()[0])[1:])

    response_from_git_log = subprocess.Popen(["git", "log"],stdout=subprocess.PIPE)
    git_log = fix_formatting(str(response_from_git_log.communicate()[0])[1:])

    print(f"git_status: {git_status}, git_diff: {git_diff}, git_log: {git_log}")

    # search for untracked files and print them
    untracked_files = []
    for line in git_status.splitlines():
        print(line)
        if line.startswith("Untracked files:"):
            untracked_files.append(line)
    print(untracked_files)

    return git_status

def last_commit_message():
    commit_message_list = []
    for commit in Repository("").traverse_commits():
        print(f"Commit {commit.hash}: {commit.msg} by {commit.author.name}")
        commit_message_list.append(commit.msg)
    return commit_message_list[-1]

commit_status = "not_ready"

if sys.argv[1] == "auto":
    print("Auto mode")
    commit_status = "ready"
    message = create_commit_message()

if sys.argv[1] == "manual":
    print("Manual mode")
    try:
        message = sys.argv[2]
        commit_status = "ready"
    except:
        print("No message")

if commit_status == "ready" and sys.argv[1] == "auto":
    print("Commiting from file: git commit -F file")
    print(f"Message: {message}")

if commit_status == "ready" and sys.argv[1] == "manual":
    print("Commiting from message: git commit -m message")
    new_message = message
    if last_commit_message() != new_message:
        print("Commiting")
        print(f"Message: {message}")