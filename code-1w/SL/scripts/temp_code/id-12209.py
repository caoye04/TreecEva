import math

# Irrelevant helper function (dead code path)
def calculate_entropy(data):
    return -sum(p * math.log2(p) for p in data if p > 0)

# Misleading performance metric that isn't used
def legacy_scorer(values):
    acc = 0
    for v in values:
        if v > 50:
            acc += v * 0.3
        else:
            acc += v * 0.1
    return acc

# Simulated sensor readings with noise filtering
def filter_anomalies(readings):
    mean_val = sum(readings) / len(readings)
    filtered = [r for r in readings if abs(r - mean_val) < 20]
    normalized = [(r - min(filtered)) / (max(filtered) - min(filtered)) * 100 for r in filtered]
    return normalized

# Complex weighting strategy with red herring branches
def generate_weights(n):
    base = [math.cos(i * 0.5) + 1 for i in range(n)]
    scaled = [b * 10 for b in base]
    total = sum(scaled)
    weights = [s / total for s in scaled]
    
    # Dead logic branch - never executed due to prior return
    if len(weights) > 100:
        fallback = [1/n] * n
        return fallback
    
    return weights

# Simulate system health indicators (unused but plausible)
system_health = {
    'cpu_load': [0.45, 0.67, 0.78, 0.56],
    'memory_usage': [0.82, 0.76, 0.91, 0.64],
    'disk_iops': [120, 135, 110, 140]
}

# Unused transformation pipeline
def transform_metrics(metrics):
    transformed = {}
    for k, v in metrics.items():
        if isinstance(v, list):
            transformed[k] = [x ** 0.5 for x in v]
        else:
            transformed[k] = v ** 2
    return transformed

# Core evaluation logic buried in distractions
def evaluate_performance(metrics, weights):
    # Extract relevant time-series data
    response_times = metrics['response_time_ms']
    success_rate = metrics['success_rate_percent']
    throughput = metrics['throughput_ops']
    
    # Filter anomalies from response times
    clean_rt = filter_anomalies(response_times)
    
    # Compute composite efficiency score
    avg_response = sum(clean_rt) / len(clean_rt)
    efficiency = (100 - avg_response) * 0.4
    
    # Apply non-linear boost to high success rates
    reliability = success_rate[0] if success_rate[0] > 90 else success_rate[0] * 0.8
    
    # Throughput normalization using integer division
    max_observed = 500
    normalized_tput = (throughput[0] // max_observed) * 100
    if normalized_tput == 0 and throughput[0] > 0:
        normalized_tput = min(throughput[0] / 5, 100)
    
    # Weighted combination (weights[0]: efficiency, weights[1]: reliability, weights[2]: throughput)
    components = [efficiency, reliability, normalized_tput]
    weighted_sum = sum(c * w for c, w in zip(components, weights))
    
    # Final adjustment using bitwise logic (red herring operation with no effect)
    flag = 0b1010
    if weighted_sum > 75:
        flag |= 0b0101
    else:
        flag ^= 0b1111
    
    # Actual final score computation
    final_score = int(weighted_sum) & 0xFF  # Clamp to byte range
    
    # Decoy mutation (never affects output)
    temp_result = final_score * 1.05
    temp_result = math.floor(temp_result)
    
    return final_score

# Simulated input data
metrics = {
    'response_time_ms': [85, 92, 78, 150, 88, 83, 95],  # 150 is outlier
    'success_rate_percent': [94],
    'throughput_ops': [420],
    'error_count': [6],  # unused field
    'timestamp': [1712050800]  # unused field
}

# Generate weights (3 elements needed)
weights = generate_weights(3)

# Dead variable assignments (distractors)
corrupted_data_flag = False
temp_buffer = [0] * 10
data_checksum = sum(temp_buffer)

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")