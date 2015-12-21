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


    
    
    



M =['YNNNN',
'NYNNN',
'NNYNN',
'NNNYN',
'NNNNY']

FriendCircle(M)

M = ['YYNN',
'YYYN',
'NYYN',
'NNNY']

FriendCircle(M)
