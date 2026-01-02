import itertools

# Simulate sensor data processing with noise filtering and signal analysis
def collect_sensor_readings():
    raw_samples = [0.1, 0.8, 0.3, 0.9, 0.2, 0.7, 0.4, 0.6]
    timestamps = list(range(len(raw_samples)))
    labeled_data = [f'sensor_{i}' for i in range(len(raw_samples))]
    
    # Irrelevant aggregation
    avg_sample = sum(raw_samples) / len(raw_samples)
    max_sample = max(raw_samples)
    sample_variance = sum((x - avg_sample) ** 2 for x in raw_samples) / len(raw_samples)
    
    # Distractor: unused transformation
    inverted = [1 - x for x in raw_samples if x < 0.5]
    
    # Relevant: zipped stream with metadata
    readings = list(zip(timestamps, raw_samples, labeled_data))
    return readings

# Noise filter using sliding window (not used in final path)
def smooth_signal(signal, window_size=2):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size)
        window = signal[start:i+1]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Auxiliary function: calculates entropy (red herring)
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * (count/total).__log__() for count in counts.values())
    return entropy

# Signal validator (used indirectly)
def validate_peaks(signal_vals):
    peak_count = 0
    for i in range(1, len(signal_vals) - 1):
        if signal_vals[i] > signal_vals[i-1] and signal_vals[i] > signal_vals[i+1]:
            peak_count += 1
    return peak_count > 2

# Core diagnostic logic
def analyze_signal_quality(buffer, threshold):
    # Extract only the numeric values
    values = [entry[1] for entry in buffer]
    
    # Distractor variables
    value_caps = [min(v, 0.7) for v in values]
    scaled_values = [v * 1.5 for v in values]
    filtered_high = [v for v in values if v > 0.5]
    
    # Unused statistical measures
    mean_val = sum(values) / len(values)
    deviation_sum = sum(abs(v - mean_val) for v in values)
    median_approx = sorted(values)[len(values)//2]
    
    # Critical computation path
    above_threshold = [v for v in values if v >= threshold]
    duration_score = len(above_threshold) * 10
    consistency_factor = sum(1 for a, b in zip(values, values[1:]) if abs(a - b) < 0.3)
    
    # Secondary distractor: complex combinatorics (unused)
    pair_combinations = list(itertools.combinations(values, 2))
    large_pairs = [p for p in pair_combinations if sum(p) > 1.0]
    
    # Key logic: use enumerate to detect sustained quality segments
    quality_segments = 0
    for idx, val in enumerate(values):
        if val >= threshold:
            # Check forward continuity
            future_window = values[idx:idx+2]
            if all(fv >= threshold * 0.9 for fv in future_window):
                quality_segments += 1
    
    # Final diagnostic score
    base_score = len(above_threshold) * 100
    adjustment = consistency_factor * 5
    penalty = 0
    
    # Conditional penalty (never triggered due to data)
    if len([v for v in values if v < 0.1]) > 1:
        penalty = 50
    
    # Redundant control flow (dead branch)
    debug_mode = False
    extra_offset = 0
    if debug_mode:
        extra_offset = sum(1 for v in values if v > 0.6 and v < 0.65)
    
    final_score = base_score + adjustment - penalty + extra_offset
    
    # Distractor: string manipulation with no impact
    status_tags = ['OK' if v >= threshold else 'LOW' for v in values]
    tag_summary = ''.join(status_tags)
    summary_length = len(tag_summary.replace('OK', ''))
    
    return final_score

# Misleading pre-processing chain
def prepare_diagnostics(raw_buffer):
    processed = []
    for t, v, l in raw_buffer:
        if v > 0.25:
            processed.append((t*2, v*0.95, l.upper()))
    return processed

# Unused recursive function (decoy)
def recursive_energy_estimate(n):
    if n <= 1:
        return 1
    return n * 0.8 + recursive_energy_estimate(n - 1)

# Main execution flow
sensor_data = collect_sensor_readings()

# Distractor transformations
processed_data = prepare_diagnostics(sensor_data)
downsampled = sensor_data[::2]

# Noise smoothing (computed but not used)
noisy_stream = [entry[1] for entry in sensor_data]
smoothed_stream = smooth_signal(noisy_stream, window_size=2)

# Entropy calculation on labels (irrelevant)
labels_only = [entry[2] for entry in sensor_data]
entropy_metric = calculate_entropy(labels_only)

# Validation check (called but result ignored)
valid_peak_structure = validate_peaks([entry[1] for entry in sensor_data])

# Critical statement
final_diagnostic = analyze_signal_quality(sensor_data, threshold=0.75)

print(f"Result: {final_diagnostic}")