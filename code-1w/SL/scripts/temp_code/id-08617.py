import math

# Simulated sensor data and calibration parameters
def generate_diagnostics(raw_readings):
    diagnostics = []
    for val in raw_readings:
        if val < 0:
            diagnostics.append((val, 'ERROR'))
        elif val == 0:
            diagnostics.append((val, 'STANDBY'))
        else:
            normalized = math.log(val) if val > 1 else val
            status = 'OPTIMAL' if normalized > 0.7 else 'CALIBRATING'
            diagnostics.append((normalized, status))
    return diagnostics

# Auxiliary function to compute moving average (not directly used in final result)
def moving_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed

# Core processing logic
def process_metrics(data, config):
    # Irrelevant preprocessing: reverse and scale (distractor)
    scaled_data = [x * 1.05 for x in data if x > 0]
    reversed_scaled = scaled_data[::-1]
    
    # Actual relevant computation begins
    valid_entries = [x for x in data if x > 0]
    total_energy = sum(valid_entries)
    
    # Simulate threshold filtering
    thresholds = config.get('thresholds', {})
    upper_lim = thresholds.get('max', 100)
    lower_lim = thresholds.get('min', 10)
    
    filtered = [x for x in valid_entries if lower_lim <= x <= upper_lim]
    
    # Efficiency model based on harmonic mean (key computation)
    if filtered:
        inv_sum = sum(1/x for x in filtered)
        harmonic_mean = len(filtered) / inv_sum
    else:
        harmonic_mean = 0
    
    # Secondary metric: peak_ratio (semi-relevant, distractor)
    peak_value = max(valid_entries) if valid_entries else 0
    peak_ratio = peak_value / total_energy if total_energy else 0
    
    # Final scoring model
    base_score = harmonic_mean * 10
    adjustment = math.sin(len(filtered))  # Minor periodic adjustment
    efficiency_score = base_score + adjustment
    
    # Dead code path - never executed due to prior filtering
    if False and not filtered:
        efficiency_score = -999
    
    # Redundant print for distraction
    debug_info = {'size': len(reversed_scaled), 'peak': peak_ratio}
    
    # Key assignment
    final_output = {
        'score': efficiency_score,
        'count': len(filtered),
        'debug': debug_info
    }
    
    return final_output

# Main execution
raw_data = [5, 12, 15, 0, -3, 20, 8, 45, 7]
config_params = {
    'mode': 'high_precision',
    'thresholds': {
        'min': 8,
        'max': 40
    }
}

# Generate unused diagnostic logs (distractor)
diag_logs = generate_diagnostics(raw_data)

# Perform actual computation
result_container = process_metrics(raw_data, config_params)
efficiency_score = result_container['score']

# Output target result
print(f"Result: {efficiency_score}")