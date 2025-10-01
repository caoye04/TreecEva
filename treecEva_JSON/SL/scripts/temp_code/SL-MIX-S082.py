import math

def process_nested_data(data):
    transformed = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                temp.append(val ** 2 if i % 2 == 0 else math.factorial(val))
            elif isinstance(val, str):
                temp.append(len(val) * (i + 1))
        transformed.append(temp)
    return transformed

def calculate_weighted_sum(matrix):
    total = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            weight = (i + 1) * (j + 1)
            total += value * weight
    return total

def apply_bitwise_operations(value, shifts):
    shifted = value
    for shift in shifts:
        if shift > 0:
            shifted = shifted << shift
        else:
            shifted = shifted >> abs(shift)
    return shifted & 0xFF

# Main execution starts here
nested_data = [
    [3, 'hello', 2],
    ['world', 4, 'test'],
    [5, 6, 'final']
]

processed_data = process_nested_data(nested_data)
weighted_sum = calculate_weighted_sum(processed_data)
bitwise_shifts = [2, -1, 3, -2]
intermediate_result = apply_bitwise_operations(weighted_sum, bitwise_shifts)

# Perform trigonometric transformation
angle_rad = math.radians(intermediate_result % 360)
sine_value = math.sin(angle_rad)
cosine_value = math.cos(angle_rad)
trig_sum = sine_value + cosine_value

# Final calculation step
result = int((trig_sum * 1000) + intermediate_result) ^ 0xAA

print(f"Result: {result}")