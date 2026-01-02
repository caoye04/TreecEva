from itertools import compress, cycle
import math

def analyze_response_time(rt):
    # Irrelevant analysis function (dead code path)
    return rt > 0.5 and rt < 2.0

def calculate_entropy(data):
    # Unused complex calculation (distractor)
    total = sum(data)
    probabilities = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

def evaluate_stability(metric_vals):
    # Misleading intermediate computation
    diffs = [abs(a - b) for a, b in zip(metric_vals, metric_vals[1:])]
    return sum(diffs) < 0.5

def aggregate_performance(metrics, weights):
    # Core logic: weighted sum after threshold filtering
    filtered_metrics = [
        m if m >= 0.6 else 0.0
        for m in metrics
    ]
    
    # Apply cyclic weighting (relevant usage of cycle)
    weighted = [
        m * w 
        for m, w in zip(filtered_metrics, cycle(weights))
    ]
    
    # Sum only elements passing arbitrary condition (key step)
    valid_contributions = [
        w for w in weighted 
        if w >= 0.1
    ]
    
    base_score = sum(valid_contributions)
    
    # Bonus logic: add entropy-like adjustment (but simplified to deterministic)
    adjustment = 0.0
    if len(valid_contributions) > 2:
        adjustment = math.sqrt(valid_contributions[1]) if valid_contributions[1] > 0 else 0
    
    return base_score + adjustment

# Simulated system metrics (real input data)
system_metrics = [0.78, 0.45, 0.82, 0.91, 0.33, 0.67]

# Weight vector for performance aggregation
weights = [0.25, 0.35, 0.4]

# Irrelevant preprocessing (distractor)
normalized_metrics = normalize(system_metrics)

# Fake stability check (misleading boolean result)
is_stable = evaluate_stability(normalized_metrics)

# Decoy data structures
diagnostic_log = {
    'timestamps': list(range(100, 100 + len(system_metrics))),
    'raw_values': system_metrics,
    'thresholded': [x if x > 0.5 else None for x in system_metrics]
}

# Unused entropy calculation on constants (red herring)
entropy_probe = calculate_entropy([1, 2, 2, 1, 3])

# Lambda for dynamic filtering (actual use of lambda)
high_performer = lambda x: x >= 0.7

# Identify high performers (used in logic)
performance_flags = [high_performer(m) for m in system_metrics]

# Use itertools.compress to extract high-performing segments (relevant)
filtered_stream = list(compress(system_metrics, performance_flags))

# Secondary derived metric (partially relevant)
avg_high_perf = sum(filtered_stream) / len(filtered_stream) if filtered_stream else 0

# Modify one weight based on average (subtle but valid)
weights[0] = round(avg_high_perf * 0.5, 2)

# Core execution point
final_score = aggregate_performance(system_metrics, weights)

print(f"Result: {final_score}")