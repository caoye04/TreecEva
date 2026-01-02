import math

# Simulated sensor fusion system for environmental anomaly detection
def collect_sensor_readings():
    raw_signals = [i * 1.5 + 2.1 for i in range(15)]
    filtered = [x for x in raw_signals if x > 5.0]
    baseline = sum(filtered) / len(filtered)
    
    # Irrelevant auxiliary computation (red herring)
    temp_offset = 0
    for i in range(5):
        temp_offset += (i ** 2) % 7
    scaling_factor = math.sin(math.pi / 6)  # Always 0.5
    
    adjusted = [round((x - baseline) * scaling_factor, 3) for x in filtered]
    return adjusted

# Legacy function - unused but looks relevant (dead code path)
def legacy_calibrate(data):
    correction_map = {i: val * 0.95 for i, val in enumerate(data)}
    return [correction_map[i] for i in range(len(data))]

# Auxiliary transformation with partial usage
def extract_features(signal):
    magnitude = sum(abs(x) for x in signal)
    peaks = [x for x in signal if x > 1.0]
    avg_peak = magnitude / len(peaks) if peaks else 0.0
    
    # Distractor: complex but unused stats
    squared_energy = sum(x**2 for x in signal)
    entropy_approx = -sum((x/magnitude)*math.log(abs(x)/magnitude+1e-9) for x in signal) if magnitude > 0 else 0
    
    # Only this is actually used later
    return {'mag': magnitude, 'peak_count': len(peaks), 'avg_peak': avg_peak}

# Core analysis with set operations and conditional logic
def evaluate_stability(features, config):
    critical_threshold = config.get('threshold', 12.0)
    volatility_set = set()
    
    if features['mag'] > critical_threshold:
        volatility_set.add('HIGH_MAGNITUDE')
    if features['avg_peak'] > 2.5:
        volatility_set.add('ELEVATED_PEAKS')
    if features['peak_count'] < 3:
        volatility_set.add('SPARSE_ACTIVITY')
    
    # Extra irrelevant set operations (distractors)
    known_patterns = {'HIGH_MAGNITUDE', 'ELEVATED_PEAKS', 'NORMAL_DECAY', 'LOW_NOISE'}
    rare_events = {'SPARSE_ACTIVITY', 'ASYMMETRIC_SPIKE'}
    common_intersection = known_patterns & volatility_set
    
    # Only cardinality matters in final logic
    return len(volatility_set) >= 2 and 'SPARSE_ACTIVITY' not in volatility_set

# Main pattern analyzer combining multiple concepts
def analyze_pattern(dataset, limits):
    results = []
    history_log = []  # Unused logging structure (distractor)
    
    for idx, segment in enumerate(dataset):
        # Simulate time-series segmentation
        window = segment[:len(segment)//2 + 1]
        
        # Real feature extraction
        feat = extract_features(window)
        
        # Fake transformation chain (misleading intermediate)
        transformed = []
        for val in window:
            transformed.append(math.cos(val) * math.exp(-abs(val)/10))
        smoothed = [t * 0.8 + 0.2 for t in transformed]
        
        # Actual decision logic
        config = {'threshold': limits[idx % len(limits)]}
        stable = evaluate_stability(feat, config)
        
        # Conditional accumulation
        if stable and feat['mag'] > 0:
            results.append(feat['mag'] * 0.75)
        else:
            results.append(-feat['peak_count'] * 1.5)
        
        # Dead branch with complex but unused logic
        if idx > 100:  # Never executed
            backup = [x for x in results if x > 0]
            if len(backup) > 2:
                results[-1] = sum(backup) / len(backup)

    # Final aggregation with distractor sets
    valid_results = {round(r, 2) for r in results if r > 0}
    negative_set = {r for r in results if r <= 0}
    overlap_check = valid_results & negative_set  # Always empty
    
    # Key computation: harmonic mean of positive branches
    if valid_results:
        inv_sum = sum(1/r for r in valid_results)
        harmonic_proxy = len(valid_results) / inv_sum
    else:
        harmonic_proxy = 0.0
    
    # Secondary influence: count of negative outcomes
    penalty_factor = len(negative_set) * 0.62
    
    # Final deterministic result
    final_diagnostic = int(harmonic_proxy - penalty_factor + 3)
    
    # Redundant print for confusion
    print(f"Diagnostics complete: {final_diagnostic} components flagged")
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    # Generate multi-segment data
    base_data = collect_sensor_readings()
    collected_data = [
        base_data[0:8],
        base_data[3:10],
        base_data[5:12],
        base_data[6:11],
        base_data[2:9]
    ]
    
    # Threshold configuration (used in modular indexing)
    thresholds = [10.5, 14.2, 9.8, 16.1]
    
    # Unused statistical summary (distractor)
    all_values = [val for segment in collected_data for val in segment]
    mean_all = sum(all_values) / len(all_values)
    std_dev = (sum((x - mean_all)**2 for x in all_values) / len(all_values)) ** 0.5
    outlier_boundary = mean_all + 2 * std_dev
    
    # Critical execution point
    final_diagnostic = analyze_pattern(collected_data, thresholds)
    
    # Required output format
    print("Result: " + str(final_diagnostic))