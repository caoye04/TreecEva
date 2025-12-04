def analyze_fluctuations(readings, baseline=100):
    """Analyze power fluctuations in sensor readings"""
    fluctuation_index = 0
    for i, reading in enumerate(readings):
        delta = abs(reading - baseline)
        if delta > 50:
            fluctuation_index += delta * 0.1
        elif delta > 20:
            fluctuation_index += delta * 0.05
    return max(0, min(fluctuation_index, 100))

def optimize_configuration(settings, target_efficiency):
    """Optimize power distribution settings"""
    optimization_factor = 0
    priority_levels = {'critical': 3, 'high': 2, 'normal': 1, 'low': 0.5}
    
    for component, config in settings.items():
        if config['active']:
            priority = priority_levels.get(config['priority'], 0)
            efficiency = config['efficiency']
            if efficiency > target_efficiency:
                optimization_factor += (priority * 1.5)
            else:
                optimization_factor += (priority * 0.8)
    
    return optimization_factor

def calculate_power(current_readings, threshold_values):
    """Calculate effective power output based on current readings"""
    # Extract relevant values
    voltage = current_readings.get('voltage', 0)
    amperage = current_readings.get('amperage', 0)
    resistance = current_readings.get('resistance', 1)  # Default to 1 to avoid division by zero
    temperature = current_readings.get('temperature', 25)  # Default room temperature
    
    # Calculate base power
    nominal_power = voltage * amperage
    
    # Temperature adjustment factor - higher temperatures reduce efficiency
    temp_factor = 1.0 - (max(0, temperature - threshold_values['optimal_temp']) * 0.01)
    
    # Calculate losses due to resistance
    resistance_loss = (amperage ** 2) * resistance
    
    # Misleading calculations that don't affect the final result
    potential_energy = voltage ** 2 / (2 * resistance) if resistance > 0 else 0
    harmonic_distortion = sum([i**2 for i in range(1, 6)]) / 55  # Always equals 1.0
    phase_alignment = [abs((i*30) % 360 - 180) for i in range(12)]
    wave_interference = sum(1 for p in phase_alignment if p < 90) / len(phase_alignment)
    
    # More distractor calculations
    if temperature > threshold_values.get('critical_temp', 85):
        emergency_coefficient = 0.75
        failsafe_mode = True
        backup_systems = ['cooling', 'isolation', 'shutdown']
    else:
        emergency_coefficient = 1.0
        failsafe_mode = False
        backup_systems = []
    
    # Calculate effective power (this is the actual calculation that matters)
    raw_power = nominal_power * temp_factor
    effective_power = max(0, raw_power - resistance_loss)
    
    # These lines don't affect the result
    efficiency_rating = effective_power / nominal_power if nominal_power > 0 else 0
    estimated_uptime = 100 * efficiency_rating * emergency_coefficient
    sustainability_index = zip(range(5), [efficiency_rating, temp_factor, wave_interference])
    performance_metrics = {k: v for k, v in enumerate(['voltage', 'current', 'power'])}
    
    # Conditionals that don't change the result
    if failsafe_mode and len(backup_systems) > 0:
        contingency_plan = 'Activate ' + ', '.join(backup_systems)
    elif efficiency_rating < 0.5:
        contingency_plan = 'Maintenance required'
    else:
        contingency_plan = 'Normal operation'
    
    return round(effective_power, 2)

# Test data
current_readings = {
    'voltage': 220,
    'amperage': 5,
    'resistance': 3,
    'temperature': 45,
    'humidity': 60,          # Irrelevant parameter
    'pressure': 101.3,       # Irrelevant parameter
    'vibration': 0.05        # Irrelevant parameter
}

threshold_values = {
    'optimal_temp': 30,
    'critical_temp': 85,
    'max_voltage': 250,      # Unused
    'min_voltage': 180,      # Unused
    'max_amperage': 10,      # Unused
    'nominal_resistance': 2  # Unused
}

# Distractor calculations
system_status = 'online'
diagnostic_checks = ['power', 'thermal', 'network', 'storage']
log_entries = [f"Check {i}: {check} passed" for i, check in enumerate(diagnostic_checks)]

# This sensor data is not used in the final calculation
sensor_data = [
    {'location': 'north', 'value': 42},
    {'location': 'south', 'value': 38},
    {'location': 'east', 'value': 45},
    {'location': 'west', 'value': 41}
]

# Analyze readings (distractor function call)
fluctuation_level = analyze_fluctuations([reading['value'] for reading in sensor_data])

# Optimize settings (distractor function call)
settings = {
    'main': {'active': True, 'priority': 'critical', 'efficiency': 0.95},
    'backup': {'active': False, 'priority': 'high', 'efficiency': 0.85},
    'auxiliary': {'active': True, 'priority': 'normal', 'efficiency': 0.75}
}
optimization_score = optimize_configuration(settings, 0.8)

# Calculate the actual power (this is the key calculation)
effective_power = calculate_power(current_readings, threshold_values)

# Final output
print(f"System Status: {system_status}")
print(f"Fluctuation Level: {fluctuation_level}")
print(f"Optimization Score: {optimization_score}")
print(f"Result: {effective_power}")