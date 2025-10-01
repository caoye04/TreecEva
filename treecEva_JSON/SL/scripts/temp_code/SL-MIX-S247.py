import math

def process_nested_data(data_structure, depth=0):
    if isinstance(data_structure, dict):
        total = 0
        for key, value in data_structure.items():
            if isinstance(value, (list, dict)):
                total += process_nested_data(value, depth + 1)
            else:
                total += value * (depth + 1)
        return total
    elif isinstance(data_structure, list):
        return sum(process_nested_data(item, depth + 1) for item in data_structure)
    else:
        return data_structure * (depth + 1)

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for i, char in enumerate(s):
        if char in vowels:
        	# Shift vowel by its position in string
            shifted = chr((ord(char) - ord('A' if char.isupper() else 'a') + i) % 26 + ord('A' if char.isupper() else 'a'))
            transformed += shifted
        else:
            # For consonants, use bitwise XOR with position
            xor_val = ord(char) ^ i
            transformed += chr(xor_val % 26 + ord('a'))
    return transformed

# Complex nested data structure
complex_data = {
    'level1': {
        'level2a': [1, 2, {'inner': [3, 4]}, 5],
        'level2b': {
            'level3': [6, 7, [8, 9]]
        }
    },
    'another_branch': [10, {'nested_dict': {'deep_value': 11}}, 12]
}

# Mathematical calculations
pi_approx = math.pi
e_approx = math.e

# String transformations
original_string = "HelloWorld"
transformed = transform_string(original_string)

# Calculate string hash value
string_hash = sum(ord(c) for c in transformed)

# Perform complex calculation using multiple values
base_value = process_nested_data(complex_data)
fib_value = fibonacci(10)  # 10th Fibonacci number

# TARGET ASSIGNMENT
result = (base_value * fib_value + string_hash) % (int(pi_approx * 10) + int(e_approx * 7))

# Additional operations to increase complexity
temp_list = [result, base_value, fib_value, string_hash]
filtered_values = [x for x in temp_list if x > 50]
squared_values = list(map(lambda x: x**2, filtered_values))
final_sum = sum(squared_values)

result = result + (final_sum >> 2)  # Right shift by 2 is equivalent to dividing by 4

print(f"Result: {result}")