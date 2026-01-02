from itertools import compress

def calculate_efficiency(temps, pressures):
    base_efficiency = 85.0
    temp_threshold = 90
    pressure_factor = 0.12
    
    # Determine if each temperature reading is within optimal range
    temp_valid = [t < temp_threshold for t in temps]
    
    # Calculate average pressure from valid segments
    valid_pressures = list(compress(pressures, temp_valid))
    avg_pressure = sum(valid_pressures) / len(valid_pressures) if valid_pressures else 0
    
    # Adjust efficiency based on average pressure
    adjusted_efficiency = base_efficiency + (avg_pressure * pressure_factor)
    
    # Additional small correction based on count of stable cycles
    stable_cycles = sum(1 for t, p in zip(temps, pressures) if t < 85 and p > 15)
    adjusted_efficiency += stable_cycles * 0.5
    
    return round(adjusted_efficiency, 3)

# Sensor data from turbine operation
temperature_readings = [88, 92, 87, 84, 95, 83]
pressure_levels = [18, 14, 16, 20, 12, 19]

# Irrelevant auxiliary variable (minor distraction)
dummy_offset = 2.3

energy_output = calculate_efficiency(temperature_readings, pressure_levels)
print(f"Result: {energy_output}")