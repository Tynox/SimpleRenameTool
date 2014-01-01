#!/usr/bin/env python
# encoding:utf-8

"""
A Simple Rename Tool.
version: 0.2
"""

import os
import sys
import getopt

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
    
    try:
        #dir = sys.argv[1]
        opts, args = getopt.getopt(sys.argv[1:], "d:", ["dir="])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit()
    else:
        parseOpts()


def parseOpts():
    """
    parse opts and arguments
    """
    # fileList = os.listdir(dir)
    global fileList
    global dir
    
    # check options. If options is None, exit.
    if opts is None:
        print "no source dictionary."
        sys.exit()
    
    for o, a in opts:
        if o in ("-d", "--dir"):
            dir = a
            fileList = os.listdir(a)
    renameFiles()


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