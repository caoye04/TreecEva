from itertools import compress, cycle
import math

def analyze_pattern(sequence):
    # Irrelevant helper function analyzing frequency (not used in final result)
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in freq.items() if v > 1}

def smooth_data(data_stream):
    # Distractor: applies moving average but unused
    smoothed = []
    window = 3
    for i in range(len(data_stream) - window + 1):
        smoothed.append(sum(data_stream[i:i+window]) / window)
    return smoothed

def evaluate_threshold(value, limit=50, penalty_factor=0.8):
    # Semi-relevant logic, only called once with fixed args
    if value > limit:
        return value * penalty_factor
    return value

# Simulated assessment scores and corresponding weight multipliers
assessments = [88, 92, 76, 85, 94, 80]
weights = [0.1, 0.15, 0.1, 0.25, 0.2, 0.2]

# Irrelevant transformations
binary_flags = [x > 85 for x in assessments]
disabled_mask = [not bit for bit in binary_flags]
filtered_assessments = list(compress(assessments, disabled_mask))  # Unused

# Misleading intermediate calculations
baseline_avg = sum(assessments) / len(assessments)
adjusted_baseline = evaluate_threshold(baseline_avg, 82)

# Use of lambda for dynamic scaling (actual usage in computation)
scale_fn = lambda x, w: round(x * w, 3)

# Complex weighted aggregation using itertools and lambdas
cyclic_weights = cycle(weights)
scaled_values = []
total_weight = 0.0

for score in assessments:
    w = next(cyclic_weights)
    scaled_values.append(scale_fn(score, w))
    total_weight += w

# Additional distractor: harmonic mean calculation (unused)
try:
    harmonic_mean = len(assessments) / sum(1/s for s in assessments if s != 0)
except ZeroDivisionError:
    harmonic_mean = 0

# Core logic: compute weighted sum and apply bonus logic based on consistency
weighted_sum = sum(scaled_values)
consistency_bonus = 5 if all(abs(assessments[i] - assessments[i+1]) < 15 for i in range(len(assessments)-1)) else 0

# Final performance score calculation
aggregate_performance = lambda data, wts: sum(scale_fn(s, w) for s, w in zip(data, wts))
final_score = aggregate_performance(assessments, weights)
final_score += consistency_bonus

# Apply ceiling cap if over threshold (no effect in this case)
if final_score > 95:
    final_score = min(final_score, 95)

Result: {final_score}