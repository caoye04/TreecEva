def process_metrics(log_entries):
    total_events = len(log_entries)
    event_weights = []
    temp_accumulator = 0
    weighted_sum = 0
    correction_factor = 0.98
    
    # Irrelevant pre-scan: counts characters in metadata (not used in final logic)
    char_count = sum(len(entry.get('meta', '')) for entry in log_entries)
    dummy_offset = char_count % 7 if char_count > 0 else 0
    
    # Primary processing with conditional expressions and weight assignment
    for entry in log_entries:
        raw_value = entry.get('value', 0)
        status_flag = entry.get('status') == 'active'
        age_in_days = entry.get('age', 0)
        
        # Compute dynamic weight using conditional expression
        weight = 1.5 if age_in_days < 30 else (0.75 if age_in_days < 90 else 0.3)
        adjusted_weight = weight * (1.1 if status_flag else 0.9)
        
        # Accumulate only active entries
        if status_flag:
            temp_accumulator += raw_value * adjusted_weight
            event_weights.append(adjusted_weight)
    
    # Secondary computation: efficiency score based on distribution
    if event_weights:
        avg_weight = sum(event_weights) / len(event_weights)
        peak_weight = max(event_weights)
        stability_ratio = min(event_weights) / peak_weight if peak_weight > 0 else 0
    else:
        avg_weight = 0
        stability_ratio = 0
    
    # Red herring calculation: unused performance index
    performance_index = (temp_accumulator * correction_factor + dummy_offset) / (total_events or 1)
    
    # Key metric: efficiency_score computed from weighted temporal decay and stability
    base_efficiency = temp_accumulator / (sum(w ** 0.5 for w in event_weights) or 1)
    efficiency_score = base_efficiency * (1 + stability_ratio) if avg_weight >= 0.8 \
        else base_efficiency * (0.8 + stability_ratio)
    
    # Final output construction (only efficiency_score is relevant)
    final_output = {
        'efficiency_score': round(efficiency_score, 4),
        'total_processed': len([e for e in log_entries if e.get('status') == 'active']),
        'debug_code': f"E{dummy_offset}{len(event_weights)}"
    }
    
    return final_output

# Input data setup
input_log = [
    {'value': 120, 'age': 15, 'status': 'active', 'meta': 'srcA'},
    {'value': 88, 'age': 45, 'status': 'active', 'meta': 'srcB'},
    {'value': 200, 'age': 120, 'status': 'inactive', 'meta': 'srcC'},
    {'value': 67, 'age': 60, 'status': 'active', 'meta': 'srcD'},
    {'value': 155, 'age': 8, 'status': 'active', 'meta': 'srcE'},
    {'value': 94, 'age': 100, 'status': 'active', 'meta': 'srcF'}
]

# Execute main function
result_dict = process_metrics(input_log)
print(f"Target result: {result_dict['efficiency_score']}")