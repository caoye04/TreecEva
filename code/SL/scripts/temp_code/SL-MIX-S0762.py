import itertools

# Energy optimization analysis for sensor network
def analyze_energy_patterns():
    sensor_readings = [12, 8, 15, 6, 9, 11, 7]
    calibration_offsets = [-1, 2, -3, 1, -2, 3, -1]
    
    # Combine readings with calibration offsets
    adjusted_readings = [reading + offset for reading, offset in zip(sensor_readings, calibration_offsets)]
    
    # Calculate energy metrics
    total_energy = sum(adjusted_readings)
    max_reading = max(adjusted_readings)
    min_reading = min(adjusted_readings)
    
    # This intermediate calculation is a distractor (not used in final result)
    energy_variance = sum((x - total_energy/len(adjusted_readings))**2 for x in adjusted_readings)
    
    # Find optimal energy subset using itertools combinations
    optimal_energy = 0
    for i in range(1, len(adjusted_readings) + 1):
        for combination in itertools.combinations(adjusted_readings, i):
            current_sum = sum(combination)
            # Select combination that maximizes efficiency
            if 18 <= current_sum <= 25 and current_sum > optimal_energy:
                optimal_energy = current_sum
    
    # More distraction calculations
    efficiency_ratio = (max_reading - min_reading) / len(sensor_readings)
    
    # Key calculation for final result
    conversion_factor = 2.5
    optimal_sum = optimal_energy
    
    # Final result calculation
    final_energy = optimal_sum * conversion_factor
    
    print(f"Target result: {final_energy}")
    return final_energy

# Execute the analysis
analyze_energy_patterns()