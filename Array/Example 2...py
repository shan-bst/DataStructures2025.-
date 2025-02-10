# Example 2: Searching an Element in an Array
def search_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element {target} found at index {i}"
    return f"Element {target} not found"

# Demonstrating Search Operation
numbers = [10, 20, 30, 40, 50]
print(search_element(numbers, 30))  # Should return index 2
print(search_element(numbers, 60))  # Should return not found