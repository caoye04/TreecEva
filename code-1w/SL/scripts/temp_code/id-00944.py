import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x > 0]

# Distractor variables
temp_buffer = [i * 0.1 for i in range(100)]
dummy_mask = [True, False] * 50
junk_sum = sum(temp_buffer) * 0.001

# Real data structures
metrics = {
    'accuracy': 0.92,
    'latency': 45,
    'throughput': 128,
    'memory_usage': 3.4,
    'error_rate': 0.01
}

weights = {
    'accuracy': 0.3,
    'latency': -0.1,
    'throughput': 0.2,
    'memory_usage': -0.05,
    'error_rate': -0.2
}

# Misleading intermediate calculation (not used in final result)
baseline_score = 0
for k in metrics:
    baseline_score += metrics[k] * weights[k] * 0.5

# Decoy function with similar name
def evaluate_performancex(data_dict, weight_dict):
    return sum(data_dict[k] + weight_dict[k] for k in data_dict)

# Lambda for dynamic adjustment (used in real logic)
normalize = lambda x, min_val, max_val: (x - min_val) / (max_val - min_val) if max_val != min_val else 0

# Simulated preprocessing (some steps are red herrings)
processed_metrics = {}
if 'accuracy' in metrics:
    processed_metrics['accuracy'] = metrics['accuracy']

if 'latency' in metrics:
    # Latency is inverted: lower is better
    inverted_latency = 100 - min(90, metrics['latency'])
    normalized_latency = normalize(inverted_latency, 10, 100)
    processed_metrics['latency'] = normalized_latency

if 'throughput' in metrics:
    normalized_throughput = normalize(metrics['throughput'], 50, 200)
    processed_metrics['throughput'] = normalized_throughput

if 'memory_usage' in metrics:
    # Memory: lower is better
    inv_memory = 8 - metrics['memory_usage']
    normalized_memory = normalize(inv_memory, 2, 8)
    processed_metrics['memory_usage'] = normalized_memory

# Unused branch (distractor)
if 'disk_io' in metrics:
    processed_metrics['disk_io'] = metrics['disk_io'] / 100

# Early exit simulation (never triggered due to condition)
critical_failure = False
if metrics['error_rate'] > 0.05:
    final_score = -1
    critical_failure = True
else:
    # Main evaluation logic
    raw_score = 0
    for key in weights:
        if key in processed_metrics:
            raw_score += processed_metrics[key] * abs(weights[key])
    
    # Apply non-linear boost using sigmoid-like transform
    boosted_score = 100 * (1 / (1 + math.exp(-10 * (raw_score - 0.5))))
    
    # Final adjustment based on error penalty (even though already considered)
    penalty_factor = (1 - metrics['error_rate'] ** 0.5)
    final_score = boosted_score * penalty_factor

# Additional irrelevant computation
dummy_matrix = [[i*j for j in range(5)] for i in range(5)]
checksum = sum(sum(row) for row in dummy_matrix)
correction_offset = math.sin(junk_sum) * checksum * 0.0001  # negligible effect

# Output the target result
Result: {final_score}