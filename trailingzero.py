"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
"""

import os, sys
import numpy as np 


res = 0
i = 5
while n / i >= 1:
    res += n / i
    i *= 5

return res

