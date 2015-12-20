# -*- coding: utf-8 -*-
"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Lesson:
# To get the full list, only return res at the end
"""


array =[2,3,6,7]
target = 7


def findComb(cand, array, target):
    cache = {}
    res = []
    if target - sum(cand) < 0:
        res = res
    elif target - sum(cand) == 0:
        cand_new = cand+[]
        cand_new.sort()
        res.append(cand_new)
        cache[str(cand_new)] = res
    else:
        for i, num in enumerate(array):
            cand_new = cand + [num]
            cand_new .sort()
            if str(cand_new) in cache:
                res_2 = cache[str(cand_new)]
            else:
                res_2 = findComb(cand_new, array, target)
            if res_2 != None:
                for r in res_2:
                    r.sort()
                    if r not in res:
                        res.append(r)
        cache[str(cand)] = res
    return res
            


array =[1,2,3,4,5,6,7,8,9,10]
target = 10
findComb([], array, target)
