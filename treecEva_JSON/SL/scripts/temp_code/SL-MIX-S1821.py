import re
from collections import deque

token_stream = "{ keyA=1 { keyB=2 keyC=3 } keyD=4 { keyE=5 { keyF=6 } } }"
tokens = re.findall(r'[{}]|\w+=\d*', token_stream)

stack = []  # Stack of dictionaries
final_checksum = 0

for token in tokens:
    if token == '{':
        stack.append({})
    elif token == '}':
        if stack:
            current_block = stack.pop()
            if len(current_block) == 3:
                xor_sum = 0
                for key in current_block:
                    for char in key:
                        xor_sum ^= ord(char)
                final_checksum ^= xor_sum
            if stack:
                # Merge current block into parent as a nested entry
                parent = stack[-1]
                parent.update(current_block)
    else:
        # Key-value pair
        if '=' in token:
            key, value = token.split('=')
            if stack:
                stack[-1][key] = int(value)

print(f"Result: {final_checksum}")