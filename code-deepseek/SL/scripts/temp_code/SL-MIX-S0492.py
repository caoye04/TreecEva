def calculate_turbine_efficiency(rotor_speed, blade_angle):
    efficiency_map = {45: 0.87, 60: 0.92, 75: 0.89, 90: 0.85}
    base_efficiency = efficiency_map.get(blade_angle, 0.80)
    speed_factor = 1.0 if rotor_speed <= 1500 else 0.95
    return base_efficiency * speed_factor

def monitor_pressure_fluctuations(pressure_readings):
    pressure_data = [p * 1.2 for p in pressure_readings]
    irrelevant_calibration = sum(p * 0.1 for p in pressure_data) - len(pressure_data)
    return pressure_data, irrelevant_calibration

def transform_power(temperature, pressure_array):
    import itertools
    
    turbine_configs = [(1200, 45), (1400, 60), (1600, 75), (1800, 90)]
    config_combinations = list(itertools.combinations(turbine_configs, 2))
    
    thermal_modifier = lambda t: 0.98 if t < 300 else 1.02
    pressure_stability = len([p for p in pressure_array if p > 85]) / len(pressure_array)
    
    efficiency_values = []
    for speed, angle in turbine_configs:
        eff = calculate_turbine_efficiency(speed, angle)
        efficiency_values.append(eff)
    
    avg_efficiency = sum(efficiency_values) / len(efficiency_values)
    
    misleading_calc = sum(speed * angle for speed, angle in config_combinations[0]) * 0.001
    pressure_sum = sum(pressure_array)
    
    power_output = avg_efficiency * thermal_modifier(temperature) * pressure_stability * pressure_sum
    
    return round(power_output, 2)

core_temp = 325
sensor_readings = [78.5, 82.3, 89.7, 91.2, 86.8, 83.1]
pressure_data, unused_calibration = monitor_pressure_fluctuations(sensor_readings)

irrelevant_analysis = [p * 1.5 for p in pressure_data[:3]]
redundant_check = len([x for x in irrelevant_analysis if x > 120])

final_energy = transform_power(core_temp, pressure_data)
print(f"Result: {final_energy}")