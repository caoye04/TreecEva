import math

def process_nested_data(data_structure):
    result = 0
    for level1 in data_structure:
        if isinstance(level1, list):
            for level2 in level1:
                if isinstance(level2, dict):
                    for key, value in level2.items():
                        if isinstance(value, str) and value.isdigit():
                            result += int(value) * 2
                        elif isinstance(value, list):
                            result += sum([x**2 for x in value if isinstance(x, (int, float))])
                elif isinstance(level2, (int, float)):
                    result += math.floor(math.sqrt(abs(level2)))
        elif isinstance(level1, dict):
            for k, v in level1.items():
                if isinstance(v, str) and len(v) > 3:
                    result += len(v) * 3
    return result

def transform_string(s):
    parts = s.split('-')
    transformed = []
    for part in parts:
        if part.isalpha():
            transformed.append(part.upper()[::-1])
        elif part.isdigit():
            transformed.append(str(int(part) ^ 15))  # XOR with 15
    return ''.join(transformed)

# Initialize complex nested data structure
complex_data = [
    [16, 25, {'a': '123', 'b': [2, 3, 4]}, "ignored_text"],
    {'key1': 'hello', 'key2': 'world'},
    [9, 36, {'nested': {'deep': [5, 6]}, 'values': '456'}],
    "separate-string-data"
]

# Perform initial processing
initial_sum = process_nested_data(complex_data)

# String transformation step
transformed_str = transform_string("abc-123-xyz-456")

# Convert transformed string characters to ASCII values and sum them
ascii_sum = sum(ord(c) for c in transformed_str)

# Perform bitwise operations
bitwise_result = (initial_sum & 0xFF) | (ascii_sum >> 2)

# Mathematical computation
computed_value = math.log(math.e**3) * math.sin(math.pi/2) + math.cos(0)

# Combine results with advanced operations
intermediate_result = int((bitwise_result ^ int(computed_value)) * 1.618033988749)  # Golden ratio

# Execution point Y
final_result = ((intermediate_result << 2) - (intermediate_result >> 1)) % 1000

print(f"Result: {final_result}")