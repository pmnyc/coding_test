
"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

def rightMove(idx):
    return [idx[0],idx[1]+1]

def downMove(idx):
    return [idx[0]+1,idx[1]]

def miniPath(cand, grid):
    cache = {}
    m = len(grid)
    n = len(grid[0])
    if cand[0] == m-1:
        path_ = []
        sum_= 0
        for i in range(cand[1], n):
            path_.append([cand[0],i])
            sum_ += grid[cand[0]][i]
        res = (path_, sum_)
        cache[str(cand)] = res
        return res
    elif cand[1] == n-1:
        path_ = []
        sum_= 0
        for i in range(cand[0], m):
            path_.append([i,cand[1]])
            sum_ += grid[i][cand[1]]
        res = (path_, sum_)
        cache[str(cand)] = res
        return res
    else:
        idx = rightMove(cand)
        if str(idx) in cache:
            out = cache[str(idx)]
        else:
            out = miniPath(idx,grid)
        path1_ = [cand] + out[0]
        sum1_ = grid[cand[0]][cand[1]] + out[1]
        res = (path1_, sum1_)
        
        idx2 = downMove(cand)
        if str(idx2) in cache:
            out = cache[str(idx2)]
        else:
            out = miniPath(idx2,grid)
        path2_ = [cand] + out[0]
        sum2_ = grid[cand[0]][cand[1]] + out[1]
        if sum1_ > sum2_:
            res = (path2_, sum2_)
        cache[str(cand)] = res
        return res

grid = [[3,4,1],[3,2,8]]
miniPath([0,0],grid)
