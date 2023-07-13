class MyCircularQueue:

		def __init__(self, k: int):
			self.size = k
			self.queue = []

		def enQueue(self, value: int) -> bool:
			if len(self.queue) == self.size:
				return False

			self.queue.append(value)
			return True

		def deQueue(self) -> bool:
			if len(self.queue) == 0:
				return False

			self.queue.pop(0)
			return True

		def Front(self) -> int:
			if self.queue:
				return self.queue[0]

			return -1

		def Rear(self) -> int:
			if self.queue:
				return self.queue[-1]

			return -1

		def isEmpty(self) -> bool:
			if self.queue:
				return False

			return True

		def isFull(self) -> bool:
			if len(self.queue) == self.size:
				return True

			return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()