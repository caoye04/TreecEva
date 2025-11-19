from collections import deque
from functools import reduce

def process_pipeline(text):
    words = text.split()
    stack = []
    queue = deque()
    
    # Push words onto stack in reverse order
    for word in words:
        stack.append(word[::-1])
    
    # Pop from stack and enqueue characters with shift
    while stack:
        word = stack.pop()
        for char in word:
            shifted = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            queue.append(shifted)
    
    # Convert queue to string
    encrypted = ''.join(queue)
    
    # Divide and conquer approach to transform
    def transform(s):
        if len(s) <= 2:
            return s.upper()
        mid = len(s) // 2
        left = transform(s[:mid])
        right = transform(s[mid:])
        return right + left
    
    transformed = transform(encrypted)
    
    # Apply functional transformation
    chars = list(transformed)
    ascii_values = list(map(ord, chars))
    doubled = list(map(lambda x: x * 2, ascii_values))
    final_sum = reduce(lambda a, b: a ^ b, doubled)
    
    return final_sum

input_text = "hello world python code"
target_result = process_pipeline(input_text)
print(f"Target result: {target_result}")