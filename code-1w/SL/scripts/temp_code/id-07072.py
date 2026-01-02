import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 2 == 0]

# Misleading metric calculation (not used in final result)
def false_metric(values):
    temp = sum([abs(v - 50) for v in values])
    adjustment = 0
    if temp > 100:
        adjustment = 10
    return temp + adjustment

# Distractor weight set (unused)
alt_weights = [0.1, 0.3, 0.4, 0.2]

# Real evaluation logic
def sigmoid(x):
    return 1 / (1 + math.exp(-x / 10))

def normalize(series):
    min_val, max_val = min(series), max(series)
    return [(x - min_val) / (max_val - min_val + 1e-8) for x in series]

def compute_efficiency(records):
    # Simulate efficiency from record lengths
    base = sum(len(r) for r in records)
    penalty = sum(1 for r in records if len(r) < 3)
    return base - penalty * 2

# Main scoring function
def evaluate_performance(metrics, weights):
    # Normalize metrics using list comprehension and slicing
    norm_metrics = normalize(metrics[:4])  # Only first 4 matter
    
    # Apply non-linear transformation with lambda
    transformed = list(map(lambda x: sigmoid(x * 100), norm_metrics))
    
    # Weighted combination
    score = sum(w * t for w, t in zip(weights, transformed))
    
    # Artificial complexity: conditional scaling (only triggers if score > 1, which it won't)
    if score > 1.0:
        scale_factor = 0.9
    else:
        scale_factor = 1.0
    
    return score * scale_factor

# Irrelevant data structures
dummy_logs = [
    [1, 2], [3, 4, 5], [], [6, 7], [8]
]

# Decoy variables
temp_result = None
intermediate_cache = {}

# Key input data
raw_metrics = [85, 92, 78, 96, 45, 67]  # Last two are ignored
weights = [0.25, 0.25, 0.25, 0.25]  # Equal weighting

# Side computation that looks important but isn't
aggregate_diagnostic = {
    'count': len(raw_metrics),
    'range': max(raw_metrics) - min(raw_metrics),
    'flagged': [x for x in raw_metrics if x < 80]
}

# Data preprocessing that affects final input
filtered_metrics = [m for m in raw_metrics if m >= 75]  # Remove low outliers

# Case conversion distraction (meaningless)
case_test = ''.join(chr(ord('A') + (m % 26)) for m in raw_metrics).lower().upper()

# Critical execution point
final_score = evaluate_performance(filtered_metrics, weights)

# Print result as required
print(f"Result: {final_score}")