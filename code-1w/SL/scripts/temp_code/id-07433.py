def evaluate_system_stability(data):
    base_score = 100
    anomaly_count = sum(1 for val in data['readings'] if val > 90)
    
    # Conditional expression used to adjust threshold
    penalty_factor = 0.85 if data['mode'] == 'high_throughput' else 1.0
    
    # Dictionary operation: update score based on flags
    critical_flags = {k: v for k, v in data['diagnostics'].items() if v == 'CRITICAL'}
    safety_margin = base_score * penalty_factor - (anomaly_count * 8)
    
    # Final rating with conditional logic
    pressure_rating = safety_margin if len(critical_flags) == 0 else safety_margin - 20
    
    return pressure_rating

# Simulated telemetry input
telemetry_data = {
    'readings': [85, 92, 88, 95, 87],
    'mode': 'high_throughput',
    'diagnostics': {
        'sensor_a': 'OK',
        'sensor_b': 'CRITICAL',
        'sensor_c': 'OK'
    }
}

pressure_rating = evaluate_system_stability(telemetry_data)
print(f"Result: {pressure_rating}")