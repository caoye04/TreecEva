import math

# Simulated sensor data collection and diagnostic analysis with extensive distractors
def collect_sensor_readings():
    raw_values = [145, 203, 98, 112, 188, 73, 165]
    noise_floor = 42
    adjusted = [v - noise_floor for v in raw_values if v > 100]
    checksum = sum(adjusted) % 17
    # Distractor: irrelevant transformation
    inverted = [255 - v for v in adjusted]
    scaled = [round(v * 1.07, 2) for v in adjusted]
    return {'readings': adjusted, 'scale_cache': scaled, 'checksum': checksum}


def compute_health_score(metrics):
    base_score = metrics.get('base', 85)
    latency_penalty = metrics.get('latency', 0) // 5
    error_factor = metrics.get('errors', 0)
    # Distractor: unused health components
    temp_warning = metrics.get('overheating', False)
    redundancy_check = metrics.get('redundancy_ok', True)
    score = base_score - latency_penalty
    if error_factor > 0:
        score -= math.ceil(math.log(error_factor + 1, 2) * 3)
    return max(score, 0)

# Legacy function – appears relevant but not used in main flow
def legacy_diagnostic(payload):
    accumulator = 0
    for i, val in enumerate(payload.get('readings', [])):
        if i % 2 == 0:
            accumulator ^= (val & 15)
    return accumulator * 11

# Auxiliary mapping – used only partially
def map_component_status(flags):
    status_map = {}
    critical_flags = set(['err_mem', 'io_fail', 'temp_high'])
    warning_flags = set(['fan_slow', 'vol_low', 'crc_mismatch'])
    
    for comp, flag in flags.items():
        if flag in critical_flags:
            status_map[comp] = 'CRITICAL'
        elif flag in warning_flags:
            status_map[comp] = 'WARNING'
        else:
            status_map[comp] = 'OK'
    
    # Distractor: dead computation path
    debug_summary = {
        'critical_count': len([s for s in status_map.values() if s == 'CRITICAL']),
        'total_components': len(status_map),
        'health_ratio': round(len(status_map) / (len(critical_flags) + 1), 3)
    }
    return status_map

# Main analysis pipeline
def analyze_metrics(data, thresholds):
    readings = data['readings']
    anomalies = 0
    trend_buffer = []
    
    # Real logic begins: detect deviations using modular arithmetic
    for i, val in enumerate(readings):
        expected = thresholds['baseline'] + (i * thresholds['drift_rate'])
        deviation = abs(val - expected)
        if deviation > thresholds['tolerance']:
            anomalies += 1
            trend_buffer.append(deviation)
    
    # Core calculation embedded within distractions
    stability_index = len(readings) - anomalies
    fluctuation_score = sum(trend_buffer) if trend_buffer else 0
    
    # Distractor: complex-looking but unused compound expression
    entropy_proxy = 0
    for x in readings:
        if x > 0:
            entropy_proxy += x * math.log(x, 2)
    normalized_entropy = round(entropy_proxy / 1000, 4) if readings else 0.0
    
    # Irrelevant data structure manipulation
    reading_pairs = [(readings[i], readings[i+1]) for i in range(len(readings)-1)]
    diff_set = {abs(a - b) for a, b in reading_pairs}
    peak_jitter = max(diff_set) if diff_set else 0
    
    # Secondary distraction: dictionary-based state tracking (partially used)
    analysis_state = {
        'phase': 'diagnostic',
        'version': '2.1',
        'flags_triggered': [],
        'last_update': '2023-11-05'
    }
    
    # Critical branching logic
    if stability_index >= 4:
        if fluctuation_score < 150:
            decision_code = 200
        else:
            decision_code = 220
    else:
        if anomalies >= 3:
            decision_code = 300
        else:
            decision_code = 250
    
    # Final result derived from multiple steps
    system_diagnostic = (stability_index * 100) + (decision_code % 100) - fluctuation_score
    
    # Dead code: looks like it updates state but doesn't affect output
    if decision_code >= 300:
        analysis_state['flags_triggered'].append('STABILITY_ALERT')
        analysis_state['phase'] = 'safe_mode'
    
    # This line produces the target result
    final_result = {
        'diagnostic_code': decision_code,
        'anomaly_count': anomalies,
        'system_diagnostic': system_diagnostic,
        'debug_info': {
            'normalized_entropy': normalized_entropy,
            'peak_jitter': peak_jitter
        }
    }
    
    return final_result

# Execution entry point
if __name__ == '__main__':
    # Initialization with meaningful and distracting values
    collected_data = collect_sensor_readings()
    
    # Distractor: unused legacy call
    _ = legacy_diagnostic(collected_data)
    
    # Component status mapping – called but result unused
    component_flags = {
        'sensor_a': 'ok',
        'sensor_b': 'crc_mismatch',
        'controller': 'err_mem',
        'power': 'vol_low',
        'network': 'ok'
    }
    _ = map_component_status(component_flags)
    
    # Threshold configuration – only this matters
    system_thresholds = {
        'baseline': 90,
        'drift_rate': 5,
        'tolerance': 25
    }
    
    # Key execution point
    final_analysis = analyze_metrics(collected_data, system_thresholds)
    
    # Output the required variable
    system_diagnostic = final_analysis['system_diagnostic']
    print(f"Result: {system_diagnostic}")