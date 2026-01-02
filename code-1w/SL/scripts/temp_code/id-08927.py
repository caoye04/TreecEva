def analyze_component(x, threshold=5):
    # Irrelevant helper function (dead code path)
    return (x ** 2 + 3 * x + 1) % 17

# Distractor variables (irrelevant sensor data)
sensor_readings = [12, 45, 67, 23, 89, 34]
calibration_offsets = [0.1, -0.3, 0.4, 0.0, -0.2]
adjusted_values = [x + sum(calibration_offsets) for x in sensor_readings]

# Real input data disguised among noise
event_log = [
    {'type': 'click', 'priority': 3, 'active': True},
    {'type': 'hover', 'priority': 1, 'active': False},
    {'type': 'submit', 'priority': 8, 'active': True},
    {'type': 'scroll', 'priority': 2, 'active': True}
]

# Misleading aggregation (not used in final result)
total_priority = sum(e['priority'] for e in event_log if e['active'])
avg_priority = total_priority / len([e for e in event_log if e['active']]) if total_priority else 0

# Core weight mapping with lambda abstraction
weight_fn = lambda t: {'click': 1.2, 'hover': 0.5, 'submit': 2.0, 'scroll': 0.8}.get(t, 0.1)

# Bitwise obfuscation of thresholds (only one matters)
THRESHOLD_MASK = 0b1101
base_level = 7
computed_bound = (base_level ^ 5) & THRESHOLD_MASK  # evaluates to 2

# Data transformation chain
priorities = [e['priority'] for e in event_log]
types = [e['type'] for e in event_log]
activity_flags = [int(e['active']) for e in event_log]

# Zip and enumerate to create indexed feature set (core logic)
indexed_metrics = []
for i, (t, p, a) in enumerate(zip(types, priorities, activity_flags)):
    impact = p * weight_fn(t) * a
    # Red herring computation
    dummy_shift = (i << 2) | (p & 3)
    index_entry = (i, t, impact, dummy_shift, impact >> 1)
    indexed_metrics.append(indexed_metrics)

# Actual metrics used in evaluation (hidden among distractions)
raw_metrics = [p * a for p, a in zip(priorities, activity_flags)]
weights = [weight_fn(t) for t in types]

# Modular arithmetic decoy
mod_sum = sum(weights) % 13
scaling_factor = (mod_sum ** 2) % 11

# Real combination via weighted sum
combined_metric = sum(m * w for m, w in zip(raw_metrics, weights))

# Recursive normalization (only executes once due to condition)
def normalize_value(val, depth=0):
    if depth >= computed_bound or val <= 1.0:
        return val
    return normalize_value(val / 1.5, depth + 1)

normalized_score = normalize_value(combined_metric)

# Final performance evaluation using correct path
def evaluate_performance(metrics, weights):
    base = sum(metrics)
    adjustment = sum(w ** 0.5 for w in weights if w > 1.0) / 4
    return int(base + adjustment)  # deterministic integer output

# Critical execution point
final_score = evaluate_performance(metrics=raw_metrics, weights=weights)

# Print result as required
print(f"Target result: {final_score}")