#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:42:00 2021

@author: VGaur
"""

#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

#   solution 


class Solution:
    def removeVowels(self, s: str) -> str:
        j = []
        for i in s:
            if i not in ('a','e','i','o','u'):
                j.append(i)

        return ''.join(j)