import math

# Simulated sensor fusion system with diagnostic logic
def collect_telemetry():
    raw_samples = [i * 0.77 for i in range(15)]
    noise_floor = sum([math.sin(x) for x in raw_samples]) / len(raw_samples)
    adjusted = [x + noise_floor for x in raw_samples]
    return adjusted

# Irrelevant helper - dead code path (distraction)
def deprecated_normalization(data):
    if not data:
        return []
    max_val = max(data)
    return [x / max_val for x in data] if max_val else data

# Unused signal conditioning (red herring)
def apply_filter(signal, mode='legacy'):
    if mode == 'legacy':
        return [x * 0.9 for x in signal]
    else:
        return [x * 1.1 for x in signal]

# Complex pattern analyzer with distractor logic
def detect_anomalies(stream):
    anomalies = []
    baseline = sum(stream[:5]) / 5
    deviation_scores = []
    
    # Distractor: elaborate scoring with unused results
    for i, val in enumerate(stream):
        z_score = abs(val - baseline) / (sum([abs(x - baseline) for x in stream[:i+1]]) / (i+1) + 1e-8)
        adjusted_z = z_score * (0.95 ** i)  # Exponential decay (unused later)
        category = 'HIGH' if z_score > 1.8 else 'LOW'
        deviation_scores.append({'index': i, 'score': z_score, 'type': category})
    
    # Actual relevant logic buried here
    for entry in deviation_scores:
        if entry['score'] > 2.0:
            anomalies.append(entry['index'])
    
    # Dead return branch (misleading)
    if len(anomalies) > 10:
        return {'count': len(anomalies), 'critical': True, 'nodes': set(anomalies)}
    
    return {'count': len(anomalies), 'critical': False, 'nodes': set(anomalies)}

# Core transformation with set operations (required feature)
def generate_threshold_map(base_signal):
    even_indices = {i for i in range(len(base_signal)) if i % 2 == 0}
    high_energy = {i for i, x in enumerate(base_signal) if x > 5.0}
    mid_range = {i for i, x in enumerate(base_signal) if 2.0 <= x <= 7.0}
    
    # Complex set interactions - some irrelevant
    primary_zones = even_indices & high_energy  # meaningful
    secondary_zones = mid_range - even_indices  # distraction
    tertiary_zones = high_energy ^ mid_range     # unused
    
    # Only primary_zones is actually used
    thresholds = {}
    for i in range(len(base_signal)):
        if i in primary_zones:
            thresholds[i] = base_signal[i] * 1.25
        else:
            thresholds[i] = base_signal[i] * 0.85
    
    # Return distractor metadata
    return {
        'values': thresholds,
        'zones': {
            'primary': primary_zones,
            'secondary': secondary_zones,  # unused
            'tertiary': tertiary_zones   # unused
        },
        'stats': {
            'peak': max(base_signal),
            'entropy': len(primary_zones) / len(base_signal)
        }
    }

# Main analysis function with multiple concepts
def analyze_pattern(buffer, thresholds_dict):
    # Logical operations and comparisons
    condition_a = len(buffer) > 10
    condition_b = sum(buffer) / len(buffer) > 4.0
    condition_c = False
    
    # Nested control flow with red herring
    if condition_a and condition_b:
        temp_result = 0
        for i, val in enumerate(buffer):
            expected = thresholds_dict['values'][i]
            if val > expected * 1.1:
                temp_result += int(val - expected)
            elif val < expected * 0.9:
                temp_result -= int(expected - val)
        
        # Bit manipulation decoy
        masked = temp_result & 0xFF
        shifted = masked << 2
        condition_c = (shifted % 7) > 3
    
    # Critical path embedded here
    anomaly_report = detect_anomalies(buffer)
    primary_zone_set = thresholds_dict['zones']['primary']
    anomaly_zone_intersection = anomaly_report['nodes'] & primary_zone_set
    
    # Multi-concept integration: boolean, arithmetic, set ops
    weight_factor = 3.75 if condition_c else 2.25
    intersection_score = len(anomaly_zone_intersection) * weight_factor
    base_offset = math.floor(thresholds_dict['stats']['peak'])
    
    # Decoy calculation (looks important but unused)
    entropy_penalty = thresholds_dict['stats']['entropy'] * 100
    adjusted_penalty = entropy_penalty if anomaly_report['critical'] else 0
    
    # Final computation (answer derivation)
    final_diagnostic = base_offset + int(intersection_score)
    
    # Dead code block (distractor)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        correction_log = {"reversed": True, "reason": "negative_diagnostic"}
    
    return final_diagnostic

# Orchestration with irrelevant setup
initial_calibration = [x * 0.5 for x in range(8)]
deprecated_normalization(initial_calibration)  # called but result ignored

# Signal acquisition
signal_buffer = collect_telemetry()

# Threshold system generation
threshold_map = generate_threshold_map(signal_buffer)

# Key statement - target of question
final_diagnostic = analyze_pattern(signal_buffer, threshold_map)

print(f"Target result: {final_diagnostic}")