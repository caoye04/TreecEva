import math

def transform_data(data):
    transformed = []
    for item in data:
        if isinstance(item, dict):
            temp = {}
            for k, v in item.items():
                if isinstance(v, list):
                    temp[k] = [x**2 for x in v if x > 0]
                elif isinstance(v, str):
                    temp[k] = v[::-1].upper()
                else:
                    temp[k] = v * 2
            transformed.append(temp)
        else:
            transformed.append(item * 3)
    return transformed

def calculate_metrics(transformed_data):
    metrics = {}
    total_sum = 0
    count = 0
    for item in transformed_data:
        if isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, list):
                    total_sum += sum(v)
                    count += len(v)
                elif isinstance(v, (int, float)):
                    total_sum += v
                    count += 1
        elif isinstance(item, (int, float)):
            total_sum += item
            count += 1
    metrics['mean'] = total_sum / count if count else 0
    metrics['total'] = total_sum
    return metrics

# Main execution
raw_data = [
    {'values': [1, -2, 3, 4], 'name': 'alpha', 'factor': 2.5},
    {'values': [-1, -3], 'name': 'beta', 'factor': 1.0},
    {'values': [2, 3, -4, 5], 'name': 'gamma', 'factor': 3.14},
    42,
    -7
]

step1_result = transform_data(raw_data)
step2_metrics = calculate_metrics(step1_result)

# Additional complex processing
aggregated = 0
for item in step1_result:
    if isinstance(item, dict):
        list_sum = sum([sum(v) if isinstance(v, list) else 0 for v in item.values()])
        factor = item.get('factor', 1)
        name_length = len(item.get('name', ''))
        aggregated += list_sum * factor + name_length
    else:
        aggregated += math.sqrt(abs(item)) * 2

final_result = int(aggregated + step2_metrics['mean'] * 10)
print(f'Result: {final_result}')