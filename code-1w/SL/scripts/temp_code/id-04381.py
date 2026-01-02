def analyze_signal_strength(readings):
    filtered = [x for x in readings if x > 50]
    strength = sum(filtered) // len(filtered) if filtered else 0
    return strength


def detect_anomalies(data_stream):
    anomalies = set()
    for i, val in enumerate(data_stream):
        if val < 30 or val > 95:
            anomalies.add(i)
    return anomalies


def compute_entropy(values):
    # Irrelevant entropy calculation (not used in final result)
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def aggregate_performance(signals, threshold):
    # Main logic begins
    processed = []
    offset = 0
    for s in signals:
        shifted = s ^ 15  # Bitwise XOR manipulation
        if shifted >= threshold:
            processed.append(shifted)
        else:
            processed.append(s // 2)
    
    # Slicing to extract relevant segment
    segment = processed[2:8]
    
    # Dummy state tracking (some distraction)
    status_log = []
    cumulative = 0
    for idx, val in enumerate(segment):
        if val % 2 == 0:
            cumulative += val
            status_log.append(f"EVEN_{idx}")
        else:
            cumulative -= val
            status_log.append(f"ODD_{idx}")
    
    # Red herring: unused average
    mean_val = sum(segment) / len(segment) if segment else 0
    temp_result = mean_val * 1.5
    
    # Key transformation
    adjusted = cumulative * 2
    
    # Simulate system calibration offset
    calibration_factor = 7
    adjusted -= calibration_factor
    
    # Final score computation
    final_score = adjusted + len(status_log)
    
    # Dead code path (never executed but looks relevant)
    if False:
        backup = sum(processed[:5])
        final_score = max(final_score, backup)
    
    return final_score

# Main execution flow
raw_data = [68, 72, 45, 88, 22, 91, 54, 33, 77, 81]
baseline_threshold = 60

# Perform signal analysis (used)
monitored_signals = [analyze_signal_strength(raw_data)] * 10

# Detect anomalies (result not used, distractor)
detected_outliers = detect_anomalies(raw_data)

# Compute entropy (completely irrelevant, adds interference)
entropy_metric = compute_entropy(raw_data)

# Core computation
final_score = aggregate_performance(monitored_signals, baseline_threshold)

# Output result
print(f"Result: {final_score}")