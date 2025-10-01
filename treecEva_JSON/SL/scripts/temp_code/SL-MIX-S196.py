import math

def complex_transform(data_list):
    transformed = []
    for i, item in enumerate(data_list):
        if isinstance(item, str):
            # Convert string to ASCII sum then apply logarithm
            ascii_sum = sum(ord(c) for c in item)
            transformed.append(int(math.log(ascii_sum) * 100))
        elif isinstance(item, int):
            # Apply bitwise operations
            transformed.append((item << 2) ^ 0xF)
        elif isinstance(item, float):
            # Apply trigonometric function and rounding
            transformed.append(round(math.sin(item) * 1000))
        else:
            transformed.append(0)
    return transformed

def nested_dict_processor(data_dict):
    total = 0
    for key, value in data_dict.items():
        if isinstance(value, list):
            processed_list = complex_transform(value)
            total += sum(processed_list) ^ (len(processed_list) & 0xFF)
        elif isinstance(value, dict):
            # Recursive processing with multiplier based on key length
            sub_total = nested_dict_processor(value)
            total += sub_total * len(key)
        else:
            total += hash(str(value)) % 1000
    return total

# Initialize complex nested data structure
data = {
    'level1': [
        'hello',
        42,
        3.14159,
        {
            'level2': [
                'world',
                100,
                2.71828,
                {
                    'level3': [
                        'nested',
                        255,
                        1.41421
                    ]
                }
            ]
        }
    ],
    'another_key': [
        'test',
        99,
        1.73205
    ],
    'simple': 'value'
}

# Process the data through multiple transformation layers
intermediate_result = nested_dict_processor(data)

# Apply mathematical transformations
scaled_result = intermediate_result * math.sqrt(2) / 100

# Bitwise manipulation with prime number
prime = 1009
bitwise_result = (int(scaled_result) & 0xFFFF) | (prime << 4)

# Final calculation step
result = (bitwise_result ^ 0xAAAA) + (intermediate_result % 97)

print(f"Result: {result}")