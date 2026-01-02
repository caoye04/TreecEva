from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostic system
def analyze_readings(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return avg, std_dev

def compute_health_score(metrics):
    # Irrelevant health scoring (distractor)
    base_score = 100
    if metrics['errors'] > 5:
        base_score -= 30
    if metrics['latency'] > 200:
        base_score -= 20
    return max(base_score, 0)

def filter_anomalies(data_stream):
    # Dead code path - never used in final computation
    anomalies = []
    threshold = 3
    mean_val = sum(data_stream) / len(data_stream)
    std_val = math.sqrt(sum((x - mean_val)**2 for x in data_stream) / len(data_stream))
    for val in data_stream:
        if abs(val - mean_val) > threshold * std_val:
            anomalies.append(val)
    return anomalies

def aggregate_logs(log_entries):
    # Distractor function: collects but doesn't impact final result
    severity_count = defaultdict(int)
    category_freq = Counter()
    
    for entry in log_entries:
        timestamp, level, module, code = entry
        severity_count[level] += 1
        category_freq[module] += 1
    
    # Meaningless transformation
    normalized = {k: v / len(log_entries) for k, v in severity_count.items()}
    return normalized

def evaluate_stability(indices):
    # Unused stability evaluation (red herring)
    if len(indices) < 2:
        return 0.0
    diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    return sum(diffs) / len(diffs)

def extract_signatures(payloads):
    # Decoy computation on irrelevant feature
    sig_map = {}
    for i, p in enumerate(payloads):
        sig = (sum(p) * i) % 17
        sig_map[i] = sig
    return sig_map

def process_metrics(log_data, state):
    # Core logic embedded within distractions
    readings = state['sensor_readings']
    config = state['config_profile']
    
    avg_temp, std_temp = analyze_readings(readings)
    
    # Key intermediate calculation
    baseline = config['reference']
    drift = abs(avg_temp - baseline)
    
    # Real logic hidden among irrelevant ones
    adjustment_factor = 1.0
    if std_temp > 5.0:
        adjustment_factor *= 0.8
    if drift > 10.0:
        adjustment_factor *= 0.7
    
    # Critical metric derivation
    raw_metric = avg_temp * adjustment_factor
    
    # Multiple data structures with cross-reference
    meta_info = {
        'version': config['version'],
        'mode': config['mode'],
        'active': True
    }
    
    if meta_info['version'] >= 2 and meta_info['mode'] == 'adaptive':
        raw_metric += 3.5
    
    # Final result based on controlled logic chain
    diagnostic_value = int(raw_metric * 10 + std_temp)
    
    # This is the actual answer variable
    final_diagnostic = diagnostic_value * 2
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # System state input
    system_state = {
        'sensor_readings': [68, 72, 75, 67, 70, 74, 69, 73, 71, 70, 68, 72],
        'config_profile': {
            'reference': 70,
            'version': 3,
            'mode': 'adaptive',
            'thresholds': [5, 10, 15]
        }
    }

    # Log data (used to trigger distractor functions)
    log_data = [
        (1623456780, 'ERROR', 'sensor_io', 5001),
        (1623456789, 'WARN', 'network', 4002),
        (1623456795, 'INFO', 'storage', 2001),
        (1623456801, 'ERROR', 'sensor_io', 5003),
        (1623456807, 'INFO', 'controller', 2005)
    ]

    payload_sequences = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]

    # Trigger multiple irrelevant computations (distractors)
    health_metrics = {
        'errors': 7,
        'latency': 210
    }
    score = compute_health_score(health_metrics)
    
    anomaly_list = filter_anomalies(system_state['sensor_readings'])
    log_summary = aggregate_logs(log_data)
    stability_index = evaluate_stability([10, 20, 30, 40])
    signatures = extract_signatures(payload_sequences)
    
    # Critical statement that produces the answer
    final_diagnostic = process_metrics(log_data, system_state)
    
    print(f"Result: {final_diagnostic}")