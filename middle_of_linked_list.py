# Problem found at https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        return nodes[(len(nodes))//2]
      
