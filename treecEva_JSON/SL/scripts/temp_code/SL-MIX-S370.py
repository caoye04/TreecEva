import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, str):
                temp.append(len(val) * (i + 1))
            elif isinstance(val, int):
                temp.append(val ** (j + 1))
            elif isinstance(val, float):
                temp.append(int(math.ceil(val)))
        result.append(sum(temp))
    return result

def calculate_checksum(numbers):
    checksum = 0
    for i, num in enumerate(numbers):
        checksum ^= (num << (i % 5))
    return checksum

data_structure = [
    ["hello", 2, 3.14, "world"],
    [4, "test", 5.67, 2, "end"],
    ["a", 7, 8.91, "bc", 10, 11.12]
]

processed_data = process_nested_data(data_structure)
checksum_value = calculate_checksum(processed_data)

# Bitwise manipulation with rotation
rotated_checksum = ((checksum_value >> 3) | (checksum_value << 29)) & 0xFFFFFFFF

# Mathematical transformation
log_value = math.log(rotated_checksum + 1, 2)
adjusted_value = int(log_value) ^ 0xFF

# Final calculation combining all transformations
final_result = (adjusted_value * 3) + (checksum_value % 17) - (len(processed_data) * 5)

print(f"Result: {final_result}")