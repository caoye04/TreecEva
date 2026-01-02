from collections import defaultdict
import itertools

# Simulate system performance metrics over time
def collect_metrics():
    timestamps = list(range(10))
    cpu_load = [0.45, 0.52, 0.61, 0.73, 0.68, 0.60, 0.55, 0.51, 0.49, 0.47]
    memory_usage = [0.62, 0.65, 0.67, 0.70, 0.72, 0.68, 0.64, 0.61, 0.59, 0.58]
    request_rate = [120, 135, 142, 150, 148, 140, 132, 128, 125, 123]
    
    metrics = defaultdict(dict)
    for t in timestamps:
        metrics[t]['cpu'] = cpu_load[t]
        metrics[t]['memory'] = memory_usage[t]
        metrics[t]['requests'] = request_rate[t]
        metrics[t]['latency'] = (request_rate[t] * 0.008) + (cpu_load[t] * 10)
    
    return metrics

# Baseline thresholds for normal operation
baseline = {
    'cpu_threshold': 0.65,
    'memory_threshold': 0.68,
    'latency_cap': 2.0,
    'min_requests': 130
}

# Analyze stability across consecutive intervals
def analyze_stability(metrics):
    stable_periods = 0
    temp_buffer = []
    for t in sorted(metrics.keys()):
        if (metrics[t]['cpu'] < baseline['cpu_threshold'] and 
            metrics[t]['memory'] < baseline['memory_threshold']):
            temp_buffer.append(t)
        else:
            if len(temp_buffer) >= 2:
                stable_periods += 1
            temp_buffer.clear()
    if len(temp_buffer) >= 2:
        stable_periods += 1
    return stable_periods

# Compute efficiency ratio (distractor function - not used in final score)
def compute_efficiency(metrics):
    total_load = sum(m['cpu'] for m in metrics.values())
    peak = max(m['requests'] for m in metrics.values())
    avg_latency = sum(m['latency'] for m in metrics.values()) / len(metrics)
    efficiency = (total_load * 0.7) / (avg_latency + 1) if avg_latency > 0 else 0
    return round(efficiency, 4)

# Core evaluation logic
def evaluate_performance(metrics, baseline):
    high_load_count = 0
    compliance_log = []
    recent_trends = []
    
    for t in sorted(metrics.keys()):
        # Relevant condition: high CPU and memory
        if (metrics[t]['cpu'] > baseline['cpu_threshold'] or 
            metrics[t]['memory'] > baseline['memory_threshold']):
            high_load_count += 1
        
        # Log compliance status (semi-relevant)
        is_compliant = (metrics[t]['latency'] <= baseline['latency_cap'])
        compliance_log.append(is_compliant)
        
        # Track trend in requests (distractor)
        if t > 0 and t < len(metrics) - 1:
            prev = metrics[t-1]['requests']
            curr = metrics[t]['requests']
            next_val = metrics[t+1]['requests']
            if prev < curr > next_val:  # local peak
                recent_trends.append(curr)
    
    # Actual scoring logic
    compliance_rate = sum(compliance_log) / len(compliance_log)
    base_score = 50 + (compliance_rate * 100)
    
    # Penalty for high load periods
    penalty = high_load_count * 3.5
    
    # Bonus for long stable sequences (uses helper)
    stability_bonus = analyze_stability(metrics) * 2.5
    
    # Final score calculation
    final_score = base_score - penalty + stability_bonus
    
    # Irrelevant transformation (distractor)
    transformed = [round((x - min(compliance_log)) / (max(compliance_log) - min(compliance_log) + 0.1), 2) 
                   for x in compliance_log]
    
    return round(final_score, 2)

# Execute workflow
metrics_data = collect_metrics()
efficiency_metric = compute_efficiency(metrics_data)  # Dead-end computation
final_score = evaluate_performance(metrics_data, baseline)
print(f"Result: {final_score}")