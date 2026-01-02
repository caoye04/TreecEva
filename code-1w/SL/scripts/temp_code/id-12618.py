def monitor_system(snapshot):
    normalize = lambda x: (x - min(snapshot)) / (max(snapshot) - min(snapshot)) if max(snapshot) != min(snapshot) else 0
    normalized_data = [normalize(value) for value in snapshot]
    
    critical_level = 0.8
    warning_level = 0.5
    
    anomalies = [val for val in normalized_data if val > critical_level]
    warnings = [val for val in normalized_data if warning_level < val <= critical_level]

    base_threshold = 100
    adjustment_factor = len(anomalies) * 15 + len(warnings) * 5
    energy_threshold = base_threshold + adjustment_factor
    
    system_load = sum(snapshot) / len(snapshot)
    temp_buffer = [x * 2 for x in snapshot]  # Irrelevant computation (distractor)
    peak_count = len([x for x in snapshot if x == max(snapshot)])
    
    final_diagnostic = energy_threshold if system_load > 50 else base_threshold
    return final_diagnostic

health_snapshot = [23, 45, 55, 78, 92, 34, 67]
final_diagnostic = monitor_system(health_snapshot)
print(f"Result: {final_diagnostic}")