from collections import defaultdict, Counter

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [
        ('cpu', [0.6, 0.7, 0.8, 0.9, 0.95]),
        ('memory', [0.4, 0.55, 0.65, 0.7, 0.8]),
        ('disk', [0.3, 0.4, 0.35, 0.5, 0.6]),
        ('network', [0.2, 0.25, 0.3, 0.35, 0.4])
    ]
    
    metrics = defaultdict(list)
    for k, v in raw_data:
        metrics[k] = v
        metrics[f'{k}_avg'] = sum(v) / len(v)
    
    # Irrelevant aggregation
    temp_snapshot = {key: values[-1] for key, values in metrics.items() if isinstance(values, list)}
    metrics['snapshot'] = temp_snapshot
    
    return metrics

# Baseline thresholds for normal operation
def get_baseline():
    return {
        'cpu': 0.75,
        'memory': 0.6,
        'disk': 0.4,
        'network': 0.3
    }

# Auxiliary function to compute anomaly counts
def count_anomalies(data, threshold):
    anomalies = 0
    for val in data:
        if val > threshold * 1.2:
            anomalies += 1
    return anomalies

# Helper: normalize score between 0 and 100
def normalize(val, min_val=0, max_val=1):
    return 100 * (val - min_val) / (max_val - min_val)

# Main evaluation logic
def evaluate_performance(metrics, baseline):
    scores = []
    debug_weights = []
    
    for component in ['cpu', 'memory', 'disk', 'network']:
        series = metrics[component]
        avg = metrics[f'{component}_avg']
        base = baseline[component]
        
        # Primary scoring based on average utilization vs baseline
        if avg <= base:
            quality = 1.0
        elif avg <= base * 1.1:
            quality = 0.8
        elif avg <= base * 1.2:
            quality = 0.6
        else:
            quality = 0.4
        
        # Anomaly penalty
        anomaly_count = count_anomalies(series, base)
        penalty = 0.1 * anomaly_count
        adjusted_quality = max(quality - penalty, 0.2)
        
        # Normalize component score
        normalized = normalize(adjusted_quality, 0.2, 1.0)
        scores.append(normalized)
        
        # Distractor: weight logging (not used in final calculation)
        weight = 1.0 if component in ['cpu', 'memory'] else 0.8
        debug_weights.append(weight)
    
    # Aggregate total score
    total = sum(scores)
    
    # Secondary metric: stability check via variance approximation (distractor)
    stabilities = []
    for comp in ['cpu', 'memory']:
        vals = metrics[comp]
        mean_val = sum(vals) / len(vals)
        var = sum((x - mean_val) ** 2 for x in vals) / len(vals)
        stable = 1 if var < 0.02 else 0.5
        stabilities.append(stable)
    
    # Bonus only if both CPU and memory are stable
    stability_bonus = 10 if all(s >= 1 for s in stabilities) else 0
    
    # Final computation
    raw_final = total + stability_bonus
    
    # Apply artificial cap and scale
    capped = min(raw_final, 95.0)
    final_score = round(capped, 2)
    
    # Dead code branch - never executed due to prior cap
    if final_score > 100:
        final_score = 100
    
    return final_score

# Additional unused helper (dead code path)
def analyze_trends(data_list):
    trend_summary = Counter()
    for seq in data_list:
        increases = sum(1 for i in range(1, len(seq)) if seq[i] > seq[i-1])
        trend_summary['up'] += increases
    return trend_summary

# Execution flow
if __name__ == '__main__':
    metrics = collect_metrics()
    baseline = get_baseline()
    
    # Key statement
    final_score = evaluate_performance(metrics, baseline)
    
    # Extract specific window for secondary validation (irrelevant to final score)
    cpu_recent = metrics['cpu'][-3:]
    memory_slice = metrics['memory'][1::2]
    
    # Print result as required
    print(f"Result: {final_score}")