import math

# Irrelevant helper function (decoy)
def analyze_health_status(vital_signs):
    heart_rate_zone = 'Normal' if 60 <= vital_signs['hr'] <= 100 else 'Elevated'
    return {'status': heart_rate_zone, 'risk': 0.0}

# Another decoy function with misleading intermediate logic
def calculate_network_latency(ping_samples):
    if not ping_samples:
        return 0
    avg = sum(ping_samples) / len(ping_samples)
    jitter = max(ping_samples) - min(ping_samples)
    # Dead code path (never reached due to early return above)
    adjusted = avg * (1 + jitter / 100) if avg > 50 else avg
    return round(avg, 2)

# Core data processing with red herrings and distractions
def preprocess_metrics(raw_entries):
    cleaned = []
    outlier_count = 0
    for entry in raw_entries:
        value = entry['value']
        timestamp = entry['ts']

        # Distractor: irrelevant validation on timestamp format
        if len(str(timestamp)) != 10:
            continue

        # Actual filtering logic
        if value < 0:
            outlier_count += 1
            continue

        # Real transformation
        normalized = math.log(value + 1) if value > 0 else 0
        category = 'high' if normalized > 2.3 else 'low'

        # Attach meaningless metadata
        cleaned.append({
            'norm': round(normalized, 4),
            'cat': category,
            'src': entry.get('source', 'unknown'),
            'flagged': False  # Never used later
        })

    # Return unused statistic to mislead
    scaling_factor = 1.0 if outlier_count < 5 else 0.9
    return cleaned

# Main evaluation logic with nested conditions and list comprehensions
def evaluate_performance(metrics, config_thresholds):
    if not metrics:
        return 0

    # Extract relevant normalized values using list comprehension
    norms = [m['norm'] for m in metrics if m['cat'] == 'high']

    # Red herring: complex but unused calculation
    weighted_sum = sum(
        norm * (index + 1) for index, norm in enumerate(norms)
    )
    average_weighted = weighted_sum / len(norms) if norms else 0

    # Real computation begins here
    base_score = sum(norms)

    # Conditional bonus based on threshold slicing
    threshold_window = config_thresholds[1:-1]  # Ignore first and last
    bonus = 0
    if len(threshold_window) >= 2 and base_score > threshold_window[0]:
        bonus = int(base_score // threshold_window[1])

    # Apply string-based condition (uses string method)
    mode_flag = 'adaptive_mode_enabled'
    if mode_flag.upper().replace('_', '').startswith('ADAPTIVE'):
        bonus += 2

    # Critical recursive component (simple recursion)
    def adjust_for_consistency(values, depth=0):
        if depth >= 3 or len(values) < 2:
            return len(values)
        mid = len(values) // 2
        left = values[:mid]
        right = values[mid:]
        if sum(left) > sum(right):
            return adjust_for_consistency(left, depth + 1)
        else:
            return adjust_for_consistency(right, depth + 1)

    consistency = adjust_for_consistency(norms)

    # Final composition with distractors
    noise_correction = math.sin(math.pi / 4)  # Always ~0.707, constant
    raw_total = base_score + bonus + consistency
    final_result = int(raw_total * 7)  # Key transformation

    # Unused variables to increase interference
    debug_trace = []
    for i, m in enumerate(metrics):
        debug_trace.append(f"Item_{i}: {m['norm']:.2f}")

    summary_hash = hash(tuple(debug_trace)) % 1000 if debug_trace else 0

    return final_result

# Simulated input data
raw_input = [
    {'value': 100, 'ts': 1678886400, 'source': 'sensor_a'},
    {'value': 250, 'ts': 1678886401, 'source': 'sensor_b'},
    {'value': 800, 'ts': 1678886402, 'source': 'sensor_a'},
    {'value': 450, 'ts': 1678886403, 'source': 'sensor_c'},
    {'value': 1200, 'ts': 1678886404, 'source': 'sensor_b'},
    {'value': -5, 'ts': 1678886405},  # Outlier (filtered out)
    {'value': 300, 'ts': 1678886406, 'source': 'sensor_d'}
]

thresholds = [0.5, 2.1, 3.75, 9.0]  # Used in slicing logic

# Preprocess the data
metric_data = preprocess_metrics(raw_input)

# Evaluate performance - key execution point
final_score = evaluate_performance(metric_data, thresholds)

# Print result as required
print(f"Result: {final_score}")