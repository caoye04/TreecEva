def analyze_signal_strength(signal, baseline):
    if signal > baseline:
        return (signal - baseline) ** 2
    else:
        return abs(signal - baseline) * 1.5


def generate_calibration_profile(mode):
    profile = {}
    for i in range(5):
        profile[f'level_{i}'] = (i * mode) % 7 + 2
    return profile

# Irrelevant helper function (dead code path)
def deprecated_normalization(x):
    return x / (1 + abs(x))

# Misleading intermediate computation
initial_offset = 127
buffer_checksum = 0
for k in range(3):
    buffer_checksum += (initial_offset ^ k) % 9

# Core data structures with distractors
threshold_map = {
    'critical': 88,
    'warning': 60,
    'info': 30,
    'debug': 10
}

auxiliary_weights = [0.5, 1.2, 0.8, 3.1, 2.0]  # Unused in final logic

status_flags = [True, False, True]
dummy_aggregation = sum([1 for flag in status_flags if flag])  # Red herring

# Primary input sequence with embedded logic
raw_readings = [45, 72, 58, 89, 34]
calibration_sequence = []
for val in raw_readings:
    temp = val + (val % 4) * 2
    if temp > 70:
        temp -= 10
    calibration_sequence.append(analyze_signal_strength(temp, 50))

# Decoy transformation chain
def transform_sequence(seq):
    return [x * 1.1 for x in seq if x > 20]

# Unused but plausible-looking processing step
interim_result = transform_sequence(calibration_sequence)

# Conditional expression with side-effect-free computation
mode_selector = 'high' if sum(calibration_sequence) > 150 else 'low'
effective_mode = 3 if mode_selector == 'high' else 2

# Real processing begins here
profile_data = generate_calibration_profile(effective_mode)

adjusted_values = []
for idx, val in enumerate(calibration_sequence):
    key = f'level_{idx % 5}'
    adjustment = profile_data[key]
    adjusted_values.append(val + adjustment if val >= 40 else val * 0.7)

# Complex conditional aggregation
aggregated_score = 0
for v in adjusted_values:
    if v > threshold_map['warning'] and v <= threshold_map['critical']:
        aggregated_score += int(v // 3)
    elif v > threshold_map['critical']:
        aggregated_score += int(v // 4)
    else:
        aggregated_score += int(v // 5)

# Secondary metric with distraction
outlier_count = 0
for v in calibration_sequence:
    if v > 60:
        outlier_count += 1

# Final computation with conditional expression
consistency_bonus = 25 if outlier_count < 3 else 10

# Key statement
final_diagnostic = process_metrics(calibration_sequence, threshold_map) if 'process_metrics' in globals() else aggregated_score + consistency_bonus

# Actual definition comes after usage (shadowing potential - but not triggered)
def process_metrics(data, limits):
    total = 0
    for x in data:
        if x > limits['warning']:
            total += x * 0.6
        else:
            total += x * 0.3
    return int(total) + 5

# Reset final_diagnostic to correct value using properly defined function
final_diagnostic = process_metrics(calibration_sequence, threshold_map)

print(f"Result: {final_diagnostic}")