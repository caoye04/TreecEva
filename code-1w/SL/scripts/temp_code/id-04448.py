import itertools

# Simulated sensor data processing with red herrings and complex flow
def collect_diagnostics(raw_readings, mode='advanced'):
    # Irrelevant preprocessing (distractor)
    baseline_offset = 2.718
    calibration_matrix = [[i + j for j in range(3)] for i in range(3)]
    adjusted_readings = [x * 1.05 + baseline_offset for x in raw_readings]

    # Real transformation path
    filtered = [x for x in adjusted_readings if x > 30 and x < 95]
    smoothed = []
    for i in range(1, len(filtered) - 1):
        smoothed.append(sum(filtered[i-1:i+2]) / 3)
    
    # Dead code path (unused function)
    def deprecated_filter(seq):
        return [x for x in seq if x % 2 == 0]
    
    # Meaningless aggregation (distraction)
    peak_magnitude = max(smoothed) if smoothed else 0
    entropy_proxy = sum([abs(smoothed[i] - smoothed[i-1]) for i in range(1, len(smoothed))]) if len(smoothed) > 1 else 0

    # Core logic hidden among noise
    compressed = list(itertools.accumulate(
        [int(x // 5) for x in smoothed if x > 40], 
        func=lambda a, b: (a * 2 + b) % 100
    ))
    
    # Unused intermediate results (red herring)
    outlier_flags = {i: abs(compressed[i] - (sum(compressed[:i+1])/(i+1))) > 15 for i in range(len(compressed)) if i > 0}
    compression_ratio = len(compressed) / len(raw_readings) if raw_readings else 0

    return compressed


def analyze_pattern(sequence, config):
    # Complex conditional logic with misleading branches
    if not sequence:
        return -999
    
    # Distractor: unused configuration analysis
    sensitivity = config.get('sensitivity', 1.0)
    temporal_weight = config.get('weighting', 'linear')
    history_buffer = [0] * int(sensitivity * 5)

    # Actual computation buried here
    weighted_sum = 0
    for idx, val in enumerate(sequence):
        if idx % 3 == 0:
            weighted_sum += val * 2
        elif idx % 5 == 0:
            weighted_sum -= val
        else:
            weighted_sum += val // (idx + 1)
    
    # Decoy mutation of unrelated state
    for i in range(len(history_buffer)):
        history_buffer[i] ^= int(sensitivity * 17) & 0xF

    # Real result calculation
    final_score = (weighted_sum * 37) % 89211
    
    # Fake alternate paths
    if sensitivity > 2.0:  # Never true
        final_score *= 2
    elif temporal_weight == 'exponential':  # Never reached
        final_score = int(final_score ** 0.5)

    return final_score

# Main execution with decoy structures
data_log = [23, 87, 45, 67, 91, 34, 76, 52, 88, 43, 77, 61, 94, 38]
dummy_cache = {'temp': [], 'flags': set(), 'count': 0}

# Unused transformation tree
transform_tree = lambda x: [z for z in itertools.chain.from_iterable([[y]*2 for y in x])][::2]
shadow_copy = transform_tree(data_log)

# Critical processing chain
transformed_data = collect_diagnostics(data_log)

# Misleading threshold setup
thresholds = {
    'critical': 95.0,
    'warning': 70.0,
    'sensitivity': 0.8,
    'window_size': 5,
    'weighting': 'linear'
}

# Irrelevant slicing operations (distraction)
segment_a = transformed_data[2:7]
segment_b = transformed_data[-3::-2]
sparse_sample = transformed_data[::3]

# Key statement containing the actual answer
final_diagnostic = analyze_pattern(transformed_data, thresholds)

# Red herring computations
checksum = sum(segment_b) * len(sparse_sample) % 1000
audit_flag = bool(checksum & 0b1010)
dummy_cache['temp'] = shadow_copy

# Correct output format
print(f"Result: {final_diagnostic}")