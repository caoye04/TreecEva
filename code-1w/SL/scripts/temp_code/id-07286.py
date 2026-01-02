def calculate_performance(data_map):
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    
    # Irrelevant tracking variables (distractors)
    debug_log = []
    temp_accumulator = 0
    snapshot_interval = 3
    
    for entry in data_map['records']:
        raw_value = entry['value']
        status_flag = entry['status']
        
        # Semi-relevant preprocessing (some used, some not)
        normalized = raw_value / data_map['scaling_factor'] if data_map['scaling_factor'] > 0 else 0
        is_critical = status_flag == 'CRITICAL'
        is_active = status_flag in ['ACTIVE', 'CRITICAL']
        
        # Conditional expression usage (required feature)
        base_increment = 10 if is_active else 5
        
        # Actual score logic
        base_score += base_increment * normalized
        
        # Misleading penalty system that's only partially applied
        if is_critical:
            penalty_adjustment -= 2
            if normalized > 50:
                penalty_adjustment -= 3

        # Dead code path (irrelevant)
        if raw_value < 0:
            temp_accumulator += abs(raw_value)
            debug_log.append(f"Negative value: {raw_value}")

        # Early return red herring (never triggered due to data)
        if len(debug_log) > 100:
            return -1  # unreachable

    # Bonus logic based on record count (semi-relevant)
    record_count = len(data_map['records'])
    if record_count > 4:
        bonus_multiplier = 1.2
    elif record_count == 3:
        bonus_multiplier = 1.1

    # Final calculation with key variable
    final_score = int((base_score + penalty_adjustment) * bonus_multiplier)
    
    # Unused aggregation (distractor)
    average_normalized = base_score / record_count if record_count else 0
    consistency_ratio = average_normalized / (final_score if final_score != 0 else 1)

    return final_score

# Setup input data
benchmark_data = {
    'scaling_factor': 2,
    'records': [
        {'value': 40, 'status': 'ACTIVE'},
        {'value': 60, 'status': 'CRITICAL'},
        {'value': 50, 'status': 'INACTIVE'},
        {'value': 70, 'status': 'ACTIVE'},
        {'value': 30, 'status': 'CRITICAL'}
    ]
}

# Execute and print result
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")