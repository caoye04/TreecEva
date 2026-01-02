from collections import defaultdict
import math

# Simulated sensor data aggregation (irrelevant but plausible)
sensor_cache = {}
for i in range(10):
    sensor_cache[f'sensor_{i}'] = [j * (i + 1) for j in range(100)]

# Core health monitoring logic with distractors
def analyze_readings(readings):
    if not readings:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return avg + std_dev

# Misleading normalization function (dead code path)
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Data preprocessing with red herring operations
def extract_features(data_batch):
    features = defaultdict(float)
    temp_aggr = 0
    for key, values in data_batch.items():
        if 'temp' in key:
            temp_aggr += sum(values)
        elif 'pulse' in key:
            features['peak_pulse'] = max(values)
        elif 'resp' in key:
            features['baseline_resp'] = min(values)
    features['thermal_sum'] = temp_aggr
    
    # Irrelevant transformation chain
    dummy_result = list(map(lambda x: x * 0.5, [temp_aggr]))
    dummy_result = [math.log(x + 1) for x in dummy_result if x > 0]
    
    return features

# Primary processing with conditional logic and distractors
def evaluate_risk_level(metrics, thresholds):
    risk_score = 0
    evaluation_trace = []
    
    # Complex nested conditionals with misleading branches
    for metric_name, metric_value in metrics.items():
        if metric_name == 'peak_pulse':
            if metric_value > thresholds.get('critical_pulse', 120):
                risk_score += 3
                evaluation_trace.append('CRITICAL_PULSE')
            elif metric_value > thresholds.get('elevated_pulse', 100):
                risk_score += 1
        elif metric_name == 'baseline_resp':
            if metric_value < thresholds.get('low_resp', 10):
                risk_score += 2
        elif metric_name == 'thermal_sum':
            adjusted_thermal = metric_value * 0.01
            if adjusted_thermal > thresholds.get('high_thermal', 50):
                risk_score += 1
    
    # Dead branch with decoy calculation
    if 'phantom_metric' in metrics:
        risk_score += int(math.sqrt(metrics['phantom_metric']))
    
    return risk_score

# Final diagnostic processor combining multiple concepts
def process_metrics(raw_data, config_map):
    # Step 1: Extract relevant features
    extracted = extract_features(raw_data)
    
    # Step 2: Compute derived metric (relevant)
    pulse_rate = extracted.get('peak_pulse', 0)
    resp_rate = extracted.get('baseline_resp', 15)
    thermal_load = extracted.get('thermal_sum', 0)
    
    # Step 3: Apply nonlinear transformation (key step)
    derived_index = (pulse_rate * 0.3) + (resp_rate * 0.1) + math.log(thermal_load + 1) * 0.5
    
    # Step 4: Risk evaluation with short-circuit logic
    high_alert = (pulse_rate > 110) or (resp_rate < 12 and thermal_load > 400)
    
    # Step 5: Conditional override (distractor)
    if high_alert and derived_index < 25:  # Contradictory condition
        derived_index *= 1.2
    
    # Step 6: Final decision with bit manipulation red herring
    alert_code = 0b1010
    if derived_index > 30:
        alert_code |= 0b0101
    
    # Step 7: Diagnostic fusion (actual answer computation)
    base_diagnostic = int(derived_index)
    adjustment_factor = 2 if high_alert else 1
    final_diagnostic = base_diagnostic * adjustment_factor
    
    # Step 8: Decoy output mutation (never executed due to logic)
    if alert_code & 0b0001 and False:  # Always false short-circuit
        final_diagnostic = -1 * (alert_code ^ 0xFF)
    
    return final_diagnostic

# Setup realistic input data
health_data = {
    'temp_sensor_1': [36.5, 36.7, 36.8, 37.2, 37.5, 38.1, 38.3, 38.5, 38.7, 38.9],
    'temp_sensor_2': [36.6, 36.8, 36.9, 37.3, 37.6, 38.2, 38.4, 38.6, 38.8, 39.0],
    'pulse_ox_1': [72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 101, 104, 107, 110, 113],
    'resp_rate_a': [18, 17, 16, 15, 14, 13, 12, 11, 10, 9]
}

threshold_map = {
    'critical_pulse': 115,
    'elevated_pulse': 95,
    'low_resp': 11,
    'high_thermal': 45
}

# Execute main logic
diagnostic_trace = analyze_readings(health_data['pulse_ox_1'])  # Irrelevant call
feature_set = extract_features(health_data)  # Partially relevant
risk_level = evaluate_risk_level(feature_set, threshold_map)  # Distractor call

final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")