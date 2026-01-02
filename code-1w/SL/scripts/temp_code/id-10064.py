def analyze_efficiency(data, thresholds):
    efficiency_list = []
    for i, val in enumerate(data):
        if val > thresholds[i % len(thresholds)]:
            efficiency_list.append(val * 0.85)
        else:
            efficiency_list.append(val * 1.15)
    return efficiency_list


def transform_metrics(raw_values):
    transformed = []
    offset = 3
    for idx, v in enumerate(raw_values):
        if idx % 2 == 0:
            transformed.append(v ** 0.5 + offset)
        else:
            transformed.append(v / 2.5 - offset)
    # Dead code path - irrelevant to final result
    if len(transformed) > 100:
        return [x * 1.5 for x in transformed]
    return transformed

# Irrelevant helper function (decoy)
def predict_trend(values):
    trend = sum(values) / len(values)
    if trend > 50:
        return "upward"
    else:
        return "downward"

# Unused data structures (red herring)
baseline_profiles = {
    'A': [10, 20, 30],
    'B': [15, 25, 35],
    'C': [12, 24, 36]
}

historical_cache = set()
for k in baseline_profiles:
    historical_cache.add(len(baseline_profiles[k]))

# Real input data
raw_input = [49, 81, 100, 64, 121]

# Distractor: complex but unused transformation chain
shadow_copy = raw_input.copy()
for i in range(len(shadow_copy)):
    shadow_copy[i] = (shadow_copy[i] + 10) * 2
    if shadow_copy[i] > 200:
        shadow_copy[i] = shadow_copy[i] // 3

# Transform the real input
treated_metrics = transform_metrics(raw_input)

# Another decoy operation using zip and enumerate (partially relevant appearance)
comparison_pairs = []
for idx, (a, b) in enumerate(zip(treated_metrics, treated_metrics[1:])):
    diff = abs(a - b)
    comparison_pairs.append((idx, diff))
    # This modifies nothing; just adds noise
    if diff > 5:
        continue

# Weighting system (some weights are misleading)
weights = [0.1, 0.3, 0.5, 0.4, 0.2]
external_factors = {"impact": 1.05, "bias": -0.02}  # Not used directly

# Critical function with multiple concepts
def evaluate_performance(metrics, w):
    normalized = []
    base_sum = sum(metrics)
    
    # Use of set operations (irrelevant branch)
    seen_values = set()
    dup_check = set()
    for m in metrics:
        if m in seen_values:
            dup_check.add(m)
        seen_values.add(m)
    
    # Actual computation path
    for i, m in enumerate(metrics):
        adjusted = m * w[i]
        if i % 2 == 1 and adjusted > 20:
            adjusted *= 0.9
        normalized.append(adjusted)
    
    # Complex conditional aggregation
    total = 0.0
    for i, val in enumerate(normalized):
        if i == 0:
            total += val * 1.1
        elif i == len(normalized) - 1:
            total += val * 0.95
        else:
            total += val
    
    # Final nonlinear adjustment
    if len(dup_check) == 0:
        total = total ** 1.05
    else:
        total = total ** 0.98
    
    return int(total)

# Secondary distraction: recursive function not affecting outcome
def calculate_depth(n):
    if n <= 1:
        return 1
    return n * calculate_depth(n - 2)

recursive_trace = []
for x in [5, 7, 9]:
    recursive_trace.append(calculate_depth(x))

# Core execution flow
metrics = analyze_efficiency(treated_metrics, [7.0, 8.5, 6.0])
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")