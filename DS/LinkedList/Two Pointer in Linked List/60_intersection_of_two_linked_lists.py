#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) ->ListNode:
        
        temp_A=set()
        while headA:
            temp_A.add(headA)
            headA = headA.next
        while headB:
            if headB in temp_A:
                return headB
            headB= headB.next
        return None
            
        # a_pointer, b_pointer = headA, headB
        # while a_pointer != b_pointer:
        #     a_pointer = a_pointer.next if a_pointer else headB
        #     b_pointer = b_pointer.next if b_pointer else headA
        # return a_pointer