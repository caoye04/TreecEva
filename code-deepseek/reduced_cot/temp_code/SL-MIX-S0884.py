def calculate_metrics(data):
    total_items = sum(data.values())
    max_key = max(data.keys())
    min_key = min(data.keys())
    avg_value = total_items / len(data)
    
    # Distractor calculations
    temp_sum = sum(k * v for k, v in data.items())
    irrelevant_metric = (max_key + min_key) * 2
    
    return {'total': total_items, 'average': avg_value}

def transform_data(metrics):
    base_value = metrics['total']
    adjustment = metrics['average'] // 2
    
    # Intermediate calculations that don't affect final result
    intermediate = base_value * 3
    dummy_operation = intermediate - adjustment + 5
    
    result = base_value - adjustment
    return result

item_counts = {1: 8, 3: 12, 5: 6, 7: 14}
# Redundant operation that seems relevant
preliminary_sum = sum(item_counts.keys()) * 2

result = transform_data(calculate_metrics(item_counts))
target_value = result

print(f"Target result: {target_value}")