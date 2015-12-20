
"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.
Each element in the array represents your maximum jump length at that
position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)
"""


def possisbleJump(cand, A):
    cache = {}
    # cand = [] starting index
    if cand == len(A)-1:
        res = 0
        cache[cand] = res
        return res
    elif cand + A[cand] >= len(A)-1:
        res = 1
        cache[cand] = res
        return res
    else:
        counter = 0
        for c in range(cand+1, cand + A[cand]+1):
            if c in cache:
                minsteps = cache[c]
            else:
                minsteps = possisbleJump(c, A)
            if counter == 0:
                res = 1 + minsteps
            else:
                res = min(res, 1 + minsteps)
            counter += 1
        return res

A= [2,2,3,1,1,4]
possisbleJump(0, A)
                