# Problem found at: https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot = 0
        letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last = 0

        for x in s:
            tot += letters.get(x)
            if last == 'I' and (x == 'V' or x == 'X'):
                tot -= 2
            if last == 'X' and (x == 'L' or x == 'C'):
                tot -= 20
            if last == 'C' and (x == 'D' or x == 'M'):
                tot -= 200
            last = x
        
        return(tot)
