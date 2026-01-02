def analyze_signal(values):
    filtered = [v for v in values if v > 0]
    magnitude = sum(abs(x) for x in filtered)
    peak = max(filtered) if filtered else 0
    noise_floor = len([x for x in values if x < -10])
    return magnitude, peak, noise_floor


def compute_checksum(data):
    checksum = 0
    for i, d in enumerate(data):
        checksum ^= (d + i) % 256
    return checksum


def extract_features(signal, config):
    raw_energy = sum(s**2 for s in signal)
    norm_factor = max(signal) if signal else 1
    normalized = [s / norm_factor for s in signal]
    energy_ratio = raw_energy / (sum(s**2 for s in normalized) + 1e-8)
    
    # Distractor: irrelevant feature extraction
    temporal_jitter = sum(abs(normalized[i] - normalized[i+1]) for i in range(len(normalized)-1))
    spectral_spread = len([x for x in normalized if x > 0.5])
    
    return {
        'energy': raw_energy,
        'ratio': energy_ratio,
        'jitter': temporal_jitter,
        'spread': spectral_spread,
        'norm': norm_factor
    }


def evaluate_performance(metrics, threshold):
    score = 0
    
    # Relevant logic chain
    if metrics['energy'] > threshold:
        score += 15
    if metrics['ratio'] > 1.0:
        score += 10
    if metrics['norm'] == 0:
        score -= 5
    
    # Red herring: unused conditional with complex expression
    anomaly_flag = (metrics['jitter'] > 2.0) and (metrics.get('spread', 0) < 3)
    if anomaly_flag and False:  # Dead code path
        score *= 0.5
    
    # Another distractor computation
    temp_adjustment = (metrics['jitter'] * metrics['spread']) % 7
    score += temp_adjustment  # Actually used but misleadingly small impact
    
    return int(score)

# Main execution
if __name__ == "__main__":
    # Simulated input data
    sensor_readings = [-5, 0, 12, -15, 23, 8, 0, 19, -2]
    config_settings = {"gain": 1.5, "filter_on": True}
    
    # Irrelevant preprocessing
    processed, _, _ = analyze_signal(sensor_readings)
    base_threshold = 100
    
    # Key feature extraction (relevant)
    feature_set = extract_features(sensor_readings, config_settings)
    
    # Secondary distractor: checksum of indices (unused)
    index_stream = list(range(len(sensor_readings)))
    validation_key = compute_checksum(index_stream)
    
    # State tracking with tuple unpacking (partially relevant)
    energy_level = feature_set['energy']
    ratio_metric = feature_set['ratio']
    norm_peak = feature_set['norm']
    extra_diagnostic = (validation_key, processed, anomaly_flag := False)
    
    # Conditional expression with distractors
    fallback_mode = True if validation_key > 1000 else False
    dynamic_boost = 5 if fallback_mode and energy_level > 200 else 0
    
    # Update feature set with a red-herring field
    feature_set['boost'] = dynamic_boost
    feature_set['mode'] = 'normal'
    
    # --- KEY STATEMENT ---
    final_score = evaluate_performance(feature_set, base_threshold)
    
    # Output result
    print(f"Result: {final_score}")