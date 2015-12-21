"""
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b
≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

def findQuadruplet(cand, S, target):
    cache = {}
    res = []
    if len(cand) > 4:
        return
    elif len(cand) == 4 and sum(cand) == target:
        c = cand+[]
        c.sort()
        if c not in res:
            res.append(c)
        cache[str(c)] = res
    else:
        cand_idx = []
        cand2 = cand + []
        cand2.sort()
        for c in cand:
            try:
                if S.index(c) not in cand_idx:
                    cand_idx.append(S.index(c))
                else:
                    S_new = S+[]
                    S_new[S.index(c)] = c+1
                    cand_idx.append(S_new.index(c))
            except:
                pass
        for i, num in enumerate(S):
            if i in cand_idx:
                continue
            else:
                cand_new = cand + [num]
                cand_new.sort()
                if str(cand_new) in cache:
                    res_2 = cache[str(cand_new)]
                else:
                    res_2 = findQuadruplet(cand_new, S, target)
                if res_2 != None:
                    for r in res_2:
                        r.sort()
                        if r not in res:
                            res.append(r)
        cache[str(cand2)]= res
    return res
            

S = [1, 0, -1, 0, -2, 2]
findQuadruplet([],S,0)
