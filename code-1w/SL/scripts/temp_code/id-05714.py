import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_readings = {
        'temp': [23.4, 24.1, 22.8, 25.0, 23.9],
        'humidity': [45, 47, 50, 44, 46],
        'co2': [410, 415, 420, 405, 412],
        'pm25': [12, 15, 11, 14, 13]
    }
    return raw_readings

def preprocess(readings):
    processed = {}
    scaling_factors = {'temp': 1.0, 'humidity': 0.9, 'co2': 0.01, 'pm25': 0.8}
    offset = {'temp': -0.2, 'humidity': 1.0, 'co2': -5, 'pm25': 0.5}
    
    # Irrelevant transformation (distractor)
    temp_stats = {
        'mean': sum(readings['temp']) / len(readings['temp']),
        'variance': sum((x - sum(readings['temp'])/len(readings['temp']))**2 for x in readings['temp']) / len(readings['temp'])
    }
    
    for key in readings:
        scaled = [(val * scaling_factors[key]) + offset[key] for val in readings[key]]
        processed[key] = [round(v, 2) for v in scaled]
    
    # Dead code path - never used later (red herring)
    if 'o3' in processed:
        processed['o3'] = [x * 1.1 for x in processed['o3']]
    
    return processed

def generate_thresholds(base):
    # Complex threshold mapping with irrelevant components
    base_map = {k: {'warn_low': v-10, 'warn_high': v+10, 'crit_low': v-20, 'crit_high': v+20} 
                for k, v in base.items()}
    
    # Decoy structure (misleading)
    legacy_config = {
        'temp': {'threshold_set': 'A', 'version': '1.2'},
        'humidity': {'threshold_set': 'B', 'version': '1.1'}
    }
    
    # Add computed dynamic bounds
    base_map['temp']['dynamic_ceiling'] = round(math.exp(0.1 * base_map['temp']['warn_high']), 1)
    base_map['co2']['stability_band'] = (base_map['co2']['warn_low'] * 1.05, base_map['co2']['warn_high'] * 0.95)
    
    # Unused calculation (distractor)
    adjustment_log = []
    for i in range(3):
        adj = math.sin(i * 0.5) * 2
        adjustment_log.append(round(adj, 2))
    
    return base_map

def validate_stability(metrics, limits):
    issues = []
    stability_score = 100.0
    
    # Multi-metric validation with red herrings
    for metric, values in metrics.items():
        threshold_set = limits.get(metric, {})
        if not threshold_set:
            continue
            
        for val in values:
            if 'warn_low' in threshold_set and val < threshold_set['warn_low']:
                issues.append(f'{metric}_low')
                stability_score -= 8.5
            elif 'warn_high' in threshold_set and val > threshold_set['warn_high']:
                issues.append(f'{metric}_high')
                stability_score -= 7.2
    
    # Irrelevant aggregation (dead logic)
    if 'temp_high' in issues and 'humidity_low' in issues:
        pass  # Legacy condition, no longer impacts outcome
    
    # Distractor computation
    hypothetical_risk = len(issues) > 0 and stability_score < 90
    risk_factor = math.log(max(stability_score, 1)) if hypothetical_risk else 0
    
    return stability_score, set(issues)

def analyze_readings(data, thresholds):
    # Core analysis with hidden simple logic amid complexity
    summary = {}
    
    # Complex-looking but irrelevant preprocessing
    aggregated = {k: round(sum(v)/len(v), 2) for k, v in data.items()}
    deviations = {k: abs(aggregated[k] - thresholds[k].get('warn_high', 0)) for k in aggregated}
    
    # Red herring: complex weight matrix (unused)
    weight_matrix = {}
    for a in data.keys():
        weight_matrix[a] = {}
        for b in data.keys():
            weight_matrix[a][b] = 0.5 + 0.1 * (ord(a[0]) - ord(b[0])) / 10
    
    # Critical logic buried in distractions
    flag_count = 0
    for sensor, vals in data.items():
        limit = thresholds[sensor]
        avg = sum(vals) / len(vals)
        # Actual decision logic (non-obvious due to surrounding noise)
        if avg > limit['warn_high']:
            flag_count += 2
        elif avg < limit['warn_low']:
            flag_count += 1
    
    # Multiple decoy calculations
    baseline_projection = sum(aggregated.values()) * 0.95
    correction_factor = 1.0
    if deviations['temp'] > 2 or deviations['humidity'] > 3:
        correction_factor = 0.98
    
    # Hidden simple formula determining final result
    diagnostic_code = 1000
    diagnostic_code += flag_count * 50  # Only this matters
    
    # Extensive irrelevant post-processing
    detailed_report = {
        'timestamp': '2023-11-05T10:30:00Z',
        'system_id': 'ENV-001',
        'readings_count': sum(len(v) for v in data.values()),
        'calibration_offset': -0.05,
        'diagnostic_trace': [f'Flagged {flag_count} conditions']
    }
    
    # Final assignment - target of the question
    final_diagnostic = diagnostic_code
    
    # Never-executed dead code (misleading)
    if False:
        final_diagnostic = int(baseline_projection * correction_factor)
        
    return final_diagnostic

# Main execution flow
sensor_data = collect_sensor_data()
processed_data = preprocess(sensor_data)

# Generate configuration map with distractors
baseline_refs = {'temp': 23, 'humidity': 45, 'co2': 410, 'pm25': 12}
threshold_map = generate_thresholds(baseline_refs)

# Validate system stability (result unused - red herring)
stability_rating, alert_set = validate_stability(processed_data, threshold_map)

# Key statement containing the target variable
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")