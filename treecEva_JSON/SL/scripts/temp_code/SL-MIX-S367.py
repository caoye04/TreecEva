import math

def transform_data(data):
    return {k: round(math.sqrt(v), 2) for k, v in data.items() if v > 0}

def aggregate_values(container):
    total = 0
    for key, value in container.items():
        if isinstance(value, dict):
            total += aggregate_values(value)
        elif isinstance(value, list):
            total += sum(value)
        else:
            total += value
    return total

# Initial complex nested data structure
raw_data = {
    'group1': {
        'a': 16,
        'b': -4,
        'c': 25
    },
    'group2': [
        3, 5, 7, {'nested': 9}
    ],
    'group3': {
        'x': 36,
        'y': {
            'deep': 49,
            'deeper': [2, 4, 6]
        },
        'z': -9
    }
}

# Step 1: Transform positive values in group1
processed_group1 = transform_data(raw_data['group1'])

# Step 2: Process group2 elements
processed_group2 = []
for item in raw_data['group2']:
    if isinstance(item, dict):
        processed_group2.append({k: v*2 for k, v in item.items()})
    else:
        processed_group2.append(item ** 2)

# Step 3: Deep process group3
processed_group3 = {}
for k, v in raw_data['group3'].items():
    if isinstance(v, dict):
        processed_group3[k] = {}
        for sub_k, sub_v in v.items():
            if isinstance(sub_v, list):
                processed_group3[k][sub_k] = [i**3 for i in sub_v]
            else:
                processed_group3[k][sub_k] = math.factorial(int(math.sqrt(sub_v)))
    elif v > 0:
        processed_group3[k] = math.log(v, 2)

# Step 4: Reconstruct data
restructured_data = {
    'processed_group1': processed_group1,
    'processed_group2': processed_group2,
    'processed_group3': processed_group3
}

# Step 5: Calculate final result
intermediate_sum = aggregate_values(restructured_data)
final_result = int(intermediate_sum * 100) % 1000

print(f'Result: {final_result}')