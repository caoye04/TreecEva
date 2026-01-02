def analyze_signal(samples):
    # Irrelevant signal processing computations
    filtered = [x * 0.9 for x in samples]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    peak = max(smoothed) if smoothed else 0
    baseline = sum(smoothed[:5]) / 5 if len(smoothed) >= 5 else 0
    deviation = peak - baseline
    return deviation  # Unused return

def preprocess_metrics(raw):
    # Distractor: data normalization that isn't used later
    normalized = {}
    for k, v in raw.items():
        if v > 0:
            normalized[k] = round((v - min(raw.values())) / (max(raw.values()) - min(raw.values()) + 1e-8), 3)
        else:
            normalized[k] = 0
    temp_result = {k: v * 1.1 for k, v in normalized.items()}
    return temp_result  # Dead path: not used in main logic

def calculate_efficiency(tasks):
    total_work = sum([t['effort'] for t in tasks])
    total_time = sum([t['duration'] for t in tasks])
    if total_time == 0:
        return 0
    return total_work / total_time

def evaluate_performance(metrics, config):
    # Core logic hidden among distractions
    base = metrics.get('throughput', 0)
    penalty = 0
    
    # Red herring: complex condition with partial impact
    if metrics.get('latency') > config['latency_threshold']:
        penalty += 15
    if metrics.get('retries') > config['retry_limit']:
        penalty += 10
    
    # Actual key computation
    score = base * 100
    
    # Misleading adjustment
    adjustment = (metrics.get('errors', 0) * -5) + (metrics.get('warnings', 0) * -2)
    score += adjustment
    
    # Conditional override that only triggers under specific conditions
    if metrics.get('consistency') >= config['consistency_floor']:
        score = score * 1.1  # Bonus applied only if consistent
    
    # Dead code branch with fake importance
    if metrics.get('debug_mode', False):
        debug_log = []
        for i in range(5):
            debug_log.append(f"Debug step {i}: {score % (i+1) if i != 0 else 0}")
        # This entire block is irrelevant

    return int(score) - penalty  # Final scoring formula

# Main execution
if __name__ == "__main__":
    # Simulated input data
    metric_data = {
        'throughput': 47,
        'latency': 120,
        'retries': 3,
        'errors': 4,
        'warnings': 6,
        'consistency': 0.87,
        'debug_mode': True
    }

    thresholds = {
        'latency_threshold': 100,
        'retry_limit': 5,
        'consistency_floor': 0.85
    }

    # Irrelevant preprocessing chain
    raw_values = {'a': 10, 'b': 20, 'c': 15}
    interim = preprocess_metrics(raw_values)
    signal_samples = [100, 105, 98, 110, 108, 103, 99]
    signal_deviation = analyze_signal(signal_samples)

    # Task efficiency (unused)
    task_list = [
        {'effort': 40, 'duration': 8},
        {'effort': 60, 'duration': 10},
        {'effort': 50, 'duration': 5}
    ]
    efficiency = calculate_efficiency(task_list)

    # Critical assignment - this is where the answer comes from
    final_score = evaluate_performance(metric_data, thresholds)

    # Output result as required
    print(f"Result: {final_score}")
