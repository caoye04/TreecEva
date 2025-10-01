import math

def transform_data(data_dict):
    processed = []
    for key, values in data_dict.items():
        sub_result = 0
        for i, val in enumerate(values):
            if isinstance(val, int):
                sub_result += (val ^ (i << 1))
            elif isinstance(val, str):
                sub_result += len(val) * ord(val[0])
        processed.append(sub_result)
    return processed

def compute_score(arr):
    score = 0
    for i in range(len(arr)):
        score += arr[i] * (math.factorial(i) if i < 4 else i**3)
    return score

data = {
    'alpha': [12, 'hello', 7, 'world'],
    'beta': [3, 'test', 15, 'data', 9],
    'gamma': ['sample', 25, 4]
}

transformed = transform_data(data)
score = compute_score(transformed)

# Perform modular arithmetic and bit operations
intermediate = (score & 0xFF) | ((score >> 8) & 0xFF)

# String manipulation and final calculation
hex_str = hex(intermediate)[2:]
final_sum = sum(int(c, 16) for c in hex_str if c.isdigit())

# TARGET POINT
result = (final_sum * 3) + (intermediate % 7)

print(f"Result: {result}")