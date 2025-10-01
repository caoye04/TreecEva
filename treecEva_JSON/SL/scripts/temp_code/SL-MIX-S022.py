import math

def process_nested_data(data):
    total = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for j, val in enumerate(sublist):
                if isinstance(val, int) and val > 0:
                    total += val * (j + 1)
        else:
            temp_sum = sum(x for x in sublist if isinstance(x, (int, float)))
            total += int(math.sqrt(temp_sum)) if temp_sum >= 0 else 0
    return total

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for i, char in enumerate(s):
        if char in vowels:
            transformed += str(i)
        elif char.isalpha():
            transformed += char.upper()
        else:
            transformed += char
    return transformed

data_structure = [
    [1, -2, 3, 'a', 4],
    [4.5, 2.5, 'hello', -1],
    [0, 5, 6, None, 7],
    ['world', 3.0, 4.0, 5.0]
]

string_input = "Hello, Beautiful World!"

processed_number = process_nested_data(data_structure)
transformed_string = transform_string(string_input)

# Extract digits from transformed string and sum them
extracted_digits = [int(ch) for ch in transformed_string if ch.isdigit()]
digit_sum = sum(extracted_digits)

# Perform bit shifting operations
shifted_value = (processed_number << 2) ^ digit_sum

# Final complex calculation
final_result = (shifted_value & 255) + (math.factorial(4) // 10) - len(transformed_string)

print(f"Result: {final_result}")