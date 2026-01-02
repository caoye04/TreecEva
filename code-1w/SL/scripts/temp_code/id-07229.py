from itertools import cycle

# Simulate environmental sensor data for thermal regulation system
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_levels = [45, 47, 50, 44, 48, 51, 46]

# Initialize system parameters
base_rating = 85
adjustment_threshold = 24.0
efficiency_factor = 1.0
overshoot_count = 0
compensation_buffer = 0

# Track fluctuation patterns using cycling iterator
temp_cycle = cycle(temperature_readings)
humid_cycle = cycle(humidity_levels)

for i in range(12):  # 12-hour simulation cycle
    current_temp = next(temp_cycle)
    current_humid = next(humid_cycle)
    
    # Apply non-linear correction based on humidity (not directly used later)
    pseudo_stress_index = (current_temp - adjustment_threshold) * (1 + current_humid / 100)
    buffer_contribution = max(0, pseudo_stress_index - 1.5)
    compensation_buffer += buffer_contribution * 0.1
    
    # Update efficiency only when temperature exceeds threshold
    if current_temp > adjustment_threshold:
        efficiency_factor *= 0.98 - (current_humid - 45) * 0.001
        overshoot_count += 1
    
    # Irrelevant diagnostic trace
    diagnostic_flag = "NORMAL"
    if current_temp > 25.0 and current_humid > 50:
        diagnostic_flag = "HIGH_LOAD"
    elif current_temp < 23.0:
        diagnostic_flag = "LOW_ACTIVITY"

# Final capacity calibration after simulation
baseline_average = sum(temperature_readings) / len(temperature_readings)
drift_correction = (baseline_average - 24.0) * 0.5

# Key statement: compute effective thermal capacity
efficiency_factor = max(0.85, efficiency_factor)  # Enforce lower bound
thermal_capacity = base_rating * efficiency_factor ** 2

# Dead code - no effect on result
if overshoot_count > 10:
    thermal_capacity *= 0.9

# Print final result
print(f"Result: {thermal_capacity}")