from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
data = {
    'sensor_a': [12, 15, 14, 13, 16, 18, 17, None, 15],
    'sensor_b': [20, None, 22, 21, 19, 23, 24, 22, 20],
    'sensor_c': [8, 9, None, 7, 10, 11, 9, 8, 12],
    'sensor_d': [30, 33, 31, 35, None, 32, 34, 33, 30]
}

# Weight configuration for different processing modes
weights = {
    'mode_x': {'a': 0.1, 'b': 0.4, 'c': 0.2, 'd': 0.3},
    'mode_y': {'a': 0.2, 'b': 0.3, 'c': 0.3, 'd': 0.2},
    'mode_z': {'a': 0.4, 'b': 0.1, 'c': 0.1, 'd': 0.4}
}

# Irrelevant calibration constants (distractors)
CALIBRATION_OFFSET_A = 0.05
CALIBRATION_OFFSET_B = -0.03
REFERENCE_VOLTAGE = 5.0
MAX_BUFFER_SIZE = 1024
TEMPORAL_DAMPING_FACTOR = 0.85

# Fake checksum validation (dead logic path)
def validate_checksum(records):
    total = sum(sum(filter(None, v)) for v in records.values())
    return total % 17 == 0

# Unused signal smoothing function (decoy)
def smooth_signal(signal, factor=0.7):
    smoothed = []
    for i, val in enumerate(signal):
        if i == 0:
            smoothed.append(val or 0)
        else:
            prev = smoothed[i-1]
            smoothed.append(factor * (val or 0) + (1-factor) * prev)
    return smoothed

# Misleading intermediate metric (not used in final calculation)
def compute_jitter_metric(values):
    diffs = [abs(a - b) for a, b in zip(values, values[1:]) if a and b]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0.0

# Auxiliary diagnostic reporting (irrelevant to main logic)
def generate_diagnostics(data):
    diagnostics = defaultdict(int)
    for k, v in data.items():
        diagnostics[f'{k}_count'] = len(v)
        diagnostics[f'{k}_missing'] = v.count(None)
        valid_vals = [x for x in v if x is not None]
        if valid_vals:
            diagnostics[f'{k}_range'] = max(valid_vals) - min(valid_vals)
    return dict(diagnostics)

# Core processing: clean and aggregate sensor data
def preprocess_sensor_data(raw_data):
    cleaned = {}
    stats = Counter()
    
    for sensor, readings in raw_data.items():
        # Remove None values and apply arbitrary offset (simulated correction)
        valid_readings = [r for r in readings if r is not None]
        
        if valid_readings:
            avg = sum(valid_readings) / len(valid_readings)
            # Apply fake temporal damping (unused in final path)
            damped_avg = avg * TEMPORAL_DAMPING_FACTOR
            # Use raw average only
            cleaned[sensor] = avg
            
            # Update statistics (some used, some not)
            stats[f'{sensor}_sum'] = sum(valid_readings)
            stats[f'{sensor}_max'] = max(valid_readings)
            stats[f'{sensor}_min'] = min(valid_readings)
        
    # Inject irrelevant aggregated metrics
    all_valid = [v for vals in raw_data.values() for v in vals if v is not None]
    stats['global_median_guess'] = sorted(all_valid)[len(all_valid)//2]
    stats['total_records'] = len(all_valid)
    
    return cleaned, stats

# Complex weight application with red herring modes
def apply_weighting(sensors, weight_config, mode='mode_x'):
    base_scores = {}
    
    # Compute raw weighted score per mode (only one will be used)
    for m, w in weight_config.items():
        score = 0.0
        score += w['a'] * sensors.get('sensor_a', 0)
        score += w['b'] * sensors.get('sensor_b', 0)
        score += w['c'] * sensors.get('sensor_c', 0)
        score += w['d'] * sensors.get('sensor_d', 0)
        base_scores[m] = score
    
    # Apply arbitrary nonlinear transformation (distraction)
    transformed = {k: math.log(v + 1) ** 1.5 for k, v in base_scores.items()}
    
    # Only 'mode_x' is actually used later
    return base_scores[mode], transformed

# Final scoring with hidden logic trap
def calculate_final_score(sensor_input, weighting_scheme):
    # Preprocess data
    processed_data, summary_stats = preprocess_sensor_data(sensor_input)
    
    # Generate useless diagnostics
    diag_report = generate_diagnostics(sensor_input)
    jitter_a = compute_jitter_metric([x for x in sensor_input['sensor_a'] if x])
    jitter_b = compute_jitter_metric([x for x in sensor_input['sensor_b'] if x])
    
    # Validate fake checksum (never checked)
    is_valid = validate_checksum(sensor_input)
    
    # Apply weights - critical line
    raw_score, alt_scores = apply_weighting(processed_data, weighting_scheme, mode='mode_x')
    
    # Secondary adjustment based on statistical dispersion (red herring)
    ranges = [summary_stats[f'{k}_max'] - summary_stats[f'{k}_min'] for k in ['sensor_a', 'sensor_b', 'sensor_c', 'sensor_d'] if f'{k}_max' in summary_stats]
    range_penalty = sum(r > 5 for r in ranges) * 1.5
    
    # Hidden condition: if global median > 15, add bonus (but it's 14)
    global_median = summary_stats['global_median_guess']
    bonus = 10 if global_median > 15 else 0
    
    # Final computation chain
    adjusted = raw_score - range_penalty
    amplified = adjusted * 1.2
    clamped = max(5, min(amplified, 100))  # Keep in bounds
    final_score = round(clamped + bonus)
    
    # Critical print statement
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
if __name__ == "__main__":
    final_score = calculate_final_score(data, weights)