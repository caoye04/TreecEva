def calculate_performance(data):
    # Irrelevant transformation (distractor)
    temp_offsets = [x * 0.1 for x in data if x > 5]
    
    # Core logic: filter, transform, reduce
    filtered = list(filter(lambda x: x % 2 == 1, data))
    
    # Secondary distractor: unused computation
    stats = {
        'max_val': max(data),
        'min_val': min(data),
        'range': max(data) - min(data)
    }
    
    # Semi-relevant but not used directly
    adjusted = [x + 2 for x in filtered if x < 15]
    
    # Actual critical computation chain
    base_score = sum(filtered)
    penalty = len([x for x in data if x < 0]) * 3
    bonus = len(adjusted) * 2
    
    # Red herring: complex-looking but unused expression
    derived_metric = (sum(temp_offsets) + stats['range']) / (len(temp_offsets) + 1) if temp_offsets else 0
    
    # Final determination
    final_score = base_score - penalty + bonus
    return final_score

# Input data with mixed properties
benchmark_data = [3, -2, 7, 4, 9, -5, 11, 6, 13, 8, 15]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")