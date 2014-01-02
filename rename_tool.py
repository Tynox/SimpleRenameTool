#!/usr/bin/env python
# encoding:utf-8

"""
A Simple Rename Tool.
"""

import os
import sys
import getopt

version = 0.2

opts = None
args = None
fileList = None
dir = None

def init():
    """
    Init and get arguments.
    """
    global opts
    global args
    
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["--help", "--version"])
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
    
    # check options. If options is None, exit. 
    for o, a in opts:
        if o in ("-h", "--help"):       # get help
            getHelp()
            sys.exit()
        elif o in ("-v", "--version"):
            showVersion()
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
    print "usage:rename_tool.py [-h|--help] [-v|--version] [<dictionary>]"
    
  
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
        print "no files in the dictionary."
        sys.exit()
        
    try:
        for i, filename in enumerate(fileList):
            os.renames(dir+filename, "{0}{1}.txt".format(dir, i+1))
    except:
        print "Error! Failed to rename files. Check the existing filenames."
    else:
        print "Done!"
        

if __name__ == "__main__":
    init()