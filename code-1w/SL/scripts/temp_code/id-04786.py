import math

# Simulated sensor data from a distributed environmental monitoring system
def fetch_sensor_readings():
    raw_signals = [
        [1.2, 0.8, 3.4, 2.1, 0.9],
        [2.3, 1.7, 0.5, 4.4, 3.3],
        [0.6, 2.2, 1.8, 3.6, 2.9],
        [1.1, 1.3, 2.7, 3.0, 4.1]
    ]
    return raw_signals

# Legacy function - unused but looks relevant
def legacy_calibrate(x):
    return [val * 0.95 for val in x]

# Noise reduction using moving average filter
def smooth_signal(signal):
    smoothed = []
    for row in signal:
        temp = [row[0]]
        for i in range(1, len(row)-1):
            temp.append((row[i-1] + row[i] + row[i+1]) / 3)
        temp.append(row[-1])
        smoothed.append([round(x, 2) for x in temp])
    return smoothed

# Character frequency analysis (distractor function - looks important)
def analyze_chars(data_str):
    freq = {}
    for c in data_str:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Generate checksum for data integrity (red herring)
def compute_checksum(arrays):
    total = 0
    for arr in arrays:
        for val in arr:
            total ^= int(val * 100)  # Bitwise XOR on scaled values
    return total % 1000

# Real-time threshold mapping based on historical baselines
def generate_thresholds(readings):
    thresholds = []
    for idx, segment in enumerate(readings):
        base = sum(segment) / len(segment)
        variation = math.sqrt(sum((x - base) ** 2 for x in segment) / len(segment))
        high_thresh = base + variation * 1.8
        low_thresh = base - variation * 0.7
        thresholds.append((high_thresh, low_thresh))
    return thresholds

# Data normalization using z-score (unused path)
def normalize_zscore(data):
    mean_val = sum(sum(row) for row in data) / sum(len(row) for row in data)
    variance = sum(sum((x - mean_val) ** 2 for x in row) for row in data) / sum(len(row) for row in data)
    std_dev = math.sqrt(variance)
    return [[(x - mean_val) / std_dev for x in row] for row in data]

# Core diagnostic engine - analyzes signal anomalies
def count_anomalies(series, thresholds):
    count = 0
    for i, val in enumerate(series):
        high, low = thresholds[i % len(thresholds)]
        if val > high or val < low:
            count += 1
    return count

# Main analysis with multiple data transformations
def analyze_signal(data_blocks, limits):
    aggregate_score = 0
    
    # Irrelevant intermediate transformation
    dummy_encoded = []
    for block in data_blocks:
        encoded = []
        for val in block:
            b = int(val * 10) & 255
            b = (b ^ 142) >> 2  # Bit manipulation red herring
            encoded.append(b)
        dummy_encoded.append(encoded)
    
    # Actual processing begins here
    flat_data = []
    for block in data_blocks:
        flat_data.extend(block)
    
    # Compute weighted significance
    weights = [math.cos(i * 0.1) ** 2 for i in range(len(flat_data))]
    weighted_sum = sum(flat_data[i] * weights[i] for i in range(len(flat_data)))
    
    # Anomaly detection across all channels
    total_anomalies = 0
    for i, block in enumerate(data_blocks):
        cycle_limits = [(limits[j][0] * (1.1 - 0.1*i), limits[j][1] * (0.9 + 0.05*i)) 
                        for j in range(len(limits))]
        anomalies_in_block = count_anomalies(block, cycle_limits)
        total_anomalies += anomalies_in_block
    
    # Secondary validation metric (distractor)
    valid_points = 0
    for block in data_blocks:
        for val in block:
            if 0.5 <= val <= 4.5:
                valid_points += 1
    
    # Critical calculation: entropy-based confidence
    entropy = 0
    for val in flat_data:
        if val > 0:
            p = val / sum(flat_data)
            entropy -= p * math.log(p)
    
    # Final diagnostic formula combining multiple factors
    size_factor = len(data_blocks) * len(data_blocks[0])
    anomaly_penalty = total_anomalies * 8.3
    entropy_boost = entropy * 15.7
    
    result = (weighted_sum * 2.4) - anomaly_penalty + entropy_boost + (size_factor * 0.9)
    
    # Dead code branch - never executed due to prior logic
    if len(dummy_encoded) > 100:
        correction = 0
        for row in dummy_encoded:
            for cell in row:
                correction += cell & 3
        result -= correction

    return round(result, 4)

# Orchestration function
def main_pipeline():
    # Fetch and preprocess data
    raw_data = fetch_sensor_readings()
    
    # Unused alternative processing path
    if any(len(row) != 5 for row in raw_data):
        raise ValueError("Inconsistent dimensions")
    
    processed_data = smooth_signal(raw_data)
    
    # Generate dynamic thresholds
    baseline_ref = [[x*0.92 for x in row] for row in raw_data]
    threshold_map = generate_thresholds(baseline_ref)
    
    # Compute irrelevant checksum
    chksum = compute_checksum(processed_data)
    
    # Analyze character patterns in metadata (complete distractor)
    meta_tag = "sensor_v4_array"
    char_analysis = analyze_chars(meta_tag)
    diversity_index = len(char_analysis)
    
    # Core diagnostic call
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execute main logic
if __name__ == "__main__":
    main_pipeline()