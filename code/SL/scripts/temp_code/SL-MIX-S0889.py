def analyze_thermal_fluctuations(temperatures):
    # Calculate average temperature (distractor - not used in final result)
    avg_temp = sum(temperatures) / len(temperatures)
    
    # Find temperature extremes using set operations
    temp_set = set(temperatures)
    max_temp = max(temp_set)
    min_temp = min(temp_set)
    
    # Calculate temperature range (distractor)
    temp_range = max_temp - min_temp
    
    # Filter moderate temperatures using list comprehension
    moderate_temps = [t for t in temperatures if 20 <= t <= 30]
    
    # Perform linear search for optimal thermal point
    thermal_equilibrium_point = None
    for temp in temperatures:
        if temp % 7 == 0 and temp > 15:  # Modular arithmetic condition
            thermal_equilibrium_point = temp
            break
    
    # Additional unused calculations (interference)
    temp_variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)
    normalized_temp = (thermal_equilibrium_point - min_temp) / temp_range
    
    final_temperature = thermal_equilibrium_point
    print(f"Target result: {final_temperature}")

# Test data
temperature_readings = [18, 25, 14, 21, 28, 35, 42, 17, 23, 29]
analyze_thermal_fluctuations(temperature_readings)