def analyze_signal_quality(raw_readings):
    # Preprocess signal: remove noise using slicing and smoothing
    filtered = [x for x in raw_readings if 10 < x < 90]
    smoothed = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    
    # Misleading computation: power analysis (not actually used)
    total_power = sum(x**2 for x in raw_readings)
    avg_power = total_power / len(raw_readings) if raw_readings else 0
    power_peaks = [x for x in raw_readings if x > avg_power * 1.5]  # Distractor

    # Signal quality metric based on variance
    mean_val = sum(smoothed) / len(smoothed) if smoothed else 0
    variance = sum((x - mean_val)**2 for x in smoothed) / len(smoothed) if smoothed else 0
    quality_score = 100 - variance  # Higher is better

    return max(0, min(100, quality_score))  # Clamp to 0-100


def detect_anomalies(signal_data, sensitivity=0.85):
    anomalies = []
    for i in range(1, len(signal_data)):
        change = abs(signal_data[i] - signal_data[i-1])
        if change > 40:  # Large jump indicates anomaly
            anomalies.append((i, change))
    # Apply sensitivity filter (some dead logic for confusion)
    if sensitivity < 0.5:
        anomalies = [a for a in anomalies if a[1] > 50]  # Never reached
    return len(anomalies)

def compute_checksum(data_str):
    # Simple XOR checksum over string character codes
    checksum = 0
    for char in data_str:
        checksum ^= ord(char) & 0xFF
    return checksum % 100

def process_diagnostics(signal_sequence, thresholds):
    # Step 1: Assess base signal quality
    base_quality = analyze_signal_quality(signal_sequence)
    
    # Step 2: Detect temporal anomalies
    spike_count = detect_anomalies(signal_sequence)
    
    # Step 3: Generate metadata tag (distractor)
    timestamp_tag = "SIG_" + "_".join(str(len(signal_sequence))[::-1])
    tag_value = compute_checksum(timestamp_tag)  # Computed but not critical
    
    # Step 4: Apply threshold filtering using slicing
    active_segments = signal_sequence[::2]  # Every other reading
    high_freq_events = [x for x in active_segments if x > thresholds['critical']]
    
    # Step 5: Bitwise state tracking (modular arithmetic + bitwise)
    state_flag = 0
    if len(high_freq_events) > thresholds['grace']:
        state_flag |= 1
    if spike_count >= 3:
        state_flag |= 2
    if base_quality < 60:
        state_flag |= 4
    
    # Step 6: Aggregate weighted impact
    weighted_impact = base_quality * 0.6 \
                     - len(high_freq_events) * 2.5 \
                     - spike_count * 3.1
    
    # Step 7: Final diagnostic score with adjustment based on state
    final_score = int(weighted_impact)
    adjustment = -5 if state_flag & 4 else 0  # Only degraded quality penalizes
    final_diagnostic = final_score + adjustment
    
    # Irrelevant aggregation (dead-end)
    summary_report = {
        'readings': len(signal_sequence),
        'spikes': spike_count,
        'quality': base_quality,
        'checksum': tag_value,
        'state': bin(state_flag)
    }
    
    return final_diagnostic

# Input data
signal_input = [85, 12, 77, 45, 91, 63, 28, 74, 15, 88, 52, 18, 94, 67, 23]
thresholds_config = {
    'critical': 80,
    'grace': 2
}

# Execution point of interest
final_diagnostic = process_diagnostics(signal_input, thresholds_config)
print(f"Result: {final_diagnostic}")