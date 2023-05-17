class ListNode:
     def __init__(self, x):
            
            self.val = x
            self.next = None

class Solution:
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:    #Cycle detected
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast