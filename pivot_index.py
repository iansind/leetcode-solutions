# Problem found at https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totsum = sum(nums)
        leftsum = 0
        for x in range(len(nums)):
            if leftsum == (totsum - nums[x] - leftsum):
                return x
            leftsum += nums[x]
        return -1
