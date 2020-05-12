#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:42:36 2020

@author: jacob
"""

import reader
import numpy as np
import itertools

bookDict = reader.bookDict

bookList = ['Matt', 'Mark', 'Luke', 'John', 'Acts', 'Rom', '1Cor', 
           '2Cor', 'Gal', 'Eph', 'Phil', 'Col', '1Thess', '2Thess', 
           '1Tim', '2Tim', 'Titus', 'Phlm', 'Heb', 'Jas', '1Pet', 
           '2Pet', '1John', '2John', '3John', 'Jude', 'Rev']

gospels = ['Matt', 'Mark', 'Luke', 'John']
pauline = ['Rom', '1Cor', '2Cor', 'Gal', 'Eph', 'Phil', 'Col', 
           '1Thess', '2Thess', '1Tim', '2Tim', 'Titus', 'Phlm']
paulineHeb = pauline.copy()
paulineHeb.append('Heb')
johannine = ['John', '1John', '2John', '3John', 'Rev']

def freqCount(title):
    """ Returns the words (by Strong's number)
    in the book with title "title", along with the frequency 
    as a decimal number (occurrences/total_words).
    ndarray: [[word, freq], ... ]
    word is a string containing a number, freq is a float """
    book = bookDict[title]
    word, count = np.unique(book, return_counts = True)
    wordCount = np.column_stack((word, count))
    ind = np.argsort(wordCount[:,1])[::-1]
    wordCountSorted = wordCount[ind]
    total_words = len(book)
    word, count = wordCountSorted[:, 0], wordCountSorted[:, 1]
    freq = count / total_words
    freqCount = np.column_stack((word, freq))
    return freqCount

def freqCountTwenty(title):
    """ Returns the top ten most used words (by Strong's)
    in the book with title "title", along with the frequency
    as a decimal number (occurrences/total_words).
    ndarray: [[word, freq], ...]
    word is a string containing a number, freq is a float """
    return freqCount(title)[0:20,:]

def freqDict(title):
    """ Returns a dictionary of the frequencies of each word (by
    Strong's) in the book (given by title).  """
    freqDict = dict()
    array = freqCount(title)
    for i in array:
        word = i[0]
        frequency = i[1]
        freqDict[word] = frequency
    return freqDict

def compare1(book1, book2, n):
    """ Returns the tuple (a, array([[word1, freq1, freq2, s_1], ... [word5,
    freq1, freq2, s_5]])
    a = the similarity coefficient (float) between the two books
    (Closer to zero means more similar)
    word1 through word5 are the words that give the largest 
    (freq1 - freq2)^2
    
    How similarity coefficient is calculated:
        Let {w_i} be the union of book1's top n words and book2's
        top n words.  
        a = sum of s_i = abs(log(freq1_i) - log(freq2_i))
    """
    dict1, dict2 = freqDict(book1), freqDict(book2)
    top_n_1, top_n_2 = freqCount(book1)[0:n,0], freqCount(book2)[0:n,0]
    word_array = np.union1d(top_n_1, top_n_2)
    word_freq1_freq2_s = list()
    for i in word_array:
        try:
            freq1 = float(dict1[i])
            freq2 = float(dict2[i])    
            sumContribution = abs(np.log(freq1) - np.log(freq2))
        except KeyError:
            sumContribution, freq1, freq2 = 0, 0, 0
            # if i in dict1:
            #     print(i, 'is only in', book1)
            # else:
            #     print(i, 'is only in', book2)
        w_f1_f2_s = [i, freq1, freq2, sumContribution]
        word_freq1_freq2_s.append(w_f1_f2_s)
    wffs = np.array(word_freq1_freq2_s)
    a = np.sum(wffs[:,3].astype(np.float))
    ind = np.argsort(wffs[:,3].astype(np.float))[::-1]
    wffs = wffs[ind]
    return (a, wffs[0:5,:])

def mostSimilarTo(book):
    """ Returns array of books and similarity coefficient ranked
    from most similar to least similar
    [[book1, a1],
     ...
     [book26, a26]]
    """
    unrankedList = list()
    for book2 in bookList:
        if book2 == book:
            continue
        a = compare1(book, book2, 10)[0]
        unrankedList.append([book2, a])
    unrankedArray = np.array(unrankedList)
    ind = np.argsort(unrankedArray[:,1].astype(np.float))
    rankedArray = unrankedArray[ind]
    return rankedArray

def printToTextFile(fileName):
    """Prints the full results of mostSimilarTo for each book 
    in fileName"""
    file = open(fileName,"a")
    for book in bookList:
        file.write(book + '\n')
        similarityArray = mostSimilarTo(book)
        file.write(np.array2string(similarityArray))
        file.write('\n')
    file.close()
    
def printToDict():
    """Returns a dictionary with keys (book1, book2) -> a, for all
    combinations of books"""
    compareDict = dict()
    for i in range(len(bookList)):
        for j in range(i+1,len(bookList)):
            book1, book2 = bookList[i], bookList[j]
            a = compare1(book1, book2, 10)[0]
            compareDict[(book1, book2)] = a
            compareDict[(book2, book1)] = a
    return compareDict


def mostSimilarIn(subList, k):
    """ Given a list of n books, subList, this returns the set of
    k < n books that are most similar to each other, along with 
    the average value of a between all pairs within the subset.
    
    Takes (list, int) -> tuple(list, float)
    
    Sublist has nCk subsets of size k, and the returned subset mini-
    mizes the sum of each degree of dissimilarity between all pairs
    of books within the subset."""
    
    compareDict = printToDict()
    mina = 1e30
    (minSubset, avga) = (list(), 0)
    for subset in itertools.combinations(subList, k):
        a = 0
        for pair in itertools.combinations(subset, 2):
            pairTup = tuple(pair)
            s = compareDict[pairTup]
            a = a + s
        if a < mina:
            mina = a
            (minSubset, avga) = (subset, a*2/(k*(k-1)))
    return (minSubset, avga)


"""
# Comment out if you want to find the most similar books
for i in range(2,14):
    print(mostSimilarIn(pauline, i))
"""
