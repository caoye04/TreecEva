import math

# Simulated system metrics with irrelevant and relevant data
def collect_diagnostics():
    return {
        'cpu_load': 78,
        'mem_usage': 43,
        'disk_reads': 1200,
        'network_latency_ms': 45,
        'temp_core_1': 67,
        'temp_core_2': 69,
        'packet_loss': 0.002,
        'uptime_hours': 127
    }

def transform_metrics(raw):
    # Relevant transformations mixed with red herrings
    transformed = {}
    transformed['load_factor'] = raw['cpu_load'] * 1.2
    transformed['memory_pressure'] = raw['mem_usage'] ** 1.5
    transformed['io_activity'] = raw['disk_reads'] // 100
    transformed['latency_norm'] = 100 / (raw['network_latency_ms'] + 1)
    transformed['thermal_score'] = (raw['temp_core_1'] + raw['temp_core_2']) / 2.5
    
    # Distractor computations (unused later)
    noise_1 = raw['uptime_hours'] % 24
    noise_2 = int(math.sqrt(raw['packet_loss'] * 100000))
    temp_flag = True if noise_1 > 10 else False
    dummy_list = [noise_1 * i for i in range(3)]  # Dead code path
    
    return transformed

def calculate_checksum(data_dict):
    # Irrelevant utility function (not used in final logic)
    keys = sorted(data_dict.keys())
    checksum = 0
    for i, k in enumerate(keys):
        checksum ^= (i + len(k)) * data_dict[k]
    return checksum % 1000

def filter_outliers(values):
    # Unused helper function — misleading presence
    mean_val = sum(values) / len(values)
    return [v for v in values if abs(v - mean_val) < 20]

def normalize_scores(scores):
    max_score = max(scores.values())
    return {k: round(v / max_score, 6) for k, v in scores.items()}

def evaluate_performance(metrics, weights):
    normed = normalize_scores(metrics)
    
    # Key computation path
    score_components = []
    weight_sum = 0
    
    for key in weights:
        if key in normed:
            score_components.append(normed[key] * weights[key])
            weight_sum += weights[key]
    
    final_raw = sum(score_components)
    
    # Red herring: unused conditional branch
    if final_raw > 1.0:
        scaling_factor = 0.95
        final_raw *= scaling_factor  # Never reached due to normalization
    
    # Final result
    final_score = int(round(final_raw * 10000))
    
    # Additional distractions below
    debug_trace = []
    for k, v in normed.items():
        debug_trace.append(f'{k}:{v}')
    metadata_log = {'processed_at': '2025-04-05', 'version': '3.1'}
    
    return final_score

# Main execution flow
raw_data = collect_diagnostics()
processed_metrics = transform_metrics(raw_data)

# Weights for evaluation (only some keys are actually present in metrics)
weights_map = {
    'load_factor': 0.3,
    'memory_pressure': 0.25,
    'latency_norm': 0.2,
    'io_activity': 0.15,
    'thermal_score': 0.1
}

# Irrelevant intermediate variables
checksum = calculate_checksum(raw_data)
outlier_test = [12, 15, 10, 1000, 14]  # Contains outlier but unused
filtered_test = filter_outliers(outlier_test)

# Critical statement
final_score = evaluate_performance(processed_metrics, weights_map)

# Output result
print(f"Result: {final_score}")