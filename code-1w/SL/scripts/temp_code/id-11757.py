def calculate_efficiency(data):
    base_efficiency = 85.0
    adjustments = [0.98, 1.02, 0.99, 1.01]
    weighted_adjustment = sum([adj * (i + 1) for i, adj in enumerate(adjustments)]) / len(adjustments)
    
    # Irrelevant metrics (distractor variables)
    max_capacity = 1200
    uptime_percentage = 99.2
    maintenance_logs = ['ok', 'ok', 'check']
    
    final_factor = data['performance_ratio'] * weighted_adjustment
    return base_efficiency * final_factor

# Main computation
metrics = {
    'performance_ratio': 0.94,
    'temperature_offset': 3.2,
    'vibration_level': 0.7
}

energy_output = calculate_efficiency(metrics)
print(f"Result: {energy_output}")