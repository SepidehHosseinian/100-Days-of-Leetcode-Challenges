class Node(object):
    
    def __init__(self, val, nxt=None, prev=None):
        self.val =val
        self.next = nxt
        self.prev = prev

class MyLinkedList():

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
            
        

    def addAtHead(self, val: int) -> None:
        
        add = Node(val)
        if self.size == 0:
            add.next = None
            self.tail = add
        else:
            add.next = self.head
            self.head.prev = add
        add.prev = None
        self.head = add
        self.size += 1

    def addAtTail(self, val):
       
        add = Node(val)
        if self.size == 0:
            add.prev = None
            self.head = add
        else:
            add.prev = self.tail
            self.tail.next = add
        add.next = None
        self.tail = add
        self.size += 1    

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            add = Node(val)
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            next_ = prev.next
            add.prev = prev
            add.next = next_
            prev.next = add
            next_.prev = add
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        if self.size == 1:
            self.head = None
            self.tail = None
        elif cur is self.head:
            cur.next.prev = cur.prev
            self.head = cur.next
        elif cur is self.tail:
            cur.prev.next = cur.next
            self.tail = cur.prev
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)