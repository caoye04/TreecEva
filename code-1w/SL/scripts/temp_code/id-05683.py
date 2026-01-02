import math

# Simulated system telemetry data with mixed signal types
def generate_signals(duration_ms):
    return [int((i * 1.7) % 13) for i in range(duration_ms)]

# Irrelevant helper: converts numeric code to symbolic label (not used in final result)
def code_to_label(code):
    labels = {1: 'INFO', 2: 'WARN', 3: 'CRIT', 4: 'DEBUG'}
    return labels.get(code, 'UNKNOWN')

# Misleading aggregation function that computes unused statistics
def compute_rolling_avg(data, window=5):
    if len(data) < window:
        return [0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages  # Never used in critical path

# Decoy function: appears important but is never called
def trigger_calibration(sequence):
    checksum = 0
    for val in sequence:
        checksum ^= (val * 3) % 17
    return checksum > 5

# Core processing pipeline
log_entries = generate_signals(128)  # 128ms sampling period

# Distraction: multiple irrelevant variables
buffer_overflow_flag = False
last_known_state = {'timestamp': 0, 'value': -1}
redundant_sum = sum(x ** 0.5 for x in log_entries if x % 3 == 0)

# Unused diagnostic thresholds
safety_margin = 0.85
grace_period_ms = 10

system_threshold = 7.5
emergency_cap = 1000  # Red herring constant

# Conditional expression and lambda usage
weight_fn = lambda x: 1.2 if x > system_threshold else 0.8

# Complex data transformation with nested logic
weighted_magnitude = 0
anomaly_count = 0
suppressed_flags = []

for idx, entry in enumerate(log_entries):
    # Nested conditional branches with side distractions
    if entry > 10:
        anomaly_count += 1
        suppressed_flags.append(idx)
    elif entry > system_threshold:
        # Multiple arithmetic operations and bit manipulation
        scaled_entry = (entry * 1.45) + 2
        adjusted = int(scaled_entry) >> 1
        weighted_magnitude += adjusted * weight_fn(entry)
    
    # Dead branch: condition never met in this data
    if idx > 200:  # Impossible given range
        backup_reset = True
        last_known_state['timestamp'] = idx

# Distractor: min/max/average calculations on irrelevant subset
peak_suppression = max(suppressed_flags) if suppressed_flags else 0
temporal_offset = min(suppressed_flags, default=128)

# Character counting decoy (based on fake message)
fault_message = "SYS_OVERLOAD_DETECTED"
char_count_score = len([c for c in fault_message if c in 'AEIOU'])

# Key computation: average magnitude per non-zero weighted segment
segment_divider = anomaly_count or 1
average_per_anomaly = weighted_magnitude / segment_divider

# Final decision logic with conditional expression
baseline_correction = 37.5 if len(log_entries) > 100 else 25.0

# Critical statement: combines arithmetic, comparison, and prior accumulations
def process_metrics(entries, threshold):
    raw_total = sum(abs(math.sin(x / 3)) for x in entries)
    adjustment_factor = 1.0 if raw_total > threshold * 10 else 0.9
    intermediate = raw_total * adjustment_factor + baseline_correction
    
    # Additional layer: compare against rolling trend (unused earlier)
    historical_trend = compute_rolling_avg(entries, 8)
    trend_influence = len(historical_trend) % 7  # Artificial influence
    
    final_value = intermediate - (trend_influence * 2.3)
    return int(final_value)  # Deterministic integer output

final_diagnostic = process_metrics(log_entries, system_threshold)

# Ensure result is printed in required format
print(f"Target result: {final_diagnostic}")