def calculate_efficiency(data):
    base_efficiency = 0.85
    adjustment_factor = 0.02
    
    # Irrelevant metadata (minimal distraction)
    sensor_model = 'SNSR-202'
    calibration_date = '2023-11-05'
    
    # Transform readings using lambda and list comprehension
    filtered_readings = [x for x in data if x > 0]
    transformed_readings = [(lambda val: val ** 0.5)(val) for val in filtered_readings]
    
    # Compute average transformed reading
    avg_reading = sum(transformed_readings) / len(transformed_readings)
    
    # Efficiency calculation based on average
    if avg_reading > 3.0:
        energy_output = base_efficiency + (avg_reading * adjustment_factor)
    else:
        energy_output = base_efficiency - (avg_reading * adjustment_factor)
    
    # Additional unused variable (minor interference)
    max_possible = 1.2 * base_efficiency
    
    return energy_output

# Input data
sensor_readings = [16, 9, 25, 4, -3, 36]

# Key computation step
energy_output = calculate_efficiency(sensor_readings)

print(f"Result: {energy_output}")