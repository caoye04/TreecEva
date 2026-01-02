def analyze_trends(data, threshold=0.5):
    trend_list = []
    for i, value in enumerate(data):
        if value > threshold:
            trend_list.append((i, value * 1.2))
        elif value < -threshold:
            trend_list.append((i, value * 0.8))
    return trend_list

# Irrelevant helper function (decoy)
def calculate_projection(x):
    return (x ** 2) + 3 * x - 7

# Unused transformation map
transform_map = {i: calculate_projection(i) for i in range(-10, 10)}

# Real data stream
raw_signals = [0.3, 0.6, -0.2, 0.9, -0.7, 0.1]

# Distractor: complex-looking but unused signal processing
filtered = [x for x in raw_signals if abs(x) > 0.25]
scaled_filtered = list(map(lambda v: v * 1.5, filtered))

# Actual relevant data preparation
event_flags = [1 if x > 0.4 else 0 for x in raw_signals]
indexed_events = list(enumerate(event_flags))

# Simulate system state with decoy dictionary
system_state = {
    'version': '2.1.0',
    'mode': 'debug',
    'cache_hit': False,
    'last_updated': '2023-11-05',
    'temp_calib': [0.1, 0.4, 0.7],
    'debug_trace': [analyze_trends(raw_signals), scaled_filtered]  # unused
}

# Core logic disguised among distractions
baseline = {'alpha': 0.6, 'beta': -0.3, 'gamma': 0.4}
metric_data = {
    'alpha': raw_signals[1],
    'beta': raw_signals[4],
    'gamma': raw_signals[3]
}

# Secondary distraction: fake weight adjustment
weights = {k: abs(v) ** 0.5 for k, v in baseline.items()}
adjusted_metrics = {k: v * weights[k] for k, v in metric_data.items()}  # looks important, not used

# Real evaluation logic hidden in complexity
def evaluate_performance(metrics, reference):
    score = 0
    discrepancies = []
    for key in metrics:
        ref_val = reference[key]
        actual_val = metrics[key]
        diff = actual_val - ref_val
        discrepancies.append(diff)
        if abs(diff) < 0.1:
            score += 10
        elif diff > 0:
            score += 5
        else:
            score -= 3
    
    # Additional logic branch that seems significant but only one case applies
    if len(discrepancies) == 3:
        variance = sum(d**2 for d in discrepancies) / 3
        if variance > 0.05:
            score -= int(variance * 20)
    
    # Hidden correction factor based on event_flags
    event_sum = sum(event_flags)
    if event_sum >= 2:
        score += 7  # critical adjustment
    
    return score

# Dead code path - never called
def legacy_evaluate():
    return sum(abs(x) for x in raw_signals) * 10

# Key execution point
final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Result: {final_score}")