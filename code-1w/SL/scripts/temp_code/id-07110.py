def calculate_energy_profile():
    temperatures = [22.5, 34.0, 45.8, 38.2, 51.1, 47.3]
    pressure_readings = [101.3, 102.1, 99.7, 103.4, 100.8]
    thermal_loads = [temp * 2.1 for temp in temperatures]
    
    # Irrelevant auxiliary calculation (minimal distraction)
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    normalizing_constant = 1.0 + (avg_pressure * 0.01)

    system_active = len(temperatures) > 4
    efficiency_factor = 0.87
    
    # Key statement with conditional expression
    energy_threshold = max(thermal_loads) * efficiency_factor if system_active else 0
    
    # Additional benign operation to simulate real code flow
    safety_margin = energy_threshold * 0.1
    final_output = energy_threshold + safety_margin
    
    print(f"Result: {energy_threshold}")

calculate_energy_profile()