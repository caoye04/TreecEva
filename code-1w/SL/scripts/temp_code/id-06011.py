def analyze_event_frequency(log):
    event_count = {}
    total_events = 0
    for entry in log:
        event_type = entry.split('_')[0]
        event_count[event_type] = event_count.get(event_type, 0) + 1
        total_events += 1
    
    # Distractor: unused computation
    avg_length = sum(len(e) for e in log) / len(log) if log else 0
    rare_events = [k for k, v in event_count.items() if v < 2]

    return event_count, total_events


def validate_structure(data_str):
    open_count = data_str.count('(')
    close_count = data_str.count(')')
    balanced = open_count == close_count
    complexity_score = abs(open_count - close_count) * 100  # Unused metric
    return balanced


def calculate_system_capacity(log_entries, flags):
    # Step 1: Extract frequency stats
    freq_map, total = analyze_event_frequency(log_entries)
    
    # Step 2: Initialize capacity with base heuristic
    base_capacity = total * 1.5 if total > 10 else total * 2.0
    
    # Step 3: Adjust based on flag conditions (conditional expressions)
    safety_margin = 10 if flags.get('redundancy_enabled', False) else 5
    performance_mode = flags.get('perf_mode', 'balanced')
    
    # Step 4: Use dictionary to map mode to multiplier
    mode_multiplier = {
        'high': 1.8,
        'balanced': 1.2,
        'low': 0.7
    }.get(performance_mode, 1.0)
    
    adjusted_capacity = base_capacity * mode_multiplier + safety_margin
    
    # Step 5: Apply constraint from structural validation (red herring call)
    fake_data = "((event_start_1)(event_error_2))"
    if validate_structure(fake_data):
        adjusted_capacity += 3  # Minor boost, semi-relevant but predictable
    
    # Step 6: Corrective reduction based on unique event types
    unique_event_types = len(freq_map)
    penalty = unique_event_types * 0.5
    final_capacity = int(adjusted_capacity - penalty)
    
    # Irrelevant tracking variables (distractors)
    peak_load_simulated = final_capacity * 1.1
    estimated_downtime = 0.0 if final_capacity > 20 else 5.0
    
    return final_capacity

# Main execution
log_data = [
    'auth_success_001', 'network_timeout_002', 'auth_success_003',
    'disk_read_004', 'disk_write_005', 'network_retry_006',
    'auth_failure_007', 'disk_read_008', 'network_ok_009',
    'disk_write_010', 'auth_success_011'
]

system_config = {
    'redundancy_enabled': True,
    'perf_mode': 'balanced',
    'debug_mode': True,  # Unused
    'max_retries': 3   # Unused
}

final_capacity = calculate_system_capacity(log_data, system_config)
print(f"Result: {final_capacity}")