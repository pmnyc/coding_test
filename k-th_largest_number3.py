"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: You may assume k is always valid, 1 <= k <= array's length.
"""

class Solution(object):
    def locateMax(self, nums):
        max_=nums[0]
        res = (0, max_)
        for i in range(1,len(nums)):
            if nums[i] > max_:
                max_ =nums[i]+0
                res = i+0
        out = (res, max_)
        return out
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i =0
        while i < k:
            idx, res = self.locateMax(nums)
            nums = nums[:idx] + nums[(idx+1):]
            i += 1
        return res

nums=[3,2,1,5,6,4]
k = 3
Solution().findKthLargest(nums, k)