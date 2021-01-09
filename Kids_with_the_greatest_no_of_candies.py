#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:33:18 2021

@author: VGaur
"""
# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a = []
        # j = 0
        for i in candies:
            i =  i + extraCandies
            # print (i)
            if i >= max(candies):
                a.append(True)
            else:
                a.append(False)
            i = i+1
        return a