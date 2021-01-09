#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:37:49 2021

@author: VGaur
"""

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = []
        total = 0
        for i in nums:
            total = total + seen.count(i)
            seen.append(i)
        return total