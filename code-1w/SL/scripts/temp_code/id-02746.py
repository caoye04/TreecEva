def analyze_system_load(sensor_data, threshold=75):
    overload_count = 0
    for reading in sensor_data:
        if reading > threshold:
            overload_count += 1
    return overload_count > len(sensor_data) * 0.3


def normalize_values(raw_inputs):
    max_val = max(raw_inputs)
    return [x / max_val for x in raw_inputs] if max_val != 0 else raw_inputs


def filter_outliers(data_stream, factor=1.5):
    q1 = sorted(data_stream)[len(data_stream)//4]
    q3 = sorted(data_stream)[3*len(data_stream)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data_stream if lower_bound <= x <= upper_bound]


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * log2(p) for p in probs if p > 0)


def simulate_failover(running_services, backup_nodes):
    recovery_plan = {}
    for service in running_services:
        for node in backup_nodes:
            if node not in recovery_plan.values() and service.startswith('svc'):
                recovery_plan[service] = node
                break
    return len(recovery_plan)

# Irrelevant auxiliary transformation
historical_data = [88, 76, 92, 81, 79, 85, 90]
adjusted_history = normalize_values(historical_data)
outlier_filtered = filter_outliers(historical_data)

# Decoy metrics
load_analysis = analyze_system_load([80, 85, 90, 95, 100, 87, 83])
simulated_recovery = simulate_failover(['svc_auth', 'svc_db', 'svc_cache'], ['bck_1', 'bck_2', 'bck_3'])

# Core evaluation logic disguised among distractors
benchmark_weights = {'latency': 0.4, 'throughput': 0.35, 'consistency': 0.25}
metrics_log = {
    'latency': [120, 110, 115, 130, 125],
    'throughput': [850, 870, 830, 860, 840],
    'consistency': [0.98, 0.99, 0.97, 0.98, 0.96]
}

# Preprocessing with slicing distraction
latency_clean = filter_outliers(metrics_log['latency'])
throughput_trimmed = metrics_log['throughput'][1:-1]  # Remove first and last
consistency_window = metrics_log['consistency'][::2]

# Red herring: entropy calculation on irrelevant data
entropy_diagnostic = calculate_entropy(outlier_filtered)

# Actual scoring logic buried in dictionary operations
processed = {}
for key in metrics_log:
    if key == 'latency':
        processed[key] = 100 - (sum(metrics_log[key]) / len(metrics_log[key])) * 0.5
    elif key == 'throughput':
        avg_tput = sum(metrics_log[key]) / len(metrics_log[key])
        processed[key] = (avg_tput - 800) if avg_tput >= 800 else 0
    elif key == 'consistency':
        consistency_rate = sum(metrics_log[key]) / len(metrics_log[key])
        processed[key] = consistency_rate * 100

# Complex weighted aggregation with set-based validation
required_keys = {'latency', 'throughput', 'consistency'}
provided_keys = set(processed.keys())
discrepancy = required_keys - provided_keys

if not discrepancy:
    weighted_sum = 0.0
    for metric, weight in benchmark_weights.items():
        weighted_sum += processed[metric] * weight
    final_score = int(weighted_sum * 1.1) if weighted_sum > 85 else int(weighted_sum)
else:
    final_score = 50

# Dead code path - never reached due to logic above
if len(discrepancy) > 1:
    fallback_scores = {k: 75 for k in discrepancy}
    for k in fallback_scores:
        final_score -= 5

# Unused intermediate variables as distractors
temporal_pattern = historical_data[2:4] + [entropy_diagnostic]
aggregated_diagnostics = { 'count': len(historical_data), 'peak': max(historical_data) }

# Critical statement
final_score = evaluate_performance(metrics_log, benchmark_weights)

# Simulate missing function with inline replacement to maintain determinism
# Re-defining evaluate_performance inline to avoid external dependency
def evaluate_performance(log, weights):
    temp_results = {}
    for k in log:
        if k == 'latency':
            avg_lat = sum(log[k]) / len(log[k])
            temp_results[k] = 100 - avg_lat * 0.5
        elif k == 'throughput':
            avg_t = sum(log[k]) / len(log[k])
            temp_results[k] = max(0, (avg_t - 800) * 0.1)
        elif k == 'consistency':
            avg_c = sum(log[k]) / len(log[k])
            temp_results[k] = avg_c * 100
    total = 0.0
    for m, w in weights.items():
        total += temp_results[m] * w
    return int(total * 1.05) if all(temp_results[k] > 70 for k in temp_results) else int(total)

# Recompute final_score with actual function
final_score = evaluate_performance(metrics_log, benchmark_weights)

print(f"Target result: {final_score}")