def calculate_engine_pressure(base_temp, pressure_factor):
    temp_celsius = base_temp - 273
    adjusted_temp = temp_celsius if temp_celsius > 0 else 0
    efficiency_map = {1: 0.8, 2: 0.85, 3: 0.9, 4: 0.95}
    mode = 3
    efficiency = efficiency_map[mode]
    compression_ratio = pressure_factor * efficiency
    offset = 15
    initial_estimate = adjusted_temp * compression_ratio
    correction = 5 if initial_estimate > 100 else 0
    final_pressure = adjusted_temp * compression_ratio + offset
    return final_pressure

result = calculate_engine_pressure(323, 10)
print(f"Result: {result}")