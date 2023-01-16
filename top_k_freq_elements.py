# Problem found at https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] = freq[x] + 1
        
        out = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        return [out[x][0] for x in range(k)]
      
