import itertools

# Simulate sensor array data for thermal regulation system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.7]
humidity_levels = [45, 47, 46, 50, 48]

# Initialize system parameters
base_rating = 17
safety_margin = 0.92
overhead_penalty = 0.05 * base_rating

# Compute derived metrics
avg_temp = sum(temperature_readings) / len(temperature_readings)
adjusted_temp = avg_temp + 2.5 if avg_temp < 24 else avg_temp - 1.0

# Distractor: irrelevant humidity computation
humidity_cycle = list(itertools.cycle(humidity_levels))
humidity_sum = sum(humidity_cycle[:10])
humidity_trend = humidity_sum / 10

# Efficiency model based on temperature bands
if adjusted_temp < 23.0:
    efficiency_factor = 0.85
elif adjusted_temp >= 24.5:
    efficiency_factor = 0.78
else:
    efficiency_factor = 0.91

# Secondary distractor: unused state tracking
status_flags = {level: level > 47 for level in humidity_levels}
flag_count = sum(status_flags.values())

# Core calculation with key assignment
thermal_capacity = base_rating * efficiency_factor

# Additional red herring: unrelated bitwise adjustment
bitwise_offset = (len(temperature_readings) << 2) ^ 5
scratch_value = bitwise_offset & 10

# Final output
Result: {thermal_capacity}