from functools import reduce

def process_readings():
    sensor_data = [
        {'type': 'A', 'raw_values': [23.5, 24.1, 22.8]},
        {'type': 'B', 'raw_values': [19.2, 20.0, 18.9]},
        {'type': 'A', 'raw_values': [25.3, 26.0, 24.7]}
    ]
    
    correction_map = {
        'A': 1.05,
        'B': 0.95
    }
    
    score_func = lambda x, corr: round(sum(x) * corr / len(x), 2)
    
    processed_scores = []
    for sensor in sensor_data:
        sensor_type = sensor['type']
        values = sensor['raw_values']
        correction = correction_map.get(sensor_type, 1.0)
        score = score_func(values, correction)
        processed_scores.append(score)
    
    # Apply additional transformation using list comprehension
    adjusted_scores = [s * 1.1 if s > 22 else s * 0.95 for s in processed_scores]
    
    # Compute average using reduce
    avg_score = reduce(lambda a, b: a + b, adjusted_scores) / len(adjusted_scores)
    
    # Determine stability index using ternary operator and short-circuit
    threshold = 23.0
    is_stable = avg_score >= threshold and len([s for s in adjusted_scores if s < 20]) == 0
    
    # Final calculation using conditional assignment
    final_stability_index = avg_score * 2 if is_stable else avg_score * 0.5
    
    return final_stability_index

final_stability_index = process_readings()
print(f"Result: {final_stability_index}")