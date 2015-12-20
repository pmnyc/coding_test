"""
This is for finding the largest k-th element in the unsorted array
"""

def push2left(nums):
    j = 1
    while True:
        if nums[j] > nums[0]:
            nums[0], nums[j] = nums[j], nums[0]
        j += 1
        if j >= len(nums):
            break
    return nums

def findKlargest(nums, k):
    for i in range(k):
        nums[i:] = push2left(nums[i:])
    return nums[k-1]

#sample usage
import numpy
array = list(numpy.random.permutation(1000000))
findKlargest(array, 3)
