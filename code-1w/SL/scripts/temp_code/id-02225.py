import math

# Simulated sensor array diagnostics with interference logic
def collect_readings(samples):
    raw_data = []
    noise_floor = 0.003
    calibration_offset = 0.012
    
    for s in samples:
        if s % 3 == 0:
            raw_data.append(math.sin(s * 0.1) + calibration_offset)
        elif s % 5 == 0:
            raw_data.append(math.cos(s * 0.05) - noise_floor)
        else:
            raw_data.append(0.0)
    
    # Irrelevant transformation (dead path)
    processed = [x * 1.05 for x in raw_data if x > 0.01]
    return raw_data

# Distraction function: looks important but unused in critical path
def compute_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 1000) & 0xFF
    return checksum

# Core entropy calculation with red herring variables
def generate_entropy_vector(values):
    entropy = []
    temp_accum = 0.0
    baseline = 0.02
    scaling_factor = 2.5  # Unused in final logic
    
    for v in values:
        if abs(v) > baseline:
            contribution = -v * math.log(abs(v))
            entropy.append(round(contribution, 6))
        else:
            entropy.append(0.0)
    
    # Decoy smoothing operation (never used)
    smoothed = []
    window_size = 3
    for i in range(len(entropy) - window_size + 1):
        smoothed.append(sum(entropy[i:i+window_size]) / window_size)
    
    return entropy

# Set-based filtering with meaningful and irrelevant operations
def filter_anomalies(entropy_vals):
    high_alert = set()
    medium_flags = set()
    ignored_indices = set()  # Distractor
    
    for idx, val in enumerate(entropy_vals):
        if val > 0.4:
            high_alert.add(idx)
        elif val > 0.2:
            medium_flags.add(idx)
        else:
            ignored_indices.add(idx)
    
    # Complex set logic with red herring intersection
    candidate_pool = high_alert.union(medium_flags)
    decoy_mask = {i for i in range(0, len(entropy_vals), 7)}  # Every 7th index
    true_alerts = candidate_pool - decoy_mask  # Real use of set operation
    
    # Dummy aggregation (misleading intermediate)
    stats_snapshot = {
        'count': len(candidate_pool),
        'decoy_count': len(decoy_mask),
        'ignored': len(ignored_indices)
    }
    
    return list(true_alerts)

# Primary analysis with multiple distractions
def analyze_pattern(sequence, thresholds):
    accumulated_score = 0
    penalty_factor = 0.0
    debug_trace = []
    
    # Simulated threshold logic with confusing control flow
    for i, val in enumerate(sequence):
        meets = False
        if i in thresholds:
            if val > 0.35:
                meets = True
        else:
            if val > 0.45:  # Stricter condition
                meets = True
        
        # Dead branch due to logic design
        if i % 10 == 0 and val < 0.1:
            penalty_factor += 0.05  # Never reached in practice
        
        if meets:
            accumulated_score += int(val * 100)
        
        # Red herring dictionary update
        debug_trace.append({
            'index': i,
            'value': val,
            'meets': meets,
            'score_contribution': int(val * 100) if meets else 0
        })
    
    # Final adjustment using set-derived size (key dependency)
    adjustment = len(thresholds) * 2
    result = accumulated_score - adjustment
    
    return result

# --- MAIN EXECUTION WITH DISTRACTORS ---
if __name__ == "__main__":
    # Input data generation (appears random but deterministic)
    sample_range = list(range(1, 51))
    
    # Step 1: Collect raw sensor readings
    sensor_output = collect_readings(sample_range)
    
    # Step 2: Compute entropy features
    entropy_sequence = generate_entropy_vector(sensor_output)
    
    # Step 3: Identify anomaly locations using set logic
    detected_outliers = filter_anomalies(entropy_sequence)
    
    # RED HERRING: Checksum computation on raw data (unused)
    _ = compute_checksum(sensor_output)
    
    # Prepare threshold set based on filtered results
    threshold_set = set(detected_outliers)
    
    # Introduce misleading alternate threshold (never used)
    fallback_threshold = {i for i, v in enumerate(entropy_sequence) if v > 0.25}
    backup_mode = False  # Dead flag
    
    # CRITICAL STATEMENT
    final_diagnostic = analyze_pattern(entropy_sequence, threshold_set)
    
    # Output target result
    print(f"Result: {final_diagnostic}")