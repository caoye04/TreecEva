import math

# Simulated sensor array data with noise and calibration factors
def fetch_sensor_data():
    raw_values = [127, 255, 64, 192, 32, 180, 95]
    calibration_map = {0: 1.02, 1: 0.98, 2: 1.05, 3: 0.99, 4: 1.01, 5: 0.97, 6: 1.03}
    calibrated = [raw_values[i] * calibration_map[i] for i in range(len(raw_values))]
    return calibrated

# Noise injection function (distractor - not actually used in final computation)
def inject_noise(data, level=0.05):
    import random
    random.seed(42)
    return [x + random.uniform(-level * x, level * x) for x in data]

# Legacy filtering (dead code path - never called)
def apply_lowpass_filter(data, cutoff=100):
    filtered = [x for x in data if x > cutoff]
    return sorted(filtered, reverse=True)

# Core processing pipeline
def preprocess_readings(sensor_data):
    # Normalize to percentage scale
    normalized = [x / 255.0 for x in sensor_data]
    
    # Apply non-linear response curve (real transformation)
    curved = [math.pow(x, 1.25) if x > 0.5 else math.pow(x, 0.75) for x in normalized]
    
    # Convert to decibel-like scale (only some values are transformed)
    db_scale = []
    for val in curved:
        if val > 0.7:
            db_scale.append(20 * math.log10(val))
        elif val < 0.3:
            db_scale.append(-10 * abs(val))
        else:
            db_scale.append(val * 10)
    
    # Irrelevant aggregation metrics (distractors)
    avg_db = sum(db_scale) / len(db_scale)
    peak = max(db_scale)
    variance_proxy = sum((x - avg_db) ** 2 for x in db_scale) / len(db_scale)
    
    # Final processed structure (only base list matters)
    result_bundle = {
        'readings': db_scale,
        'metrics': {
            'average': avg_db,
            'peak': peak,
            'variance': variance_proxy,
            'count': len(db_scale)
        },
        'timestamp': '2023-11-05T14:32:10Z',
        'version': '2.1.0'
    }
    
    return result_bundle

# Diagnostic engine with conditional logic and bit flags
def analyze_readings(bundle, threshold):
    readings = bundle['readings']
    metrics = bundle['metrics']
    
    # Flag system using bitwise operations (red herring - only one flag is meaningful)
    FLAG_CRITICAL = 1 << 0
    FLAG_STABLE = 1 << 1
    FLAG_FLUCTUATING = 1 << 2
    FLAG_SATURATED = 1 << 3
    FLAG_CALIBRATING = 1 << 4
    
    status_flags = 0
    critical_count = 0
    stable_count = 0
    
    # Primary analysis loop
    for val in readings:
        if val > threshold:
            critical_count += 1
            status_flags |= FLAG_CRITICAL
        elif val < -5:
            status_flags |= FLAG_SATURATED
        elif -2 <= val <= 2:
            stable_count += 1
    
    # Secondary correlation check (never activates due to data constraints)
    if metrics['variance'] > 5 and metrics['peak'] > 5:
        status_flags |= FLAG_FLUCTUATING
    
    # Stability assessment (distractor computation)
    stability_ratio = stable_count / len(readings) if readings else 0
    if stability_ratio > 0.6:
        status_flags |= FLAG_STABLE
    
    # Decoy state machine (unused)
    states = ['INIT', 'WARMUP', 'ACTIVE', 'COOLDOWN']
    current_state = states[2]
    if critical_count > 2:
        next_state = states[0]
    else:
        next_state = states[-1]
    
    # Real decision logic (obscured by context)
    base_score = 0
    for val in readings:
        if val > threshold:
            base_score += int(abs(val) * 1.5)
        elif val < -threshold:
            base_score -= int(abs(val))

    # Final diagnostic calculation (this is the answer)
    adjustment_factor = 0.87
    if status_flags & FLAG_CRITICAL:
        adjustment_factor *= 1.2
    
    final_diagnostic = int(base_score * adjustment_factor) + 33
    
    # Unused string manipulation block (distractor)
    log_entry = f"DIAG|{current_state}|FLAGS={bin(status_flags)}|SCORE={base_score}"
    tokens = log_entry.split('|')
    reversed_parts = [part[::-1] for part in tokens if 'FLAG' not in part]
    joined_log = '-'.join(reversed_parts)
    masked_log = joined_log.replace('DIAG', '****')
    
    # Another irrelevant set operation
    unique_chars = set(masked_log)
    char_sum = sum([ord(c) % 10 for c in unique_chars if c.isalnum()])
    
    return final_diagnostic

# Misleading initialization sequence
system_status = {
    'initialized': True,
    'sensors': 7,
    'mode': 'diagnostic',
    'debug_override': False
}

temp_buffer = [0] * 8
for i in range(len(temp_buffer)):
    temp_buffer[i] = (i * 17 + 13) % 255

# Actual execution chain
if __name__ == '__main__':
    raw_data = fetch_sensor_data()
    processed_data = preprocess_readings(raw_data)
    threshold = 1.8
    final_diagnostic = analyze_readings(processed_readings(raw_data), threshold)
    print(f"Result: {final_diagnostic}")