import itertools

# Simulated system performance metrics from a distributed computing environment
def collect_metrics():
    raw_data = [120, 85, 90, 70, 110, 95]
    processed = [x * 0.95 for x in raw_data]
    outliers = [x for x in processed if x < 80]
    filtered = [x for x in processed if x >= 80]  # Remove outliers
    return {
        'latency': sum(filtered) / len(filtered),
        'throughput': sum(raw_data),
        'error_rate': len(outliers),
        'peak_load': max(raw_data),
        'baseline': 88
    }

# Irrelevant auxiliary function - dead code path (distractor)
def analyze_network_traffic(logs):
    total_packets = 0
    suspicious_ips = set()
    for entry in logs:
        total_packets += entry.get('size', 0)
        if entry.get('anomaly'):
            suspicious_ips.add(entry['ip'])
    return len(suspicious_ips)

# Another decoy: system health check with no impact on final result
def system_health_check():
    temperatures = [68, 72, 75, 69, 74]
    avg_temp = sum(temperatures) / len(temperatures)
    threshold_exceeded = any(t > 73 for t in temperatures)
    status = 'WARNING' if threshold_exceeded else 'OK'
    return {'avg_temp': avg_temp, 'status': status}

# Core logic disguised among distractions
def apply_calibration(data, mode='standard'):
    calibrated = {}
    for k, v in data.items():
        if k == 'latency':
            calibrated[k] = v * 0.88 if mode == 'aggressive' else v * 0.93
        elif k == 'throughput':
            calibrated[k] = v * 1.07
        elif k == 'error_rate':
            calibrated[k] = max(0, v - 1)
        else:
            calibrated[k] = v
    return calibrated

# Bit manipulation red herring (unused but plausible)
def scramble_key(value):
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return (toggled >> 2) | (value << 6)

# Conditional expression and set operations used meaningfully
def adjust_for_variance(metrics):
    keys_needed = {'latency', 'throughput', 'error_rate'}
    provided = set(metrics.keys())
    missing = keys_needed - provided
    
    base_latency = metrics['latency'] if 'latency' in metrics else 100
    base_throughput = metrics['throughput'] if 'throughput' in metrics else 500
    base_error = metrics['error_rate'] if 'error_rate' in metrics else 2
    
    adjusted_latency = base_latency * (0.97 if base_throughput > 500 else 1.02)
    penalty_factor = 1.1 if missing else 1.0
    
    # Use conditional expression with itertools to simulate load distribution
    simulated_loads = list(itertools.accumulate([1, 2, 1, 3, 2], lambda x, y: x + y * 0.5))
    load_factor = sum(simulated_loads) / 5
    
    return {
        'adjusted_latency': adjusted_latency * load_factor * penalty_factor,
        'adjusted_throughput': base_throughput / load_factor,
        'adjusted_error': base_error * penalty_factor
    }

# Main evaluation logic buried in abstraction
benchmark_weights = {
    'latency': 0.4,
    'throughput': 0.35,
    'error_rate': 0.25
}

def evaluate_performance(metrics, weights):
    calibrated = apply_calibration(metrics, mode='standard')
    adjusted = adjust_for_variance(calibrated)
    
    # Final scoring formula
    latency_score = 100 - (adjusted['adjusted_latency'] - 80)
    throughput_score = min(adjusted['adjusted_throughput'] / 10, 100)
    error_score = max(0, 100 - (adjusted['adjusted_error'] * 20))
    
    # Weighted composite score
    score = (
        latency_score * weights['latency'] +
        throughput_score * weights['throughput'] +
        error_score * weights['error_rate']
    )
    
    # Decoy calculation that looks important but isn't used
    secondary_metric = (latency_score + throughput_score) / 2 * (1 - adjusted['adjusted_error'] / 100)
    
    return int(round(score))

# Orchestration with irrelevant steps
if __name__ == '__main__':
    # Collect real metrics
    raw_metrics = collect_metrics()
    
    # Run unrelated diagnostics (distractors)
    network_logs = [
        {'ip': '192.168.1.10', 'size': 1500, 'anomaly': False},
        {'ip': '10.0.0.5', 'size': 1200, 'anomaly': True},
    ]
    analyze_network_traffic(network_logs)  # Dead call
    system_health_check()  # Dead call
    
    # Apply meaningful transformations
    final_score = evaluate_performance(raw_metrics, benchmark_weights)
    
    # Print required result
    print(f"Result: {final_score}")