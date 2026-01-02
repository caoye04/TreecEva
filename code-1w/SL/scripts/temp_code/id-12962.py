import math

def analyze_signal_strength(signal):
    # Irrelevant preprocessing
    normalized = [x * 0.98 for x in signal]
    filtered = [x for x in normalized if x > -50]
    return sum(filtered) / len(filtered)

def compute_entropy(data):
    # Distractor function: not used in main logic
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_features(dataset):
    # Red herring feature extraction
    means = [sum(seq) / len(seq) for seq in dataset]
    variances = []
    for seq in dataset:
        mean = sum(seq) / len(seq)
        variance = sum((x - mean) ** 2 for x in seq) / len(seq)
        variances.append(variance)
    
    # Misleading intermediate
    peak_to_average_ratio = max(means) / (sum(means) / len(means)) if means else 0
    
    # Unused transformation
    transformed = [math.sin(x / 10) for x in means]
    
    return means, variances  # Only means used later

def validate_readings(readings):
    # Complex validation with dead code branches
    status_flags = []
    for reading in readings:
        if len(reading) == 0:
            status_flags.append(-1)
        elif sum(reading) < 0:
            status_flags.append(0)
        elif all(x > 10 for x in reading):
            status_flags.append(2)
        else:
            status_flags.append(1)
    
    # Dead code path (never executed due to logic above)
    for i in range(len(status_flags)):
        if status_flags[i] == 999:  # Impossible condition
            status_flags[i] = -999
    
    return status_flags

def aggregate_metrics(nested_readings, thresholds):
    # Core logic buried in distractions
    
    # Irrelevant slicing and set operations (distractors)
    flat_data = [item for sublist in nested_readings for item in sublist]
    unique_values = set(flat_data)
    outlier_region = flat_data[::3]  # Every third element – unused
    
    # Key computation: average of max values per sequence
    max_per_seq = [max(seq) for seq in nested_readings if seq]
    avg_max = sum(max_per_seq) / len(max_per_seq)
    
    # Secondary metric (misleading)
    threshold_met = [1 for m in max_per_seq if m > thresholds.get('critical', 85)]
    compliance_rate = len(threshold_met) / len(max_per_seq)
    
    # Bit manipulation decoy
    bit_analysis = 0
    for val in max_per_seq:
        bit_analysis ^= int(val) & 0xFF
    
    # Hidden key calculation: median of averages above threshold
    valid_sequences = [seq for seq in nested_readings if max(seq) > thresholds.get('minimum', 20)]
    averages = [sum(seq)/len(seq) for seq in valid_sequences]
    sorted_averages = sorted(averages)
    n = len(sorted_averages)
    if n % 2 == 1:
        median_avg = sorted_averages[n//2]
    else:
        median_avg = (sorted_averages[n//2-1] + sorted_averages[n//2]) / 2
    
    # Final diagnostic based on median average, NOT the obvious metrics
    scaling_factor = thresholds.get('scale', 1.75)
    adjustment = math.log(median_avg + 1, 2) if median_avg > 0 else 0
    final_diagnostic = int((median_avg * scaling_factor) - adjustment)
    
    # Print irrelevant diagnostics
    print(f"Signal baseline: {analyze_signal_strength(flat_data[:10])}")
    print(f"Entropy proxy: {compute_entropy([int(x) for x in flat_data[::2]])}")
    
    return final_diagnostic

# Main execution with red herrings
if __name__ == "__main__":
    # Simulated sensor array readings (real data)
    nested_readings = [
        [23, 85, 12, 77, 91],
        [67, 45, 88, 29],
        [],
        [15, 73, 94, 33, 82],
        [90, 87, 93]
    ]

    # Threshold configuration (some keys unused)
    thresholds = {
        'minimum': 20,
        'warning': 60,
        'critical': 85,
        'scale': 1.75,
        'decay': 0.92
    }

    # Unused variables and misleading assignments
    baseline_ref = [x[0] for x in nested_readings if x]
    fallback_value = sum(baseline_ref) // len(baseline_ref) if baseline_ref else 0
    temp_matrix = [[i + j for j in range(3)] for i in range(3)]
    
    # Validate readings (result not used)
    validation_status = validate_readings(nested_readings)
    
    # Extract features (partially used)
    feature_means, _ = extract_features(nested_readings)
    
    # Introduce string manipulation distraction
    log_tag = "DIAG-" + "-".join(f"{int(x)}" for x in feature_means[:3])
    timestamp_code = sum(ord(c) for c in "2023-11-05") % 1000
    
    # Core call
    final_diagnostic = aggregate_metrics(nested_readings, thresholds)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")