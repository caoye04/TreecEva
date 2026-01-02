def analyze_component(data, threshold=0.5):
    """Irrelevant analysis function - distractor"""
    if not data:
        return False
    avg = sum(data) / len(data)
    return avg > threshold

# Distractor variables
temp_buffer = [0.1, 0.4, 0.35, 0.87]
decoy_matrix = [[1, 0], [0, 1]]
useless_flag = any(x > 0.5 for x in temp_buffer)

# Real input data
metrics = {
    'latency': 120,      # ms
    'throughput': 850,   # requests/sec
    'error_rate': 0.02,  # ratio
    'memory': 450        # MB
}

weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'error_rate': -0.2,  # negative weight: lower is better
    'memory': -0.1
}

# Misleading normalization chain
normalized = {}
for k in metrics:
    if k == 'latency':
        normalized[k] = round(100 - (metrics[k] / 10), 2)
    elif k == 'throughput':
        normalized[k] = min(100, round(metrics[k] / 10, 2))
    elif k == 'error_rate':
        normalized[k] = max(0, 100 - (metrics[k] * 1000))
    elif k == 'memory':
        normalized[k] = max(0, 100 - (metrics[k] / 5))

# Dead code path - never executed but looks important
if __debug__:
    checksum = 0
    for val in normalized.values():
        checksum ^= int(val)

# Another decoy function with string manipulation
def validate_string(s):
    return s.upper().replace('_', '').endswith('DATA')

config_name = "system_perf_data"
valid_config = validate_string(config_name)

# Core evaluation logic disguised among noise
def evaluate_performance(met, wgt):
    base = 0.0
    bonus = 0
    penalty = 0

    # Latency affects base and may trigger bonus
    if met['latency'] < 100:
        base += 10
        if met['throughput'] > 800:
            bonus += 5
    else:
        base += 5

    # Throughput tiers
    if met['throughput'] >= 900:
        base += 15
    elif met['throughput'] >= 800:
        base += 10
    else:
        base += 5

    # Error rate penalties
    if met['error_rate'] < 0.01:
        base += 8
    elif met['error_rate'] < 0.03:
        base += 5
    else:
        penalty += 10

    # Memory usage bands
    if met['memory'] < 400:
        base += 7
    elif met['memory'] < 500:
        base += 4
    else:
        penalty += 5

    # Apply weights to normalized metrics (red herring section)
    weighted_total = 0.0
    for key in met:
        if key in wgt:
            # This calculation is misleading but looks central
            weighted_total += (normalized[key] * wgt[key])

    # Final score is NOT weighted_total - that's the trap
    final_raw = base + bonus - penalty

    # Last-minute adjustment based on string property (subtle but valid)
    adjustment = 1.0
    if len(config_name) % 5 == 0:
        adjustment = 1.1

    return int(final_raw * adjustment)

# Irrelevant data structure transformation
tuple_snapshot = tuple(f'{k}:{v}' for k, v in metrics.items() if v > 0)
dict_copy = {**metrics}
dict_copy['timestamp'] = 1678886400

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Additional distraction: unused bit manipulation
bit_fiddle = (len(tuple_snapshot) << 2) ^ 0x0F
flag_check = (bit_fiddle & 0x01) == 0

# Print result as required
print(f"Result: {final_score}")