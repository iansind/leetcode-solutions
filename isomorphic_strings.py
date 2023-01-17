# Problem found at https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def conv(word):
            convs = {}
            i = 1
            for x in word:
                if x not in convs:
                    convs[x] = i
                    i += 1
            out = []
            for x in word:
                out.append(convs[x])
            return out

        return conv(s) == conv(t)
      
