# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: list[ListNode]) -> bool:
        
        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.next
        if arr == arr[::-1]:
            return True
        else: return False
#         self.front_pointer = head

#         def recursively_check(current_node=head):
            
#             if current_node is not None:
#             if not recursively_check(current_node.next):
#                 return False
#             if self.front_pointer.val != current_node.val:
#                 return False
#             self.front_pointer = self.front_pointer.next
#             return True

#         return recursively_check()