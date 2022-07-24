# Problem found at: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for x in range(len(s)):
            if s[x] == '(' or s[x] == '[' or s[x] == '{':
                stack.append(s[x])
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if not popped == '(' and s[x] == ')' or not popped == '[' and s[x] == ']' \
                or not popped == '{' and s[x] == '}':
                    return False
        return len(stack) == 0
