# -*- coding: utf-8 -*-
"""
Problem Statement

An Introduction to the Longest Increasing Subsequence Problems

The task is to find the length of the longest subsequence in a given array 
of integers such that all elements of the subsequence are sorted in 
ascending order. For example, the length of the LIS for { 15, 27, 
14, 38, 26, 55, 46, 65, 85 } is 6 and the longest increasing 
subsequence is {15, 27, 38, 55, 65, 85}. 

"""


def merge2lsits(a,b):
    # a = [[2,3],[4]]
    # b = [[5],[6]]
    if a[-1][-1] > b[0][0]:
        return a+b
    else:
        return a[:-1] + [a[-1]+b[0]] + b[1:]

def findfirsrbreak(array):
    res = len(array)-1
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            res = i
            break
    return res

def longestSeq(array):
    # cand = [15] and expanding
    cache = {}
    i = findfirsrbreak(array)
    if i == len(array) -1:
        res = [array]
        cache[str(array)] = res
        return res
    else:
        left = array[:i+1]
        right = array[i+1:]
        if str(left) in cache:
            res_left = cache[str(left)]
        else:
            res_left = longestSeq(left)
        if str(right) in cache:
            res_right = cache[str(right)]
        else:
            res_right = longestSeq(right)
        res = merge2lsits(res_left,res_right)
        cache[str(array)] = res
        return res

array = [15, 27, 14, 38, 26, 55, 46, 65, 85]
longestSeq(array)
