def calculate_performance(base, data):
    adjust = lambda x: x * 1.5 if x > base else x * 0.8
    processed = {k: adjust(v) for k, v in data.items()}
    
    # Irrelevant intermediate variable (minor distraction)
    temp_values = [v for v in processed.values()]
    
    total = sum(processed.values())
    count = len(processed)
    average = total / count
    
    # Secondary adjustment based on set membership
    categories = set(data.keys())
    bonus_category = {'throughput', 'latency', 'bandwidth'}
    bonus_applied = len(categories & bonus_category)
    
    final_score = average + (bonus_applied * 2.5)
    return final_score

baseline = 75
metrics = {
    'throughput': 80,
    'latency': 60,
    'error_rate': 40,
    'bandwidth': 90
}

final_score = calculate_performance(baseline, metrics)
print(f"Target result: {final_score}")