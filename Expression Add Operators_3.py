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

def isLeading0(x):
    if len(x) >1 and x.startswith('0'):
        return True
    else:
        return False

def addOperators(cand, target):
    cache = {}
    res = []
    if eval(cand) == target and not(isLeading0(cand)):
        if cand not in res:
            res.append(cand)
        cache[(cand, target)] = res
        return res
    else:
        for i in range(len(cand)-1):
            left = cand[:i+1]
            right = cand[i+1:]
            if isLeading0(right):
                continue
            else:
                # for +
                if (left, target - int(right)) in cache:
                    res1 = cache[(left, target - int(right))]
                else:
                    res1 = addOperators(left, target - int(right))
                if res1 != None:
                    res1 = map(lambda x: x+"+"+right, res1)
                    for r in res1:
                        if r not in res:
                            res.append(r)
                # for *
                if int(right) != 0:
                    if (left, target / int(right)) in cache:
                        res2 = cache[(left, target / int(right))]
                    else:
                        res2 = addOperators(left, target / int(right))
                    if res2 != None:
                        res2 = map(lambda x: "("+x+")"+"*("+right+")", res2)
                        for r in res2:
                            if r not in res:
                                res.append(r)
                # for -
                if (left, target + int(right)) in cache:
                    res3 = cache[(left, target + int(right))]
                else:
                    res3 = addOperators(left, target + int(right))
                if res3 != None:
                    res3 = map(lambda x: x+"-"+right, res3)
                    for r in res3:
                        if r not in res:
                            res.append(r)
        cache[(cand, target)] = res
        return res

num = "232"
target = 8
addOperators(num, target)
