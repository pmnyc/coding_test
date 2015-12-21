# -*- coding: utf-8 -*-
"""
Problem Statement

There are N students in a class. Some of them are friends, while 
some are not. Their friendship is transitive in nature, i.e., if 
A is friend of B and B is friend of C, then A is also friend of C. 
A friend circle is a group of students who are directly or indirectly friends.

You are given a N×N−matrix M which consists of characters Y or N. 
If M[i][j]=Y, then ith and jth students are friends with each other, 
otherwise not. You have to print the total number of friend circles in the class.
"""


import numpy as np

def merge2list(a,b):
     x = np.unique(a+b)
     x.sort()
     return list(x)

def getDuplicateEle(x):
    # x= [[1,2],[2,3],[4]]
    out = []
    res = []
    for a in x:
        out += a
    for a in set(out):
        if out.count(a) > 1:
            res += [a]
    return res
    
def inputData(M):
    out = []
    for m in M:
        out.append(map(lambda x: x, m))
    return out
   
def hasCommon(a,b):
    res = False
    if len(a) > len(b):
        a,b = b,a
    for c in a:
        if c in b:
            res = True
            break
    return res

def isComplete(circles):
    n = len(circles)
    res = (True, [])
    for i in range(n-1):
        for j in range(i+1,n):
            if hasCommon(circles[i], circles[j]):
                res = (False, [i,j])
                break
    return res

def addOneFriend(x,M):
    # x = [0,1]
    if type(M[0]) is not list:
        M = inputData(M)
    people = range(len(M))
    rest_people = list(np.setdiff1d(people, x))
    res = x + []
    for p in x:
        for r in rest_people:
            if M[p][r] == 'Y':
                res += [r]
                break
    return res

def findCircles(M):
    if type(M[0]) is not list:
        M = inputData(M)
    people = range(len(M))
    circles = []
    while len(people) > 0:
        p = people[0]
        circle = [p]
        for i in range(len(people)-1):
            circle_ = addOneFriend(circle,M)
            if circle_ != circle:
                circle = circle_
            else:
                break
        circles.append(circle)
        visited = []
        for c in circles:
            visited += c
        people = list(np.setdiff1d(people, visited))
    return circles



M = ['YYNN',
'YYYN',
'NYYN',
'NNNY']

findCircles(M)
