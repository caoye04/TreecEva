import math

# Simulated sensor readings and system configuration
def collect_telemetry():
    raw_readings = [23.4, 19.5, 20.1, 25.3, 18.7, 22.0, 20.3]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800, 1623456805, 1623456810]
    statuses = ['OK', 'WARNING', 'OK', 'CRITICAL', 'OK', 'OK', 'ERROR']
    return list(zip(timestamps, raw_readings, statuses))

# Irrelevant helper - looks important but unused in critical path
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Distraction function: processes status but not used in final result
def analyze_status_pattern(status_log):
    transitions = 0
    for i in range(1, len(status_log)):
        if status_log[i-1] != status_log[i]:
            transitions += 1
    return transitions * 100  # red herring

# Core transformation pipeline
def filter_outliers(readings, threshold=1.8):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return [x for x in readings if abs(x - mean) <= threshold * std_dev]

# Unused but plausible preprocessing step
def normalize_range(data, new_min=0.0, new_max=1.0):
    old_min, old_max = min(data), max(data)
    return [(x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for x in data]

# Signal transformation with frequency analysis (distractor)
def compute_dft(samples):
    N = len(samples)
    real_parts = []
    for k in range(N):
        real = sum(samples[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        real_parts.append(real)
    return real_parts

# Data enhancement with irrelevant features
def augment_features(clean_data):
    enhanced = []
    for val in clean_data:
        feature_set = {
            'raw': val,
            'squared': val ** 2,
            'log_plus_one': math.log(val + 1),
            'inv_square': 1 / (val ** 2 + 1e-5),
            'oscillatory': math.sin(val) * math.cos(val / 2)
        }
        enhanced.append(feature_set)
    return enhanced

# Real processing chain starts here
transformed_data = []
def preprocess_stream(telemetry):
    global transformed_data
    readings_only = [item[1] for item in telemetry if item[2] != 'ERROR']
    
    # Actual relevant filtering
    filtered = filter_outliers(readings_only)
    
    # Add dummy timestamp grouping (partially relevant)
    grouped = {}
    for ts, val, st in telemetry:
        sec = ts // 10
        if sec not in grouped:
            grouped[sec] = []
        if st != 'ERROR':
            grouped[sec].append(val)
    
    # Only use values from valid groups
    consolidated = []
    for g in grouped.values():
        if len(g) >= 2:
            consolidated.extend(g)
    
    # Re-filter on consolidated data
    final_clean = filter_outliers(consolidated)
    
    # Apply lambda-based transformation
    transform_fn = lambda x: round(x ** 1.15 - 4.2, 3)
    transformed_data = [transform_fn(x) for x in final_clean]
    
    # Dead code branch - looks like it does something
    if len(transformed_data) > 10:
        transformed_data = transformed_data[:10]
    
    return transformed_data

# Configuration with misleading parameters
config = {
    'threshold': 0.95,
    'mode': 'aggressive',
    'weighting': 'quadratic',
    'version': '2.1b',
    'debug_trace': True,
    'sample_rate': 5,
    'units': 'kPa'
}

# Decoy accumulator - collects but doesn't contribute
historical_weights = []
for i in range(8):
    weight = (i + 1) * 0.25
    decay = 0.9 ** i
    historical_weights.append(weight * decay)

def aggregate_metrics(dataset, cfg):
    # Irrelevant branching based on config version
    if cfg['version'].startswith('1.'):
        scale = 0.5
    elif cfg['mode'] == 'conservative':
        scale = 0.7
    else:
        scale = 1.0  # this actually applies
    
    # Real accumulation logic
    base_sum = sum(dataset)
    
    # Red herring: complex weighting that isn't used
    temp_accum = 0.0
    for idx, val in enumerate(dataset):
        temp_accum += val * (0.95 ** idx)
    
    # Spurious normalization attempt
    if cfg['weighting'] == 'linear':
        adjusted = base_sum * 0.8
    elif cfg['weighting'] == 'exponential':
        adjusted = base_sum * 1.2
    else:
        adjusted = base_sum * 1.1  # actual adjustment
    
    # Final computation with truncation
    preliminary = adjusted * scale
    
    # Additional manipulation via list comprehension
    refined_values = [x * 1.05 for x in dataset if x > 18.0]
    refinement_bonus = sum(refined_values) * 0.01
    
    # The real answer contribution
    final_score = preliminary + refinement_bonus
    
    # Dead assignment - looks diagnostic but unused
    diagnostics = {
        'input_count': len(dataset),
        'processed_count': len(refined_values),
        'attenuation_factor': 0.99,
        'final_score': final_score
    }
    
    # Critical result
    final_diagnostic = int(round(final_score * 100))
    
    # Distractor: another unused metric
    signal_to_noise = final_score / (sum([abs(x) for x in compute_dft([1,2,3,4])]) + 1)
    
    return final_diagnostic

# Execution flow
sensor_data = collect_telemetry()
preprocess_stream(sensor_data)
final_diagnostic = aggregate_metrics(transformed_data, config)
print(f"Target result: {final_diagnostic}")