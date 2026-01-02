import math

def analyze_signal_strength(signal, baseline):
    # Irrelevant signal processing function (dead code path)
    adjusted = [s * 0.95 for s in signal]
    avg = sum(adjusted) / len(adjusted)
    return avg if avg > baseline else baseline + 0.1

def compute_entropy(data):
    # Unused entropy computation (distractor)
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    probabilities = [f / len(data) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probabilities)

def validate_checksum(record):
    # Misleading validation not used in main logic
    return sum(ord(c) for c in record) % 256 == 0

def extract_features(logs):
    # Complex but partially irrelevant feature extraction
    features = {}
    for key, values in logs.items():
        if key.startswith('sensor'):
            magnitude = sum(abs(v) for v in values)
            peak = max(values)
            features[key] = {
                'magnitude': magnitude,
                'peak': peak,
                'ratio': magnitude / (peak + 1e-8)
            }
    return features

def filter_anomalies(dataset, limit=100):
    # Dead-end filtering with early returns
    if not dataset:
        return []
    scores = []
    for val in dataset:
        if val < 0:
            continue
        transformed = math.sqrt(val) * 1.5
        if transformed > limit:
            break
        scores.append(int(transformed))
    return scores[:10]

def evaluate_health_status(metrics, config):
    # Nested conditional logic with red herring variables
    critical_count = 0
    warning_count = 0
    status_flags = []

    for sensor_id, reading in metrics.items():
        threshold_set = config.get(sensor_id, {})
        warn_low = threshold_set.get('warn_low', 0)
        warn_high = threshold_set.get('warn_high', 50)
        crit_low = threshold_set.get('crit_low', -10)
        crit_high = threshold_set.get('crit_high', 75)

        if reading < crit_low or reading > crit_high:
            critical_count += 1
            status_flags.append('CRITICAL')
        elif reading < warn_low or reading > warn_high:
            warning_count += 1
            status_flags.append('WARNING')
        else:
            status_flags.append('NORMAL')

    system_risk = 'GREEN'
    if critical_count > 2:
        system_risk = 'RED'
    elif warning_count > 4 or critical_count > 0:
        system_risk = 'YELLOW'

    # This intermediate result looks important but isn't final
    interim_score = (critical_count * 100) + (warning_count * 10)
    return system_risk, interim_score, status_flags

def process_metrics(log_data, thresholds):
    # Core relevant function with embedded distractions
    aggregate = 0
    temp_cache = {}
    diagnostic_codes = set()

    for log_id, entries in log_data.items():
        entry_sum = 0
        valid_count = 0

        for e in entries:
            # Simulate complex preprocessing
            if isinstance(e, dict) and 'value' in e:
                raw_val = e['value']
                if 'mask' in e and e['mask']:
                    raw_val = raw_val ^ 0xFF  # Bitwise decoy
                clamped = max(0, min(raw_val, 100))
                entry_sum += clamped
                valid_count += 1

                # Store in cache (partially unused)
                temp_cache[log_id] = temp_cache.get(log_id, 0) + clamped

        if valid_count > 0:
            avg_entry = entry_sum / valid_count
            category = 'default'
            if avg_entry < 30:
                category = 'low'
            elif avg_entry < 70:
                category = 'medium'
            else:
                category = 'high'

            # Conditional expression used
            adjustment = 1.25 if category == 'high' else (0.85 if category == 'low' else 1.0)
            aggregate += avg_entry * adjustment

    # Use dictionary to map states (real dependency)
    state_weights = {'low': -10, 'medium': 5, 'high': 15}
    for k in log_data.keys():
        w = state_weights.get('high')  # Deliberately missing dynamic lookup
        aggregate += w if k.endswith('_urgent') else 0

    # Real decision logic buried here
    primary_sensor = log_data.get('sensor_01', [])
    if primary_sensor:
        first_value = primary_sensor[0]
        if isinstance(first_value, dict):
            base = first_value['value']
            if base > 50:
                aggregate *= 1.1

    # Final computation that depends on multiple paths
    modifier = 1.0
    for t_key, t_val in thresholds.items():
        if t_key in ['sensor_01', 'sensor_02']:
            if 'offset' in t_val:
                modifier += t_val['offset'] * 0.01

    final_diagnostic = int(aggregate * modifier)

    # Print required at end
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution block with realistic simulation data
if __name__ == '__main__':
    # Simulated log data (mix of relevant and irrelevant structure)
    log_data = {
        'sensor_01': [
            {'value': 64, 'mask': False},
            {'value': 71, 'mask': True},  # masked but still processed
            {'value': 58, 'mask': False}
        ],
        'sensor_02': [
            {'value': 45, 'mask': False},
            {'value': 33, 'mask': False}
        ],
        'sensor_03_urgent': [
            {'value': 88, 'mask': False},
            {'value': 92, 'mask': False}
        ],
        'auxiliary_debug': [
            {'value': 10, 'meta': 'debug'}
        ]
    }

    # Threshold configuration with decoy fields
    system_thresholds = {
        'sensor_01': {
            'warn_low': 20, 'warn_high': 60,
            'crit_low': 10, 'crit_high': 80,
            'offset': 5
        },
        'sensor_02': {
            'warn_low': 25, 'warn_high': 65,
            'crit_low': 15, 'crit_high': 75,
            'offset': 10
        }
    }

    # Spurious calls to distractor functions
    _ = analyze_signal_strength([60, 65, 70], 55)
    _ = compute_entropy([1, 1, 2, 2, 3])
    _ = filter_anomalies([10, 20, 150, 30, 200, 40], limit=100)

    # Key execution point
    final_diagnostic = process_metrics(log_data, system_thresholds)