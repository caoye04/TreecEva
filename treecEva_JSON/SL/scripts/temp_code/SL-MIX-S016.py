import math

def process_data(data):
    total = 0
    for key, values in data.items():
        if isinstance(values, list):
            for i, val in enumerate(values):
                if i % 2 == 0:
                    total += val ** 2
                else:
                    total -= math.sqrt(abs(val))
        elif isinstance(values, dict):
            for sub_key, sub_val in values.items():
                if sub_key.startswith('pos'):
                    total += sub_val * 3
                else:
                    total -= sub_val // 2
    return int(total)

data_structure = {
    'group1': [4, -9, 2, 16, -25],
    'group2': {
        'pos_a': 7,
        'neg_b': 14,
        'pos_c': 5
    },
    'group3': [1, -4, 9, -16]
}

# Perform initial processing
interim_result = process_data(data_structure)

# Apply transformation using bitwise operations
transformed = interim_result << 2  # Left shift by 2 (equivalent to multiply by 4)
transformed ^= 0xFF  # XOR with 255

# String manipulation segment
message = "The value is {} after transformations"
formatted_msg = message.format(transformed)
char_sum = sum(ord(c) for c in formatted_msg if c.isdigit())

# Final calculation combining all previous results
final_result = (transformed + char_sum) % 1000
print(f"Result: {final_result}")