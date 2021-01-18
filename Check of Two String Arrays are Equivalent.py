#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:29:38 2021

@author: VGaur
"""


#Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

#A string is represented by an array if the array elements concatenated in order forms the string.

 

#Example 1:

#Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
#Output: true
#Explanation:
#word1 represents string "ab" + "c" -> "abc"
#word2 represents string "a" + "bc" -> "abc"
#The strings are the same, so return true.


#------------------------------------------------

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        nw1 = ""
        nw2 = ""
        for i in word1:
            nw1 += i
        for j in word2:
            nw2 += j
        if nw1 == nw2:
            return True