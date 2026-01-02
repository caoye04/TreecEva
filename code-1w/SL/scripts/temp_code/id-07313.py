def analyze_trend(data, threshold=0.5):
    positive_changes = [x for x in data if x > threshold]
    negative_changes = [x for x in data if x <= -threshold]
    return len(positive_changes) - len(negative_changes)


def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]


def compute_weighted_average(records):
    weights = [0.1, 0.2, 0.3, 0.4]
    total = sum(record['value'] * weights[i] for i, record in enumerate(records))
    return total


def detect_anomalies(events):
    anomalies = set()
    for e in events:
        if e['type'] == 'ERROR' and e['severity'] > 3:
            anomalies.add(e['id'])
    return anomalies


def calculate_efficiency(runs):
    total_time = sum(runs)
    adjusted_time = total_time * 0.9 if len(runs) > 5 else total_time
    efficiency = (1000 / adjusted_time) if adjusted_time > 0 else 0
    return efficiency

# Irrelevant utility function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading intermediate variables
temp_offset = 42
scaling_factor = 1.05
buffer_cache = [0] * 100

# Simulated system metrics
metrics = [
    {'name': 'latency', 'value': 120, 'unit': 'ms'},
    {'name': 'throughput', 'value': 850, 'unit': 'req/s'},
    {'name': 'error_rate', 'value': 0.03, 'unit': '%'},
    {'name': 'cpu_load', 'value': 78, 'unit': '%'}
]

# Baseline configuration with decoy entries
baseline = {
    'target_latency': 100,
    'min_throughput': 800,
    'max_error_rate': 0.05,
    'optimal_cpu': 70,
    'decoy_key_ignored': [1, 2, 3],
    'unused_flag': True
}

# Complex evaluation logic with distractors
def evaluate_performance(met, base):
    score = 0
    
    # Extract relevant metric values
    latency_val = next(m['value'] for m in met if m['name'] == 'latency')
    throughput_val = next(m['value'] for m in met if m['name'] == 'throughput')
    error_rate_val = next(m['value'] for m in met if m['name'] == 'error_rate')
    cpu_load_val = next(m['value'] for m in met if m['name'] == 'cpu_load')
    
    # Evaluate each dimension against baseline
    if latency_val <= base['target_latency']:
        score += 25
    elif latency_val < base['target_latency'] * 1.1:
        score += 15
    else:
        score += 5
    
    if throughput_val >= base['min_throughput']:
        score += 25
    
    if error_rate_val <= base['max_error_rate']:
        score += 30
    
    if cpu_load_val <= base['optimal_cpu']:
        score += 20
    else:
        penalty = (cpu_load_val - base['optimal_cpu']) * 0.5
        score -= int(penalty)
    
    # Red herring: irrelevant data transformation
    shadow_metrics = [{**m, 'adjusted': m['value'] * scaling_factor} for m in met]
    temp_result = sum(m['value'] for m in shadow_metrics) // len(shadow_metrics)
    
    # Hidden correction factor based on modular arithmetic
    correction = (score * 7) % 13
    if correction > 10:
        score += 5
    elif correction < 3:
        score -= 2
    
    # Final adjustment using conditional expression
    final_score = score + (10 if temp_result > 300 else 0)
    
    return final_score

# Unused data structures (distractor)
log_entries = [
    {'id': 101, 'level': 'INFO', 'msg': 'System start'},
    {'id': 102, 'level': 'WARN', 'msg': 'High load'},
    {'id': 103, 'level': 'ERROR', 'msg': 'Timeout'}
]

anomaly_set = detect_anomalies(log_entries)
efficiency_rating = calculate_efficiency([120, 110, 115, 130, 105, 100])

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")