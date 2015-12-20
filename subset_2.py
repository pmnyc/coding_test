"""
Subsets:
Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:
"""


S = [1,2,3]


def findSubset(cand):
    cache = {}
    res = []
    if len(cand) == 1:
        res = [cand] + [[]]
        cache[str(cand)] = res
        return res
    elif cand == []:
        res = [[]]
        cache[str(cand)]=res
        return res
    else:
        for i, num in enumerate(cand):
            cand_new = cand[:i] + cand[i+1:]
            if str(cand_new) in cache:
                res_new = cache[str(cand_new)]
            else:
                res_new = findSubset(cand_new)
            res = res_new
            for r in res_new:
                res_cand = r + [num]
                res_cand.sort()
                if res_cand not in res:
                    res = res + [res_cand]
            cache[str(cand)] = res
            return res

findSubset(S)