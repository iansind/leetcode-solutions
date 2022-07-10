# Problem found at: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            diff = target - nums[x]
            idx1 = x
            if diff in nums[x+1:]:
                idx2 = nums[x+1:].index(diff) + x + 1
                break
        return(idx1, idx2)
