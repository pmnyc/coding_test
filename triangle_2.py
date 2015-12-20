"""
Triangle:
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""


triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


def findMinPath(cand, triangle):
    # cand is like [3,1]
    cache= {}
    nrows = len(triangle)
    if cand[0] == nrows-1:
        res = triangle[cand[0]][cand[1]]
        cache[str(cand)] = res
        return res
    else:
        down_1 = [cand[0]+1,cand[1]]
        down_2 = [cand[0]+1,cand[1]+1]
        if str(down_1) in cache:
            sum_1 = cache[str(down_1)]
        else:
            sum_1 = findMinPath(down_1, triangle)
        if str(down_2) in cache:
            sum_2 = cache[str(down_2)]
        else:
            sum_2 = findMinPath(down_2, triangle)
        res = triangle[cand[0]][cand[1]] + min(sum_1, sum_2)
        cache[str(cand)] = res
        return res

findMinPath([0,0], triangle)
