"""
# Definition for a Node."""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: list[Node]) -> list[Node]:
        #approve01
        parents = []
        node = head
        while node:
            if node.child:
                node.next and parents.append(node.next)
                node.next = node.child
                node.next.prev = node
                node.child = None
            if not node.next and len(parents) > 0:
                node.next = parents.pop()
                node.next.prev = node
            node = node.next
        return head
        #430
        #approve02
        #  if not head:return None
        # nodes = []
        # def dfs(node):
        #     if node is None:return
        #     nodes.append(node)
        #     if node.child:dfs(node.child)
        #     if node.next:dfs(node.next)
        # dfs(head)
        # head = nodes[0]
        # head.child=None
        # for i in range(1, len(nodes)):
        #     node = nodes[i]
        #     prev = nodes[i-1]
        #     node.child=None
        #     node.prev=prev
        #     prev.next = node
        # return head