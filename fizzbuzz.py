# Problem found at https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        
        for x in range(1, n+1):
            if (x % 3 == 0) & (x % 5 == 0):
                out.append('FizzBuzz')
            elif (x % 3 == 0):
                out.append('Fizz')
            elif (x % 5 == 0):
                out.append('Buzz')
            else:
                out.append(str(x))
        
        return out
