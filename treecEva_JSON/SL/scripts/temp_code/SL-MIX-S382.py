import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, dict):
            result += process_nested_data(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    result += item
                elif isinstance(item, str):
                    result += len(item)
        elif isinstance(value, int):
            result += value
    return result

def calculate_advanced_ops(x, y):
    a = math.pow(x, 2) + math.log(y) if y > 0 else 0
    b = math.sin(x) * math.cos(y)
    c = int(a) ^ int(b)  # bitwise XOR
    return c

def manipulate_strings(strings):
    combined = ''.join(strings)
    unique_chars = set(combined)
    return len(unique_chars) * sum(ord(c) for c in unique_chars)

# Main execution starts here
nested_data = {
    'level1': {
        'level2a': [10, 'hello', 20],
        'level2b': {
            'level3': [30, 'world', 40]
        }
    },
    'direct_list': [50, 'test', 60],
    'direct_int': 70
}

string_list = ['abc', 'def', 'ghi', 'abc']

# Step 1: Process nested data
processed_value = process_nested_data(nested_data)

# Step 2: Perform advanced mathematical operations
advanced_result = calculate_advanced_ops(processed_value, 100)

# Step 3: Manipulate strings
string_result = manipulate_strings(string_list)

# Step 4: Complex calculation combining all results
intermediate = (advanced_result << 2) + (string_result >> 1)  # Bitwise shifts
final_result = ((intermediate & 0xFF) | 0x100) ^ 0xAA  # Complex bitwise operations

print(f'Result: {final_result}')