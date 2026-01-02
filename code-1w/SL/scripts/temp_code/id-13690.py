def analyze_performance(log_entries):
    total_ops = 0
    error_count = 0
    timestamp_buffer = []
    op_weights = {'read': 1, 'write': 2, 'delete': 3}
    weighted_sum = 0
    temp_aggregate = 0  # distractor

    for entry in log_entries:
        action = entry['action']
        duration = entry['duration']
        timestamp = entry.get('ts', 0)
        
        if action in op_weights:
            weight = op_weights[action]
            total_ops += 1
            weighted_sum += weight * (1 + duration // 100)
            
        if duration > 500:
            error_count += 1
        
        # Irrelevant data accumulation
        if timestamp > 0:
            timestamp_buffer.append(timestamp)

    # Distractor computation: not used in final result
    if len(timestamp_buffer) > 0:
        avg_timestamp = sum(timestamp_buffer) / len(timestamp_buffer)
        temp_aggregate += avg_timestamp % 47

    # Core logic hidden among distractions
    base_efficiency = weighted_sum * (100 - error_count * 2) if total_ops > 0 else 0
    
    correction_factor = 0.9 if error_count == 0 else max(0.5, 1 - error_count / 20)
    adjusted_efficiency = base_efficiency * correction_factor
    
    # Secondary metric with partial relevance
    stability_index = (len(log_entries) - error_count) / len(log_entries) if log_entries else 0
    
    # Final score computed via lambda and list comprehension
    calculate_bonus = lambda x: x * 1.5 if x > 0.8 else x * 0.7
    bonuses = [calculate_bonus(stability_index) for _ in range(2)]  # always two
    bonus = sum(bonuses) / 2
    
    efficiency_score = int(adjusted_efficiency + bonus * 10)
    
    # Final collection
    final_metrics = []
    final_metrics.append(efficiency_score)
    
    print(f"Result: {efficiency_score}")

# Simulated input
log_data = [
    {'action': 'read', 'duration': 120, 'ts': 1678886400},
    {'action': 'write', 'duration': 95, 'ts': 1678886401},
    {'action': 'write', 'duration': 510, 'ts': 1678886402},
    {'action': 'delete', 'duration': 200, 'ts': 1678886403},
    {'action': 'read', 'duration': 80, 'ts': 1678886404},
    {'action': 'read', 'duration': 600, 'ts': 1678886405},
    {'action': 'write', 'duration': 110, 'ts': 1678886406}
]

analyze_performance(log_data)