from collections import defaultdict
import itertools

# Simulate system health metrics over time
def collect_metrics():
    data_stream = [
        (1, 'cpu', 75), (2, 'memory', 80), (3, 'cpu', 60),
        (4, 'disk', 90), (5, 'network', 30), (6, 'cpu', 85),
        (7, 'memory', 88), (8, 'disk', 70), (9, 'cpu', 55)
    ]
    
    metrics = defaultdict(list)
    for timestamp, component, value in data_stream:
        metrics[component].append(value)
    
    return dict(metrics)

# Analyze trends with irrelevant auxiliary computations
def analyze_trends(metrics):
    trend_summary = {}
    volatility_index = 0
    total_components = 0
    
    for comp, values in metrics.items():
        if len(values) > 1:
            diffs = [abs(a - b) for a, b in zip(values, values[1:])]
            avg_diff = sum(diffs) / len(diffs)
            # Irrelevant but plausible calculation
            squared_impact = sum(d ** 2 for d in diffs) / len(diffs)
            trend_summary[comp] = {'stability': 100 - avg_diff, 'noise': squared_impact}
            volatility_index += avg_diff
        else:
            trend_summary[comp] = {'stability': 100, 'noise': 0}
        total_components += 1
    
    # Dead computation - not used later
    if total_components > 0:
        global_volatility = volatility_index / total_components
    
    return trend_summary

# Evaluate performance against baseline with distraction logic
def evaluate_performance(metrics, baseline):
    # Extract only CPU and memory for actual evaluation
    relevant_components = ['cpu', 'memory']
    score = 0
    penalty_adjustment = 0.0
    
    # Complex slicing to simulate windowed analysis
    cpu_history = metrics.get('cpu', [])
    recent_cpu = cpu_history[-3:] if len(cpu_history) >= 3 else cpu_history
    
    # Actual scoring logic
    for comp in relevant_components:
        values = metrics.get(comp, [])
        if values:
            avg_load = sum(values) / len(values)
            if avg_load > baseline[comp]:
                score -= int((avg_load - baseline[comp]) * 2)
            else:
                score += 10
    
    # Distractor: elaborate disk analysis that doesn't affect final score
    disk_values = metrics.get('disk', [])
    if disk_values:
        max_disk = max(disk_values)
        disk_trend = 'critical' if max_disk > 85 else 'stable'
        # Simulated early warning system (unused)
        alerts = list(itertools.dropwhile(lambda x: x < 85, sorted(disk_values)))
        alert_count = len(alerts)
        # This entire block is irrelevant to final_score
        if alert_count > 0:
            temp_correction = alert_count * 0.5
            penalty_adjustment += temp_correction  # never applied
    
    # Another red herring: network jitter simulation
    network_vals = metrics.get('network', [])
    if len(network_vals) > 1:
        jitter = sum(abs(a - b) for a, b in zip(network_vals, network_vals[1:]))
        normalized_jitter = jitter / (max(network_vals) + 1)
        score -= int(normalized_jitter)  # looks meaningful but skews irrelevantly
    
    # Final adjustment based on CPU stability (key part)
    if recent_cpu:
        peak_pressure = max(recent_cpu)
        if peak_pressure > 80:
            score -= 15
    
    final_score = score + 50  # Base offset to ensure positive result
    return final_score

# Driver code
if __name__ == '__main__':
    metrics = collect_metrics()
    baseline = {'cpu': 70, 'memory': 85, 'disk': 75}  # Baseline thresholds
    trends = analyze_trends(metrics)  # Called but result unused
    final_score = evaluate_performance(metrics, baseline)
    print(f"Result: {final_score}")