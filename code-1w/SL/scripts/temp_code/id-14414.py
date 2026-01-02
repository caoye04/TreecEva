import math

# Simulated sensor data from wind turbine array
turbine_ids = [f'TURB-{i}' for i in range(1, 6)]
raw_readings = [
    [3.2, 4.1, 3.9, 4.0, 4.2],
    [5.5, 5.7, 0.0, 5.6, 5.8],
    [2.1, 2.3, 2.0, 2.2, 2.1],
    [7.0, 7.1, 7.0, 0.0, 7.2],
    [1.8, 1.9, 1.7, 1.8, 1.9]
]

# Irrelevant auxiliary mapping (distractor)
status_labels = {0: 'OFF', 1: 'STANDBY', 2: 'ACTIVE', 3: 'ERROR'}

# Fault masking thresholds per turbine (used in logic)
threshold_map = {
    'TURB-1': 3.5,
    'TURB-2': 5.0,
    'TURB-3': 2.2,
    'TURB-4': 6.8,
    'TURB-5': 1.6
}

# Historical baseline (red herring - not used)
historical_averages = {
    'TURB-1': 3.88,
    'TURB-2': 5.65,
    'TURB-3': 2.14,
    'TURB-4': 7.06,
    'TURB-5': 1.82
}

# Data cleaning function with decoy logic
def sanitize_readings(readings_list):
    cleaned = []
    for seq in readings_list:
        valid = [x for x in seq if x > 0]  # Remove zero placeholders
        avg = sum(valid) / len(valid)
        # Distractor: normalize to fake baseline
        normalized = [x - 0.1 for x in valid]  # Irrelevant adjustment
        cleaned.append(normalized)
    return cleaned

# Misleading transformation (never called)
def legacy_recalibrate(data):
    return [[round(x * 0.98, 2) for x in row] for row in data]

# Core diagnostic engine
def analyze_turbine_health(sensor_data, thresholds):
    results = {}
    
    # Apply sanitize (actual usage)
    processed_data = sanitize_readings(sensor_data)
    
    # Use enumerate and zip together (required idiom)
    for idx, (turbine, readings) in enumerate(zip(turbine_ids, processed_data)):
        key = f'TURB-{idx + 1}'
        threshold = thresholds[key]
        
        # Compute rolling deviation
        deviations = [abs(r - threshold) for r in readings]
        max_dev = max(deviations)
        
        # Bit manipulation as part of health scoring (complexity)
        base_score = int(100 - (max_dev * 10))
        masked_score = base_score & 0b111111  # Cap at 63
        
        # Conditional override based on pattern detection
        if any(dev > 1.5 for dev in deviations[:3]):
            adjusted_score = masked_score ^ 15  # XOR obfuscation
        else:
            adjusted_score = masked_score | 4  # Ensure minimum
        
        # Store result
        results[key] = adjusted_score
    
    return results

# Secondary aggregator with lambda (required feature)
def aggregate_metrics(turbine_data, threshold_map):
    health_scores = analyze_turbine_health(turbine_data, threshold_map)
    
    # Extract scores using lambda and enumerate
    score_list = list(map(lambda item: item[1], sorted(health_scores.items())))
    
    # Complex aggregation with distractors
    total_weight = 0.0
    weighted_sum = 0.0
    
    for i, score in enumerate(score_list):
        weight = 1.0 + (i * 0.1)  # Increasing weight by position
        total_weight += weight
        weighted_sum += score * weight
        
        # Dead code path (never executed due to logic)
        if score < 0:
            fallback_correction = math.log(abs(score))

    # Final computation
    final_mean = weighted_sum / total_weight
    
    # Additional transformation (irrelevant to result)
    ceiling_bump = math.ceil(final_mean * 0.01)
    
    # Key result variable
    final_diagnostic = int(round(final_mean + ceiling_bump))
    
    # Debug print (not affecting logic)
    debug_trace = [f'{k}:{v}' for k, v in sorted(health_scores.items())]
    
    return final_diagnostic

# Execution entry point
if __name__ == '__main__':
    # Spurious precomputation (distractor)
    temp_snapshot = [sum(row) for row in raw_readings]
    snapshot_avg = sum(temp_snapshot) / len(temp_snapshot)
    
    # Actual critical call
    final_diagnostic = aggregate_metrics(raw_readings, threshold_map)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")