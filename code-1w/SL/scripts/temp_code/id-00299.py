def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant signal processing steps
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    high_freq_components = [x for x in normalized if x > threshold]
    return len(high_freq_components) > 0


def compute_checksum(data_sequence):
    # Bitwise checksum, not actually used in final logic
    checksum = 0
    for val in data_sequence:
        checksum ^= int(val * 100) & 0xFF
    return checksum

# Simulated sensor readings and system flags
detection_flags = {"sensor_a": True, "sensor_b": False, "sensor_c": True}
baseline_metrics = [0.82, 0.91, 0.77, 0.65, 0.88]

# Distractor: unused intermediate calculations
temporal_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
weighted_avg = sum(baseline_metrics[i] * temporal_weights[i] for i in range(len(temporal_weights)))

# Unused data structure (set operation red herring)
expected_range = set(range(50, 100))
observed_values = {int(x * 100) for x in baseline_metrics}
outliers = observed_values - expected_range  # Not used later

# Simulate auxiliary status (distractor)
system_status = {}
system_status['calibrated'] = all(x > 0.6 for x in baseline_metrics)
system_status['redundancy_active'] = sum(detection_flags.values()) >= 2
system_status['fallback_mode'] = False

# Additional irrelevant function
def trigger_diagnostic(level):
    return f'Diagnostic level {level} initiated'

# Real logic begins here — conditional state tracking
active_sensors = [k for k, v in detection_flags.items() if v]
coverage_ratio = len(active_sensors) / len(detection_flags)

# Boolean logic chain with short-circuiting
if coverage_ratio >= 0.5 and any(baseline_metrics) or False:
    performance_bonus = 10
else:
    performance_bonus = 0

# Core arithmetic-bits hybrid computation
raw_sum = sum(int(x * 10) for x in baseline_metrics)
bit_adjustment = (raw_sum >> 2) ^ 7  # Right shift then XOR

# Set-based filtering (relevant use)
valid_metrics_set = {x for x in baseline_metrics if x >= 0.7}
metric_count = len(valid_metrics_set)

# Final evaluation function (uses only specific inputs)
def evaluate_performance(flags, metrics):
    # Only uses presence of active sensors and count of valid metrics
    active_count = sum(flags.values())
    score = active_count * metric_count * 5
    score += performance_bonus  # Closure over outer scope
    return score

# Critical execution point
final_score = evaluate_performance(detection_flags, baseline_metrics)

# Output result
print(f'Result: {final_score}')