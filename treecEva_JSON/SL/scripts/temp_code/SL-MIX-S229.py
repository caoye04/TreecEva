import math

def process_data(data):
    result = []
    for item in data:
        if isinstance(item, list):
            sub_result = 1
            for sub_item in item:
                if isinstance(sub_item, int):
                    sub_result *= sub_item
            result.append(sub_result)
        elif isinstance(item, dict):
            sub_result = 0
            for key, value in item.items():
                if isinstance(value, int):
                    sub_result += value * len(key)
            result.append(sub_result)
        else:
            result.append(0)
    return result

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for char in s:
        if char in vowels:
            transformed += char.upper()
        else:
            transformed += char.lower()
    return transformed

data = [
    [2, 3, 5],
    {'hello': 10, 'world': 20},
    [7, 11],
    {'python': 5, 'code': 15},
    'This is a Test String'
]

processed_numbers = process_data(data[:4])
transformed_string = transform_string(data[4])

# Calculate the sum of processed numbers
sum_processed = sum(processed_numbers)

# Calculate the length of the transformed string
len_transformed = len(transformed_string)

# Perform a complex mathematical operation
complex_calc = math.floor(math.sqrt(sum_processed * len_transformed) + math.log(sum_processed + 1))

# Bitwise operations
bitwise_result = (complex_calc & 0xFF) | (len_transformed << 2)

# Final calculation
final_result = (bitwise_result ^ sum_processed) % 1000

print(f'Result: {final_result}')