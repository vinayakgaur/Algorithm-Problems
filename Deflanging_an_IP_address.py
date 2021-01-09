#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:36:21 2021

@author: VGaur
"""

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        j = ""
        for i in address:
            if i == ".":
                # i.replace(".","[.]")
                j = j +"[.]"
            else:
                j = j +i
        return j