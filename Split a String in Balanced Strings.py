#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:32:00 2021

@author: VGaur
"""

#Balanced strings are those who have equal quantity of 'L' and 'R' characters.

#Given a balanced string s split it in the maximum amount of balanced strings.

#Return the maximum amount of splitted balanced strings.

 

#Example 1:

#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.



class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r,l,c = 0,0,0
        for i in s:
            if i == "R":
                r += 1
            elif i == "L":
                l += 1
            if r == l:
                c +=1
                r= l =0
        return c