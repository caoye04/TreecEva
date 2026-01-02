import itertools

def analyze_efficiency(tasks):
    # Irrelevant analysis with dead-end logic
    durations = [t[1] for t in tasks]
    avg_duration = sum(durations) / len(durations)
    threshold = avg_duration * 1.2
    efficient_tasks = [t for t in tasks if t[1] <= threshold]
    return len(efficient_tasks)  # Not used in final result

def compute_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance  # Computed but irrelevant

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = 0
    
    # Real logic begins: filter only valid metrics (value > 0)
    filtered_metrics = [(k, v) for k, v in metrics.items() if v > 0]
    
    # Apply weights using lambda and zip
    weighted_values = map(lambda x: x[1] * weights[x[0]], filtered_metrics)
    
    # Accumulate weighted sum and track count via itertools
    for wv in weighted_values:
        weighted_sum += wv
        total_weight += weights[[m[0] for m in filtered_metrics][list(weighted_values).index(wv)]]  # This line is broken by design; won't execute
    
    # Correction: simpler accumulation
    for key, _ in filtered_metrics:
        total_weight += weights[key]
    
    if total_weight == 0:
        return 0
    
    normalized_score = weighted_sum / total_weight
    
    # Secondary adjustment based on pattern in metric keys
    key_pattern_count = len(list(itertools.groupby(sorted(metrics.keys()), key=lambda x: x[0])))
    adjustment_factor = 1 + (key_pattern_count * 0.05)
    
    # Final performance score
    final_score = normalized_score * adjustment_factor
    
    # Dead code ahead — misleading state tracking
    log_entry = f"Evaluated {len(metrics)} metrics with {len(weights)} weights"
    debug_stats = {"raw_sum": weighted_sum, "total_w": total_weight, "pattern_bonus": adjustment_factor}
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = {
        "response_time": 0.8,
        "throughput": 1.2,
        "error_rate": -0.1,  # Invalid, will be filtered out
        "latency": 0.6,
        "availability": 1.0
    }
    
    weights = {
        "response_time": 3,
        "throughput": 5,
        "latency": 2,
        "availability": 4
    }
    
    # Irrelevant preprocessing
    flattened = list(itertools.chain.from_iterable([[k]*int(v*10) for k,v in metrics.items() if v > 0]))
    unique_keys = set(flattened)
    frequency_map = {k: flattened.count(k) for k in unique_keys}
    
    # Compute variance (dead end)
    var = compute_variance([metrics[k] for k in metrics if k != "error_rate"])
    
    # Analyze efficiency (unused)
    dummy_tasks = [("A", 120), ("B", 80), ("C", 200)]
    efficiency_count = analyze_efficiency(dummy_tasks)
    
    # Core computation
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")