def analyze_component_health(sensor_data, thresholds):
    healthy_count = 0
    for reading in sensor_data:
        if reading < thresholds['critical'] and reading > thresholds['optimal']:
            healthy_count += 1
    return healthy_count

# Irrelevant health monitoring system (distraction)
sensor_readings = [0.45, 0.67, 0.33, 0.89, 0.55]
critical_thresholds = {'optimal': 0.2, 'critical': 0.8}
health_status = analyze_component_health(sensor_readings, critical_thresholds)

# Core algorithm: Recursive tuple-based efficiency evaluator
def compute_efficiency_factor(data_stream, index=0):
    if index >= len(data_stream):
        return 1
    current = data_stream[index]
    if isinstance(current, tuple):
        # Recursively process nested tuples
        nested_value = sum(compute_efficiency_factor(list(current), 0))
        return nested_value * 0.9 + compute_efficiency_factor(data_stream, index + 1)
    else:
        return (current ** 0.5) * 0.8 + compute_efficiency_factor(data_stream, index + 1)

# Data transformation pipeline with distractors
temp_buffer = [x * 1.1 for x in range(8)]  # Unused preprocessing path
offset_lookup = {i: i*2 for i in range(5)}  # Dead lookup table

# Real input data disguised among noise
event_sequence = [
    (25, 16),
    36,
    (49, (64, 81)),
    100
]

# Set operations as required feature
unique_roots = set()
for item in event_sequence:
    if isinstance(item, tuple):
        flat_items = []
        stack = [item]
        while stack:
            elem = stack.pop()
            if isinstance(elem, tuple):
                stack.extend(elem)
            else:
                flat_items.append(elem)
        for val in flat_items:
            unique_roots.add(int(val ** 0.5))
    else:
        unique_roots.add(int(item ** 0.5))

# Secondary irrelevant metric calculation
drift_analysis = []
for i, val in enumerate(temp_buffer):  # Uses enumerate but irrelevant
    if i % 2 == 0:
        drift_analysis.append(val * 0.05)

# Benchmark weights with misleading normalization
benchmark_weights = {
    'raw_power': 0.35,
    'stability': 0.25,
    'consistency': 0.40
}

# Multi-metric evaluation with zip usage (required feature)
basic_metrics = [compute_efficiency_factor(event_sequence)]
additional_diagnostics = [sum(unique_roots) * 0.7]
diagnostic_pairs = list(zip(basic_metrics, additional_diagnostics))

# Final scoring logic buried in abstraction
def evaluate_performance(metrics, weights):
    raw_power = metrics[0]
    stability = sum(unique_roots) * 0.3
    consistency = 0
    
    # Simulate historical comparisons (distractor loop)
    historical_baselines = [12.5, 13.2, 11.8, 14.1, 10.9]
    improvement_trend = 0
    for i in range(len(historical_baselines) - 1):  # Another enumerate alternative
        if historical_baselines[i+1] > historical_baselines[i]:
            improvement_trend += 1

    # Actual consistency calculation
    temp_vals = []
    for item in event_sequence:
        if isinstance(item, tuple):
            inner_stack = [item]
            while inner_stack:
                elem = inner_stack.pop()
                if isinstance(elem, tuple):
                    inner_stack.extend(elem)
                else:
                    temp_vals.append(elem)
    consistency = len(temp_vals) * 0.6

    # Weighted score computation
    weighted_sum = (
        raw_power * weights['raw_power'] +
        stability * weights['stability'] +
        consistency * weights['consistency']
    )
    
    # Apply set-derived bonus (actual relevance)
    bonus_multiplier = 1 + (len(unique_roots) * 0.01)
    return int(weighted_sum * bonus_multiplier)

# Execute main logic
efficiency_baseline = compute_efficiency_factor(event_sequence)
final_score = evaluate_performance([efficiency_baseline], benchmark_weights)

print(f"Target result: {final_score}")