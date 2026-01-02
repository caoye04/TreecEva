import itertools

# Simulated sensor data processing with performance evaluation
raw_readings = [0.88, 0.92, 0.76, 0.94, 0.85, 0.81, 0.90]
decoy_readings = [x ** 2 for x in raw_readings if x > 1]  # Dead logic: no values > 1

# Noise filtering using moving average (irrelevant to final result)
def apply_filter(data, window=3):
    filtered = []
    for i in range(len(data) - window + 1):
        filtered.append(sum(data[i:i+window]) / window)
    return filtered

filtered_data = apply_filter(raw_readings)  # Computed but unused later

# System health indicators (some are red herrings)
health_flags = {'temp': 'nominal', 'pressure': 'high', 'vibration': 'ok'}
flag_scores = {'nominal': 1, 'ok': 1, 'caution': 0.5, 'high': -1, 'critical': -2}

# Misleading health score calculation (not used in final path)
health_risk = sum(flag_scores.get(v, 0) for v in health_flags.values())

# Core metric transformation pipeline
transform = lambda x: round((x - 0.7) * 100)  # Normalize relative to baseline

# Apply transformation only to qualifying readings
valid_indices = [i for i, x in enumerate(raw_readings) if x >= 0.8]
adjusted_metrics = [transform(raw_readings[i]) for i in valid_indices]

# Add dummy offset that looks important but is partially overridden
baseline_offset = len(valid_indices) * 2
offset_adjusted = [m + baseline_offset for m in adjusted_metrics]

temp_debug = [x for x in offset_adjusted if x > 30]  # Unused debugging artifact

# Weight assignment using itertools cycle (distractor usage)
weight_pattern = itertools.cycle([0.8, 1.1, 0.9])
weights = [next(weight_pattern) for _ in range(len(adjusted_metrics))]

# Decoy function that appears related but is never called
def compute_stress_factor(data):
    return max(data) - min(data) if len(data) > 1 else 0

# Secondary metrics with fake aggregation
auxiliary_metrics = {"jitter": 0.03, "drift": 0.07, "gain": 1.02}
aux_score = sum(abs(val) for val in auxiliary_metrics.values()) * 5  # Looks useful, isn't used

# Primary evaluation function with nested logic and closures
def evaluate_performance(metrics, weights):
    
    def get_multiplier(w):
        if w > 1.0:
            return 1.2
        elif w < 0.9:
            return 0.85
        else:
            return 1.0
    
    multipliers = [get_multiplier(w) for w in weights]
    
    # Simulate conditional activation based on threshold
    total = 0.0
    for i, metric in enumerate(metrics):
        if metric > 15:  # Only two metrics qualify
            contribution = metric * weights[i] * multipliers[i]
            total += contribution
        elif metric > 10:
            contribution = metric * weights[i] * 0.5  # Reduced impact
            total += contribution
        else:
            total += metric * 0.3  # Marginal contribution
    
    # Final nonlinear adjustment
    if total > 40:
        total = total * 0.9 + 5
    else:
        total = total * 1.1
    
    return int(round(total))

# Spurious post-processing that does nothing
def finalize_result(x):
    return x + 0  # No-op

# Critical execution point
final_score = evaluate_performance(adjusted_metrics, weights)

# Output required format
print(f"Result: {final_score}")