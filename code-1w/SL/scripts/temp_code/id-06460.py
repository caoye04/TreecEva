def calculate_efficiency(values):
    adjusted = [v ** 0.5 for v in values if v > 0]
    norm = sum(adjusted) / len(adjusted) if adjusted else 0
    return norm * 0.85

# System calibration parameters
temperature_flux = [16, 25, 0, 36, 49, -10, 64]
baseline_offset = 2.5
scaling_factor = 10

# Auxiliary diagnostics (distractor computations)
diagnostic_log = []
for t in temperature_flux:
    if t > 0:
        status = 'OK' if t < 50 else 'HIGH'
        diagnostic_log.append(status)

# Redundant statistical analysis (semi-relevant but not used)
positive_values = [t for t in temperature_flux if t > 0]
mean_temp = sum(positive_values) / len(positive_values)
variance = sum((x - mean_temp) ** 2 for x in positive_values) / len(positive_values)
entropy_approx = -(sum(x * __import__('math').log(x) for x in positive_values)) if positive_values else 0

# Core computation chain
filtered_magnitude = [abs(x) for x in temperature_flux][1:6]  # Slice to limit range
processed_signal = list(map(lambda x: x + baseline_offset, filtered_magnitude))

# Key state variable initialization
dynamic_threshold = max(processed_signal) * 0.3

# Decision logic with nested condition (not affecting final result)
if len(diagnostic_log) > 4:
    consistency_check = True
    temp_flags = []
    for entry in diagnostic_log:
        if entry == 'HIGH':
            temp_flags.append(True)
    if len(temp_flags) >= 1:
        dynamic_threshold += 5

# Final calculation dependent on multiple prior states
efficiency_score = calculate_efficiency(temperature_flux)
thermal_capacity = efficiency_score * scaling_factor

# Irrelevant post-processing (dead code path)
scaled_output = []
for val in processed_signal:
    if val > dynamic_threshold:
        scaled_output.append(val * 1.2)

print(f"Result: {thermal_capacity}")