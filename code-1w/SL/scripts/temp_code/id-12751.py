def analyze_signal_integrity(raw_samples, threshold=0.75):
    filtered = [x for x in raw_samples if abs(x) > threshold]
    squared_energy = sum([x**2 for x in filtered])
    normalized_power = squared_energy / len(raw_samples) if raw_samples else 0
    return normalized_power


def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 6)


def transform_dataset(data_stream):
    # Irrelevant transformation path (dead logic)
    temp_buffer = []
    for item in data_stream:
        if isinstance(item, int) and item % 2 == 0:
            temp_buffer.append(item * 1.5)
    # Actual relevant logic
    processed = [x * 0.1 for x in data_stream if isinstance(x, (int, float))]
    return processed

# Misleading initialization block (distractor)
baseline_offset = 3.14159
reference_anchor = [1, 1, 2, 3, 5, 8, 13]
calibration_matrix = [[i+j for j in range(3)] for i in range(3)]

# Core system variables
raw_telemetry = [10, -20, 15, 0, -25, 30, 40, -10, 5, 0, -5]

# Decoy signal processing chain (unused)
signal_chain_a = analyze_signal_integrity(raw_telemetry, threshold=15.0)  # No effect due to high threshold

# Real signal analysis
active_signals = [x for x in raw_telemetry if x != 0]
dynamic_range = max(active_signals) - min(active_signals)
compression_ratio = len(raw_telemetry) / len(active_signals) if active_signals else 0

# Simulated diagnostic flags (some are red herrings)
flag_set = set()
if dynamic_range > 50:
    flag_set.add('RANGE_OVERFLOW')
elif dynamic_range > 30:
    flag_set.add('ELEVATED_RANGE')  # This will trigger

if compression_ratio < 1.2:
    flag_set.add('LOW_VARIANCE')

# Dummy entropy computation on transformed data (distractor)
transformed_data = transform_dataset(raw_telemetry)
dummy_entropy = compute_entropy([int(abs(x*10)) for x in transformed_data if x != 0])

# Conditional expression with meaningful outcome
status_code = 100 if 'ELEVATED_RANGE' in flag_set else 200

# Set operations for diagnostic grouping (required Python feature)
warning_flags = {'ELEVATED_RANGE', 'NOISE_SUSPECTED'}
critical_flags = {'RANGE_OVERFLOW', 'ELEVATED_RANGE'}
overlap = warning_flags & critical_flags  # Shared: ELEVATED_RANGE
severity_score = len(overlap) * 50

# Primary processing chain (key logic)
processing_chain = [
    sum(raw_telemetry),
    dynamic_range,
    severity_score,
    status_code
]

diagnostics = {
    'samples': len(raw_telemetry),
    'non_zero': len(active_signals),
    'power_level': analyze_signal_integrity(raw_telemetry, threshold=0),
    'stability': 'stable' if status_code == 100 else 'unstable'
}

# Final aggregation function (contains conditional expression)
def aggregate_metrics(chain, meta):
    base = chain[0] + chain[1]  # sum + dynamic_range
    penalty = 0
    if meta['stability'] == 'unstable':
        penalty = meta['samples'] // 4
    adjusted = base - penalty
    multiplier = 2 if chain[2] > 0 else 1  # Use severity
    result = adjusted * multiplier
    return int(result)

# Dead code path (never called)
def legacy_diagnostic(seq):
    return sum(seq) % 7

# Unused but plausible-looking computation
phantom_metric = sum(calibration_matrix[i][i] for i in range(3))

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Output required format
print(f"Target result: {final_diagnostic}")