import itertools

# System diagnostics log processor - computes operational integrity score

def analyze_sequence(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

def generate_pairs(data):
    # Irrelevant utility - generates all pairs but not used in main logic
    return list(itertools.combinations(data, 2))

def filter_outliers(values, threshold=3.0):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) / std_dev < threshold]

# Unused recursive decoy function
def recursive_transform(n, depth=0):
    if depth > 5 or n < 1:
        return 0
    return n + recursive_transform(n // 2, depth + 1)

# Misleading data transformation chain
raw_metrics = [12, 8, 15, 23, 7, 19, 14, 6]
sorted_metrics = sorted(raw_metrics, reverse=True)
normalized = [x / max(sorted_metrics) for x in sorted_metrics]
adjusted = [round(x * 100) for x in normalized]  # Distractor: scaled to percentages but unused

# Simulated sensor confidence weights (some irrelevant)
confidence_levels = [0.9, 0.6, 0.8, 0.7, 0.95, 0.4, 0.65, 0.75]
reliability_weights = [w ** 2 for w in confidence_levels]  # Actual weight system

# Efficiency logs with red herring transformations
efficiency_logs = [22, 18, 25, 30, 14, 20, 24, 16]
efficiency_logs.append(sum(efficiency_logs[:3]))  # Artificial insertion - never used
shifted_logs = [x - 10 for x in efficiency_logs if x > 15]  # Dead code path
trimmed_logs = efficiency_logs[:len(reliability_weights)]  # Aligns lengths

# Decoy statistical analysis
mean_log = sum(trimmed_logs) / len(trimmed_logs)
variance = sum((x - mean_log) ** 2 for x in trimmed_logs) / len(trimmed_logs)
entropy_proxy = -sum(p * p for p in normalized if p > 0)  # Meaningless metric

# Core calculation buried in noise
weighted_efficiency = []
for i in range(len(trimmed_logs)):
    adjustment = 1.0
    if reliability_weights[i] > 0.7:
        adjustment = 1.2
    elif reliability_weights[i] < 0.5:
        adjustment = 0.8
    weighted_efficiency.append(trimmed_logs[i] * adjustment)

# Secondary weighting based on position parity (hidden logic)
position_multipliers = [1.1 if i % 2 == 0 else 0.9 for i in range(len(weighted_efficiency))]
final_contributions = [a * b for a, b in zip(weighted_efficiency, position_multipliers)]

# Accumulation using itertools (required feature) - only sum matters
accumulated = list(itertools.accumulate(final_contributions))
total_accumulation = accumulated[-1]

# Normalize against system baseline
baseline_reference = 18.5
integrity_factor = total_accumulation / baseline_reference

# Final aggregation with dummy control flow
if len(reliability_weights) == len(efficiency_logs):
    scaling_factor = 0.95
else:
    scaling_factor = 1.0  # Dead branch - condition false

intermediate_result = integrity_factor * scaling_factor

# Critical statement buried in multiple layers
final_score = int(round(intermediate_result))

# Output required result
print(f"Result: {final_score}")