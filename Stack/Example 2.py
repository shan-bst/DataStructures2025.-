# Example 2: Using Stack to Reverse a String
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Demonstrating String Reversal
input_string = "hello"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))