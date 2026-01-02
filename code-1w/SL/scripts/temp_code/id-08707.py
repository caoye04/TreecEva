import math

def preprocess_signal(data_stream):
    # Irrelevant preprocessing step (dead code path)
    return [x * 1.05 for x in data_stream if x > 0]

def compute_checksum(sequence):
    # Distractor function: used nowhere in critical path
    return sum((i + val) % 7 for i, val in enumerate(sequence)) % 1000

def detect_anomalies(readings, threshold=3.5):
    anomalies = []
    for idx, r in enumerate(readings):
        if abs(r - 5.0) > threshold and idx % 2 == 0:
            anomalies.append(idx)
    return anomalies  # Unused result

def evaluate_stability_index(log_chunk):
    base_score = 0
    for entry in log_chunk:
        if entry['status'] == 'active':
            base_score += 0.7
        elif entry['status'] == 'standby':
            base_score += 0.3
        else:
            base_score -= 0.1
    return round(base_score, 4)

def analyze_system_state(log, thresholds):
    # Core logic begins here — heavily masked by distractions
    cumulative_weight = 0.0
    event_sequence = []

    # Extract diagnostic codes using slicing and filtering
    raw_codes = [entry['diagnostic'] for entry in log]
    filtered_codes = raw_codes[1::2]  # Every second code starting from index 1

    # Real computation: count occurrences of specific code
    code_freq = {}
    for code in filtered_codes:
        code_freq[code] = code_freq.get(code, 0) + 1

    # Misleading branch based on decoy threshold
    adjustment = 0
    if len(filtered_codes) > thresholds['size_cap']:
        adjustment = -1
    else:
        adjustment = 1  # This will be applied

    # Lambda-based transformation (actual use)
    scale_factor = lambda x: math.log(x + 2) if x > 0 else 0.5

    temp_offset = 0
    for k, v in code_freq.items():
        temp_offset += scale_factor(v) * (k % 3)

    # Nested condition with actual impact
    stability = evaluate_stability_index(log)
    if stability > 4.0:
        cumulative_weight += temp_offset * 1.8
    else:
        cumulative_weight += temp_offset * 0.9

    # Critical calculation hidden among red herrings
    trigger_points = [e['timestamp'] for e in log if 'error' in e['message'].lower()]
    penalty = len(trigger_points) * 0.4

    cumulative_weight -= penalty
    cumulative_weight += adjustment * 0.25

    # Final assignment — this is the answer
    final_diagnostic = int(round(cumulative_weight * 100))

    # Decoy output variables
    summary_report = {
        'checksum': compute_checksum([1, 2, 3, 4]),
        'anomaly_count': len(detect_anomalies([1.2, 4.8, 6.7, 2.1])),
        'preprocessed': preprocess_signal([-1, 0, 5, 10])
    }

    return final_diagnostic

# Simulated telemetry data (real input)
telemetry_log = [
    {'timestamp': 1001, 'diagnostic': 7, 'status': 'active', 'message': 'Normal operation'},
    {'timestamp': 1002, 'diagnostic': 7, 'status': 'standby', 'message': 'No issues'},
    {'timestamp': 1003, 'diagnostic': 4, 'status': 'active', 'message': 'error detected in subsystem'},
    {'timestamp': 1004, 'diagnostic': 4, 'status': 'active', 'message': 'Back to normal'},
    {'timestamp': 1005, 'diagnostic': 7, 'status': 'standby', 'message': 'Stable'},
    {'timestamp': 1006, 'diagnostic': 4, 'status': 'active', 'message': 'All clear'},
    {'timestamp': 1007, 'diagnostic': 7, 'status': 'active', 'message': 'error in sensor array'},
    {'timestamp': 1008, 'diagnostic': 7, 'status': 'active', 'message': 'Recovered'}
]

fault_thresholds = {
    'size_cap': 10,
    'critical_level': 8.5,
    'timeout_limit': 300
}

# Execution point of interest
final_diagnostic = analyze_system_state(telemetry_log, fault_thresholds)
print(f"Result: {final_diagnostic}")