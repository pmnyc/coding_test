# -*- coding: utf-8 -*-
"""
 Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []


Lessons:
If the problem requires extensive iteration of all scenarios, then try to break into
    left right pieces and do recursion, of course, with memorization
"""

num = "123"
target = 6



def findconsecutivenumbers(nums):
    # nums = '123*4-5'
    res = False
    for i in range(len(nums)-1):
        c = nums[i]
        n = nums[i+1]
        if c.isdigit() and n.isdigit():
            res = True
            break
    return res

def Operators(cand):
    # cand is like 12*3
    cache={}
    operators = "+-*"
    res = []
    if not(findconsecutivenumbers(cand)):
        if cand not in res:
            cache[cand] = res
            res.append(cand)
        return res
    else:
        for i in range(len(cand)-1):
            go_ind = cand[max(i-1,0)].isdigit() and cand[i].isdigit() and cand[min(len(cand)-1,i+1)].isdigit()
            if not(go_ind):
                continue            
            else:
                left = cand[:i+1]
                right = cand[i+1:]
                if left in cache:
                    lefts = cache[left]
                else:
                    lefts = Operators(left)
                if right in cache:
                    rights = cache[right]
                else:
                    rights = Operators(right)
                if cand not in res:
                    res.append(cand)
                for o in operators:
                    for l in lefts:
                        for r in rights:
                            out = l + o + r
                            if out not in res:
                                res.append(out)
        cache[cand] = res
    return res

def isvalieExpression(x):
    # x = '1*05' or x '10*5'
    operators = "+-*"
    res = True
    for i, o in enumerate(x):
        if o not in operators:
            continue
        else:
            try:
                if x[i+1] == '0' and x[i+2].isdigit():
                    res = False
                    break
            except:
                pass
    return res

def addOperators(num, target):
    outs = Operators(num)
    res = []
    for o in outs:
        if isvalieExpression(o) and eval(o) == target and o not in res:
            res.append(o)
    return res

num = "3456237490"
target = 9191
addOperators(num, target)
