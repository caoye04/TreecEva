def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = {}

    for key in records:
        if key in importance_weights:
            raw_value = len(records[key]) * importance_weights[key]
            
            # Irrelevant string processing (distractor)
            processed_key = key.upper().replace('_', '').strip()
            key_length_sum = sum(ord(c) for c in processed_key)
            
            # Real logic begins
            if 'error' not in records[key] and 'fail' not in records[key]:
                base_score += raw_value
                if raw_value > 10:
                    bonus_tracker.append(raw_value * 0.1)
            else:
                penalty_adjustment -= 2
    
    # Distractor: unused dictionary operation
    temp_result['max_key_ascii'] = key_length_sum if 'key_length_sum' in locals() else 0
    
    # Actual aggregation
    total_bonus = sum(bonus_tracker)
    final_score = int(base_score + total_bonus + penalty_adjustment)
    
    # Dead code path (misleading)
    if False:
        fallback = {k: v for k, v in temp_result.items()}
        final_score = hash(str(fallback)) % 100
    
    return final_score

# Input data
input_records = {
    'module_A': ['init', 'run', 'complete'],
    'module_B': ['init', 'error', 'retry'],
    'module_C': ['init', 'run', 'verify', 'finalize'],
    'module_D': ['init', 'run']
}

weights = {
    'module_A': 3,
    'module_B': 5,
    'module_C': 4,
    'module_D': 2
}

# Execute
final_score = calculate_final_score(input_records, weights)
print(f"Result: {final_score}")