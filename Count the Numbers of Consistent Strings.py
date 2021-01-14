#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:20:38 2021

@author: VGaur
"""

#You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

#Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sum = 0
        for i in words:
            for l in set(i):
                if l not in allowed:
                    break
                else:
                    sum += 1
        return sum