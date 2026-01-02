from itertools import combinations

# System performance evaluation with mixed metrics

def analyze_response_times(times):
    if len(times) < 2:
        return 0
    avg = sum(times) / len(times)
    variance = sum((t - avg) ** 2 for t in times) / len(times)
    return round(avg + variance ** 0.5, 3)

def compute_efficiency_index(ops, memory):
    # Irrelevant efficiency calculation (distractor)
    base = ops / (memory + 1)
    penalty = 0
    for i in range(min(ops, 5)):
        penalty += i * 0.1
    return base - penalty

def extract_key_indicators(logs):
    # Parsing log data for relevant indicators
    counts = {'success': 0, 'warning': 0, 'error': 0}
    categories = []
    for log in logs:
        if 'ERROR' in log:
            counts['error'] += 1
            categories.append('error')
        elif 'WARN' in log:
            counts['warning'] += 1
            categories.append('warning')
        else:
            counts['success'] += 1
    
    # Distractor: unused transformation
    severity_pairs = list(combinations(categories, 2))
    critical_count = len([p for p in severity_pairs if 'error' in p])
    
    return counts, critical_count

def calculate_weighted_average(values, factors):
    # Unused helper (dead code path)
    total = sum(v * f for v, f in zip(values, factors))
    norm = sum(factors)
    return total / norm if norm else 0

def normalize_metrics(data):
    # Normalize metric values to [0,1] range
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def evaluate_stability_index(history):
    # Evaluate system stability over time
    changes = [abs(history[i+1] - history[i]) for i in range(len(history)-1)]
    if not changes:
        return 1.0
    fluctuation = sum(changes) / len(changes)
    return round(1 / (1 + fluctuation), 4)

def evaluate_performance(metrics, weights):
    # Core logic: evaluate overall performance score
    normalized = normalize_metrics(list(metrics.values()))
    weighted_sum = 0
    for i, key in enumerate(metrics.keys()):
        if key == 'latency':
            weighted_sum += normalized[i] * weights['latency'] * -1  # Invert latency
        elif key == 'throughput':
            weighted_sum += normalized[i] * weights['throughput']
        elif key == 'error_rate':
            weighted_sum += (1 - normalized[i]) * weights['error_rate']  # Invert error rate
    
    # Additional adjustment based on stability
    stability_log = [metrics['throughput'], metrics['latency'], metrics['error_rate']]
    stability_bonus = evaluate_stability_index(stability_log)
    
    # Final computation
    raw_score = weighted_sum + stability_bonus * weights.get('stability', 0.5)
    return int(round(raw_score * 100))

# Main execution block
if __name__ == "__main__":
    # Simulated monitoring data
    response_times = [120, 115, 130, 95, 140, 125, 110, 135]
    operation_count = 4850
    memory_usage = 768
    system_logs = [
        "INFO: Process started",
        "WARN: High latency detected",
        "INFO: Normal operation",
        "ERROR: Disk write failed",
        "WARN: Memory pressure",
        "INFO: Checkpoint saved"
    ]
    performance_history = [89, 92, 85, 94, 87, 91, 88]

    # Extract relevant metrics (some variables are distractions)
    avg_response = analyze_response_times(response_times)
    efficiency = compute_efficiency_index(operation_count, memory_usage)
    log_counts, high_severity_pairs = extract_key_indicators(system_logs)
    
    # Real metric collection
    raw_metrics = {
        'latency': avg_response,
        'throughput': operation_count / 100.0,
        'error_rate': log_counts['error'] / len(system_logs)
    }
    
    # Weight configuration (critical parameter)
    weights_config = {
        'latency': 0.3,
        'throughput': 0.4,
        'error_rate': 0.2,
        'stability': 0.1
    }
    
    # Distractor: unused combination analysis
    metric_values = list(raw_metrics.values())
    triplets = list(combinations(metric_values, 3)) if len(metric_values) >= 3 else []
    complexity_factor = len(triplets) * 0.05
    
    # Key statement
    final_score = evaluate_performance(raw_metrics, weights_config)
    
    # Print result as required
    print(f"Result: {final_score}")