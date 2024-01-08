#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:05:00 2022

@author: Yang

Think python chap 9, chap 13.
"""
# 1, counting letters.

res = 0
f = open("has_no_e.txt")
for line in f:
    for char in line:
        if char == "e" or char == "E":
            res = res + 1
print(res)

# 2, analyzing books.
# go to gutenberg.com for more copyright-free books.

# 2-1 word histogram (what is a histogram?)
import string

def process_file(fname):
    hist = dict()
    f = open(fname)
    for line in f:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace("-"," ")
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace + "“""")
        word = word.lower()
        hist[word] = hist.get(word,0) + 1

h = process_file("sherlockholmes.txt")

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

print("Total number of words:{}".format(total_words(h)))
print("Number of different words: {}".format(different_words(h)))

# 2-2 most common words

def most_common(hist):
    wordlist = []
    for key, value in hist.items():
        wordlist.append((value,key))
    wordlist.sort(reverse=True)
    return wordlist

l = most_common(h)
n = 50 # easy for other nums
print("The most {} common words are:".format(n))
for freq, word in l[:n]:
    print(word, freq, sep="\t"*2)

# 2-3 random words

