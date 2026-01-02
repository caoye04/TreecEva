import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings(base_signal, noise_level, samples):
    return [base_signal + math.sin(i) * noise_level for i in range(samples)]

def filter_outliers(data, limit):
    # Irrelevant filtering function (dead code path)
    return [x for x in data if abs(x) < limit]

def compute_entropy(values):
    # Distractor: computes entropy but not used in final result
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities)

def shift_cipher(sequence, key):
    # Misleading transformation: looks important but unused
    return [(x + key) % 256 for x in sequence]

def detect_anomaly_cluster(series, sensitivity):
    # Dead logic branch: simulates anomaly detection
    anomalies = []
    for i in range(1, len(series)):
        if abs(series[i] - series[i-1]) > sensitivity:
            anomalies.append(i)
    return anomalies if len(anomalies) > 5 else []

def transform_sequence(raw_seq, mode):
    if mode == 'encode':
        return [int(x * 10) & 255 for x in raw_seq]  # Apply scaling and bitmask
    else:
        return [x ^ 170 for x in raw_seq]  # XOR obfuscation (not taken)

def analyze_pattern(dataset, cutoff):
    # Core logic: count how many values exceed cutoff after conditional adjustment
    adjusted = []
    for val in dataset:
        if val < 0:
            adjusted.append(abs(val) ** 1.5)
        elif val == 0:
            adjusted.append(1.0)
        else:
            adjusted.append(math.sqrt(val))
    # Key step: count entries above threshold
    count = sum(1 for x in adjusted if x > cutoff)
    # Secondary transformation: map count through bitwise manipulation
    temp = (count << 3) ^ 42
    temp = temp & 255  # Mask to byte range
    # Final nonlinear scaling
    return int((temp * 1.7) - 28)

# Main execution flow
if __name__ == "__main__":
    # Generate initial signal
    signal_stream = collect_readings(base_signal=4.2, noise_level=3.1, samples=97)
    
    # Irrelevant entropy computation (distractor)
    entropy_metric = compute_entropy(signal_stream)
    
    # Transform data using encode mode
    transformed_data = transform_sequence(signal_stream, mode='encode')
    
    # Unused cipher attempt
    obscured = shift_cipher(transformed_data, key=42)
    
    # Detect anomalies (result unused)
    clusters = detect_anomaly_cluster(transformed_data, sensitivity=50)
    
    # Filtering outliers (computed but not used)
    clean_data = filter_outliers(transformed_data, limit=200)
    
    # Define threshold based on constant pattern
    threshold = len([x for x in transformed_data if x > 128]) // 4  # Depends on data
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")