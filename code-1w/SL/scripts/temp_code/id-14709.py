def analyze_readings(sensor_data, thresholds):
    alert_level = 0
    temp_score = 0
    stability_index = 1.0
    decay_factor = 0.98

    # Irrelevant pre-processing (distractor)
    baseline_offset = sum([x * 0.01 for x in sensor_data])
    adjusted_data = [x + baseline_offset for x in sensor_data]

    for i, reading in enumerate(adjusted_data):
        if reading > thresholds['high']:
            alert_level += 2
            temp_score -= 1
        elif reading < thresholds['low']:
            alert_level += 1
            temp_score -= 2
        else:
            temp_score += 1

        # Red herring: unused transformation
        inverted = 1 / (reading + 1e-5)
        normalized = (reading - thresholds['low']) / (thresholds['high'] - thresholds['low'] + 1e-5)

    # Dead code path (never executed due to logic)
    if alert_level > 100:
        return -999

    return temp_score + alert_level


def evaluate_consistency(log_entries):
    # Unused function - decoy
    return len(set(log_entries)) / (len(log_entries) + 1)


def transform_sequence(seq, mode='standard'):
    # Distractor transformation with bit manipulation
    result = []
    mask = 0b1111
    shift_op = 3

    for val in seq:
        masked = val & mask
        shifted = val >> shift_op
        combined = masked ^ shifted
        result.append(combined * 2)

    return result

# Main execution chain with relevant and irrelevant components
raw_signals = [12, 15, 10, 8, 23, 7, 9, 14]
safety_limits = {'low': 9, 'high': 20}

# Complex but partially irrelevant data structure setup
event_timeline = {i: {'timestamp': t, 'flagged': False} for i, t in enumerate(range(100, 100 + len(raw_signals)))}

for idx, signal in enumerate(raw_signals):
    if signal < safety_limits['low'] or signal > safety_limits['high']:
        event_timeline[idx]['flagged'] = True

# Decoy list comprehension with string operations (irrelevant)
diagnostic_tags = ['ERR' if 'flagged' in item and item['flagged'] else 'OK' for item in event_timeline.values()]
error_count = diagnostic_tags.count('ERR')

# Core processing chain (relevant)
processing_chain = [
    analyze_readings(raw_signals[:4], safety_limits),
    analyze_readings(raw_signals[4:], safety_limits),
    analyze_readings(raw_signals[::-1], safety_limits)
]

# Set operations as required feature (partially distracting)
unique_diagnostics = set(processing_chain)
all_diagnostics = set(range(-20, 20))
exclusive_zone = all_diagnostics - unique_diagnostics  # Unused

# Conditional expression with zip and enumerate (required python features)
validation_map = {}
for i, (a, b) in enumerate(zip(processing_chain, processing_chain[1:] + [0]))):
    key_metric = a * 0.7 + b * 0.3
    validation_map[i] = 'valid' if key_metric > 0 else 'invalid'

# Critical statement embedded in complex logic
intermediate_result = sum(x * (x > 0) for x in processing_chain)
backup_state = transform_sequence([int(x) for x in processing_chain])

# Final computation - only this matters
final_diagnostic = 0
for k, v in validation_map.items():
    if v == 'valid':
        final_diagnostic += processing_chain[k] * (k + 1)

# Irrelevant floating-point accumulation
cumulative_drift = 0.0
for x in raw_signals:
    cumulative_drift += x * 0.001
    cumulative_drift = round(cumulative_drift, 6)

# Output required result
print(f"Result: {final_diagnostic}")