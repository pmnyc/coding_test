"""
Given a string of numbers and operators, return all possible results from
computing all the different possible ways to group numbers and operators. The
valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


def differentways(cand):
    # cand is like 2*(3-4)*5
    cache = {}
    operators = "+-*"
    res = []
    operators_num = len(filter(lambda x: x in operators,cand))
    if cand.count("(") == operators_num:
        if cand not in res:
            res.append(cand)
            cache[cand] = res
    else:
        for i, c in enumerate(cand):
            if c not in operators:
                continue
            else:
                left = cand[:i]
                right = cand[i+1:]
                if left in cache:
                    a = cache[left]
                else:
                    a = differentways(left)
                if right in cache:
                    b = cache[right]
                else:
                    b = differentways(right)
                for aa in a:
                    for bb in b:
                        r = "(" + aa + c + bb + ")"
                        if r not in res:
                            res.append(r)
        cache[cand] = res
    return res


string = "2*3-4*5+5-5+2*0-3"
differentways(string)
