import math

# Simulated system metrics for performance analysis
def collect_metrics():
    raw_data = [127, 83, 194, 65, 221]
    metrics = {}
    for i, val in enumerate(raw_data):
        metrics[f'node_{i}'] = {
            'raw': val,
            'squared': val ** 2,
            'binary_shift': ((val << 2) ^ 15) & 255,
            'active': (val % 2 == 1)
        }
    # Irrelevant transformation
    temp = [x * 1.5 for x in raw_data if x > 100]
    temp_sum = sum(temp)  # Dead-end variable
    return metrics

# Misleading auxiliary function that looks important
def analyze_stability(data_map):
    stability_index = 0
    for k, v in data_map.items():
        if 'node' in k:
            stability_index += (v['squared'] % 17)
    # Complex but irrelevant calculation
    adjustment = math.sin(math.pi / 4) * len(data_map)
    fake_score = int(stability_index / (adjustment + 1))
    return fake_score  # Not used in final result

# Another red herring: network health simulation
def compute_health(nodes):
    healthy_count = 0
    checksum = 0
    for node_id, attrs in nodes.items():
        if attrs['raw'] > 128:
            healthy_count += 1
        checksum ^= attrs['raw']
    health_factor = healthy_count * 10 + (checksum % 8)
    return health_factor  # Computed but not used

# Core logic buried among distractions
def filter_outliers(log):
    values = [entry['raw'] for entry in log.values()]
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    threshold = mean_val + 1.5 * std_dev
    # Return only nodes below threshold (this actually matters)
    filtered = {k: v for k, v in log.items() if v['raw'] <= threshold}
    return filtered

# Decoy function using sets — looks relevant but isn't
def detect_anomalies(log):
    all_values = set(entry['raw'] for entry in log.values())
    expected_range = set(range(60, 200))
    anomalies = all_values - expected_range
    return anomalies  # Never used

# Real evaluation function — depends on prior filtering
def evaluate_performance(log, base_config):
    # Only some nodes are considered after outlier removal
    clean_log = filter_outliers(log)
    total_power = 0
    contribution_count = 0
    
    # Real logic starts here
    for node_id, attrs in clean_log.items():
        if attrs['active']:
            # Apply modular weighting based on binary pattern
            mod_weight = (attrs['raw'] % 13) + 1
            weighted_val = attrs['squared'] // mod_weight
            total_power += weighted_val
            contribution_count += 1
    
    # Baseline adjustment from config dictionary
    scaling_factor = base_config.get('scaling', 1.0)
    penalty_rate = base_config.get('penalty', 0.1)
    
    # Final score formula
    raw_score = total_power * scaling_factor
    adjusted_score = int(raw_score - (penalty_rate * raw_score))
    
    # Critical assignment point
    final_score = adjusted_score
    return final_score

# Orchestration with decoy calls
if __name__ == '__main__':
    # Collect real data
    metrics_log = collect_metrics()
    
    # Unused operations to distract
    _ = analyze_stability(metrics_log)
    _ = compute_health(metrics_log)
    _ = detect_anomalies(metrics_log)
    
    # Actual baseline configuration (dictionary usage)
    baseline = {
        'scaling': 0.85,
        'penalty': 0.12,
        'threshold_mode': 'adaptive',
        'debug_level': 99  # Unused field
    }
    
    # Key execution point
    final_score = evaluate_performance(metrics_log, baseline)
    print(f"Result: {final_score}")