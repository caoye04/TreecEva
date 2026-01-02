from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_diagnostics():
    readings = [105, 203, 189, 203, 99, 99, 150, 189]
    stats = defaultdict(int)
    for val in readings:
        stats[val] += 1
    return dict(stats)

# Auxiliary function to compute entropy (unused but adds distraction)
def compute_entropy(data):
    from math import log2
    total = sum(data.values())
    entropy = 0
    for count in data.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Core logic for performance evaluation
def evaluate_metric(base: int, multiplier: float) -> float:
    temp = base * 0.87
    adjusted = temp + (base % 10) * 0.1
    return adjusted * multiplier

def apply_correction(value: float, mode: str) -> float:
    if mode == "aggressive":
        return value * 1.1
    elif mode == "conservative":
        return value * 0.95
    return value

# Main processing pipeline
diagnostic_data = collect_diagnostics()
frequency_map = {k: v for k, v in diagnostic_data.items()}

# Misleading intermediate calculations
repeated_values = [k for k, v in frequency_map.items() if v > 1]
duplicate_count = len(repeated_values)
placeholder_result = sum(repeated_values) / duplicate_count if duplicate_count else 0

# Real metric components
raw_counts = list(frequency_map.values())
total_observations = sum(raw_counts)
unique_sensors = len(frequency_map)

# Weighted scoring setup
metric_weights = {
    'stability': 0.3,
    'consistency': 0.25,
    'coverage': 0.2,
    'reliability': 0.25
}

raw_results = {
    'stability': evaluate_metric(total_observations, 1.0),
    'consistency': evaluate_metric(unique_sensors, 2.0),
    'coverage': len([v for v in raw_counts if v >= 2]) * 10,
    'reliability': sum([k*v for k,v in frequency_map.items()]) / total_observations
}

# Apply non-linear correction using lambda (real usage)
correct_fn = lambda x: round(x ** 0.5, 3)
for key in raw_results:
    raw_results[key] = correct_fn(raw_results[key] * metric_weights[key])

# Final score computation
weighted_sum = 0
for key in metric_weights:
    weighted_sum += raw_results[key]

final_score = int(round(weighted_sum * 10))

# Distractor: unused transformation chain
shadow_buffer = [evaluate_metric(k, 0.1) for k in frequency_map.keys()]
shadow_score = sum(shadow_buffer) // 2
normalization_factor = apply_correction(1.0, "neutral")

print(f"Result: {final_score}")