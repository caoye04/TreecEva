def analyze_trend(data, threshold=0.5):
    trend_scores = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff > threshold:
            trend_scores.append(1.2)
        elif diff < -threshold:
            trend_scores.append(-0.8)
        else:
            trend_scores.append(0.1)
    return sum(trend_scores)

# Irrelevant auxiliary function (dead path)
def unused_helper(x):
    return x ** 2 + 3 * x - 7

# Misleading computation with decoy variables
total_aggregate = 0
for k in range(5):
    total_aggregate += k * 2

# Another red herring: complex but unused transformation
buffer_data = [i * 2 + 1 for i in range(10)]
processed = buffer_data[::2]
processed = [x for x in processed if x % 3 != 0]

# Real input data
metrics = [0.4, 0.7, 0.3, 0.9, 0.6]
weights = [1, 2, 1, 3, 2]

# Distractor: fake normalization (not used)
normalized_metrics = [m / max(metrics) for m in metrics]

# Auxiliary logic that feeds into final result
def calculate_weighted_sum(vals, wts):
    temp_sum = 0
    for v, w in zip(vals, wts):
        temp_sum += v * w
    return temp_sum

# Another distraction: simulated time series analysis (unused)
time_series = [0.1 * t + 0.05 * (t ** 1.5) for t in range(6)]
baseline_shift = sum(time_series) / len(time_series)

# Core logic hidden among noise
def adjust_for_bias(value, factor=0.95):
    return value * factor if value > 0.5 else value * 1.1

# Secondary processing chain
corrected_metrics = [adjust_for_bias(m) for m in metrics]

# More misdirection: unused data structure manipulation
history_log = {}
for idx, val in enumerate(corrected_metrics):
    history_log[f'entry_{idx}'] = val * 100

# Real evaluation function
def evaluate_performance(measures, importance):
    # Step 1: Apply weights
    weighted_total = calculate_weighted_sum(measures, importance)
    
    # Step 2: Apply trend bonus if positive momentum
    trend_value = analyze_trend(measures)
    bonus_eligible = trend_value > 1.0
    
    # Step 3: Adjustment based on spread
    variance_proxy = sum((x - 0.5) ** 2 for x in measures) / len(measures)
    stability_factor = 1.0 if variance_proxy < 0.05 else 0.85
    
    # Step 4: Final composition
    base_score = weighted_total * stability_factor
    if bonus_eligible:
        base_score += 2.5  # performance bonus
    
    # Irrelevant intermediate (distraction)
    dummy_score = sum(measures) * 10
    
    # Final adjustment
    final_component = base_score + 0.7  # minor offset
    return final_component

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")