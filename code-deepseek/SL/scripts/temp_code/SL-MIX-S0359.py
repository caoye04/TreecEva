def calculate_temperature_projection(base_temp, adjustments):
    temperature_readings = [base_temp * 1.5, base_temp * 0.8, base_temp * 1.2]
    
    # Distractor calculation that doesn't affect final result
    projected_high = max(temperature_readings) + 15
    projected_low = min(temperature_readings) - 8
    
    temp_sum = sum(temperature_readings)
    avg_temp = temp_sum / len(temperature_readings)
    
    # Main logic chain
    adjustment_factors = [1.1, 0.9, 1.05]
    adjusted_values = []
    
    for i, (temp, factor) in enumerate(zip(temperature_readings, adjustment_factors)):
        adjusted_values.append(temp * factor)
    
    # Intermediate calculation that's not used
    variance_calc = sum((val - avg_temp) ** 2 for val in temperature_readings)
    
    adjusted_temp = sum(adjusted_values) / len(adjusted_values)
    temp_correction = (base_temp * 0.15) if base_temp > 20 else (base_temp * 0.25)
    
    final_temperature = adjusted_temp - temp_correction
    print(f"Target result: {final_temperature}")

# Execute with base temperature
calculate_temperature_projection(25, [1.1, 0.9, 1.05])