#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:12:51 2021

@author: VGaur
"""
#Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        time = 0
        cursor = 0
        for i in word:
            time += abs(cursor - keyboard.index(i))
            cursor = keyboard.index(i)
        return time