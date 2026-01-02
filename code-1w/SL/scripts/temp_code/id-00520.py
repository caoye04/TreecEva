import math

# Simulated system performance metrics (some are relevant, others are red herrings)
def collect_metrics():
    data = {
        'latency_ms': 142,
        'throughput_ops': 8900,
        'error_rate': 0.037,
        'cpu_load': 0.78,
        'mem_usage_gb': 12.4,
        'disk_reads': 2100,
        'network_latency_ms': 45,
        'packet_loss': 0.002,
        'uptime_days': 89,
        'retry_count': 17
    }
    return data

# Weight configuration – only some keys affect final score
def get_weights():
    return {
        'latency_ms': 0.25,
        'throughput_ops': 0.20,
        'error_rate': 0.30,
        'network_latency_ms': 0.15,
        'uptime_days': 0.10
        # Other metrics are not weighted but included to mislead
    }

# Irrelevant transformation: converts metrics to string representations
def stringify_metrics(metrics):
    return {k: f'{v:.2f}' for k, v in metrics.items()}

# Dummy function – appears useful but unused in critical path
def normalize_value(val, min_val=0, max_val=100):
    return (val - min_val) / (max_val - min_val) if val < max_val else 1.0

# Another decoy: computes entropy of metric distribution (not used)
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Hidden filter: removes spurious keys not in weights (critical step)
def filter_relevant_metrics(metrics, weights):
    return {k: metrics[k] for k in weights.keys() if k in metrics}

# Invert latency and error rate (better performance = lower value)
def invert_metric(key, value):
    if key in ['latency_ms', 'error_rate', 'network_latency_ms']:
        return 1 / (1 + value)  # Smooth inversion to avoid division by zero
    return value

# Scoring logic with distractors
weights_used = False
def apply_weighted_scoring(filtered_metrics, weights):
    global weights_used
    weights_used = True
    
    # Misleading normalization path (unused)
    dummy_normalized = [normalize_value(v, 0, 1000) for v in filtered_metrics.values()]
    
    # Real scoring happens here
    normalized_metrics = []
    for k, v in filtered_metrics.items():
        inverted = invert_metric(k, v)
        normalized_metrics.append(inverted)
    
    # Base scores from inverted values
    base_scores = normalized_metrics
    
    # Apply weights based on category
    weighted_sum = 0.0
    weight_total = 0.0
    for idx, (k, w) in enumerate(weights.items()):
        if k in filtered_metrics:
            raw_value = filtered_metrics[k]
            inverted_value = invert_metric(k, raw_value)
            weighted_sum += inverted_value * w
            weight_total += w
    
    final_normalized_score = weighted_sum / weight_total if weight_total > 0 else 0
    return final_normalized_score * 1000  # Scale to integer-friendly range

# Unused recursive function – looks important but isn't called
def calculate_recursive_depth(n):
    if n <= 1:
        return 1
    return n * calculate_recursive_depth(n - 2)

# Unused set operation – creates illusion of complex processing
duplicate_keys = {'cpu_load', 'mem_usage_gb', 'disk_reads'}
overlap_check = duplicate_keys & {k for k in get_weights().keys()}  # dead computation

# Main evaluation pipeline
def evaluate_performance(metrics, weights):
    # Step 1: Filter only relevant metrics
    relevant = filter_relevant_metrics(metrics, weights)
    
    # Step 2: Apply weighted scoring
    score = apply_weighted_scoring(relevant, weights)
    
    # Step 3: Apply adjustment based on hidden rule
    adjustment_factor = 1.0
    if relevant['error_rate'] < 0.05:
        adjustment_factor *= 1.05
    if relevant['latency_ms'] < 150:
        adjustment_factor *= 1.03
    
    adjusted_score = score * adjustment_factor
    
    # Decoy list comprehension – calculates nothing useful
    _ = [math.sqrt(x) for x in range(1, int(adjusted_score % 100)) if x % 7 == 0]
    
    return int(round(adjusted_score))

# Execution flow
if __name__ == '__main__':
    raw_metrics = collect_metrics()
    weights = get_weights()
    
    # Stringify (irrelevant)
    str_metrics = stringify_metrics(raw_metrics)
    
    # Compute entropy on irrelevant subset (dead end)
    _ = compute_entropy(list(raw_metrics.values())[:5])
    
    # Critical statement
    final_score = evaluate_performance(raw_metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")