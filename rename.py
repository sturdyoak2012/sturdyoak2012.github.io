#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:58:19 2021

@author: jacob
"""

import os 
import tempfile

def rename(filename, originalString, replacingString):
    exists = False
    changed = False
    tmp = tempfile.mkstemp()
    
    with open(filename) as replacingFile, open(tmp[1],'w') as temporaryFile:
        for line in replacingFile:
            if originalString in line:
                exists = True
            line = line.replace(originalString,replacingString)
            temporaryFile.write(line)
            
            if replacingString in line:
                changed = True
        
    os.rename(tmp[1],filename)
    
    return (exists, changed)


def fileList():
    walk_list = [f for f in  \
                 os.walk('/home/jacob/Documents/sturdyoak2012.github.io/')]
    
    # walk_list is a list of tuples [(subdir_str, [], [file_str, ...]), ...]
    
    file_list = list()
    for tup in walk_list:
        subdir_str = tup[0]
        for file in tup[2]:
            if file[-4:] == 'html':
                if subdir_str[-3:] == 'io/':
                    filename = subdir_str + file
                    file_list.append(filename) 
                else:
                    filename = subdir_str + '/' + file 
                    file_list.append(filename)
    
    return file_list



def physicstoresearch():
    
    orig1 = 'id=\'pages\'><p>physics'
    repl1 = 'id=\'pages\'><p>research'
    
    orig2 = 'physics.html\">physics</a>'
    repl2 = 'physics.html\">research</a>'
    
    
    
    for filename in fileList():
        try:
            (exists1, changed1) = rename(filename, orig1, repl1)
            (exists2, changed2) = rename(filename, orig2, repl2)
        except:
            print(filename)
        
        if (exists1, changed1) != (True, True):
            print(filename + '\n      failed on desktop')
        if (exists2, changed2) != (True, True):
            print(filename + '\n      failed on mobile')
        
    return
    
    
def linkFix():
    
    orig = 'physics.html'
    repl = 'research.html'
    
    
    for filename in fileList():
        try: 
            (exists, changed) = rename(filename, orig, repl)
        except:
            print(filename)
    
    return
    