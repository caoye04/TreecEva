import itertools

# Simulated sensor diagnostics system with red herrings and distractors
def analyze_component_health(status_log, baseline):
    cumulative_stress = 0
    transient_spikes = 0
    for entry in status_log:
        if entry > baseline * 1.3:
            transient_spikes += 1
        cumulative_stress += max(0, entry - baseline * 0.8)
    # Distractor: this function is never used
    return cumulative_stress if transient_spikes < 5 else -1

# Misleading auxiliary function that appears relevant
def compute_anomaly_score(data_stream):
    score = 0
    for i, val in enumerate(data_stream):
        if i % 3 == 0 and val > 75:
            score += 2
        elif val < 20:
            score -= 1
    return score * 1.5  # Dead end

# Core processing function with embedded logic chain
def process_readings(readings, limits):
    # Step 1: Filter valid sensors (only those with 'active' flag)
    active_sensors = {k: v for k, v in readings.items() if v['status'] == 'active'}
    
    # Step 2: Extract raw values and initialize tracking variables
    sensor_values = [v['reading'] for v in active_sensors.values()]
    adjustment_factor = 0.9
    normalized_total = 0
    peak_count = 0
    
    # Step 3: Apply dynamic normalization based on limit thresholds
    for val in sensor_values:
        if val > limits['upper'] * 0.75:
            peak_count += 1
        normalized_val = val * adjustment_factor
        if normalized_val < limits['lower']:
            normalized_val = limits['lower']
        normalized_total += normalized_val
    
    # Step 4: Use itertools to generate sliding window pairs (distractor usage)
    pairs = list(itertools.pairwise(sensor_values))
    fluctuation_count = sum(1 for a, b in pairs if abs(a - b) > 20)
    
    # Step 5: Conditional suppression based on peak-to-fluctuation ratio
    if peak_count > 0 and fluctuation_count / peak_count > 2:
        normalized_total *= 0.85
    
    # Step 6: Introduce fake correction term (irrelevant unless debug mode)
    debug_correction = 0
    debug_mode = False
    if debug_mode:  # This will never execute
        debug_correction = len(pairs) - fluctuation_count
    
    # Step 7: Aggregate secondary metric from metadata (decoy calculation)
    metadata_sum = 0
    for sensor in active_sensors.values():
        if 'calibration' in sensor:
            metadata_sum += sensor['calibration']  # Always zero in input data
    
    # Step 8: Final diagnostic computed purely from normalized_total and peak_count
    final_diagnostic = int(normalized_total - (peak_count * 12))
    
    # Irrelevant late-stage reassignment (does not affect outcome)
    temp_result = metadata_sum + debug_correction
    temp_result = temp_result * 0 if temp_result > 100 else temp_result
    
    return final_diagnostic

# Simulated input data with mixed relevance
sensor_data = {
    'sensor_a': {'reading': 85, 'status': 'active', 'calibration': 0},
    'sensor_b': {'reading': 92, 'status': 'active', 'calibration': 0},
    'sensor_c': {'reading': 45, 'status': 'inactive', 'calibration': 0},  # filtered out
    'sensor_d': {'reading': 78, 'status': 'active', 'calibration': 0},
    'sensor_e': {'reading': 103, 'status': 'active', 'calibration': 0},
    'sensor_f': {'reading': 67, 'status': 'active', 'calibration': 0}
}

thresholds = {
    'upper': 100,
    'lower': 50
}

# Execution point of interest
final_diagnostic = process_readings(sensor_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")