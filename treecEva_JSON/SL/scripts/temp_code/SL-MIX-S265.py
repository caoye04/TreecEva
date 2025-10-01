import math

def transform_data(data):
    transformed = []
    for item in data:
        if isinstance(item, dict):
            temp = {}
            for k, v in item.items():
                if isinstance(v, list):
                    temp[k] = sum(v)
                else:
                    temp[k] = v * 2
            transformed.append(temp)
        elif isinstance(item, list):
            transformed.append([x**2 for x in item])
        elif isinstance(item, tuple):
            transformed.append(tuple(x + 1 for x in item))
        else:
            transformed.append(item)
    return transformed

def calculate_metrics(transformed):
    metrics = {}
    total_sum = 0
    element_count = 0
    for item in transformed:
        if isinstance(item, dict):
            for v in item.values():
                total_sum += v
                element_count += 1
        elif isinstance(item, list):
            total_sum += sum(item)
            element_count += len(item)
        elif isinstance(item, tuple):
            total_sum += sum(item)
            element_count += len(item)
        else:
            total_sum += item
            element_count += 1
    metrics['average'] = total_sum / element_count if element_count else 0
    metrics['sum'] = total_sum
    return metrics

data_structure = [
    {'a': [1, 2, 3], 'b': 4},
    [2, 3, 4],
    (5, 6),
    7,
    {'c': [10, 20], 'd': 3, 'e': [1, 1, 1]}
]

transformed_data = transform_data(data_structure)
metrics = calculate_metrics(transformed_data)

# Perform advanced computation using metrics
log_avg = math.log(metrics['average']) if metrics['average'] > 0 else 0
exp_sum = math.exp(metrics['sum'] % 10) if metrics['sum'] > 0 else 1

# Bitwise operations
bitwise_result = int(log_avg) & int(exp_sum)

# Final complex calculation
final_result = (bitwise_result ** 2) + (int(log_avg) | int(exp_sum)) - (metrics['sum'] // 10)
print(f"Result: {final_result}")