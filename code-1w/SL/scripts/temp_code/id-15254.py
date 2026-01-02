import math

# Simulated system performance metrics
def collect_diagnostics():
    return {
        'cpu_load': 78,
        'memory_usage': 65,
        'disk_io': 43,
        'network_latency': 21,
        'temperature': 67
    }

def calculate_efficiency_index(load, mem):
    # Irrelevant efficiency calculation (red herring)
    base = (100 - load) * 0.6 + (100 - mem) * 0.4
    penalty = 0.1 * max(0, load - 80)
    return round(base - penalty, 2)

def analyze_trend(data_list):
    # Dead code path - never used in main logic
    if len(data_list) < 2:
        return 0
    return sum([b - a for a, b in zip(data_list[:-1], data_list[1:])])

def validate_thresholds(diag):
    # Distractor function: checks safety but not used in final score
    alerts = []
    if diag['cpu_load'] > 90:
        alerts.append('CPU_HIGH')
    if diag['temperature'] > 75:
        alerts.append('OVERHEAT')
    return alerts

def normalize_metric(value, min_val=0, max_val=100):
    # Utility function used in scoring
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))

def compute_health_factor(metrics):
    # Another decoy health score (not used in final result)
    weights = {'cpu_load': 0.3, 'memory_usage': 0.25, 'disk_io': 0.15, 'network_latency': 0.2, 'temperature': 0.1}
    score = 0
    for k, w in weights.items():
        normalized_inv = 1 - normalize_metric(metrics[k])
        score += normalized_inv * w * 100
    return round(score, 1)

def filter_outliers(data_dict, threshold=95):
    # Unused data filtering routine (misleading)
    filtered = {}
    for k, v in data_dict.items():
        if v <= threshold:
            filtered[k] = v
    return filtered

def evaluate_performance(m, weights):
    # Core logic: compute weighted performance score
    temp_score = 0
    for metric, weight in weights.items():
        if metric == 'response_time':
            # Special handling for response time (inverted)
            normalized = 1 - normalize_metric(m.get('network_latency'), 0, 50)
        else:
            # Most metrics: lower raw value is better, so invert normalized usage
            raw = m.get(metric.split('_')[0], 0)  # assume prefix matches key
            normalized = 1 - normalize_metric(raw)
        temp_score += normalized * weight
    
    # Apply non-linear boost for balanced performance
    metric_values = [m['cpu_load'], m['memory_usage'], m['disk_io'], m['network_latency']]
    variance_penalty = (max(metric_values) - min(metric_values)) * 0.005
    temp_score -= variance_penalty
    
    # Final scaling to 0-100 range
    return int(round(temp_score * 100, 0))

# Main execution block
system_data = collect_diagnostics()

# Irrelevant preprocessing steps (distractors)
efficiency = calculate_efficiency_index(system_data['cpu_load'], system_data['memory_usage'])
health_score = compute_health_factor(system_data)
system_data['diagnostic_code'] = hash(tuple(system_data.values())) % 1000

# Generate trend history (unused)
historical_loads = [76, 79, 77, 81, 78]
trend_analysis = analyze_trend(historical_loads)

# Validation step that does not affect outcome
alerts = validate_thresholds(system_data)

# Normalize and prepare for evaluation
processed_metrics = {
    'cpu_util': system_data['cpu_load'],
    'mem_util': system_data['memory_usage'],
    'io_activity': system_data['disk_io'],
    'response_time': system_data['network_latency']
}

# Benchmark weighting schema (only this matters)
benchmark_weights = {
    'cpu_util': 0.35,
    'mem_util': 0.25,
    'io_activity': 0.20,
    'response_time': 0.20
}

# Critical statement
final_score = evaluate_performance(processed_metrics, benchmark_weights)

# Output result as required
print(f"Result: {final_score}")