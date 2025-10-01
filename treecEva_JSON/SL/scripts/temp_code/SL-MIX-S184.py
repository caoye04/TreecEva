import math

def transform_data(data):
    transformed = []
    for item in data:
        if isinstance(item, int):
            transformed.append(item ** 2)
        elif isinstance(item, str):
            transformed.append(len(item))
        elif isinstance(item, list):
            transformed.append(sum(item))
        else:
            transformed.append(0)
    return transformed

def calculate_checksum(values):
    checksum = 0
    for i, val in enumerate(values):
        checksum += (i + 1) * val
    return checksum

data_structure = [
    [1, 2, 3],
    "hello",
    5,
    [10, 20],
    "world!",
    3.5,
    [7, 14, 21]
]

# Step 1: Transform the data structure
step1_result = transform_data(data_structure)

# Step 2: Apply a mathematical transformation
step2_result = [math.sqrt(x) if x > 0 else 0 for x in step1_result]

# Step 3: Calculate checksum
checksum = calculate_checksum(step2_result)

# Step 4: Bitwise operations
bitwise_result = int(checksum) & 0xFF

# Step 5: Final calculation
final_result = (bitwise_result ^ 0xAA) + sum([ord(c) for c in "RESULT"])

print(f"Result: {final_result}")