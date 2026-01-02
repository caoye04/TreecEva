def analyze_efficiency(data, threshold=0.75):
    """ Analyze system efficiency with red-herring metrics """
    normalized = [x / sum(data) for x in data]
    above_threshold = [i for i, val in enumerate(normalized) if val > threshold]
    return len(above_threshold) > 0

# Simulated sensor readings (irrelevant to final result)
sensor_logs = [23, 45, 67, 89, 12, 34, 56]
dummy_stats = {'max_val': max(sensor_logs), 'sum_sq': sum(x**2 for x in sensor_logs)}

# Core performance metrics (only some are used)
metrics = {
    'latency': 42,
    'throughput': 86,
    'reliability': 91,
    'bandwidth': 73,
    'jitter': 15
}

# Weight configuration – only latency, reliability, and throughput matter
weights = {
    'latency': 0.3,
    'throughput': 0.5,
    'reliability': 0.2,
    'bandwidth': 0.0,  # Unused weight (distractor)
    'jitter': 0.0       # Unused weight (distractor)
}

# Red herring: complex bit manipulation on jitter (never used)
jitter_binary = bin(metrics['jitter'])[2:]
bitwise_xor_chain = 0
for bit in jitter_binary:
    bitwise_xor_chain ^= int(bit)
bitwise_xor_chain <<= 4
bitwise_xor_chain |= 0b1010

# Auxiliary function that looks important but isn't called
def calculate_integrity_score(records):
    total = 0
    for i, r in enumerate(records):
        total += r * (i + 1)
    return total / len(records) if records else 0

# Another decoy: string-based analysis from numeric metrics (dead code path)
metric_names = list(metrics.keys())
char_count_map = {name: len(name) for name in metric_names}
name_length_product = 1
for length in char_count_map.values():
    name_length_product *= length

# Real logic hidden among distractions
def weighted_average(values, w):
    return sum(values[key] * w[key] for key in w if w[key] > 0)

# Simulate historical baseline (unused in final computation)
historical_avg = 78.4
adjustment_factor = (metrics['latency'] + metrics['throughput']) / 2
projected_trend = adjustment_factor * 1.05

# Evaluate performance using only selected metrics and weights
def evaluate_performance(m, w):
    # Filter out zero-weight components
    relevant_keys = [k for k in w if w[k] > 0]
    
    # Extract values and apply weights
    subtotal = 0.0
    for key in relevant_keys:
        if key == 'latency':
            # Latency is inverted: lower is better, so we normalize inversely
            normalized_latency = 100 - m[key]  # Convert to 'goodness' score
            subtotal += normalized_latency * w[key]
        else:
            subtotal += m[key] * w[key]
    
    # Apply bonus if all primary metrics exceed 80
    primary_metrics = ['latency', 'throughput', 'reliability']
    high_performer_bonus = 5 if all(m[k] >= 80 for k in primary_metrics) else 0
    
    # Final adjustment based on pattern in metric digits (hidden rule)
    digit_sum = sum(sum(int(d) for d in str(m[k])) for k in primary_metrics)
    digit_mod = digit_sum % 4
    
    return subtotal + high_performer_bonus + digit_mod

# Execute main logic
temp_buffer = []
for idx, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
    temp_buffer.append(f'{k}:{v}')

delimited_output = '|'.join(temp_buffer)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")