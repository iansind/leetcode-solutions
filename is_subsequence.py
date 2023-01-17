# Problem found at https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        ps = 0

        for x in t:
            if x == s[ps]:
                ps += 1
                if ps == len(s):
                    return True
        
        return False
      
