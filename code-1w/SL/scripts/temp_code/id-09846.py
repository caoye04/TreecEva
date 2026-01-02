def calculate_performance(data):
    base_points = 0
    bonus_multiplier = 1.0
    
    for index, (name, value) in enumerate(zip(data['labels'], data['values'])):
        if 'critical' in name.lower():
            base_points += value * 2
        elif value > 50:
            base_points += value
            
        # Apply incremental multiplier based on position
        if index % 3 == 0:
            bonus_multiplier += 0.1
    
    # Unrelated tracking variable (minimal distraction)
    temp_debug_log = f'Processed {len(data["labels"])} entries'
    
    return int(base_points * bonus_multiplier)

# Input data
benchmark_data = {
    'labels': ['system_critical', 'network_throughput', 'memory_utilization', 'critical_cache', 'disk_io'],
    'values': [45, 78, 63, 52, 88]
}

# Computation entry point
final_score = calculate_performance(benchmark_data)
print(f'Result: {final_score}')