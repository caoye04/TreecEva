import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp_sum = sum(sublist)
        transformed = [(x ** 2) + math.log(x + 1) for x in sublist if x > 0]
        if transformed:
            avg_transformed = sum(transformed) / len(transformed)
            result.append((temp_sum << 2) ^ int(avg_transformed))
        else:
            result.append(temp_sum ** 3)
    return result

def calculate_checksum(numbers):
    checksum = 0
    for num in numbers:
        checksum ^= (num & 0xFF) | ((num >> 8) & 0xFF)
    return checksum

data_structure = [
    [1, 2, 3],
    [4, -1, 5],
    [0, 6, 7, 8],
    [-2, -3],
    [9, 10]
]

processed_data = process_nested_data(data_structure)
checksum_val = calculate_checksum(processed_data)

# Apply final transformation
final_result = (checksum_val * 3) + (checksum_val >> 2) - (checksum_val & 0xF)

print(f"Result: {final_result}")