def analyze_phase_shifts(readings):
    adjusted = []
    for i, val in enumerate(readings):
        if i % 2 == 0:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)
    return adjusted

# Simulate system calibration data
calibration_sequence = [23, 45, 67, 89, 12, 34]
baseline_offset = sum(calibration_sequence) / len(calibration_sequence)

# Apply phase analysis
processed_readings = analyze_phase_shifts(calibration_sequence)

# Generate quality flags using bitwise patterns
quality_flags = []
for x in processed_readings:
    flag = int(x) & 15  # Lower 4 bits as diagnostic code
    quality_flags.append(flag)

# Performance metrics with distractor computations
performance_data = []
dummy_accumulator = 0
useless_tracker = 0
for idx, (qf, pr) in enumerate(zip(quality_flags, processed_readings)):
    normalized = pr / (idx + 1 + baseline_offset)
    dummy_accumulator += normalized ** 2  # Irrelevant computation
    useless_tracker += qf ^ idx  # Misleading XOR pattern
    score_component = normalized * (qf | 3)  # Logical OR used meaningfully
    performance_data.append(score_component)

# Red herring function - never called
def deprecated_evaluation(seq):
    return [s * 0.1 for s in seq if s > 50]

# Unused intermediate transformation
intermediate_weights = [p * 0.85 for p in performance_data if p > 5]

# Core processing logic
reliability_mask = [1 if q in [3, 7, 11, 15] else 0 for q in quality_flags]

# Final integration step
running_total = 0
weight_factor = 1.25
for i, data_point in enumerate(performance_data):
    if reliability_mask[i]:
        running_total += data_point * weight_factor
    else:
        running_total += data_point * 0.75

# Additional distraction: unused control flow
if len(processed_readings) > 10:
    final_adjustment = 999
else:
    final_adjustment = 0  # Dead code path (condition always false)

# Key statement
final_score = int(running_total + baseline_offset // 4)

# Print result as required
print(f"Result: {final_score}")