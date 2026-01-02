def analyze_contributions(values):
    # Irrelevant computation: computes sum of squares but not used in final result
    sum_of_squares = sum(x ** 2 for x in values)
    adjusted = [v * 1.05 for v in values if v > 10]
    return adjusted

# Decoy data structures
decoys = {
    'outliers': [999, 888, 777],
    'noise_floor': 0.001,
    'weights': (0.1, 0.2, 0.3),
    'flags': set([True, False])
}

baseline_data = [12, 15, 18, 21, 24]
metric_set = {6, 12, 18, 24, 30}  # Used in intersection

# Misleading transformation chain
transformed = []
for x in baseline_data:
    temp_val = x // 2
    if temp_val % 3 == 0:
        transformed.append(temp_val * 2)

# Dead code path with side-effect-free operations
def unused_helper(data):
    cumulative = 0
    for item in data:
        cumulative += item << 1
    return cumulative

# Simulate historical logs - irrelevant to main logic
historical_logs = []
for i in range(5):
    entry = f"log_{i}: status=active"
    historical_logs.append(entry)

# Complex but partially irrelevant set and list processing
temp_results = []
for val in baseline_data:
    if val in metric_set:
        temp_results.append(val)

# Compute redundant metrics
redundant_total = sum(baseline_data) // len(baseline_data)  # integer division
redundant_total = redundant_total * 2 + 5

# Set operations: actual relevant logic begins here
def evaluate_performance(metrics, base):
    # Step 1: filter base values present in metric threshold
    valid_points = [b for b in base if b in metrics]
    
    # Step 2: apply scaling via recursion (simple recursion)
    def recursive_scale(n, factor=1.1):
        if n <= 1:
            return 1
        return factor * recursive_scale(n - 1)
    
    # Step 3: compute scaled contributions
    scaled_vals = []
    for v in valid_points:
        scale_factor = recursive_scale(v // 6)  # depends on magnitude
        scaled_vals.append(v * scale_factor)
    
    # Step 4: use set difference to eliminate duplicates conceptually
    unique_candidates = set(scaled_vals)
    decoy_set = {min(scaled_vals), max(scaled_vals)}
    filtered_set = unique_candidates - decoy_set  # removes min and max
    
    # Step 5: aggregate remaining values
    raw_score = sum(filtered_set)
    
    # Step 6: normalization using string-derived constant (string manipulation red herring)
    version_tag = 'v2.4-release'
    norm_factor_str = ''.join(filter(str.isdigit, version_tag))  # '244'
    norm_factor = int(norm_factor_str) / 100  # 2.44
    
    # Step 7: finalize score
    final = raw_score / norm_factor
    
    # Step 8: rounding based on integer division logic
    rounded = int(final + 0.5) if final >= 0 else int(final - 0.5)
    
    return rounded

# Key statement
final_score = evaluate_performance(metric_set, baseline_data)

# Output result as required
print(f"Result: {final_score}")