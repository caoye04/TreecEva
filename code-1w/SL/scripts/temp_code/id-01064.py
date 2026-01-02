import math

def analyze_sensor(x):
    return x ** 2 + 3 * x + 1 if x > 0 else abs(x)

def compute_stress_factor(load, temp):
    base = (load / (temp + 273)) * 100
    adjusted = base * (1 + 0.05 * math.sin(math.pi / 4))
    return round(adjusted, 3)

def evaluate_efficiency(rpm, flow_rate):
    # Irrelevant helper with dead logic path
    if rpm < 0 or flow_rate <= 0:
        return 0
    efficiency = (rpm * flow_rate) / 1000
    penalty = 0
    if efficiency > 85:
        penalty = 5
    elif efficiency > 70:
        penalty = 3
    return efficiency - penalty

def filter_anomalies(data_list):
    # Distraction: processes data but not used in final result
    anomalies = []
    for val in data_list:
        if val < -10 or val > 100:
            anomalies.append(val)
    return anomalies

def generate_report_header(project_id, version):
    # Unused function - red herring
    return f'Report-{project_id}-v{version}'

def aggregate_metrics(sensor_inputs, log_frame):
    # Core logic hidden among distractions
    processed = []
    for val in sensor_inputs:
        result = analyze_sensor(val)
        processed.append(result)
    
    # Distractor variables
    temp_cache = [compute_stress_factor(80 + i, 25) for i in range(5)]
    shadow_copy = processed.copy()
    shadow_copy.reverse()
    
    # Real computation intermixed with noise
    total_signal = sum(processed)
    correction_factor = log_frame.get('calibration_offset', 0.98)
    raw_diagnostic = total_signal * correction_factor
    
    # Bit manipulation decoy
    masked_value = int(raw_diagnostic) & 0xFFFF
    inverted = ~masked_value & 0xFFFF
    
    # Lambda and dictionary operation (required feature)
    scale_func = lambda x: x * 1.05 if x < 500 else x * 1.02
    status_map = {'normal': 1, 'caution': 2, 'alert': 3}
    
    # Set operation (required feature)
    unique_signals = set(processed)
    diversity_bonus = len(unique_signals) * 2.5
    
    # Final calculation chain
    intermediate = scale_func(raw_diagnostic)
    adjusted_diagnostic = intermediate + diversity_bonus
    
    # More misdirection
    dummy_stats = {
        'mean': sum(processed) / len(processed),
        'peak': max(processed),
        'noise_floor': min(shadow_copy),
        'version': '2.1a'
    }
    
    # Actual answer depends only on specific path
    final_diagnostic = int(adjusted_diagnostic - inverted % 100)
    
    # Dead code branch - never executed
    if False:
        fallback = 0
        for k in status_map:
            fallback += status_map[k]
        final_diagnostic = fallback
    
    return final_diagnostic

# Simulated input data
baseline_readings = [7, -3, 12, 8, 15, 6]
turbine_data = [x * 2 for x in baseline_readings]  # [14, -6, 24, 16, 30, 12]

diagnostics_log = {
    'timestamp': '2023-11-05T14:30:00Z',
    'node_id': 'TURB-7X',
    'calibration_offset': 0.98,
    'status': 'normal'
}

# Irrelevant pre-processing
buffer_queue = []
for item in turbine_data:
    buffer_queue.append(item * 0.1)

# Key execution point
final_diagnostic = aggregate_metrics(turbine_data, diagnostics_log)

# Output result
print(f"Result: {final_diagnostic}")