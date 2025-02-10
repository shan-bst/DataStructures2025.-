# Example 1: Basic Linked List Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

# Demonstrating Linked List Operations
ll = LinkedList()
ll.insert(5)
ll.insert(15)
ll.insert(25)
print("Linked List after insertion:", ll.display())