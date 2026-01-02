import itertools

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    return {
        'latency_ms': 120,
        'throughput_ops': 850,
        'error_rate': 0.035,
        'cpu_util': 78.2,
        'memory_mb': 4120,
        'disk_io_ops': 230,
        'network_latency_ms': 45,
        'packet_loss': 0.0012
    }

# Irrelevant helper: computes harmonic mean (not used in final calculation)
def harmonic_mean(data):
    if not data:
        return 0
    return len(data) / sum(1/x for x in data if x > 0)

# Decoy function: looks important but unused
def calculate_reliability_score(metrics):
    base = metrics['error_rate'] * 100
    penalty = metrics['packet_loss'] * 5000
    return max(0, 100 - base - penalty)

# Misleading transformation: processes only part of the data
def transform_for_visualization(metrics):
    transformed = {}
    for k, v in metrics.items():
        if 'latency' in k:
            transformed[k] = round(v * 0.95, 2)
        elif 'ops' in k:
            transformed[k] = int(v * 1.05)
        else:
            transformed[k] = round(v * 1.1, 2)
    return transformed

# Real weighting logic (obscured by noise)
WEIGHT_PROFILES = {
    'balanced': [0.2, 0.2, 0.15, 0.15, 0.1, 0.1, 0.05, 0.05],
    'performance': [0.3, 0.25, 0.05, 0.1, 0.05, 0.05, 0.1, 0.15]
}

# Critical function buried among distractions
def evaluate_performance(metrics, profile_key='balanced'):
    keys_in_order = [
        'latency_ms', 'throughput_ops', 'error_rate', 'cpu_util',
        'memory_mb', 'disk_io_ops', 'network_latency_ms', 'packet_loss'
    ]
    
    # Normalize and invert where necessary (lower is better for latency/error)
    normalized = []
    for key in keys_in_order:
        value = metrics[key]
        if key in ['latency_ms', 'error_rate', 'packet_loss', 'network_latency_ms']:
            # Invert: convert to benefit score (higher is better)
            if 'latency' in key:
                norm_val = max(0, (200 - value) / 200)  # assuming max 200ms is acceptable
            elif key == 'error_rate':
                norm_val = max(0, (0.1 - value) / 0.1)
            elif key == 'packet_loss':
                norm_val = max(0, (0.01 - value) / 0.01)
            else:
                norm_val = value / 100.0
        else:
            # Direct scaling (higher is better)
            if key == 'throughput_ops':
                norm_val = min(value / 1000.0, 1.0)
            elif key == 'cpu_util':
                norm_val = (100 - abs(75 - value)) / 100  # optimal at 75%
            elif key == 'memory_mb':
                norm_val = min(value / 8000.0, 1.0)  # assume 8GB max relevant
            elif key == 'disk_io_ops':
                norm_val = min(value / 500.0, 1.0)
        normalized.append(max(0.0, min(1.0, norm_val)))
    
    weights = WEIGHT_PROFILES[profile_key]
    
    # Apply weighted sum
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    
    # Additional adjustment based on consistency across metrics
    variation = sum(abs(a - b) for a, b in itertools.pairwise(normalized)) / len(normalized)
    stability_bonus = max(0, 0.1 - variation * 0.05)
    
    final_score = round(weighted_sum + stability_bonus, 6)
    
    # Dead code branch: never executed due to fixed profile_key
    if profile_key == 'invalid_case':
        final_score *= 0.5  # decoy penalty
    
    return final_score

# Unused list comprehension red herring
dummy_aggregates = [sum(1 for x in collect_metrics().values() if x > threshold) for threshold in [100, 500, 1000]]

# Main execution flow
if __name__ == "__main__":
    raw_metrics = collect_metrics()
    
    # Distractor: transform but don't use
    viz_data = transform_for_visualization(raw_metrics)
    
    # Another distractor call
    _ = harmonic_mean([raw_metrics['latency_ms'], raw_metrics['network_latency_ms']])
    
    # Key statement
    final_score = evaluate_performance(raw_metrics, 'balanced')
    
    # Irrelevant filtering operation
    significant_keys = [k for k, v in raw_metrics.items() if v > 100 and 'ops' not in k and 'rate' not in k]
    
    print(f"Result: {final_score}")