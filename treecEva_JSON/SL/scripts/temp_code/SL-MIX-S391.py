import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if isinstance(val, str):
            transformed.append(len(val) ^ (i + 1))
        elif isinstance(val, int):
            transformed.append(val * 2 if val % 2 == 0 else val * 3)
        else:
            transformed.append(int(math.sqrt(abs(val)) * 10))
    return transformed

def process_nested(container):
    results = []
    for item in container:
        if isinstance(item, list):
            results.append(sum(complex_transform(item)))
        elif isinstance(item, dict):
            temp = 0
            for k, v in item.items():
                temp += len(k) * v if isinstance(v, int) else int(ord(str(v)[0]))
            results.append(temp)
        else:
            results.append(item.bit_length() if isinstance(item, int) else 0)
    return results

# Initial data structures
matrix = [
    ["hello", 4, -9.64],
    {"key1": 5, "key2": "value"},
    2048,
    ["a", 7, 16.0, "xyz"]
]

# Transformation pipeline
stage1 = process_nested(matrix)
stage2 = [x for x in stage1 if x > 10]
stage3 = [(x & 0xFF) ^ (x >> 8) for x in stage2]

# Mathematical processing
accumulator = 0
for i, val in enumerate(stage3):
    accumulator += val * math.factorial(i) if i < 4 else val

# Final aggregation
result = accumulator % 1000
bytes_data = bytes([result])
encoded = ''.join(format(x, '02x') for x in bytes_data)
result = int(encoded, 16)  # END OF COMPUTATION

print(f"Result: {result}")