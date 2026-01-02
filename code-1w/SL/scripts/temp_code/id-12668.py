from itertools import compress

def calculate_thermal_capacity(data_stream, config):
    base_multiplier = config['scaling_factor']
    threshold = config['threshold']
    
    # Extract temperature and pressure values using slicing
    temperatures = [entry[0] for entry in data_stream]
    pressures = [entry[1] for entry in data_stream]
    
    # Irrelevant derived variable (distractor)
    avg_pressure = sum(pressures) / len(pressures) if pressures else 0
    
    # Determine valid segments based on threshold (conditional logic)
    valid_indices = [i for i, t in enumerate(temperatures) if t > threshold]
    filtered_temps = [temperatures[i] for i in valid_indices]
    
    # Secondary filtering using itertools.compress (irrelevant for final result)
    mask = [t > threshold + 5 for t in temperatures]
    enhanced_filter = list(compress(temperatures, mask))
    
    # Dummy accumulation (dead computation path)
    cumulative_drift = 0
    for temp in pressures:
        cumulative_drift += abs(temp - avg_pressure) * 0.01
    
    # Core calculation: weighted sum of high-temp readings
    adjustment_factor = 1.0 if len(filtered_temps) > 3 else 0.8
    raw_sum = sum(filtered_temps)
    
    # Final capacity computation (depends only on raw_sum and base_multiplier)
    thermal_capacity = (raw_sum * base_multiplier) * adjustment_factor
    
    # Unrelated state tracking (distractor)
    status_log = []
    for i, t in enumerate(temperatures):
        status = 'HIGH' if t > threshold else 'LOW'
        status_log.append((i, t, status))
    
    return int(thermal_capacity)  # Deterministic integer output

# Main execution block
fluid_data = [
    (88, 102), (95, 110), (70, 105), (90, 108),
    (105, 112), (65, 100), (97, 107), (83, 103)
]
system_config = {
    'scaling_factor': 2.5,
    'threshold': 85
}

# Intermediate unused transformation (distractor)
data_slice = fluid_data[1:6:2]
duplicate_check = len(data_slice) != len(set([x[0] for x in data_slice]))

# Key statement
thermal_capacity = calculate_thermal_capacity(fluid_data, system_config)

# Output result as required
print(f"Result: {thermal_capacity}")