def calculate_efficiency(temps, pressures):
    total_efficiency = 0.0
    temp_sum = sum(temps)
    pressure_sum = sum(pressures)
    scaling_factor = 1.5 if temp_sum > 200 else 0.8
    
    for i, (t, p) in enumerate(zip(temps, pressures)):
        adjusted_temp = t * scaling_factor
        efficiency = adjusted_temp * p / (i + 1) if i % 2 == 0 else adjusted_temp + p
        total_efficiency += efficiency
    
    return int(total_efficiency)

# Sensor data from reactor core
temperature_readings = [68, 72, 70, 69, 74]
pressure_readings = [12, 15, 14, 13, 16]

# Irrelevant auxiliary variable (minor distraction)
diagnostic_code = "OK-2024"

energy_output = calculate_efficiency(temperature_readings, pressure_readings)
print(f"Result: {energy_output}")