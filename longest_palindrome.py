# Problem found at https://leetcode.com/problems/longest-palindrome/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        count = 0
        for char in s:
            if char in seen:
                count += 2
                seen.remove(char)
            else:
                seen.add(char)
        if len(seen) > 0:
            count += 1
        return count
      
