def adjust_thermal(capacity, factor):
    if factor > 0.75:
        return int(capacity * 1.15)
    elif factor > 0.5:
        return int(capacity * 1.05)
    else:
        return int(capacity * 0.9)

# System calibration parameters
target_voltage = 230
measured_fluctuation = 0.12
baseline_risk = 4.7

# Sensor readings and derived metrics
sensor_array = [85, 92, 78, 96, 88]
valid_readings = [temp for temp in sensor_array if temp > 75]
raw_average = sum(valid_readings) / len(valid_readings)

# Environmental efficiency calculation
environment_flag = 'STABLE' if raw_average < 90 else 'VOLATILE'
efficiency_factor = 0.8 if environment_flag == 'STABLE' else 0.6

# Secondary system checks (distractor computations)
power_cycles = 12
stress_factor = power_cycles * 0.03
reliability_score = 100 - (stress_factor * 5)  # Not used in final logic

# Redundant string-based status check (irrelevant but plausible)
system_status = "nominal" if efficiency_factor >= 0.7 else "degraded"
status_length = len(system_status)  # Distractor
status_capital = system_status.upper()  # Dead code

# Primary thermal computation chain
base_capacity = 5000
adjustment_ratio = (raw_average / 85) ** 0.5
thermal_capacity = int(base_capacity * adjustment_ratio)

# Final adjustment based on efficiency (key statement)
thermal_capacity = adjust_thermal(thermal_capacity, efficiency_factor)

# Output result as required
print(f"Result: {thermal_capacity}")