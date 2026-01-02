import itertools

# Simulated sensor data from a distributed monitoring system
def fetch_sensor_readings():
    return [18, 22, 19, 25, 21, 17, 24, 20, 23, 16]

# Legacy calibration adjustment (irrelevant for current model)
def legacy_adjust(values):
    return [v * 0.98 + 1.2 for v in values]

# Critical: Normalize readings to baseline range [0, 1]
def normalize(readings):
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

# Apply noise filter using moving average (distraction)
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

# Bitmask-based fault detection (partially relevant)
def detect_anomalies(values):
    flags = []
    for v in values:
        # Simulate bit-encoded diagnostics: bit 2 set if outlier
        is_outlier = v < 0.2 or v > 0.8
        flag = (1 << 3) if is_outlier else 0
        flag |= (1 << 1)  # Always set debug mode
        flags.append(flag)
    return flags

# Compute entropy of distribution (red herring)
def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    return -sum((count / total) * log2(count / total) for count in freq.values())

# Core diagnostic aggregator (critical path)
def aggregate_metrics(chains, diagnostics):
    base_score = 0
    for chain in chains:
        for val in chain:
            base_score += int(val * 100)  # Convert normalized to integer score
    # XOR all diagnostic flags
    final_flag = 0
    for d in diagnostics:
        final_flag ^= d
    # Final computation combines score and flag bits
    return base_score ^ final_flag  # Key deterministic result

# Unused recursive validator (dead code path)
def validate_hierarchy(data, index=0):
    if index >= len(data):
        return True
    if data[index] < 0:
        return False
    return validate_hierarchy(data, index + 1)

# Simulate multi-stage processing pipeline
if __name__ == '__main__':
    raw_readings = fetch_sensor_readings()
    
    # Irrelevant legacy processing branch
    calibrated = legacy_adjust(raw_readings)
    entropy_value = compute_entropy(calibrated)  # Unused metric
    
    # Main processing chain
    normalized = normalize(raw_readings)
    filtered = smooth_signal(normalized, window=2)  # Slight smoothing
    
    # Diagnostic generation
    anomaly_flags = detect_anomalies(normalized)
    
    # Construct multiple processing chains (only first used)
    processing_chain = []
    processing_chain.append(normalized)
    processing_chain.append([x ** 2 for x in normalized])  # Unused transformation
    processing_chain.append([abs(x - 0.5) for x in normalized])  # Unused asymmetry check
    
    # Spurious sorting operation (no effect on result)
    sorted_flags = sorted(anomaly_flags, reverse=True)
    
    # Critical aggregation step
    final_diagnostic = aggregate_metrics(processing_chain, anomaly_flags)
    
    # Dead logic branch
    if sum(anomaly_flags) < 10:
        final_diagnostic = -1  # Never reached due to flag values
    
    # Additional distraction: slicing with no impact
    tail_data = filtered[-5:]
    peak_slice = tail_data[:3]
    
    # Generate combinatorial pairs (completely irrelevant)
    pairs = list(itertools.combinations([1, 2, 3], 2))
    
    # Output target result
    print(f"Result: {final_diagnostic}")