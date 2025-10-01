import math

def compute_weighted_sum(data_dict):
    total = 0
    for key, values in data_dict.items():
        weight = len(key)
        for idx, val in enumerate(values):
            if isinstance(val, int) and val % 2 == 0:
                total += val * weight * (idx + 1)
            elif isinstance(val, float):
                total += int(math.floor(val)) * weight
    return total

data_structure = [
    {
        'alpha': [2, 3.5, 4, 7],
        'beta': [1.2, 8, 10, 15]
    },
    {
        'gamma': [6, 9.9, 12],
        'delta': [5, 14, 3.3, 16]
    }
]

# Flatten the list of dictionaries into one dictionary
flattened = {}
for d in data_structure:
    flattened.update(d)

# Perform weighted sum calculation
intermediate_sum = compute_weighted_sum(flattened)

# Apply transformation using trigonometric functions
angle_rad = math.radians(60)
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
transformed_value = round(intermediate_sum * sin_val / cos_val)

# Bitwise operations
shift_amount = 2
masked_value = transformed_value & ((1 << 6) - 1)  # Mask to last 6 bits
shifted_value = masked_value >> shift_amount

# Final computation combining previous results
final_result = (shifted_value ^ 0xF) + 1
print(f'Result: {final_result}')