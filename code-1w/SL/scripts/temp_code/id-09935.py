import itertools

# Simulate sensor fusion system with weighted metric evaluation
def evaluate_performance(weights, readings):
    # Preprocess: normalize readings using min-max scaling
    flat_readings = list(itertools.chain.from_iterable(readings))
    min_val, max_val = min(flat_readings), max(flat_readings)
    
    normalized = [[(x - min_val) / (max_val - min_val + 1e-8) for x in row] for row in readings]

    # Misleading intermediate: entropy calculation (not used in final score)
    entropy_lambda = lambda data: sum(-x * __import__('math').log(x + 1e-8) for x in data)
    _ = [entropy_lambda(row) for row in normalized]  # dead computation

    # Weighted aggregation by metric
    aggregated = []
    for i, weight in enumerate(weights):
        if weight > 0.1:
            smoothed = sum(normalized[i]) / len(normalized[i])
            adjusted = smoothed * (1 + weight) ** 1.5
            aggregated.append(adjusted)
        else:
            aggregated.append(0)

    # Secondary distraction: simulate confidence intervals (unused)
    ci_lower = [val * 0.92 for val in aggregated]
    ci_upper = [val * 1.08 for val in aggregated]
    _ = [(lo + hi) / 2 for lo, hi in zip(ci_lower, ci_upper)]  # irrelevant re-centering

    # Final fusion logic
    base_score = sum(aggregated)
    penalty = 0
    for i in range(len(aggregated)):
        if i > 0 and abs(aggregated[i] - aggregated[i-1]) > 0.3:
            penalty += 0.1
    
    final = base_score * 100 - penalty * 50
    
    # Key distractor: redundant transformation
    _temp_result = final * 1.0  # no effect
    _debug_log = {'raw': readings, 'norm': normalized, 'agg': aggregated}  # unused debug

    return int(round(final))

# Input data: multi-sensor readings across time steps
sensor_metrics = [
    [85, 90, 87],  # temperature consistency
    [76, 74, 75],  # pressure stability
    [95, 93, 94],  # humidity accuracy
    [60, 62, 58]   # vibration levels (lower is better)
]

# Metric importance weights (dynamic based on calibration)
metric_weights = [0.25, 0.20, 0.30, 0.05]

# Auxiliary distraction: hypothetical scenario simulation (never invoked)
def predict_outcome(seq, factor=1.1):
    growth = lambda x: x * factor
    return [list(map(growth, s)) for s in seq]

# Unused state tracker
historical_bias = {"offset": 0.03, "decay": 0.98}

# Core execution point
final_score = evaluate_performance(metric_weights, sensor_metrics)

# Output result as required
print(f"Result: {final_score}")