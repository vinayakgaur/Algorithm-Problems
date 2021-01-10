#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:55:34 2021

@author: VGaur
"""

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A"

class Solution:
    def numJewelsInStones(self, jewels: str, stone: str) -> int:
        l = []
        sum =0
        for i in jewels:
            l.append(i)
        for j in stone:
            if j in l:
              sum += 1
        return sum