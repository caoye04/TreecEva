def analyze_readings(readings):
    adjusted = [r * 1.05 for r in readings if r > 0]
    offset = sum(adjusted) / len(adjusted) if adjusted else 0
    return offset

baseline = 42
readings = [10, -5, 20, 0, 30, -10, 25]

temp_offset = analyze_readings(readings)

# Simulate sensor calibration drift
calibration_factor = 1.1 if temp_offset > 20 else 0.9
reference_points = {i: val * calibration_factor for i, val in enumerate(readings)}

# Irrelevant tracking variables (distractors)
count_positive = sum(1 for x in readings if x > 0)
sum_negative = sum(x for x in readings if x < 0)
avg_abs = sum(abs(x) for x in readings) / len(readings)

# Secondary processing path with partial reuse
deviations = [abs(r - baseline) for r in readings]
threshold_met = [d for d in deviations if d > 15]

# Conditional expression used to determine adjustment logic
adjustment = 10 if len(threshold_met) >= 3 else 5

# Core calculation chain
base_performance = sum(deviations) + adjustment

# Misleading complex-looking but unused transformation
transformed = [(x ** 0.5 if x > 0 else 0) for x in threshold_met]
ignored_total = sum(transformed)

# Final performance score computed through layered logic
final_score = base_performance - int(temp_offset) + adjustment

# Output the target result
print(f"Result: {final_score}")