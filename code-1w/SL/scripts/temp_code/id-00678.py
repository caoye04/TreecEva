import math

# Simulated system performance metrics with red herrings
temp_cache = [i ** 2 for i in range(10)]
buffer_overflow_flag = False
system_uptime = 98765
dummy_matrix = [[0 for _ in range(5)] for _ in range(5)]

# Core data structures (some fields are decoys)
metrics = {
    'response_time': 120.5,
    'throughput': 890,
    'error_rate': 0.045,
    'latency_jitter': 18.2,
    'bandwidth_usage': 76.3,
    'memory_leak_estimate': 0.003,  # irrelevant
    'disk_io_ops': 432,              # irrelevant
    'cpu_spike_count': 7             # irrelevant
}

weights = {
    'response_time': 0.3,
    'throughput': 0.25,
    'error_rate': 0.35,
    'latency_jitter': 0.1,
    'bandwidth_usage': 0.0          # explicitly zero weight (distractor)
}

# Unused but plausible helper functions
def calculate_entropy(data):
    return -sum(p * math.log2(p) for p in data if p > 0)

def validate_checksum(arr):
    return sum(arr) % 256

def deprecated_normalizer(x):
    return 1 / (1 + math.exp(-x))

# Real processing begins here
preprocess_fn = lambda x, w: (100 / (1 + x)) * w if x > 0 else 100 * w

# Distractor: complex-looking but unused transformation
correlation_map = {
    (i, j): math.cos(i * 0.1) * math.sin(j * 0.1)
    for i in range(3) for j in range(3)
}

historical_data = [
    {'timestamp': t, 'value': (t * 0.3) % 100} for t in range(100)
]

# Another red herring: sophisticated but unused algorithm
moving_average = [
    sum(d['value'] for d in historical_data[i:i+5]) / 5
    for i in range(len(historical_data) - 4)
]

# Key computation chain starts here
effective_metrics = {}
for key in weights:
    if key in metrics and weights[key] > 0:
        if key == 'error_rate':
            # Invert error rate: lower is better
            effective_metrics[key] = preprocess_fn(1/metrics[key], weights[key])
        elif key == 'response_time':
            effective_metrics[key] = preprocess_fn(metrics[key], weights[key])
        else:
            # Direct weighted contribution
            norm_value = min(metrics[key] / 1000.0, 1.0)  # normalize throughput-like values
            effective_metrics[key] = norm_value * 100 * weights[key]

# Dead code path (never executed)
if system_uptime < 0:
    final_score = -999
else:
    # Actual score calculation
    base_score = sum(effective_metrics.values())
    
    # Secondary adjustment based on jitter threshold
    if metrics['latency_jitter'] > 15.0:
        penalty_factor = 0.95
    else:
        penalty_factor = 1.0
    
    adjusted_score = base_score * penalty_factor
    
    # Hidden rule: bonus if throughput exceeds 800
    throughput_bonus = 5.0 if metrics['throughput'] > 800 else 0.0
    
    # Final composition
    intermediate = adjusted_score + throughput_bonus
    
    # Normalize to cap at 100 (but won't exceed anyway)
    final_score = min(intermediate, 100.0)

# Irrelevant post-processing
encryption_key = bytes([i % 256 for i in temp_cache[:8]])
checksum = validate_checksum(temp_cache)
entropy = calculate_entropy([0.1, 0.2, 0.7])

# Output the required result
print(f"Result: {final_score}")