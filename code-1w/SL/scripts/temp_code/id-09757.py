def calculate_energy_consumption():
    # Simulated sensor readings in kilowatts
    power_readings = [12.5, 14.0, 13.8, 15.2, 9.4, 16.0, 11.7, 10.9]
    
    # Irrelevant metadata (minimal distraction)
    device_info = {'model': 'PX200', 'firmware': 'v1.3.5'}
    calibration_offset = 0.3

    # Filter readings above threshold using list comprehension
    high_usage_hours = [reading for reading in power_readings if reading > 13.0]
    filtered_readings = [h - calibration_offset for h in high_usage_hours]
    
    # Efficiency factor from system specs
    efficiency_factor = 0.88
    
    # Key computation step
    total_energy = sum(filtered_readings) * efficiency_factor
    
    # Print result in required format
    print(f"Result: {total_energy}")
    
    return total_energy

# Execute function
calculate_energy_consumption()