def apply_calibration(value):
    adjust = lambda x: x * 1.5 if x < 30 else x - 5
    return adjust(value)

# System baseline parameters
temperature_offset = 7
calibration_factor = 2
raw_signal = 18

# Primary computation chain
filtered_value = raw_signal + temperature_offset
normalized_power = filtered_value * calibration_factor
threshold_score = normalized_power - 10

# Diagnostic calibration step
final_diagnostic = apply_calibration(threshold_score)

print(f"Result: {threshold_score}")