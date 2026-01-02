def analyze_metrics(data_stream):
    # Irrelevant signal processing
    filtered = [x for x in data_stream if x > 0.5]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    entropy = 0.0
    for val in normalized:
        if val > 0: entropy -= val * math.log(val)
    return sum(normalized) % 10

import math

def compute_robustness(index, pattern):
    # Misleading complexity: dead function (never used in critical path)
    temp = 0
    for i, p in enumerate(pattern):
        temp += (i + 1) * (p % 3) ** 2
    return temp % index if index != 0 else 0

# Distractor variables
system_load = [0.87, 0.92, 0.65, 0.73, 0.91]
cache_hits = {'level1': 428, 'level2': 119, 'level3': 67}
baseline_offset = 2.718
temporal_weights = [0.1, 0.3, 0.4, 0.2]  # Unused in logic

# Real data used in computation
feedback_sequence = [85, 90, 78, 92, 88]
benchmark_weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Red herring: complex-looking but irrelevant sorting permutation
sorted_pairs = sorted(enumerate(feedback_sequence), key=lambda x: x[1], reverse=True)
sorted_indices = [i for i, _ in sorted_pairs]
rank_adjustment = sum(i * idx for i, idx in enumerate(sorted_indices))  # Distractor

# Simulated calibration curve (unused)
def calibrate_input(seq):
    adjusted = []
    for s in seq:
        s = s + math.sin(math.pi * s / 100)
        adjusted.append(round(s, 2))
    return adjusted

# Core logic hidden among noise
intermediate_scores = []
for idx, (score, weight) in enumerate(zip(feedback_sequence, benchmark_weights)):
    if score >= 80:
        boosted = score * (1 + 0.05 * math.log(weight * 10 + 1))
        intermediate_scores.append(boosted * weight)
    else:
        intermediate_scores.append(score * weight)

# Conditional branch with misleading comment
# "Adjusting for latency bias" — actually just adds fixed offset
latency_bias = 0.0
if len(intermediate_scores) > 4:
    latency_bias = 0.11  # Minor adjustment

# Decoy list comprehension with string manipulation (irrelevant)
diagnostic_tags = ['ERR', 'OK', 'WARN']
status_log = [tag.lower() + '_' + str(len(tag)) for tag in diagnostic_tags if tag != 'ERR']

# Actual aggregation
raw_total = sum(intermediate_scores) + latency_bias

# Extra transformation to obscure result
scaling_factor = math.cos(math.radians(30))  # Constant ≈0.866
adjusted_total = raw_total / scaling_factor

# Final evaluation function (only this matters)
def evaluate_performance(scores, weights):
    base = 0.0
    for s, w in zip(scores, weights):
        penalty = 0.0
        if s < 80:
            penalty = (80 - s) * w * 0.1
        contribution = s * w - penalty
        base += contribution
    # Final nonlinear adjustment
    return int(base * 10 + 0.5)  # Simulates rounding to nearest int

# Key execution point
final_score = evaluate_performance(feedback_sequence, benchmark_weights)

# Output result as required
print(f"Result: {final_score}")