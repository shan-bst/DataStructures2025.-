# Example 1: Basic Array Operations
class Array:
    def __init__(self):
        self.array = []
    
    def insert(self, item):
        self.array.append(item)
    
    def delete(self, index):
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        return "Invalid index"
    
    def display(self):
        return self.array

# Demonstrating Array Operations
arr = Array()
arr.insert(100)
arr.insert(200)
print("Array after insertion:", arr.display())
print("Deleted element:", arr.delete(0))
print("Array now:", arr.display())