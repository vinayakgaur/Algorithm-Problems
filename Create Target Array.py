#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:16:09 2021

@author: VGaur
"""

#Given two arrays of integers nums and index. Your task is to create target array under the following rules:

#Initially target array is empty.
#From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read in nums and index.
#Return the target array.

#It is guaranteed that the insertion operations will be valid.


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        m = 0
        for i in nums:
            target.insert(index[m], i)
            m +=1 
        return target