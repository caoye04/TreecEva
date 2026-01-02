import math

# Simulated sensor array data processing for environmental anomaly detection
def collect_sensor_readings():
    raw_readings = [
        1.2, 3.5, 2.1, 4.8, 5.0, 3.3, 2.7, 4.4, 6.1, 5.9,
        0.8, 1.9, 3.0, 4.2, 5.5, 6.3, 7.0, 6.8, 5.7, 4.9
    ]
    return raw_readings

# Irrelevant helper: converts floats to strings (distractor)
def float_to_code(values):
    return [f'V{int(v * 10):03d}' for v in values]

# Noise filtering using moving average (partially relevant)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        window_avg = sum(signal[start:end]) / (end - start)
        smoothed.append(window_avg)
    return smoothed

# Transform data into z-scores (relevant)
def standardize(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return [0 for _ in data]
    return [(x - mean_val) / std_dev for x in data]

# Detect upward trends using pairwise comparison (red herring)
def detect_trends(sequence):
    trend_flags = []
    for i in range(1, len(sequence)):
        trend_flags.append(1 if sequence[i] > sequence[i-1] else 0)
    return trend_flags  # unused later

# Apply non-linear transformation to amplify extremes (relevant)
def nonlinear_amplify(z_scores):
    return [math.tanh(x * 1.5) * 2 for x in z_scores]

# Dummy function that looks important but does nothing (dead code path)
def validate_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, float):
            checksum ^= int(item * 100) & 0xFF
    return hex(checksum)  # never used

# Core analysis: count significant deviations above threshold (key logic)
def analyze_pattern(processed, limits):
    count_a = sum(1 for x in processed[:len(processed)//2] if x > limits[0])
    count_b = sum(1 for x in processed[len(processed)//2:] if x < limits[1])
    interaction_score = 0
    for i, val in enumerate(processed):
        if i % 3 == 0 and val > limits[0]:
            interaction_score += 1
    return count_a * 3 - count_b + interaction_score

# Secondary analysis that seems related but isn't used (decoy)
def compute_entropy(data):
    from collections import Counter
    counts = Counter([round(x, 1) for x in data])
    total = len(data)
    entropy = -sum((cnt/total) * math.log2(cnt/total) for cnt in counts.values())
    return round(entropy, 4)

# Unused pattern matcher (distractor)
def find_repeating_patterns(seq, length=3):
    seen = {}
    for i in range(len(seq) - length + 1):
        sub = tuple(seq[i:i+length])
        seen[sub] = seen.get(sub, 0) + 1
    return {k: v for k, v in seen.items() if v > 1}

# Main execution pipeline
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    readings = collect_sensor_readings()
    
    # Step 2: Convert to codes (irrelevant - distractor)
    codes = float_to_code(readings)
    
    # Step 3: Smooth signal (partially relevant preprocessing)
    filtered = smooth_signal(readings)
    
    # Step 4: Standardize to z-scores (relevant)
    z_data = standardize(filtered)
    
    # Step 5: Amplify non-linearly (relevant)
    transformed_data = nonlinear_amplify(z_data)
    
    # Step 6: Detect trends (unused result - red herring)
    trends = detect_trends(transformed_data)
    
    # Step 7: Validate checksum (no side effects - dead code)
    chk = validate_checksum(transformed_data)
    
    # Step 8: Compute entropy (computed but not used - decoy)
    entropy_metric = compute_entropy(transformed_data)
    
    # Step 9: Find repeating patterns (never used - distractor)
    patterns = find_repeating_patterns(transformed_data)
    
    # Step 10: Define thresholds for anomaly detection
    thresholds = [0.75, -0.75]  # high positive, low negative
    
    # Step 11: Analyze pattern for diagnostic score (KEY STATEMENT)
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Step 12: Print result
    print(f"Result: {final_diagnostic}")