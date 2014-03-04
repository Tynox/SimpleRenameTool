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

version = 0.8

opts = None
args = None
fileList = None
dir_source = None
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
    global dir_source
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
    
    # get dir_source
    if args is None or len(args) == 0:
        print "SRT:no source dictionary."
        sys.exit()
    dir_source = args[0]
    try:
        fileList = os.listdir(dir_source)
        fileList.sort()
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


def resortFiles(fileList):
    """
    rename all files to avoid target name existing. And then sort items by st_mtime.
    """
    if fileList is None or not len(fileList):
        print "SRT:nofiles in the dictionary."
        sys.exit()

    new_file_list = list()
    for f in fileList:
        new_file_list.append(PFileStat(dir_source, f, os.lstat(dir_source + "/" + f)))

    new_file_list.sort(key=lambda i: i.st_mtime)
    return new_file_list


def renameFiles():
    """
    rename files
    """
    # check fileList. if fileList is None, exit.
    if fileList is None:
        print "SRT:no files in the dictionary."
        sys.exit()
        
    print "----------"
    
    # rename all files to avoid target name existing. And then sort items by st_mtime.
    new_filelist = resortFiles(fileList)

    try:
        b = begin if begin is not None else 0
        n = name if name is not None else ""
        count = 0
        for i in new_filelist:
            if suffix is None:
                if i.original_name.rfind(".") != -1:
                    s = i.original_name[i.original_name.rfind("."):]
                else:
                    s = ""
            else:
                s = suffix
            new_name = "{0}{1}{2}".format(dir_source+"/"+n, count+b, s)
            os.renames(dir_source+"/"+i.name, new_name)
            count += 1
            print "SRT:Rename file '{0}' --> '{1}'".format(dir_source+"/"+i.original_name, new_name)
    except:
        print "SRT:error occurred."
    else:
        print "----------"
        print "SRT:Rename successfully!"
        

class PFileStat(object):
    def __init__(self, dir_source, name, fstat):
        self.__name = name
        self.__fstat = fstat
        self.__ex_name = name + name

        # rename the file name
        os.renames(dir_source + "/" + self.__name, dir_source + "/" + self.__ex_name)

    @property
    def name(self):
        return self.__ex_name

    @property
    def original_name(self):
        return self.__name

    @property
    def fstat(self):
        return self.__fstat

    @property
    def st_mtime(self):
        return self.__fstat.st_mtime


if __name__ == "__main__":
    init()
