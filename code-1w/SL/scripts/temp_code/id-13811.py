def calculate_efficiency(data):
    base_efficiency = 0.85
    adjustment_factor = lambda x: 0.1 if x > 75 else 0.05
    
    temp_avg = sum(data['temperatures']) / len(data['temperatures'])
    pressure_ratio = data['max_pressure'] / data['min_pressure']
    
    efficiency = base_efficiency * pressure_ratio
    efficiency -= adjustment_factor(temp_avg)
    
    return efficiency

# System telemetry data
telemetry = {
    'temperatures': [68, 72, 77, 81, 74],
    'max_pressure': 120,
    'min_pressure': 80,
    'status_codes': {200, 201, 202, 400}  # Irrelevant to calculation
}

# Distractor variable (not used in main logic)
system_uptime = 1420

thermal_capacity = calculate_efficiency(telemetry)
Result: {thermal_capacity:.4f}