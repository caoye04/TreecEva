from collections import defaultdict, Counter

# Simulated IoT sensor data processing with health diagnostics
def analyze_readings(readings):
    stats = defaultdict(int)
    anomalies = []
    base_level = 0
    temp_buffer = []

    for r in readings:
        if r < 0:
            stats['negative'] += 1
        elif r > 100:
            anomalies.append(r)
            stats['high_anomaly'] += 1
        else:
            stats['valid'] += 1

        if 40 <= r <= 60:
            stats['optimal'] += 1

        # Irrelevant transformation
        transformed = (r * 2 + 1) % 97
        temp_buffer.append(transformed)

    # Dead code path — never accessed in normal flow
    if len(temp_buffer) > 1000:
        backup = [x ^ 3 for x in temp_buffer]
        stats['checksum'] = sum(backup) // len(backup)

    return stats, anomalies

def evaluate_stability(metrics, history):
    score = 0
    penalty = 0

    # Real logic
    if metrics['valid'] > 5:
        score += 10
    if metrics['optimal'] >= 3:
        score += 15

    # Distractor: complex-looking but unused calculation
    shadow_score = 0
    for h in history:
        shadow_score += (h.get('peak', 0) // 3) * 2
        if h.get('flag') == 'alert':
            shadow_score -= 5

    # More red herrings
    debug_trace = [score * i for i in range(1, 4)]
    intermediate_result = sum(debug_trace) / 3 if debug_trace else 0

    # Unused nested structure
    metadata_log = {
        'version': '2.1a',
        'flags': [f'X{i}' for i in range(metrics['valid']) if i % 7 == 0],
        'aux_data': {'level': base_level if 'base_level' in locals() else -1}
    }

    return score - penalty

def process_metrics(data, config):
    # Core computation
    readings = data['values']
    metrics, errs = analyze_readings(readings)
    stability = evaluate_stability(metrics, data['history'])

    # Key distraction block — looks important but doesn't affect result
    error_signature = 0
    if errs:
        cnt = Counter(errs)
        error_signature = sum(k * v for k, v in cnt.items()) % 1000

    adjustment_factor = 1
    mode_flag = data.get('mode', 'normal')
    if mode_flag == 'turbo':
        adjustment_factor = 2
    elif mode_flag == 'eco':
        adjustment_factor = 0.5

    # Actual answer derivation
    base_diagnostic = metrics['optimal'] * 100 + stability
    final_diagnostic = int(base_diagnostic * adjustment_factor)

    # More misleading computations
    diagnostic_chain = []
    for i in range(3):
        hashed = (final_diagnostic ^ (i * 37)) % 9973
        diagnostic_chain.append(hashed)

    # Fake checksum that appears critical
    validation_key = sum(diagnostic_chain) & 0xFFFF
    audit_log = f"CHK-{validation_key:04X}"

    # This print is required to expose the target variable
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution context
if __name__ == "__main__":
    # Input data setup
    health_data = {
        'values': [45, 55, 105, 50, 30, 58, 65, 52],
        'history': [
            {'timestamp': 1, 'peak': 98, 'flag': None},
            {'timestamp': 2, 'peak': 102, 'flag': 'alert'}
        ],
        'device_id': 'SENSOR-X42',
        'mode': 'normal'
    }

    # Threshold configuration (partially unused)
    threshold_map = {
        'critical': 95,
        'warning': 75,
        'relaxation_factor': 1.1
    }

    # Auxiliary variables — distractions
    calibration_sequence = [i**2 % 53 for i in range(10)]
    system_uptime = 1274
    last_sync = (system_uptime // 60) % 24

    # Trigger point
    final_diagnostic = process_metrics(health_data, threshold_map)