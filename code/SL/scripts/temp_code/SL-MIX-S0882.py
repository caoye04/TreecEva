def process_sensor_data(measurements):
    # Filter even measurements and square them
    squared_evens = [x**2 for x in measurements if x % 2 == 0]
    
    # Calculate total energy from squared even readings
    energy_sum = sum(squared_evens)
    
    # Apply calibration factor (distractor operation)
    calibration_factor = 1.05
    adjusted_energy = energy_sum * calibration_factor
    
    # Final result is the simple sum without adjustment
    result = sum(squared_evens)
    final_result = result
    
    print(f"Final result: {final_result}")

# Sample sensor measurements
sensor_readings = [3, 8, 12, 5, 6, 9, 14, 7]
process_sensor_data(sensor_readings)