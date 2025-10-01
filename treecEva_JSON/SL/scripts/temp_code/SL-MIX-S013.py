import math

def complex_transform(data_dict):
    result = 0
    for key, value in data_dict.items():
        if isinstance(value, list):
            temp = sum(value)
            result += temp * len(key)
        elif isinstance(value, dict):
            nested_sum = sum(v for v in value.values() if isinstance(v, (int, float)))
            result += nested_sum * len(str(key))
        else:
            result += value if isinstance(value, (int, float)) else 0
    return result

def process_nested_structure(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += process_nested_structure(item)
        elif isinstance(item, dict):
            total += complex_transform(item)
        elif isinstance(item, (int, float)):
            total += item * 2
    return total

data = {
    'alpha': [1, 2, 3, [4, 5]],
    'beta': {
        'gamma': [6, 7],
        'delta': {
            'epsilon': 8,
            'zeta': [9, 10, 11]
        }
    },
    'gamma': 12,
    'delta': [
        {
            'theta': 13,
            'iota': [14, 15]
        },
        [
            {
                'kappa': [16, 17],
                'lambda': {
                    'mu': 18,
                    'nu': [19, 20]
                }
            }
        ]
    ]
}

# Stage 1: Process the main data structure
stage1_result = complex_transform(data)

# Stage 2: Apply mathematical transformations
stage2_result = math.pow(stage1_result, 1.5) // 100

# Stage 3: Process nested structures
stage3_result = process_nested_structure(data['delta'])

# Stage 4: Combine results with bitwise operations
combined = int(stage2_result) ^ (stage3_result & 0xFF)

# Stage 5: Final calculation
final_result = ((combined << 2) + (stage1_result % 7) - (int(math.sqrt(stage3_result)) & 0xF)) // 3

print(f'Result: {final_result}')