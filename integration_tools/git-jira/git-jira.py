#!/usr/bin/env python
import sys
import os
import getopt

actions = [
    "help", "list-actions", 
    "action=", "issue=", "dateFormat=", "type=", "summary=", "assignee=", 
    "label=", "step=", "resolution=", "comment=", "description=", "project=",
    "field=", "values=", "name=", "outputFormat="
]


arg_dict = {}


def _sanitize_args(args, accepted_args=None):
    accepted_args = accepted_args or []
    _args = ["action", "issue"] + accepted_args
    for key in args.keys():
        if key not in _args:
            del args[key]
    return args


def format_command(**kwargs):
    cmd = "--action %s " % kwargs["action"]
    for key in kwargs.keys():
        if key != "action":
            cmd += "--%s \"%s\" " % (key, kwargs[key])
    return cmd


def create_issue(args, accepted_args):
    failed_arg = ""
    if "project" not in args:
        failed_arg = "project"
    elif "type" not in args:
        failed_arg = "type"
    elif "summary" not in args:
        failed_arg = "summary"

    if failed_arg != "":
        print "--%s is required for createIssue command" % failed_arg
        sys.exit(0)
    return format_command(**_sanitize_args(args, accepted_args))


def get_comment_list(args, accepted_args):
    return format_command(**_sanitize_args(args))

def get_comments(args, accepted_args):
    return format_command(**_sanitize_args(args))    

def get_issue(args, accepted_args):
    return format_command(**_sanitize_args(args, accepted_args))

action_map = {
    "createIssue": { 
        "callback": create_issue,
        "accepted_args": ["project", "type", "summary", "parent", "assignee", "description", "comment"]
    },
    "getCommentList": {
        "callback": get_comment_list,
        "accepted_args": []
    },
    "getComments": {
        "callback": get_comments,
        "accepted_args": []
    },
    "getIssue": {
        "callback": get_issue,
        "accepted_args": ["outputFormat", "dateFormat"] 
    }
}

def list_actions():
    print """
Available commands and parameters:

    * getComments
    * getCommentList
        --dateFormat="yyyy-MM-dd"
    * getIssue
        --dateFormat="yyyy-MM-dd"
        --outputFormat="2"
    * createIssue
        --project=<some_project>    (required)
        --type=<some_type>          (required)
        --summary="some summary"    (required)
        --description="some desc"   (required)
        --label="some_label"
    * progressIssue
        --step="some_step"
        --resolution="Fixed"
        --comment="some comment"
"""


def usage():
    print """
Contacts JIRA to perform a variety of actions.

usage: git jira [-h, -l] -i issue_number -a action

OPTIONS:
    -h, --help                  show this help message
    -l, --list-actions          list the possible JIRA actions and their arguments
    -a, --action=<the_action>   the action to perform
    -i  --issue=<the_issue>     the JIRA issue that action will be performed on
""" 

def main():
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hli:a:", actions)
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(0)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-l", "--list-actions"):
            list_actions()
            sys.exit(0)
        elif o in ("-i"):
            arg_dict["issue"] = a
            issue = a
        elif o in ("-a"):
            arg_dict["action"] = a
        else:
            arg_dict[o.replace("--", "").replace("=", "")] = a
    if arg_dict["action"] != "createIssue" and "issue" not in arg_dict:
        print "You must proved a --issue in order to run that command."
        sys.exit(0)

    callback = action_map[arg_dict["action"]]["callback"]
    accepted_args = action_map[arg_dict["action"]]["accepted_args"]
    cmd = callback(arg_dict, accepted_args)
    print "calling: %s" % cmd
    os.system("jira %s" % cmd)

if __name__ == "__main__":
    main()
