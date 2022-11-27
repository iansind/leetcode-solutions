# Problem found at https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for x in range(len(nums)):
            out.append(sum(nums[0:x+1]))
            
        return out
