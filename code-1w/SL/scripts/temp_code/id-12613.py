def calculate_efficiency(temp, press):
    base_efficiency = 85.0
    temp_factor = 1.0 if 20 <= temp <= 80 else 0.8 if temp < 20 else 0.75
    press_factor = 1.0 if 100 <= press <= 300 else 0.9 if press < 100 else 0.85
    
    # Adjust efficiency using conditional expressions
    adjusted_efficiency = base_efficiency * temp_factor if temp_factor < 1.0 else base_efficiency * press_factor
    final_efficiency = adjusted_efficiency * 0.95  # Safety margin
    
    return final_efficiency

# Sensor readings
temperature = 85
pressure = 320

# Initial diagnostics (irrelevant to final result, minor distraction)
diagnostic_code = 200
status = "OK" if diagnostic_code == 200 else "ERROR"

# Core computation
energy_output = calculate_efficiency(temperature, pressure)

print(f"Result: {energy_output}")