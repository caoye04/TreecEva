from itertools import cycle, islice

# Simulate sensor readings over a 7-phase environmental cycle
temperature_readings = [22.1, 23.5, 24.0, 23.8, 25.2, 26.0, 24.9]
humidity_levels = [45, 47, 50, 52, 49, 46, 48]
base_pressure = 1013.25

# Misleading initialization - not directly used in final result
calibration_offset = 0.87
fudge_factor = sum(humidity_levels) / len(humidity_levels) * 0.03
adjusted_base = base_pressure - 10.5  # Actual adjustment

# Track phase-specific corrections (only even phases contribute)
corrections = []
for i, temp in enumerate(temperature_readings):
    if i % 2 == 0:
        correction = temp * 0.1
        corrections.append(correction)
    else:
        # Dead code path - never executed due to condition above
        dummy = temp ** 0.5

# Compute efficiency score using modular arithmetic and logical filtering
efficiency_flags = [temp > 24.0 for temp in temperature_readings]
efficiency_count = sum(efficiency_flags)
efficiency_score = efficiency_count * 1.5 if efficiency_count >= 3 else 1.0

# Generate repeating cycle factor using itertools
cycle_pattern = [1, -1, 2]
cycle_iter = cycle(cycle_pattern)
cycle_sequence = list(islice(cycle_iter, len(temperature_readings)))
cycle_factor = abs(sum(cycle_sequence[:3]))  # Uses only first 3: 1 + (-1) + 2 = 2

# Final computation step
final_pressure = adjusted_base + (cycle_factor * efficiency_score)

# Print result for evaluation
print(f"Result: {final_pressure}")