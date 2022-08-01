# Problem found at: https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def makeDicts(u):
            counts = {}
        
            for x in u:
                if x not in counts:
                    counts[x] = 1
                else: 
                    counts[x] += 1
            
            return sorted(counts.items())
          
        return makeDicts(s) == makeDicts(t) 
        
