from collections import defaultdict, Counter
import math

# Simulated system health monitoring with performance evaluation

def analyze_component_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    stability = math.exp(-variance / (avg + 1e-5))
    return round(stability, 6)

def compute_redundancy_factor(primary, backup_list):
    # Irrelevant function - decoy
    return len([b for b in backup_list if b > primary]) * 0.1

def detect_anomalies(log_data):
    counts = Counter(log_data)
    anomalies = [k for k, v in counts.items() if v < 2]
    return anomalies[:3]  # Dead code path

def calculate_latency_penalty(response_times):
    # Distractor: looks important but unused
    sorted_times = sorted(response_times)
    median = sorted_times[len(sorted_times)//2]
    penalty = 0.0
    for t in response_times:
        if t > 2 * median:
            penalty += 0.05
    return penalty

def extract_signal_strength(signal_packet):
    # Signal extraction using bit manipulation (relevant)
    raw_value = signal_packet & 0xFFFF
    noise_floor = signal_packet >> 12
    clean_signal = (raw_value ^ noise_floor) & 0x7FF
    return clean_signal / 1024.0

def evaluate_performance(metrics, threshold):
    # Core logic buried among distractors
    aggregated = defaultdict(float)
    temp_results = []

    for k, v in metrics.items():
        if 'sensor' in k:
            processed = extract_signal_strength(v['data'])
            temp_results.append(processed)
            aggregated['signal_avg'] += processed
        elif 'cpu' in k:
            load = v['util']
            inv_load = 1 / (load + 1)  # Normalize
            aggregated['efficiency'] += inv_load

    # Real computation path
    signal_avg = aggregated['signal_avg']
    efficiency = aggregated['efficiency']

    # Key intermediate (misleading)
    preliminary_score = (signal_avg * 100) + (efficiency * 50)

    # Red herring normalization
    normalized_prelim = min(preliminary_score / 2, 85.0)

    # Actual key transformation
    if signal_avg > threshold:
        adjustment = efficiency * 15
    else:
        adjustment = -abs(efficiency * 10)

    # Final integration
    final_raw = preliminary_score + adjustment

    # Decoy post-processing
    outlier_check = [x for x in temp_results if x < 0.1]
    if len(outlier_check) > 1:
        final_raw *= 0.9  # Never triggers due to data design

    return int(round(final_raw))

# --- Simulated input data ---
metrics = {
    'sensor_array_a': {
        'data': 0xABCD,  # Bit-packed signal
        'calib': 0.98
    },
    'sensor_array_b': {
        'data': 0xBCDE,
        'calib': 0.99
    },
    'cpu_node_1': {
        'util': 0.75,
        'temp': 68
    },
    'cpu_node_2': {
        'util': 0.82,
        'temp': 71
    },
    'network_link': {
        'latency': [12, 15, 14, 100, 13],  # Spike anomaly
        'jitter': 5
    }
}

# Baseline threshold for decision boundary
baseline_threshold = 0.45

# Unused variables - red herrings
system_log = ['OK', 'OK', 'WARNING', 'OK']
data_buffer = [0] * 128
temp_snapshot = {'time': 12345, 'value': 999}

# Critical execution point
final_score = evaluate_performance(metrics, baseline_threshold)

# Output result as required
print(f"Result: {final_score}")