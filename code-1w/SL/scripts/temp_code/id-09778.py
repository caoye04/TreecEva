import itertools

def analyze_response(time_series, threshold=0.5):
    smoothed = [sum(time_series[i:i+3]) / 3 for i in range(len(time_series) - 2)]
    anomalies = [i for i, val in enumerate(smoothed) if val > threshold]
    return anomalies if anomalies else [0]

# Simulate sensor feedback over time
time_data = [0.1, 0.4, 0.6, 0.7, 0.3, 0.2, 0.8, 0.9, 0.1]

# Misleading preprocessing: unused transformation
distorted_data = [round(x**2 + 0.1, 2) for x in time_data]  # Distractor
offset_adjustment = sum([x for x in distorted_data if x > 0.5])  # Semi-relevant but unused

# Critical analysis step
trigger_points = analyze_response(time_data, threshold=0.45)

# Simulate corrective actions based on triggers
actions_taken = []
baseline_shift = 0.0
for tp in trigger_points:
    adjustment = (tp % 3) * 0.1
    baseline_shift += adjustment
    actions_taken.append(f"Adjust-{tp}")

# Auxiliary state tracking (some values used later)
state_log = {"triggers": len(trigger_points), "actions": len(actions_taken), "shift": baseline_shift}

# Generate performance metrics across dimensions
metrics = [
    len(trigger_points) * 1.5,
    state_log["shift"] * 10,
    len(actions_taken) + state_log["triggers"]
]

# Use lambda and conditional expression to filter effective outcomes
eval_metric = lambda m: m > 2.0
valid_metrics = list(filter(eval_metric, metrics))

# Compute redundancy score (unused distractor)
redundancy_pairs = list(itertools.combinations_with_replacement(valid_metrics, 2))
redundancy_score = sum(abs(a - b) for a, b in redundancy_pairs) / (len(redundancy_pairs) or 1)

# Core aggregation logic
aggregate_performance = lambda fb: (
    sum(valid_metrics) + state_log["triggers"] * 0.5
    if fb else 0
)

# Introduce conditional data flow
feedback_loop = len(trigger_points) > 0

# Final computation — key execution point
final_score = aggregate_performance(feedback_loop)

# Print result as required
print(f"Result: {final_score}")