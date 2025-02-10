# Example 1: Basic Queue Operations
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.popleft() if self.queue else "Queue is empty"
    
    def display(self):
        return list(self.queue)

# Demonstrating Queue Operations
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Queue after enqueue:", queue.display())
print("Dequeued element:", queue.dequeue())
print("Queue now:", queue.display())