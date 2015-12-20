"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


import numpy as np


def lognestcommonpre(string):
    str1 = string[0]
    commonstring = ""
    for i in range(len(str1)):
        letters = map(lambda x: x[i], string)
        if len(np.unique(letters)) == 1:
            commonstring += letters[0]
    return commonstring
    

string = ['abc','abed','abeee']
lognestcommonpre(string)