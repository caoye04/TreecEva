def process_metrics(entries, importance):
    total = 0
    base_offset = len(entries) * 0.5
    temp_results = []
    
    # Initialize auxiliary tracking (some used, some not)
    max_value = float('-inf')
    min_value = float('inf')
    running_squares = 0
    ignored_counter = 0
    
    for i, (key, value) in enumerate(entries.items()):
        # Irrelevant transformation
        transformed_key = key.upper().replace('_', '')
        ignored_counter += len(transformed_key)
        
        weight = importance.get(key, 1.0)
        adjusted = value * weight + base_offset
        
        if adjusted > 10:
            adjusted = adjusted / 2
        
        temp_results.append(adjusted)
        
        # Track real-time stats (only max used later)
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
        
        running_squares += value ** 2
    
    # Secondary loop with filtering
    filtered_vals = []
    for idx, val in enumerate(temp_results):
        if idx % 2 == 0 or val >= 6:
            filtered_vals.append(val)
    
    # Dummy aggregation (not affecting final score)
    avg_square = running_squares / len(entries) if entries else 0
    dummy_metric = sum(x**2 for x in filtered_vals) / len(filtered_vals) if filtered_vals else 0
    
    # Core logic: weighted sum with lambda-based correction
    correction_factor = (lambda x: x * 0.9 if x > 5 else x * 1.1)(max_value)
    total = sum(filtered_vals) + correction_factor
    
    # Final adjustment based on length and offset
    final_score = int(total - base_offset + len(importance))
    
    # Dead code branch (never executed under current inputs)
    if False:
        fallback = sum(entries.values())
        final_score = fallback * 2
    
    return final_score

# Input data
raw_data = {
    'latency': 8,
    'throughput': 12,
    'reliability': 4,
    'efficiency': 6
}

weights = {
    'latency': 0.8,
    'throughput': 1.2,
    'efficiency': 1.0
    # reliability has default weight
}

result = process_metrics(raw_data, weights)
print(f"Result: {result}")