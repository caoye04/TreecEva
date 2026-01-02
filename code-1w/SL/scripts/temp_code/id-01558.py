def evaluate_system_load(node_statuses, thresholds, debug=False):
    system_capacity = 1250.0
    base_threshold = thresholds[0]
    peak_threshold = thresholds[1] if len(thresholds) > 1 else base_threshold
    
    # Irrelevant intermediate calculation (distractor)
    avg_threshold = sum(thresholds) / len(thresholds) if thresholds else 0
    temp_buffer = [x * 0.1 for x in thresholds]  # Unused data structure

    node_power_map = {i: 1.8 + i * 0.2 for i in range(len(node_statuses))}
    active_nodes = 0
    stress_events = 0

    for idx, status in enumerate(node_statuses):
        load_level = status.get('load', 0)
        temp_status = status.get('temp', 'normal')
        
        # Check for high load with conditional expression
        is_overloaded = load_level > peak_threshold if temp_status == 'high' else load_level > base_threshold
        
        if is_overloaded:
            stress_events += 1
        
        # Only nodes with sufficient power and within temp limits are active
        if load_level <= peak_threshold and temp_status != 'critical':
            if node_power_map[idx] > 2.0 or temp_status == 'normal':
                active_nodes += 1

    # Distractor: unused loop over zipped elements
    backup_nodes = [101, 102, 103]
    for node_id, status in zip(backup_nodes, node_statuses):
        fallback_load = status.get('load', 0) * 0.5  # Not affecting main logic

    # Efficiency depends on active ratio with slicing distraction
    recent_statuses = node_statuses[-3:] if len(node_statuses) >= 3 else node_statuses
    efficiency_factor = 0.9 if len(recent_statuses) == 3 and all(s.get('temp') == 'normal' for s in recent_statuses) else 0.75

    # Key statement
    final_load = system_capacity * efficiency_factor if active_nodes else 0
    
    # Debug output that's conditionally unused
    if debug:
        print(f'Active nodes: {active_nodes}, Stress events: {stress_events}')
    
    print(f"Result: {final_load}")
    return final_load

# Inputs
statuses = [
    {'load': 78, 'temp': 'normal'},
    {'load': 85, 'temp': 'high'},
    {'load': 72, 'temp': 'normal'},
    {'load': 90, 'temp': 'critical'}
]
thresholds = [80, 88]

# Execute
evaluate_system_load(statuses, thresholds)