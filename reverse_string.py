# Problem found at https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        
        for x in range(int(len(s)/2)):
            s[x], s[l-x-1] = s[l-x-1], s[x]
            
