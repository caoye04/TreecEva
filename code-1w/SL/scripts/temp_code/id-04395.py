from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic evaluation
def preprocess_sensor_readings(raw_batches):
    aggregated = []
    for batch in raw_batches:
        filtered = [x for x in batch if 10 <= x <= 100]
        if len(filtered) > 3:
            smoothed = sum(filtered) / len(filtered)
            aggregated.append(round(smoothed, 2))
    return aggregated

def generate_frequency_profile(data_stream):
    profile = defaultdict(int)
    for val in data_stream:
        bin_key = int(val // 10)
        profile[bin_key] += 1
    return profile

def evaluate_stability_metrics(stream):
    if not stream:
        return 0.0
    mean_val = sum(stream) / len(stream)
    variance = sum((x - mean_val) ** 2 for x in stream) / len(stream)
    return round(variance, 3)

def compute_spectral_entropy(freq_dist):
    total = sum(freq_dist.values())
    if total == 0:
        return 0.0
    probabilities = [count / total for count in freq_dist.values()]
    entropy = -sum(p * __import__('math').log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def derive_calibration_sequence(base_values):
    # Irrelevant calibration routine (dead path)
    calib_seq = []
    for v in base_values:
        temp = v
        for _ in range(3):
            temp = (temp * 7 + 13) % 101
        calib_seq.append(temp)
    return calib_seq  # Never used

def assess_anomaly_score(metrics, weights):
    # Distractor function: looks important but unused
    score = 0.0
    for i, m in enumerate(metrics):
        weight = weights.get(f'w{i}', 1.0)
        score += m * weight
    return round(score, 3)

def analyze_signal(processed_data, threshold_map):
    if not processed_data:
        return -1
    
    # Real computation begins
    avg_signal = sum(processed_data) / len(processed_data)
    freq_profile = generate_frequency_profile(processed_data)
    stability = evaluate_stability_metrics(processed_data)
    entropy = compute_spectral_entropy(freq_profile)
    
    # Key logic branch
    critical_band_count = sum(1 for k, v in freq_profile.items() if k in [5, 6, 7] and v >= threshold_map['band_count'])
    
    # Multiple nested conditions with red herrings
    baseline_ref = threshold_map['reference_level']
    adjustment_factor = 1.0
    if avg_signal > baseline_ref:
        if stability < threshold_map['stability_cap']:
            if entropy > threshold_map['entropy_min']:
                adjustment_factor = 1.25
                # Dead code ahead (misleading intermediate)
                temp_debug = [x * adjustment_factor for x in processed_data[:2]]
                temp_debug = [round(x, 2) for x in temp_debug]  # Unused
    else:
        adjustment_factor = 0.85
    
    # Core calculation
    raw_diagnostic = avg_signal * adjustment_factor
    
    # Additional filtering based on band activity
    if critical_band_count >= 2:
        raw_diagnostic *= 1.15
    elif critical_band_count == 1:
        raw_diagnostic *= 1.05
    else:
        raw_diagnostic *= 0.95
    
    # Final clamping
    min_limit, max_limit = threshold_map['output_range']
    final_value = max(min_limit, min(raw_diagnostic, max_limit))
    
    # Red herring: complex but unused transformation
    decoy_transform = [(x ** 0.5) * final_value for x in freq_profile.values() if x > 2]
    decoy_stats = {
        'count': len(decoy_transform),
        'peak': max(decoy_transform) if decoy_transform else 0,
        'avg': sum(decoy_transform)/len(decoy_transform) if decoy_transform else 0
    }
    
    return int(round(final_value))

# Main execution
if __name__ == '__main__':
    # Simulated input data
    raw_sensor_batches = [
        [12, 15, 23, 45, 55, 67, 88, 92],
        [11, 22, 33, 44, 55, 66],
        [19, 29, 39, 49, 59, 69, 79, 89, 99],
        [14, 28, 42, 56, 70, 84],
        [21, 31, 41, 51, 61, 71, 81, 91]
    ]

    # Irrelevant preprocessing (distractor)
    flat_data = [item for sublist in raw_sensor_batches for item in sublist]
    outlier_flags = [1 if x < 15 or x > 95 else 0 for x in flat_data]
    spike_count = sum(outlier_flags)

    # Actual relevant processing starts here
    processed_data = preprocess_sensor_readings(raw_sensor_batches)

    # Threshold configuration (only some fields are used)
    threshold_map = {
        'reference_level': 45.0,
        'stability_cap': 200.0,
        'entropy_min': 1.8,
        'band_count': 2,
        'output_range': (30, 95),
        'fallback_mode': False,
        'legacy_offset': 3.14
    }

    # Unused diagnostic paths (misleading)
    stability_metric = evaluate_stability_metrics(processed_data)
    freq_diag = generate_frequency_profile(processed_data)
    entropy_measure = compute_spectral_entropy(freq_diag)
    
    # Dead function call with no impact
    _ = derive_calibration_sequence(processed_data)
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")