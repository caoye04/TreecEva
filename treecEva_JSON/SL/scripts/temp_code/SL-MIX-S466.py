import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def aggregate_stats(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return {
        'sum': total,
        'mean': mean,
        'variance': variance,
        'std_dev': math.sqrt(variance)
    }

def process_nested_structure(structure):
    output = {}
    for key, value in structure.items():
        if isinstance(value, list):
            transformed = complex_transform(value)
            stats = aggregate_stats(transformed)
            output[key] = stats
        elif isinstance(value, dict):
            output[key] = process_nested_structure(value)
        else:
            output[key] = value * 3
    return output

data_structure = {
    'group_a': [4, -9, 16, -25, 36],
    'group_b': {
        'subgroup_1': [1, -4, 9, -16],
        'subgroup_2': 7
    },
    'group_c': 5
}

processed = process_nested_structure(data_structure)

# Calculate final result based on processed data
a_sum = processed['group_a']['sum']
b_mean = processed['group_b']['subgroup_1']['mean']
c_value = processed['group_c']

intermediate = (a_sum * b_mean) % (c_value ** 2)
final_result = int(intermediate) ^ 0xFF

print(f"Result: {final_result}")