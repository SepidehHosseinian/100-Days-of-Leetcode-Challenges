# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        if head is None:
            return head
        
        current = head
        previous = None
        
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        return previous