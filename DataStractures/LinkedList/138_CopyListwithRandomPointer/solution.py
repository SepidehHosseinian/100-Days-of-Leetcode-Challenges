"""
# Definition for a Node."""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: list[Node]) -> list[Node]:
        
        # return deepcopy(head)
        if head is None:
            return head
        temp=head
        mp = {}
        while temp:
            mp[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.next:
                mp[temp].next=mp[temp.next]
            if temp.random:
                mp[temp].random=mp[temp.random]
            temp=temp.next
        return mp[head]
        #138
