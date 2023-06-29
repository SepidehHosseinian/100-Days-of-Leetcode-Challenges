# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: list[ListNode]) -> list[ListNode]:
        count=0
        res=head
        while res:
             count+=1 
             res=res.next
        if count<=1 :return None
        if count%2==0 :
            middel=(count//2) +1
        else:
            middel=count//2+1
        temp=head
        for i in range(middel-2):
            temp=temp.next

        temp.next=temp.next.next

        return head   
        # 2095