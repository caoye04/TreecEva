import math

def analyze_component_health(sensor_data, thresholds):
    # Irrelevant helper function (dead code path)
    health_flags = {}
    for k, v in sensor_data.items():
        health_flags[k] = v < thresholds.get(k, 100)
    return {k: False for k in health_flags}  # Distractor: always returns False

def transform_payload(raw_sequence, mode="encode"):
    # Unused transformation logic (red herring)
    if mode == "encode":
        return [((x << 2) ^ 0xAA) % 256 for x in raw_sequence]
    else:
        return [(x ^ 0xAA) >> 2 for x in raw_sequence]

def calculate_entropy(data_list):
    # Misleading statistical distraction
    total = sum(data_list)
    if total == 0:
        return 0.0
    probs = [v / total for v in data_list]
    return round(-sum(p * math.log2(p) for p in probs if p > 0), 6)

def update_calibration_table(table, factor=1.05):
    # Decoy function with no real impact
    new_table = {}
    for k, v in table.items():
        if isinstance(v, list):
            new_table[k] = [round(x * factor, 3) for x in v]
        else:
            new_table[k] = round(v * factor, 3)
    return new_table

def extract_key_metrics(logs):
    # Relevant but partially obscured logic
    metrics = {
        'response_time': 0,
        'retry_count': 0,
        'timeout_events': 0,
        'packet_loss': 0
    }
    for entry in logs:
        if 'response' in entry:
            metrics['response_time'] += entry['response']
        if 'retry' in entry:
            metrics['retry_count'] += entry['retry']
        if 'status' in entry:
            if entry['status'] == 'timeout':
                metrics['timeout_events'] += 1
            elif entry['status'] == 'lost':
                metrics['packet_loss'] += 1
    return metrics

def adjust_for_environment(metrics, env_profile):
    # Partially relevant adjustment
    adjusted = metrics.copy()
    load_factor = env_profile.get('load', 1.0)
    temp_bias = env_profile.get('temperature', 25)
    adjusted['response_time'] *= load_factor
    adjusted['retry_count'] += int(temp_bias > 30)
    return adjusted

def evaluate_performance(metrics_log, baseline_config):
    # Core logic buried among distractions
    cumulative = 0
    weights = baseline_config['weights']
    scaling = baseline_config['scaling_factor']

    # Real computation begins
    for key in ['response_time', 'retry_count', 'timeout_events']:
        raw_val = metrics_log.get(key, 0)
        weight = weights.get(key, 0)
        contribution = raw_val * weight
        cumulative += contribution  # Key accumulation

    # Non-linear penalty component
    packet_penalty = metrics_log.get('packet_loss', 0) ** 2 * 10
    cumulative += packet_penalty

    final_raw = cumulative * scaling

    # Normalize using a fixed reference (deterministic)
    normalized = final_raw / 0.75

    # Final threshold clamp (not actually triggered)
    if normalized > 10000:
        normalized = 9876.54

    # The actual answer is derived here
    final_score = int(round(normalized))

    # Dead code branch - misleading
    if final_score < 0:
        fallback_table = {"backup": [1, 2, 3], "version": 2}
        for k in fallback_table:
            pass  # Useless loop

    return final_score

# --- Main Execution ---
if __name__ == "__main__":
    # Simulated input data
    system_logs = [
        {'response': 120, 'retry': 1, 'status': 'ok'},
        {'response': 150, 'retry': 0, 'status': 'timeout'},
        {'response': 180, 'retry': 2, 'status': 'lost'},
        {'response': 90,  'retry': 1, 'status': 'timeout'},
        {'response': 210, 'retry': 0, 'status': 'ok'}
    ]

    config = {
        'weights': {
            'response_time': 0.25,
            'retry_count': 15.0,
            'timeout_events': 20.0
        },
        'scaling_factor': 1.8
    }

    # Irrelevant auxiliary data structures
    sensor_readings = {'cpu_temp': 68, 'fan_speed': 2200, 'voltage': 3.3}
    threshold_map = {'cpu_temp': 80, 'fan_speed': 2000}
    payload_stream = [0x1A, 0x2F, 0x4B, 0x5C, 0x6D]

    # Actual execution path
    extracted_metrics = extract_key_metrics(system_logs)
    environmental_metrics = adjust_for_environment(extracted_metrics, {'load': 1.1, 'temperature': 28})
    final_score = evaluate_performance(environmental_metrics, config)

    # Print result as required
    print(f"Result: {final_score}")
