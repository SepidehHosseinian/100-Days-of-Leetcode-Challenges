# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: list[ListNode], k: int) -> list[ListNode]:
        size=0
        pc=head
        while pc :
            size+=1
            pc=pc.next
        
        if head is None:return
        
        if k>=size : 
            k=k%size
            
        if k==0 : return head

        pa=head 
        for i in range (k):
            while pa.next:
                pb=pa
                pa=pa.next
            if size>1:
                pb.next=pa.next
                print(pb.next)
                pa.next=head
                print(pa.next)
                head=pa
                print(head)
            else:
                return head
        return head
                                    
                
                
        