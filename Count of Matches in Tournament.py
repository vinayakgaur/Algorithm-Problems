#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:28:16 2021

@author: VGaur
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        # total = 0
        # teams = 0
        matches = 0
        while n >  1:
            if n % 2 == 0:
                n = n // 2
                matches += n
            else:
                n = (n + 1) // 2
                matches += n - 1
        return matches