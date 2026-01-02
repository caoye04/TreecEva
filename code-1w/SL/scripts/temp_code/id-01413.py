def calculate_system_efficiency(components, sensor_readings):
    efficiency_map = {comp: 0 for comp in components}
    index_map = {i: name for i, name in enumerate(components)}

    # Initialize tracking variables
    total_efficiency = 0
    adjustment_factor = 1.25

    # Process each sensor reading and update component efficiency
    for idx, (reading, status) in enumerate(zip(sensor_readings, [True, False, True, True])):
        comp_name = index_map[idx]
        base_efficiency = reading * 0.8

        if status:
            base_efficiency *= adjustment_factor
        
        efficiency_map[comp_name] = round(base_efficiency, 3)

    # Aggregate total system efficiency
    for eff in efficiency_map.values():
        total_efficiency += eff

    return total_efficiency

# System configuration
equipment = ['pump', 'valve', 'compressor', 'filter']
sensor_data = [75, 60, 88, 92]

# Irrelevant auxiliary variable (minimal distraction)
startup_sequence = [1, 0, 1]

# Main computation
total_efficiency = calculate_system_efficiency(equipment, sensor_data)
print(f"Result: {total_efficiency}")