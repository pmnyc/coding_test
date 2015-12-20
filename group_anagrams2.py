
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case.
"""


def anagram(a,b):
    """ a='tea' and b = 'eat' are anagram"""
    if set(a) == set(b):
        return True
    else:
        return False

def findAnagrams(A):
    res = []
    queque = A +[]
    while len(queque)>0:
        a = queque[0]
        out = [a]
        out_idx = [0]
        for i, s in enumerate(queque):
            if i == 0:
                continue
            else:
                if anagram(a, s):
                    out += [s]
                    out_idx += [i]
        idx_ = filter(lambda x: x not in out_idx, range(len(queque)))
        queque = map(lambda x : queque[x],idx_)
        res.append(out)
    return res


A = ["eat", "tea", "tan", "ate", "nat", "bat"]
findAnagrams(A)