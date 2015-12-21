# -*- coding: utf-8 -*-
"""
 All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cache = {}
        length = 10
        res = []
        for i in range(len(s)):
            seq = s[i:i+length]
            if len(seq) != length:
                continue
            else:
                if seq in cache:
                    cache[seq] += 1
                    if seq not in res:
                        res.append(seq)
                else:
                    cache[seq] = 1
        return res
