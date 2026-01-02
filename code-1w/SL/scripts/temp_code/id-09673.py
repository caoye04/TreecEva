def calculate_performance(data):
    base_points = 0
    bonus_multiplier = 1.0
    penalty_count = 0
    temp_result = 0
    final_score = 0
    
    # Process each test case in benchmark data
    for entry in data:
        category = entry['type']
        value = entry['value']
        status = entry['status']
        
        if category == 'arithmetic':
            base_points += value * 2
            if status == 'optimized':
                bonus_multiplier += 0.1
        elif category == 'boolean':
            base_points += value
            if not entry.get('short_circuit', True):
                penalty_count += 1
        elif category == 'assignment':
            # Simulate unpacking overhead
            a, b = value, value + 1
            base_points += (a + b) // 2
        
        # Irrelevant string processing (distractor)
        debug_info = f"Processing {category.upper()} with value {str(value).zfill(3)}"
        log_entry = debug_info.replace('P', 'p').split(' ')[-1]
        temp_result += len(log_entry)

    # Additional distraction: unused helper calculation
    avg_penalty = penalty_count / len(data) if data else 0
    projected_gain = base_points * bonus_multiplier
    
    # Actual scoring logic
    final_score = int(projected_gain - (penalty_count * 5))
    
    # Dead code path (never executed due to logic)
    if False and avg_penalty > 100:
        final_score = max(final_score, 500)
        
    return final_score

# Benchmark dataset
benchmark_data = [
    {'type': 'arithmetic', 'value': 15, 'status': 'optimized'},
    {'type': 'boolean', 'value': 8, 'status': 'normal', 'short_circuit': False},
    {'type': 'assignment', 'value': 12, 'status': 'normal'},
    {'type': 'arithmetic', 'value': 20, 'status': 'normal'},
    {'type': 'boolean', 'value': 10, 'status': 'normal', 'short_circuit': True}
]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")