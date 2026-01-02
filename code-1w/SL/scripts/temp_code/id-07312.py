def analyze_signal(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    normalized = [round((x - min(data)) / (max(data) - min(data)), 3) for x in data]
    return ratio, normalized

# Irrelevant preprocessing
raw_data = [0.1, 0.8, 0.3, 0.9, 0.4, 0.7]
signal_ratio, scaled_values = analyze_signal(raw_data)

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

entropy_value = compute_entropy([1, 2, 2, 3, 3, 3])  # Dead-end computation

# Decoy model parameters
temp_weights = [0.2, 0.3, 0.5]
baseline_scores = {'accuracy': 0.88, 'precision': 0.75, 'recall': 0.65}

# Real logic begins: system health evaluation
metrics = {
    'latency': 45,           # ms
    'throughput': 1200,       # req/sec
    'error_rate': 0.013,      # fraction
    'memory_usage': 78.4,     # percent
    'cpu_load': 67.2          # percent
}

weights = {
    'latency': 0.25,
    'throughput': 0.2,
    'error_rate': 0.3,
    'memory_usage': 0.15,
    'cpu_load': 0.1
}

# Distractor: fake normalization
fake_norm = {k: v / 100 if isinstance(v, float) else v for k, v in metrics.items()}

# Misleading transformation chain
decay_factor = 0.9
adjusted_metrics = {}
for key, value in metrics.items():
    if key == 'latency':
        adjusted_metrics[key] = max(10, value * 0.8)
    elif key == 'throughput':
        adjusted_metrics[key] = min(1500, value * 1.1)
    elif key == 'error_rate':
        adjusted_metrics[key] = max(0.005, value * 0.9)
    else:
        adjusted_metrics[key] = value  # cpu and memory unchanged

# Another red herring: string-based status
status_flags = ['OK', 'WARNING', 'CRITICAL']
current_status = status_flags[1] if metrics['error_rate'] > 0.01 else status_flags[0]
status_code = hash(current_status) % 100  # Unused distraction

# Actual scoring logic
base_latency_score = 100 - (adjusted_metrics['latency'] - 10)  # Ideal at 10ms
throughput_bonus = adjusted_metrics['throughput'] // 100
error_penalty = int(adjusted_metrics['error_rate'] * 1000)
resource_penalty = round((adjusted_metrics['memory_usage'] + adjusted_metrics['cpu_load']) / 20)

# Conditional expression used (Python feature)
system_age = 3
age_adjustment = 5 if system_age < 2 else (-3 if system_age > 5 else -1)

# Composite score before weighting
preliminary_scores = {
    'latency': max(0, base_latency_score),
    'throughput': min(100, throughput_bonus * 8),
    'error_rate': max(0, 100 - error_penalty * 10),
    'memory_usage': max(0, 100 - resource_penalty * 5),
    'cpu_load': max(0, 100 - resource_penalty * 5)
}

# String method distractor
log_entry = f"System assessment: {list(preliminary_scores.keys())}".replace(' ', '_').upper()
diagnostic_tag = log_entry.split('_')[2]  # 'ASSESSMENT:' - irrelevant

# Final weighted evaluation (key statement)
def evaluate_performance(met, wgt):
    total = 0.0
    for k in met:
        if k in wgt:
            total += preliminary_scores[k] * wgt[k]
    return round(total, 4)

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")