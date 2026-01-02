import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    # Real data sources
    primary_readings = [23.4, 25.1, 22.8, 24.6, 26.3]
    secondary_readings = [24.0, 23.9, 25.2, 24.1, 25.8]
    
    # Irrelevant calibration artifacts (distractors)
    calib_phase_a = [0.1, -0.2, 0.3, -0.1, 0.0]
    calib_phase_b = [0.05, -0.15, 0.25, -0.05, 0.1]
    dummy_checksums = [sum(primary_readings[:i]) for i in range(3)]  # Unused
    
    return primary_readings, secondary_readings

# Signal processing pipeline
def filter_noise(raw_seq, strength=0.85):
    filtered = []
    for i in range(len(raw_seq)):
        if i == 0:
            filtered.append(raw_seq[i])
        else:
            adjusted = filtered[i-1] * strength + raw_seq[i] * (1 - strength)
            filtered.append(adjusted)
    
    # Dead code path - never executed due to loop structure (red herring)
    if len(filtered) > 100:
        backup = [x * 0.9 for x in filtered]
        return backup
    
    return filtered

# Advanced feature extraction
def extract_features(signal_stream):
    # Compute multiple statistical features (some irrelevant)
    mean_val = sum(signal_stream) / len(signal_stream)
    variance = sum((x - mean_val) ** 2 for x in signal_stream) / len(signal_stream)
    peak_to_peak = max(signal_stream) - min(signal_stream)
    rms = math.sqrt(sum(x**2 for x in signal_stream) / len(signal_stream))
    
    # Distractor computations with no downstream use
    spectral_estimate = sum(math.sin(x * 0.1) for x in signal_stream[:3])
    entropy_approx = -sum((x / rms) * math.log(abs(x / rms) + 1e-8) for x in signal_stream[:4])
    
    # Only these two are actually used later
    return {'avg': mean_val, 'variability': variance, 'peak_deviation': peak_to_peak}

# Data fusion logic
def fuse_streams(primary, secondary):
    # Weighted fusion with decay factor
    alpha = 0.7
    fused = [alpha * p + (1 - alpha) * s for p, s in zip(primary, secondary)]
    
    # Extra transformation chain (partially irrelevant)
    smoothed_fusion = filter_noise(fused, 0.75)
    enhanced_metrics = extract_features(smoothed_fusion)
    
    # Decoy structure creation
    audit_trail = {"version": "2.1", "fused_count": len(fused), "processed": True}
    audit_trail["checksum"] = sum(fused[i] * (i+1) for i in range(len(fused)))  # Unused
    
    return enhanced_metrics

# Diagnostic analysis engine
def analyze_readings(metrics_bundle):
    baseline_threshold = 24.0
    variability_cap = 2.0
    
    current_avg = metrics_bundle['avg']
    current_var = metrics_bundle['variability']
    
    # Complex conditional evaluation with red herrings
    risk_score = 0.0
    if current_avg > baseline_threshold:
        risk_score += 15
        if current_var > variability_cap:
            risk_score += 25
    elif current_avg < baseline_threshold - 1.5:
        risk_score += 10
        # Nested distraction: unused compensation logic
        adjustment_log = []
        for i in range(3):
            adjustment_log.append(math.exp(-i) * risk_score)
    
    # Secondary criteria with misleading intermediate calculation
    deviation_penalty = 0
    if 'peak_deviation' in metrics_bundle:
        temp_dev = metrics_bundle['peak_deviation']
        # Complex but ultimately unused formula
        theoretical_limit = (temp_dev ** 2) / (current_var + 1e-6)
        compliance_ratio = baseline_threshold / (current_avg + 1e-6)
        
        # Only this line matters
        deviation_penalty = 20 if temp_dev > 3.0 else 0
    
    # Final diagnostic computation (only risk_score and deviation_penalty used)
    final_value = int(risk_score + deviation_penalty)
    
    # Multiple decoy variables and transformations
    normalized_score = final_value / 60.0
    confidence_interval = (normalized_score * 0.8, normalized_score * 1.2)
    anomaly_pattern = [math.cos(math.pi * normalized_score / 2)]
    
    return final_value

# Legacy compatibility wrapper (never called)
def legacy_analysis(data):
    transform_fn = lambda x: x * 1.05
    return [transform_fn(x) for x in data]

# Main execution flow
primary_sensors, secondary_sensors = collect_sensor_data()

# Process primary channel
clean_primary = filter_noise(primary_sensors)
features_primary = extract_features(clean_primary)

# Process secondary channel (partial - distractor)
clean_secondary = filter_noise(secondary_sensors)
feature_snapshot = extract_features(clean_secondary[:4])  # Incomplete usage

# Critical fusion step
processed_data = fuse_streams(primary_sensors, secondary_sensors)

# Final diagnostic assessment
final_diagnostic = analyze_readings(processed_data)

# Output target result
print(f"Result: {final_diagnostic}")