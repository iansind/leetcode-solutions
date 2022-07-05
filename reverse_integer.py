# Problem found at: https://leetcode.com/problems/reverse-integer/submissions/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower = -2**31
        upper = 2**31 - 1

        if lower <= x <= upper:
            x = str(x)
            if x[0] == '-':
                x = x[1:]
                x = int(x[::-1]) * -1
            else:
                x = int(x[::-1])
            
            if lower <= x <= upper:
                return x

            return 0
        
        return 0
        
