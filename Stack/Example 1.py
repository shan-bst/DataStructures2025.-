# Example 1: Basic Stack Operations
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"
    
    def display(self):
        return self.stack

# Demonstrating Stack Operations
stack = Stack()
stack.push(10)
stack.push(20)
print("Stack after push:", stack.display())
print("Popped element:", stack.pop())
print("Stack now:", stack.display())