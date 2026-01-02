def calculate_stability_factor(data):
    base_score = sum(data) / len(data)
    deviation = sum(abs(x - base_score) for x in data) / len(data)
    correction_factor = 0.9 if deviation < 5 else 1.1
    
    # Conditional expression based on system mode
    mode_multiplier = 1.2 if 'critical' in data_tags else 0.8
    
    # Calculate final stability factor
    stability = base_score * correction_factor * mode_multiplier
    
    # Irrelevant distraction: logging unrelated status
    system_status = "nominal"
    log_entry = f"System: {system_status}, Time: 14:32"
    
    return round(stability, 3)

# Sensor readings from thermal array
data_tags = ['standard', 'monitoring']
readings = [23.5, 24.1, 22.7, 25.0, 23.9]

# Initial threshold setting
base_threshold = 20.0
energy_threshold = base_threshold + 5

# Key computation
energy_threshold = calculate_stability_factor(readings)

print(f"Result: {energy_threshold}")