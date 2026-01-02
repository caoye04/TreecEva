def analyze_sensor_data(raw_readings):
    adjusted = [x * 1.05 for x in raw_readings if x > 0]
    baseline = sum(adjusted) / len(adjusted) if adjusted else 0
    return baseline

raw_values = [87, -5, 92, 0, 88, 90, -1, 85]
baseline_value = analyze_sensor_data(raw_values)

status_flags = {"stable": True, "calibrated": False, "ready": True}
previous_yield = 217.4
efficiency_ratio = baseline_value / 100.0

if efficiency_ratio < 0.8:
    adjustment_factor = 0.9
else:
    adjustment_factor = 1.1

projected_output = previous_yield * adjustment_factor

# Distractor: irrelevant temperature conversion
ambient_celsius = 23
ambient_fahrenheit = (ambient_celsius * 9/5) + 32
target_pressure = 1013.25 * (efficiency_ratio ** 2)

# Simulate calibration offset (unused)
calibration_offset = sum([i * 0.01 for i in range(len(raw_values))]) if status_flags["calibrated"] else 0.0

# Main calculation path
normalized_efficiency = efficiency_ratio + (0.05 if status_flags["stable"] else -0.05)

# Conditional expression used
interim_yield = projected_output if normalized_efficiency >= 0.9 else previous_yield * 0.95

# Additional distractor: character counting in status keys
char_count = sum(len(key) for key in status_flags.keys())
flag_state_summary = ''.join([str(int(v)) for v in status_flags.values()])

# Critical execution point
final_yield = interim_yield * (1.0 + (normalized_efficiency - 0.85))

# Red herring computation
theoretical_max = 300 * efficiency_ratio
buffer_zone = theoretical_max * 0.05 if final_yield > 250 else 0

Result: final_yield