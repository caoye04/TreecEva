def analyze_system_performance(levels):
    base_rating = 89
    adjustment_factor = 0
    efficiency_log = []
    temp_cache = {}
    
    for i in range(len(levels)):
        level = levels[i]
        if i % 2 == 0:
            adjusted = level * 1.5 + base_rating // 4
            efficiency_log.append(adjusted)
        else:
            # Distractor: complex but unused computation
            temp_cache[i] = (level ** 2) // (i + 1) - base_rating % 7
            smoothed = round((level + base_rating) / 2.3, 2)
            efficiency_log.append(smoothed)
    
    # Irrelevant string processing - distractor
    status_flags = ['OK', 'PENDING', 'CRITICAL']
    flag_summary = ''.join([f[0] for f in status_flags]).lower()
    diagnostic_key = flag_summary.upper()[::-1]
    
    # Unused set operations - distractor
    unique_values = set(efficiency_log)
    outliers = {v for v in unique_values if v > 100}
    filtered_metrics = unique_values - outliers
    
    # Actual logic hidden among distractions
    avg_efficiency = sum(efficiency_log) / len(efficiency_log)
    fluctuation_index = 0
    for j in range(1, len(efficiency_log)):
        fluctuation_index += abs(efficiency_log[j] - efficiency_log[j-1])
    
    # Helper function defined inside - increases nesting and complexity
    def calculate_thermal_rating(log_data):
        base = sum(log_data) / len(log_data)
        penalty = 0
        for val in log_data:
            if val < 90:
                penalty += (90 - val) * 0.1
        return int(base - penalty)  # Final integer result
    
    thermal_capacity = calculate_thermal_rating(efficiency_log)
    
    # Dead code path - misleading control flow
    if thermal_capacity < 0:
        thermal_capacity = 0
    elif thermal_capacity > 200:
        backup_check = [x for x in filtered_metrics if x > 50]
        thermal_capacity = len(backup_check) * 2
    
    # Redundant dictionary update - distractor
    summary_report = {
        'capacity': thermal_capacity,
        'flag': diagnostic_key,
        'count': len(filtered_metrics)
    }
    summary_report.update({'final': thermal_capacity})
    
    # Critical print statement
    print(f"Result: {thermal_capacity}")

# Input data
sensor_levels = [68, 72, 85, 91, 64]
analyze_system_performance(sensor_levels)