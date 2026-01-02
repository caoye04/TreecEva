import itertools

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_readings():
    base_signal = [1.1, 2.3, -0.7, 4.5, -2.2, 3.8, 0.0, -1.9]
    noise_floor = [0.1 * i for i in range(8)]
    raw_data = [base_signal[i] + noise_floor[i] for i in range(8)]
    return raw_data

# Irrelevant auxiliary function - distractor
def calculate_efficiency_rating(data):
    total = sum(data)
    rating = total * 0.85 if total > 0 else total * 1.2
    adjustment = 0
    for x in data:
        if x > 2.0:
            adjustment += 0.3
    return rating + adjustment

# Signal transformation with embedded logic path
def apply_window_filter(signal):
    windowed = []
    for i in range(len(signal)):
        weight = 0.5 + 0.5 * (i % 3) / 2.0
        windowed.append(signal[i] * weight)
    return windowed

# Decoy function - never called but adds confusion
def generate_synthetic_echo(samples, intensity=1.0):
    echo = []
    for s in samples:
        if s > 1.0:
            echo.append(s * intensity * 0.7)
        elif s < -1.0:
            echo.append(s * intensity * 0.3)
        else:
            echo.append(0.0)
    return echo

# Core transformation with red herring operations
def transform_signal_sequence(raw_readings):
    shifted = [x + 1.0 for x in raw_readings]
    squared = [x ** 2 for x in shifted]
    normalized = [x / max(squared) * 10.0 for x in squared]
    
    # Dead code path - unreachable due to prior logic
    temp_debug = []
    if len(normalized) < 5:
        temp_debug = [y * 2 for y in normalized]
    else:
        pass  # Placeholder for removed feature
    
    # Actual relevant transformation
    filtered = list(itertools.accumulate(normalized, lambda a, b: a * 0.7 + b * 0.3))
    return filtered

# Threshold analysis with misleading intermediate variables
def evaluate_stability_index(processed):
    peak = max(processed)
    avg = sum(processed) / len(processed)
    variance_proxy = sum((x - avg) ** 2 for x in processed) / len(processed)
    fluctuation_score = 0
    for i in range(1, len(processed)):
        if abs(processed[i] - processed[i-1]) > 1.0:
            fluctuation_score += 1.5
    
    # This looks important but isn't used in final result
    stability_ratio = peak / (variance_proxy + 1e-5) if variance_proxy > 0 else 0
    
    # Relevant metric
    return fluctuation_score * 2

# Main diagnostic analyzer combining multiple concepts
def analyze_pattern(data, config_thresholds):
    threshold_primary = config_thresholds['primary']
    magnitude_sum = sum(x for x in data if x > threshold_primary)
    
    # Complex conditional with short-circuit and bit manipulation red herring
    flag_state = (magnitude_sum > 50) or (len(data) & 7 == 0 and magnitude_sum > 30)
    
    # Distractor block: elaborate but unused calculation
    cumulative_xor = 0
    for val in data:
        int_val = int(abs(val * 10)) % 256
        cumulative_xor ^= int_val
        if cumulative_xor > 200:
            cumulative_xor = cumulative_xor >> 1
    
    # Real computation path - depends on evaluate_stability_index output
    stability_metric = evaluate_stability_index(data)
    adjustment_factor = 0.9 if flag_state else 1.1
    
    # Final result influenced by multiple indirect paths
    result = (magnitude_sum * adjustment_factor) - stability_metric
    return int(result)

# Misleading setup - suggests dynamic configuration
config_store = {
    'calibration': {'level': 3, 'mode': 'strict'},
    'thresholds': {
        'primary': 4.0,
        'secondary': 2.0,
        'debug_mode': False
    }
}

# Unused but plausible-looking utility
def validate_configuration(cfg):
    t = cfg['thresholds']
    if t['primary'] < t['secondary']:
        return False
    if t['primary'] > 10.0:
        return False
    return True

# Orchestration with hidden dependencies
if __name__ == "__main__":
    readings = collect_sensor_readings()
    filtered_readings = apply_window_filter(readings)
    transformed_data = transform_signal_sequence(filtered_readings)
    
    # Dummy variable to mislead about control flow
    audit_trace = [sum(transformed_data[:4]), sum(transformed_data[4:])] 
    
    # Key thresholds - primary matters, others are distractions
    thresholds = {
        'primary': 3.5,
        'spurious': 1.2,
        'phantom_limit': 100
    }
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Additional irrelevant logging
    debug_snapshot = [
        f"Entry: {len(transformed_data)}",
        f"Max: {max(transformed_data):.2f}"
    ]
    
    print(f"Result: {final_diagnostic}")