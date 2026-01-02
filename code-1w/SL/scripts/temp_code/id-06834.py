from collections import defaultdict, Counter

# Simulate system health telemetry from distributed nodes
def collect_telemetry(nodes):
    data = defaultdict(list)
    for node_id, readings in nodes.items():
        for metric, values in readings.items():
            data[metric].extend(values)
    return data

# Analyze frequency of status codes across nodes
def analyze_status_frequency(telemetry):
    status_log = ["OK", "WARNING", "ERROR", "OK", "OK", "CRITICAL", "WARNING"]
    freq = Counter(status_log)
    # Irrelevant transformation
    normalized = {k: v / len(status_log) for k, v in freq.items()}
    return freq  # Unused return

# Legacy function - dead code path (never called)
def deprecated_aggregation(x, y):
    temp = x ^ y
    mask = 0xFFFF
    return (temp & mask) >> 2

# Auxiliary calculation with red herring variables
def compute_bias_correction(samples, base=1.0):
    correction_factor = 0.95
    bias_shift = 0
    accumulator = 0
    for i, val in enumerate(samples):
        if i % 3 == 0:
            accumulator += val * correction_factor
        else:
            bias_shift += val // 2  # Distractor logic
    return accumulator  # Only part used

# Core weight adjustment using bit manipulation
def adjust_weights(raw_weights):
    adjusted = []
    for w in raw_weights:
        temp_val = (w << 2) ^ 5
        temp_val = temp_val & 0xFF  # Mask to 8 bits
        if temp_val > 100:
            temp_val = 100
        adjusted.append(temp_val / 100.0)
    return adjusted

# Misleading intermediate computation on fake metrics
def compute_fake_metric_a(data):
    result = 0
    for k, v in data.items():
        result += len(v) * hash(k) % 7
    return result  # Never used

def compute_fake_metric_b(seq):
    total = 0
    for i in range(len(seq)):
        total += i * seq[i] % 2
    return total  # Dead end

# Main evaluation logic with critical path
def evaluate_performance(metrics, weights):
    scores = []    
    keys = list(metrics.keys())
    zipped_data = zip(keys, [metrics[k] for k in keys], weights)
    
    for idx, (name, vals, weight) in enumerate(zipped_data):
        if name == "response_time":
            avg = sum(vals) / len(vals)
            # Normalize to 0-1 scale (lower is better)
            score = max(0, min(1, 1 - (avg / 500)))
        elif name == "throughput":
            avg = sum(vals) / len(vals)
            score = min(1, avg / 1000)
        elif name == "error_rate":
            rate = sum(vals) / len(vals)
            score = max(0, 1 - rate)
        else:
            continue  # Skip irrelevant
        scores.append(score * weight)
    
    raw_final = sum(scores)
    
    # Apply non-linear boost (sigmoid-like)
    final = 100 * (raw_final / (1 + abs(raw_final - 1))) if raw_final != 1 else 50
    
    # Critical red herring: unused but plausible-looking adjustment
    adjustment = 0
    for i in range(5):
        adjustment += (final ^ i) % 3
    
    return int(round(final))  # Answer determined here

# Simulated input data from monitoring system
node_data = {
    'node_01': {
        'response_time': [200, 250, 180, 300],
        'throughput': [950, 900, 1050, 980],
        'error_rate': [0.02, 0.01, 0.03, 0.02]
    },
    'node_02': {
        'response_time': [220, 190, 240, 270],
        'throughput': [970, 1020, 960, 990],
        'error_rate': [0.01, 0.02, 0.01, 0.03]
    }
}

# Extract metrics
telemetry = collect_telemetry(node_data)

# Irrelevant preprocessing
freq_analysis = analyze_status_frequency(telemetry)
fake_a = compute_fake_metric_a(telemetry)
fake_b = compute_fake_metric_b([1, 0, 1, 1, 0])

# Real signal path begins
metrics = {
    'response_time': telemetry['response_time'],
    'throughput': telemetry['throughput'],
    'error_rate': telemetry['error_rate']
}

# Raw weights subject to transformation
raw_weights = [3, 2, 5]

# Adjust weights using bitwise logic
weights = adjust_weights(raw_weights)

# Compute bias correction on dummy data (distractor)
bias = compute_bias_correction([4, 8, 15, 16, 23, 42])

# MAIN STATEMENT: this determines the answer
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")