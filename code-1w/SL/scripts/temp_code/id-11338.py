def analyze_metric(data, threshold=0.75):
    if len(data) == 0:
        return 0
    avg = sum(data) / len(data)
    return avg > threshold

# Irrelevant helper function (decoy)
def compute_entropy(sequence):
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Unused constant (red herring)
MAX_ITERATIONS = 50000

# Simulate sensor drift compensation (distractor logic)
sensor_offsets = [0.1, -0.05, 0.2, 0.0]
adjusted_readings = []
for i in range(4):
    adjusted_readings.append(round(sensor_offsets[i] * 100))

# Core data pipeline
raw_inputs = [15, 27, 12, 36, 9, 45]
normalized = [x / 3 for x in raw_inputs if x > 10]  # Filtering and scaling

# Misleading transformation chain
shadow_copy = [x + 1 for x in normalized]
duplicate_check = any(shadow_copy.count(x) > 1 for x in shadow_copy)

# Conditional expression with relevance
status_flag = 'active' if len(normalized) >= 4 else 'standby'

# Primary processing stages
def transform_value(x, mode='fast'):
    if mode == 'fast':
        return (x ** 2) // 10 + 1
    else:
        return int(x * 0.75) + 2

processed = [transform_value(x) for x in normalized]

# Feedback loop simulation
def evaluate_stability(values):
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return sum(diffs) < 15

evaluation_snapshot = [12, 14, 18, 20]
stability = evaluate_stability(evaluation_snapshot)

# Nested control flow with distractors
temp_log = []
summary_stats = {}
for idx, val in enumerate(processed):
    if val % 2 == 0:
        temp_log.append((idx, val))
        # Dead code path (early break never reached)
        if val > 1000:
            break
    else:
        continue

# Key intermediate structure
feedback_loop = {
    'metrics': processed,
    'baseline': sum(normalized[:3]),
    'mode_flag': status_flag,
    'valid_entries': len(temp_log)
}

# Decoy function that's defined but not used
def trigger_calibration():
    nonlocal_adjustment = 0
    for _ in range(3):
        nonlocal_adjustment += 0.5
    return nonlocal_adjustment

# Main aggregation logic
def aggregate_performance(report):
    metrics = report['metrics']
    base = report['baseline']
    flag_active = report['mode_flag'] == 'active'
    valid_count = report['valid_entries']
    
    # Complex conditional expression (core concept)
    adjustment_factor = 1.5 if flag_active and valid_count >= 2 else 0.8
    
    metric_sum = sum(m for m in metrics if m < 25)  # Filter outliers
    
    # Composite calculation
    raw_score = metric_sum * adjustment_factor
    penalty = (len(metrics) - valid_count) * 2
    
    # Final computation
    return int(raw_score - penalty + base)

# Execution point of interest
final_score = aggregate_performance(feedback_loop)

# Output requirement
print(f"Target result: {final_score}")