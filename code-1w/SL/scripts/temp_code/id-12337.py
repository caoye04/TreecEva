def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Misleading preprocessing block (distractor)
raw_inputs = [0.1, 0.4, 0.35, 0.8, 0.6, 0.9, 0.75]
filtered = [x for x in raw_inputs if x > 0.3]
sorted_vals = sorted(filtered, reverse=True)
ranked = [(i+1, val) for i, val in enumerate(sorted_vals)]

# Actual relevant data
metrics = [0.85, 0.92, 0.78, 0.88, 0.91]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Decoy calculation with misleading intermediate result
temp_result = 0
for i in range(len(metrics)):
    temp_result += metrics[i] * (weights[i] + 0.05)  # Incorrect weight adjustment

# Conditional expression and slicing distraction
offset = len(metrics) > 4 ? 0.05 : 0.0  # Syntax error avoided: using Python ternary
offset = 0.05 if len(metrics) > 4 else 0.0
slice_preview = metrics[1:4]

# Core logic buried among distractors
efficiency_ratio = sum(m * w for m, w in zip(metrics, weights))
penalty_factor = 0.95 if efficiency_ratio > 0.8 else 0.9
adjusted_metrics = [m * penalty_factor for m in metrics]

# Another decoy structure
history_log = [{'epoch': i, 'value': m} for i, m in enumerate(metrics)]
summary_stats = {
    'max': max(metrics),
    'min': min(metrics),
    'span': len(metrics)
}

# Key function with nested logic and slicing
def aggregate_performance(mets, wgts):
    if len(mets) != len(wgts):
        raise ValueError("Mismatched dimensions")
    
    # Apply dynamic scaling based on position (slicing used)
    central_values = mets[1:-1]  # Exclude first and last
    base_score = sum(m * w for m, w in zip(mets, wgts))
    
    # Bonus logic with conditional expression
    bonus = 0.03 if all(x > 0.75 for x in central_values) else 0.01
    
    # Final aggregation
    final = base_score + bonus
    
    # Red herring: unused transformation
    transformed = [x**2 for x in wgts]
    total_transform = sum(transformed)
    
    return final

# Execution point of interest
final_score = aggregate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")