#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:52:51 2021

@author: VGaur
"""

# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sh = list(s)
        for i in range(len(indices)):
            sh[indices[i]] = s[i]
        return ''.join(sh)