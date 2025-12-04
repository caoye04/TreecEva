def analyze_energy_readings(readings):
    # Process sensor readings
    filtered_readings = [r for r in readings if r > 50 and r < 200]
    
    # Calculate base energy (distractor - not used in final calculation)
    base_calc = sum(filtered_readings) * 0.1
    
    # Find energy extremes
    energy_values = [reading * 0.8 for reading in filtered_readings]
    max_energy = max(energy_values)
    min_energy = min(energy_values)
    
    # Intermediate calculation (distractor)
    temp_variance = (max_energy - min_energy) * 1.5
    
    # Base energy from different source
    base_energy = len(filtered_readings) * 25
    
    # Final energy calculation
    final_energy = max(energy_values) - min(energy_values) + base_energy
    
    # Print result
    print(f"Target result: {final_energy}")
    return final_energy

# Sensor readings data
sensor_data = [45, 78, 92, 150, 185, 210, 65, 120, 95, 175, 55, 135]
result = analyze_energy_readings(sensor_data)