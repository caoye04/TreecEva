from collections import deque

def transform_layer(text_queue, operation_map):
    result_stack = []
    while text_queue:
        char = text_queue.popleft()
        op_code = ord(char) % 4
        transformed = operation_map[op_code](char)
        result_stack.append(transformed)
    return result_stack

def calculate_score(char_stack):
    score = 0
    while char_stack:
        item = char_stack.pop()
        score += (ord(item) << 2) if item.isalpha() else (ord(item) ^ 0xFF)
    return score

# Main processing pipeline
document_content = "Hello_World_2023"
processing_queue = deque(document_content)

# Operation mapping using ternary logic
ops = {
    0: lambda c: c.upper() if c.isalpha() else c,
    1: lambda c: c.lower() if c.isalpha() else chr(ord(c) ^ 0x0F),
    2: lambda c: '_' if c.isalpha() else c,
    3: lambda c: c
}

# Layer 1: Character transformation
transformed_chars = transform_layer(processing_queue, ops)

# Layer 2: Conditional filtering with short-circuit evaluation
filtered_chars = [c for c in transformed_chars if c.isalpha() or (not c.isalpha() and c != '_')]

# Layer 3: Score calculation with bitwise operations
char_stack = list(filtered_chars)
base_score = calculate_score(char_stack)

# Final adjustment using string operations and ternary operator
final_score = base_score + (len(document_content) << 3) if base_score > 1000 else base_score - (len(document_content) >> 1)

print(f"Result: {final_score}")