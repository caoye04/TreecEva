import math

def process_data(data):
    transformed = []
    for key, values in data.items():
        if isinstance(values, list):
            squared = [x**2 for x in values if isinstance(x, (int, float))]
            transformed.append({
                'key': key.upper(),
                'sum_of_squares': sum(squared),
                'sqrt_of_sum': math.sqrt(sum(squared)) if sum(squared) >= 0 else 0
            })
        elif isinstance(values, dict):
            sub_sum = sum(v for v in values.values() if isinstance(v, (int, float)))
            transformed.append({
                'key': key.lower(),
                'sub_sum': sub_sum,
                'log_sub_sum': math.log(sub_sum) if sub_sum > 0 else 0
            })
    return transformed

def calculate_final(processed):
    total = 0
    for item in processed:
        if 'sum_of_squares' in item:
            total += item['sum_of_squares'] * 0.5
        elif 'sub_sum' in item:
            total += item['sub_sum'] * 2
    return round(total)

# Main execution
raw_data = {
    'alpha': [1, 2, 3, 'skip', 4],
    'beta': {'x': 5, 'y': 10, 'z': 'ignore'},
    'gamma': [2.5, 3.5, -1],
    'delta': {'m': 0, 'n': 20}
}

processed_data = process_data(raw_data)
weight_factor = math.ceil(math.sqrt(17))
adjusted_data = [
    {**item, 'weighted': item.get('sum_of_squares', 0) * weight_factor if 'sum_of_squares' in item else item.get('sub_sum', 0) * weight_factor}
    for item in processed_data
]

final_result = calculate_final(adjusted_data) + len(adjusted_data) * 10
print(f'Result: {final_result}')