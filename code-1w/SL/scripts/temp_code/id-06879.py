import math

# Simulated system performance metrics (some are red herrings)
def get_system_metrics():
    raw_data = {
        'latency_ms': 120,
        'throughput_ops': 450,
        'cpu_util': 78.5,
        'mem_usage_mb': 2048,
        'disk_iops': 320,
        'error_rate': 0.003,
        'network_latency_ms': 45,
        'cache_hit_ratio': 0.88,
        'power_draw_watts': 150,  # irrelevant metric
        'temperature_c': 67       # irrelevant metric
    }
    return raw_data

# Legacy function - never called but looks important
def calculate_efficiency_rating(data):
    efficiency = (data['throughput_ops'] * data['cache_hit_ratio']) / (data['power_draw_watts'] + 1)
    return round(efficiency, 2)

# Weighted scoring using lambda for dynamic thresholds
evaluate_dimension = lambda val, threshold: 10 if val >= threshold else (5 if val >= threshold * 0.7 else 2)

# Core evaluation logic with distractors
def preprocess_metrics(metrics):
    processed = {}
    
    # Relevant transformations
    processed['response_time'] = max(10, 100 - metrics['latency_ms'] // 2)  # scaled inverse latency
    processed['load_handling'] = min(10, metrics['throughput_ops'] / 50)     # throughput score
    processed['stability'] = 10 if metrics['error_rate'] < 0.01 else 3
    
    # Distractor computations (unused)
    energy_waste = metrics['power_draw_watts'] * 24 * 365  # annual consumption - unused
    thermal_factor = metrics['temperature_c'] ** 2          # made-up thermal index - unused
    hypothetical_savings = math.log(energy_waste) if energy_waste > 1000 else 0.0  # dead code path
    
    # More relevant scores
    processed['resource_efficiency'] = evaluate_dimension(metrics['cpu_util'], 80)
    processed['iops_score'] = evaluate_dimension(metrics['disk_iops'], 300)
    processed['network_score'] = evaluate_dimension(metrics['network_latency_ms'], 50)
    
    # Dummy entries to mislead
    processed['deprecated_flag'] = False
    processed['legacy_mode'] = None
    
    return processed

def apply_normalization(scores, method='standard'):
    # Normalization not actually applied; only certain fields used later
    normalized = {}
    for k, v in scores.items():
        if isinstance(v, (int, float)) and k not in ['deprecated_flag', 'legacy_mode']:
            if method == 'standard':
                normalized[k] = round((v - 2) / 8 * 10, 2)  # rescale to 0-10
            elif method == 'aggressive':
                normalized[k] = max(0, v - 1)  # alternate scaling - unused
        else:
            normalized[k] = v
    # This function appears critical but most results are ignored later
    return normalized

def filter_relevant_dimensions(score_dict):
    # Only extract keys we actually use in final calculation
    key_dims = ['response_time', 'load_handling', 'stability', 'iops_score']
    return {k: score_dict[k] for k in key_dims}

def evaluate_performance(metrics, weights):
    # Preprocess all metrics (many will be discarded)
    prep = preprocess_metrics(metrics)
    norm = apply_normalization(prep)  # result partially ignored
    
    # Extract only a subset
    core = filter_relevant_dimensions(norm)
    
    # Irrelevant debugging block (dead code path)
    debug_mode = False
    if debug_mode:
        print("Debug:", {k: v for k, v in core.items()})
        temp_report = [f'{k}:{v}' for k, v in core.items() if 'score' in k]
        log_entry = ';'.join(temp_report)

    # Actual computation uses only specific components
    weighted_sum = (
        core['response_time'] * weights['time'] +
        core['load_handling'] * weights['load'] +
        core['stability'] * weights['stable'] +
        core['iops_score'] * weights['iops']
    )
    total_weight = sum(weights[w] for w in ['time', 'load', 'stable', 'iops'])
    
    # Final score is average, rounded to nearest integer
    final_raw = weighted_sum / total_weight
    final_score = int(round(final_raw))
    
    # Many variables introduced above are distractions
    return final_score

# Misleading auxiliary dictionary (looks like configuration)
system_profiles = {
    'high_perf': {'priority': 'throughput', 'tolerance': 0.005},
    'low_power': {'priority': 'efficiency', 'tolerance': 0.02},
    'balanced': {'priority': 'mixed', 'tolerance': 0.01}
}

# Weights used in evaluation (only this matters)
weights_config = {
    'time': 0.3,
    'load': 0.25,
    'stable': 0.35,
    'iops': 0.1
    # Note: 'network', 'energy', 'thermal' weights missing intentionally
}

# Execution flow
metrics_data = get_system_metrics()

# Unused transformation paths
snapshot_log = [metrics_data['latency_ms'], metrics_data['throughput_ops']]
duplicate_check = set(snapshot_log)  # looks important, isn't used

# Key execution point
final_score = evaluate_performance(metrics_data, weights_config)

print(f"Result: {final_score}")