def calculate_thermal_capacity(state):
    base_factor = 1.75
    adjustment = 0.95
    temp_ratio = state['temperature'] / 273.15
    pressure_factor = state['pressure'] * 0.01
    
    # Irrelevant computation - red herring
    humidity_influence = state['humidity'] * 0.02
    dew_point = state['temperature'] - ((100 - state['humidity']) / 5)
    stability_index = dew_point + pressure_factor
    
    # Real calculation path
    efficiency = (state['efficiency_rating'] / 10) * base_factor
    thermal_multiplier = temp_ratio * pressure_factor * adjustment
    
    # Multiple assignment - distractor
    (min_cap, max_cap) = (50, 500)
    avg_cap = (min_cap + max_cap) / 2
    
    # Core formula
    capacity = (state['volume'] * efficiency * thermal_multiplier)
    
    # Destructuring irrelevant data
    diagnostics = {'sensor_a': 1, 'sensor_b': 0, 'status': 'OK'}
    sensor_a = diagnostics['sensor_a']
    status_flag = diagnostics['status']
    
    # Final adjustment based on operational mode
    if state['mode'] == 'high_performance':
        capacity *= 1.2
    elif state['mode'] == 'eco':
        capacity *= 0.85
    else:
        capacity *= 1.0  # neutral mode

    return int(capacity)

# Initialize system state with meaningful parameters
system_state = {
    'temperature': 350.0,      # Kelvin
    'pressure': 120.0,         # kPa
    'volume': 2.5,             # cubic meters
    'humidity': 60,            # percent - not used in final calc
    'efficiency_rating': 8,    # out of 10
    'mode': 'high_performance'
}

# Dead code - misleading function call
def log_diagnostics(data):
    timestamp = 1678886400
    log_entry = f'{timestamp}: System nominal'
    return log_entry

# Unused variable - distraction
calibration_offset = 0.0034
reference_units = ['K', 'kPa', 'm^3']

# Critical execution point
thermal_capacity = calculate_thermal_capacity(system_state)

# Output result as required
print(f"Target result: {thermal_capacity}")