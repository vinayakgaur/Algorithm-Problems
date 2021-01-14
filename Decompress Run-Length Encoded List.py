#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:14:35 2021

@author: VGaur
"""

#We are given a list nums of integers representing a list compressed with run-length encoding.

#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

#Return the decompressed list.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new = []
        fre =0
        val =0
        for i in range(len(nums)):
            fre += i 
            val += i+1
            new.append(fre*val)
            i = i+2
        return new
