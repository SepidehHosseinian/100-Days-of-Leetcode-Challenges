# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        num1=[]
        num2=[]
        while l1:
                num1.append(str(l1.val))
                l1= l1.next
    
        while l2 :
                num2.append(str(l2.val))
                l2= l2.next
                
        res=int(''.join(map(str,reversed(num1))))+int(''.join(map(str,reversed(num2))))
        arr =str(res)[::-1]
        root=n=ListNode(0)
        for i in arr :
            root.next= ListNode(i)
            root=root.next
        return n.next