# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next
        if not fast: return head.next
        while fast.next: 
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
        