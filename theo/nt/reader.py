#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:06:02 2020

@author: jacob
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = 'nt.csv'

# Read .csv file into pandas dataframe
df = pd.read_csv(fileName, sep='\t', header=0, usecols=[0,4], \
                      index_col=False, dtype='str')

# clean up strong's numbers: 1080&5656 -> 1080
def clean(string):
    if '&' in string:
        index = string.find('&')
        new = string[0:index]
        return new
    else:
        return string
df = df.applymap(clean)

# create one array per book and create a dictionary called
# bookDict that takes the key 'title' and returns an array
# containing all the words in that book.
def bcvToBook(string):
    """ Convert 'Matt 1:1' to 'Matt' """
    if ' ' in string:
        spaceIndex = string.find(' ')
        book = string[0:spaceIndex]
        return book
    else:
        return string
df = df.applymap(bcvToBook) 
array = df.to_numpy()
# find the index of the row where each book ends:
lastWordIndices = list()
for rowNum in range(len(array)):
    if rowNum < len(array)-1:
        currentBook = array[rowNum, 0]
        nextBook = array[rowNum + 1, 0]
        if currentBook != nextBook:
            lastWordIndices.append(rowNum)
    else:
        lastWordIndices.append(rowNum)
# split up the books
bookDict = dict()
for i in range(len(lastWordIndices)):
    if i == 0:
        lastWord = lastWordIndices[i]
        book = array[0:lastWord + 1, 1]
        bookTitle = array[lastWord, 0]
        bookDict[bookTitle] = book
    else:
        lastWord = lastWordIndices[i]
        prevlastWord = lastWordIndices[i-1]
        book = array[prevlastWord + 1:lastWord + 1, 1]
        bookTitle = array[lastWord, 0]
        bookDict[bookTitle] = book

