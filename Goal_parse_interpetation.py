#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:39:07 2021

@author: VGaur
"""

#You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")