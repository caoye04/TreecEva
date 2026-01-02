import math

def preprocess_logs(raw):
    # Irrelevant preprocessing (dead function)
    return [x.strip() for x in raw if x != '']

def compute_entropy(data):
    # Distractor: computes entropy but not used in final result
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def extract_metrics(entries):
    # Extract durations and statuses from log entries
    durations = []
    statuses = []
    for entry in entries:
        parts = entry.split('|')
        duration_str = parts[2].split(':')[1].strip()
        status = parts[3].split(':')[1].strip()
        durations.append(float(duration_str))
        statuses.append(1 if status == 'SUCCESS' else 0)
    return durations, statuses

def calculate_anomaly_score(times):
    # Complex distractor with slicing and statistical red herring
    n = len(times)
    if n < 2:
        return 0.0
    mean_time = sum(times) / n
    variance = sum((t - mean_time) ** 2 for t in times) / n
    std_dev = math.sqrt(variance)
    z_scores = [(t - mean_time) / std_dev for t in times[-10:]]  # Last 10 only
    return max(abs(z) for z in z_scores) if z_scores else 0.0

def evaluate_stability(metrics):
    # Another decoy function using dictionary operations
    stability = {
        'jitter': 0.0,
        'drift': 0.0
    }
    values = metrics.get('response_times', [])
    if len(values) > 1:
        diffs = [abs(a - b) for a, b in zip(values, values[1:])]
        stability['jitter'] = sum(diffs) / len(diffs)
        stability['drift'] = values[-1] - values[0]
    return stability

def aggregate_performance(logs, limits):
    # Core logic hidden among distractions
    durations, outcomes = extract_metrics(logs)
    
    # Real computation begins
    valid_durations = [d for d in durations if d <= limits['time_cap']]
    success_count = sum(outcomes)
    total_count = len(outcomes)
    
    # Compute weighted score
    base_score = (success_count / total_count) * 100 if total_count > 0 else 0
    time_efficiency = (sum(valid_durations) / len(valid_durations)) if valid_durations else 0
    penalty = 0
    
    # Apply penalties based on thresholds
    if time_efficiency > limits['optimal_time']:
        penalty += 15
    if success_count / total_count < limits['min_success_rate']:
        penalty += 25
    
    # Final aggregation
    raw_score = base_score - penalty + (10 * math.log(len(valid_durations) + 1))
    
    # Misleading normalization path (not actually used)
    temp_normalized = raw_score / 120.0
    if temp_normalized > 1.0:
        temp_normalized = 1.0  # Clamping
    
    # Actual answer derivation
    final_value = int(round(raw_score))
    
    # Dead code branch: never executed due to structure
    if False:
        backup = compute_entropy(durations)
        final_value = int(backup * 10)
    
    return final_value

# Simulated input data
log_data = [
    "ID:001|TS:12:34:56|DURATION: 23.1|STATUS: SUCCESS",
    "ID:002|TS:12:35:02|DURATION: 45.6|STATUS: FAILURE",
    "ID:003|TS:12:35:10|DURATION: 18.9|STATUS: SUCCESS",
    "ID:004|TS:12:35:25|DURATION: 67.2|STATUS: SUCCESS",
    "ID:005|TS:12:35:40|DURATION: 34.1|STATUS: SUCCESS",
    "ID:006|TS:12:35:55|DURATION: 89.5|STATUS: FAILURE",
    "ID:007|TS:12:36:10|DURATION: 27.8|STATUS: SUCCESS",
    "ID:008|TS:12:36:25|DURATION: 15.3|STATUS: SUCCESS",
    "ID:009|TS:12:36:40|DURATION: 52.4|STATUS: FAILURE",
    "ID:010|TS:12:36:55|DURATION: 38.7|STATUS: SUCCESS"
]

thresholds = {
    'time_cap': 75.0,
    'optimal_time': 30.0,
    'min_success_rate': 0.6
}

# Unused variables - red herrings
baseline_metrics = {'avg': 33.5, 'p95': 70.1}
analysis_window = log_data[1:8:2]
summary_stats = {k: v for k, v in thresholds.items()}
summary_stats['dynamic_cap'] = summary_stats['time_cap'] * 1.1

# Key computation
final_score = aggregate_performance(log_data, thresholds)

# Print result as required
print(f"Target result: {final_score}")