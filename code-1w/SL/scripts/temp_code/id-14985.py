import math

# Simulated system performance metrics (some are relevant, others are red herrings)
def collect_diagnostics():
    return {
        'latency_ms': 42.5,
        'cpu_load': 0.78,
        'memory_usage_mb': 1024,
        'cache_hit_ratio': 0.88,
        'request_rate_per_sec': 230,
        'error_count': 3,
        'retry_count': 7,
        'packet_loss_percent': 0.02,
        'thread_count': 16,
        'disk_io_ops': 128
    }

def calculate_efficiency_index(raw_metrics):
    # Irrelevant computation - distractor
    base = raw_metrics['latency_ms'] * raw_metrics['cpu_load']
    overhead = math.log(raw_metrics['memory_usage_mb'])
    return (base / overhead) * 100

def assess_stability_factor(diag_data):
    # Another misleading intermediate calculation
    if diag_data['error_count'] == 0:
        return 1.0
    else:
        penalty = diag_data['retry_count'] / (diag_data['error_count'] + 1)
        return max(0.1, 1.0 - penalty * 0.05)

def derive_signal_strength(diag_map):
    # Decoy function with complex but unused logic
    raw_value = diag_map['request_rate_per_sec'] * (1 - diag_map['packet_loss_percent'])
    adjusted = raw_value ** 0.5
    if adjusted > 100:
        for i in range(3):
            adjusted = math.sin(adjusted) + adjusted // 10
    return adjusted

def normalize_metric(value, min_val, max_val):
    # Useful utility used later
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.0

def compute_health_vector(metrics_dict):
    # Partially relevant transformation
    vector = {}
    vector['norm_latency'] = normalize_metric(metrics_dict['latency_ms'], 10, 100)
    vector['norm_requests'] = normalize_metric(metrics_dict['request_rate_per_sec'], 50, 500)
    vector['norm_cache'] = normalize_metric(metrics_dict['cache_hit_ratio'], 0.5, 1.0)
    vector['temp_debug'] = vector['norm_latency'] * 1000  # Red herring value
    return vector

def apply_weighted_sum(components, weights):
    # Core calculation buried among noise
    total = 0.0
    for key in weights:
        if key in components:
            total += components[key] * weights[key]
    return total

def evaluate_performance(met, weights):
    # This function contains the critical path
    health = compute_health_vector(met)
    
    # Irrelevant branching - distracts from main flow
    if met['thread_count'] > 8:
        debug_snapshot = [met['disk_io_ops'] << 2, met['cpu_load'] * 256]
        temp_result = debug_snapshot[0] ^ int(debug_snapshot[1])
        _ = temp_result & 0xFF  # Dead computation
    
    # Actual important work happens here
    score = apply_weighted_sum(health, weights)
    
    # Misleading adjustment that looks important but doesn't affect final output
    if met['error_count'] < 5:
        simulated_prediction = []
        for i in range(5):
            simulated_prediction.append(math.cos(i * score))
        moving_avg = sum(simulated_prediction[-3:]) / 3
        _ = round(moving_avg, 4)  # Unused result
    
    return int(round(score * 100))  # Final conversion to integer score

# Main execution block
if __name__ == '__main__':
    # Collect real metrics
    system_metrics = collect_diagnostics()
    
    # Define benchmark weights (only keys matching health vector will matter)
    benchmark_weights = {
        'norm_latency': 0.4,
        'norm_requests': 0.35,
        'norm_cache': 0.25
    }
    
    # Irrelevant preprocessing - creates distraction
    raw_keys = [k for k in system_metrics.keys() if 'count' in k or 'rate' in k]
    summary_stats = {key: system_metrics[key] for key in raw_keys}
    aggregated = sum(summary_stats.values())
    _ = aggregated / len(summary_stats) if summary_stats else 0  # Unused aggregate
    
    # Compute various decoy indicators
    efficiency = calculate_efficiency_index(system_metrics)
    stability = assess_stability_factor(system_metrics)
    signal = derive_signal_strength(system_metrics)
    
    # These variables look important but aren't used in final score
    diagnostic_fingerprint = (
        int(system_metrics['cpu_load'] * 100) ^
        system_metrics['thread_count'] ^
        int(signal)
    )
    
    # Critical line: this determines the answer
    final_score = evaluate_performance(system_metrics, benchmark_weights)
    
    # Print result as required
    print(f"Result: {final_score}")