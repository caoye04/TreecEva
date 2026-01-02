import itertools

def calculate_efficiency(temps, pressures):
    base_efficiency = 95.0
    temp_correction = 0.0
    pressure_correction = 0.0

    # Average temperature deviation from optimal (75°C)
    avg_temp = sum(temps) / len(temps)
    temp_deviation = abs(avg_temp - 75)
    
    if temp_deviation > 10:
        temp_correction = -temp_deviation * 0.5
    
    # Pressure fluctuation penalty using pairwise differences
    pressure_pairs = list(itertools.pairwise(pressures))
    total_fluctuation = sum(abs(curr - prev) for prev, curr in pressure_pairs)
    
    if total_fluctuation > 20:
        pressure_correction = -total_fluctuation * 0.2

    final_efficiency = base_efficiency + temp_correction + pressure_correction
    return round(final_efficiency, 3)

# Sensor data from reactor core
temperatures = [72, 76, 78, 70, 74]
pressure_levels = [100, 102, 98, 105, 103]

# Irrelevant calibration offset (minimal distraction)
calibration_offset = 0.15

energy_output = calculate_efficiency(temperatures, pressure_levels)
print(f"Target result: {energy_output}")