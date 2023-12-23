# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: list[ListNode]) -> list[ListNode]:
        count=0
        res=head
        while res:
             count+=1 
             res=res.next

        middel=count//2+1

        for i in range(middel-1):
            head=head.next
        return head  
        #876  