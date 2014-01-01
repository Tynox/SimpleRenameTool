#!/usr/bin/env python
# encoding:utf-8

"""
批量重命名文件小工具
version: 0.1
"""

import os
import sys
import getopt

# get argv
try:
    #dir = sys.argv[1]
    opts, args = getopt.getopt(argv[1:], "d:n", ["dir=", "name"]
    print "dir:{0}".format(dir)
except getopt.GetoptError, err:
    print str(err)
    sys.exit()

# parse argv
try:
    # fileList = os.listdir(dir)
    for o, a in opts:
        if o in ("-d", "--dir"):
            fileList = os.listdir(a)
        elif o in ("-n", "--name"):
            pass
except:
    print "Error! Failed to find the folder."
    
#elif isinstance(fileList, str):
#    print "This is an undecodable filename."
else:
    try:
        for i, filename in enumerate(fileList):
            os.renames(dir+filename, "{0}{1}.png".format(dir, i+1))
    except:
        print "Error! Failed to rename files. Check the existing filenames."
    else:
        print "Done!"