# Problem found at https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def word_sum(word):
            num_conv = ''
            for x in word:
                num_conv += str(ord(x)-97)
            return int(num_conv)
        
        first = word_sum(firstWord)
        second = word_sum(secondWord)
        target = word_sum(targetWord)
        
        return (first + second == target)
