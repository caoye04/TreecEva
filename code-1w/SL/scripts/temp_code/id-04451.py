import itertools

def preprocess_readings(raw_readings):
    # Irrelevant preprocessing: converts to dB but unused later
    return [20 * abs(r) ** 0.5 for r in raw_readings if r > -5]

def compute_harmonic(series):
    # Distractor function: calculates harmonic mean but not used in final path
    total = sum(1 / x for x in series if x != 0)
    return len(series) / total if total else 0

def detect_anomalies(stream, threshold=0.85):
    # Dead code path: never called in execution
    flags = []
    for i, val in enumerate(stream):
        if val > threshold * max(stream):
            flags.append(i)
    return flags

def generate_phase_shift(signal):
    # Unused transformation: simulates phase shift but irrelevant
    shifted = [signal[i - 2] for i in range(len(signal))]
    return [s * 0.9 + 1.1 for s in shifted]

def validate_consistency(entries):
    # Misleading validation: computes checksum but not tied to output
    checksum = 0
    for idx, e in enumerate(entries):
        checksum += (idx + 1) * e % 3
    return round(checksum, 3)

def extract_peaks(readings):
    # Partially relevant: extracts peaks but only peak_count is used indirectly
    peaks = [readings[i] for i in range(1, len(readings)-1)
             if readings[i-1] < readings[i] > readings[i+1]]
    peak_count = len(peaks)
    smoothed_peaks = [p * 0.95 for p in peaks]
    return smoothed_peaks, peak_count  # Only peak_count matters

def calculate_entropy(values):
    # Red herring: computes information entropy, never used
    freqs = {}
    for v in values:
        freqs[v] = freqs.get(v, 0) + 1
    from math import log
    total = len(values)
    entropy = -sum((count/total) * log(count/total, 2) for count in freqs.values())
    return round(entropy, 4)

def aggregate_metrics(dataset, sequence):
    # Core logic with distractors
    baseline = [d * 1.05 for d in dataset]
    
    # Key branching logic
    if len(baseline) > 5:
        subset = baseline[1:-1]
    else:
        subset = baseline
        
    # Real computation begins
    indexed_pairs = list(enumerate(subset))
    paired_data = list(zip(subset, sequence))
    
    # Extract key features
    weighted_sum = 0
    for i, (val, seq_val) in enumerate(paired_data):
        if i % 2 == 0:
            weighted_sum += val * seq_val
        else:
            weighted_sum -= val * 0.5
    
    # Critical intermediate
    adjusted_total = weighted_sum * 1.2
    
    # Simulated diagnostic filters
    filters_applied = 0
    temp_log = []
    for j in range(3):
        if adjusted_total > 100:
            adjusted_total *= 0.9
            filters_applied += 1
            temp_log.append(f"Filter-{j}")
        else:
            break
    
    # Extract peaks (only count matters)
    _, peak_count = extract_peaks(subset)
    
    # Decoy accumulation
    decoy_accumulator = 0
    for group in itertools.groupby(sorted(subset), key=lambda x: x // 10):
        decoy_accumulator += len(list(group[1]))
    
    # Final metric formation
    stability_score = adjusted_total / (peak_count + 1)
    noise_floor = sum(1 for x in subset if x < 15) * 2.5
    final_diagnostic = int(stability_score - noise_floor + filters_applied * 3)
    
    # Unused trace variables
    debug_trace = f"Final state: score={stability_score}, floor={noise_floor}"
    auxiliary_metric = calculate_entropy([int(x) for x in subset])
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input data
    turbine_data = [23.5, 18.2, 45.7, 31.8, 39.1, 27.4, 41.6]
    calibration_sequence = [1.1, 0.9, 1.2, 0.8, 1.0, 1.3, 0.7]
    
    # Irrelevant preprocessing calls
    processed = preprocess_readings(turbine_data)
    harmonic = compute_harmonic(turbine_data)
    consistency = validate_consistency(turbine_data)
    
    # Actual target computation
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
    
    # Output result
    print(f"Result: {final_diagnostic}")