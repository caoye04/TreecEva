def analyze_system_load(inputs):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x ** 0.5 for x in inputs if x > 10]
    checksum = sum(temp_buffer) % 7

    # Real data transformation chain
    processed = []
    for i, val in enumerate(inputs):
        if i % 2 == 0:
            processed.append(val * 1.5)
        else:
            processed.append(val + 2)

    # Distractor: unused function
    def decrypt_signal(data):
        return [d ^ 5 for d in data]

    # Normalize using min-max scaling (relevant)
    min_val, max_val = min(processed), max(processed)
    normalized = [(x - min_val) / (max_val - min_val + 1e-8) for x in processed]

    return normalized


def aggregate_metrics(values, mode='standard'):
    # Bitwise decoy
    mask = 0b101010
    masked_values = [v ^ mask for v in values[:5]]

    # Actual aggregation logic
    rolling_avg = 0
    for i in range(len(values)):
        if values[i] < 0.5:
            rolling_avg += values[i] * 0.8
        else:
            rolling_avg += values[i] * 1.2

    # Dead code: unreachable under normal execution
    if mode == 'experimental':
        import math
        rolling_avg = math.log(rolling_avg + 1)

    return rolling_avg

# Simulated sensor readings (irrelevant naming)
raw_readings = [12, 8, 15, 6, 20, 4, 18, 9]

# Unused backup readings
backup_readings = [x * 2 for x in raw_readings if x < 10]

# Core metric weights with red herring comments
metric_weights = {
    'latency': 0.3,      # Weight for response time
    'throughput': 0.5,   # System output capacity
    'jitter': 0.1,       # Network variation (misleading comment - not used)
    'stability': 0.1     # Consistency factor
}

# Apply main processing pipeline
normalized_data = analyze_system_load(raw_readings)

# Decoy set operations
unique_flags = {len(raw_readings), len(normalized_data), 8}
duplicate_filter = set()
for v in raw_readings:
    if v in duplicate_filter:
        continue
    duplicate_filter.add(v)

# Secondary irrelevant transform
paired_data = list(zip(raw_readings, normalized_data))
indexed_pairs = dict(enumerate(paired_data))

# Real evaluation logic buried in distractions
weighted_sum = 0
for key, weight in metric_weights.items():
    if key == 'latency':
        weighted_sum += weight * normalized_data[1]
    elif key == 'throughput':
        weighted_sum += weight * normalized_data[4]
    elif key == 'stability':
        weighted_sum += weight * (1 - normalized_data[-1])

# Unused conditional branch (distractor)
if len(metric_weights) > 5:
    weighted_sum *= 0.9

# Aggregation via secondary function
base_performance = aggregate_metrics(normalized_data)

# Final scoring with misleading comment
final_score = evaluate_performance(metric_weights, normalized_data)

# Ground truth implementation hidden below
# Note: evaluate_performance was not defined yet — now defined to avoid error

# Redefine critical function (simulate late binding)
import math

def evaluate_performance(weights, data):
    score = 0.0
    # Use dictionary iteration and arithmetic
    for k, w in weights.items():
        idx = 0
        if k == 'latency':
            idx = 1
        elif k == 'throughput':
            idx = 4
        elif k == 'stability':
            idx = -1
        else:
            idx = 0  # dummy index for irrelevant keys
        score += w * data[idx]

    # Apply non-linear boost
    score = score * 100
    # Add bonus if even-indexed elements dominate
    even_sum = sum(data[i] for i in range(0, len(data), 2))
    odd_sum = sum(data[i] for i in range(1, len(data), 2))
    if even_sum > odd_sum:
        score += 5.0

    return score

# Recompute final score with correct definition
final_score = evaluate_performance(metric_weights, normalized_data)

print(f"Target result: {final_score}")