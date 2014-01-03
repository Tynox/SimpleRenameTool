#!/usr/bin/env python
# encoding:utf-8

"""
A Simple Rename Tool.
SRT: rename all files in the dictionary start from '0'.

author:Tynox
website:http://tarkrul.info

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""

import os
import sys
import getopt

version = 0.3

opts = None
args = None
fileList = None
dir = None
suffix = None
begin = None
name = None

def init():
    """
    Init and get arguments.
    """
    global opts
    global args
    
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvs:b:n:", ["--help", "--version", 
                                    "--suffix=", "--begin=", "--name="])
    except getopt.GetoptError as err:
        print str(err)
        getHelp()
        sys.exit()
    else:
        parseOpts()


def parseOpts():
    """
    parse opts and arguments
    """
    global dir
    global fileList
    global suffix
    global begin
    global name
    
    shouldExit = False
    
    # check options. If options is None, exit. 
    for o, a in opts:
        if o in ("-h", "--help"):       # get help
            getHelp()
            shouldExit = True
        elif o in ("-v", "--version"):  # show version
            showVersion()
            shouldExit = True
        elif o in ("-s", "--suffix"):   # set suffix
            suffix = a
        elif o in ("-b", "--begin"):    # set begin
            begin = int(a)
        elif o in ("-n", "--name"):     # specify a name
            name = a
            
    if shouldExit:
        sys.exit()
    
    # get dir
    if args is None or len(args) == 0:
        print "SRT:no source dictionary."
        sys.exit()
    dir = args[0]
    try:
        fileList = os.listdir(dir)
    except:
        print "SRT:wrong path"
        sys.exit()
    else:
        renameFiles()
    
 
def getHelp():
    """
    get tool help
    """
    showVersion()
    print "SRT: rename all files in the dictionary start from '0' by default."
    print "usage:rename_tool.py [-h|--help] [-v|--version] [[-s|--suffix] [-b|--begin] [-n|--name] <arg:dictionary>]"
    print "      -h --help      Show help"
    print "      -v --version   Show version"
    print "      -s --suffix    Set suffix. Rename files with the suffix"
    print "      -b --begin     Set begging file count: -b 1 --> start from 1"
    print "      -n --name      Set a specified name"
    
  
def showVersion():
    """
    show version
    """
    print "Simple Rename Tool version:v{0}".format(version)


def renameFiles():
    """
    rename files
    """
    # check fileList. if fileList is None, exit.
    if fileList is None:
        print "SRT:no files in the dictionary."
        sys.exit()
        
    print "----------"
        
    try:
        s = suffix if suffix is not None else ""
        b = begin if begin is not None else 0
        n = name if name is not None else ""
        for i, filename in enumerate(fileList):
            new_name = "{0}{1}{2}".format(dir+n, i+b, s)
            os.renames(dir+filename, "{0}".format(new_name))
            print "SRT:Rename file '{0}' --> '{1}'".format(dir + filename, new_name)
    except:
        print "SRT:Error! Failed to rename files. Check the existing filenames."
    else:
        print "----------"
        print "SRT:Rename successfully!"
        

if __name__ == "__main__":
    init()