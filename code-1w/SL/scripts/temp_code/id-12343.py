from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 45, 67, 200, 150, 89, 95, 110, 134, 178]
node_loads = [0.45, 0.67, 0.89, 0.34, 0.78, 0.56, 0.91, 0.23]
packet_loss_rates = [0.001, 0.003, 0.012, 0.002, 0.005, 0.015, 0.004, 0.008]

# Irrelevant data — red herring (not used in final calculation)
user_sessions = ["sess_001", "sess_002", "sess_003", "sess_004"]
session_data = {session: {'duration': i*30, 'active': True} for i, session in enumerate(user_sessions)}

# Distractor function — never called
def analyze_user_behavior(data):
    return sum(d['duration'] for d in data.values()) // len(data)

# Another decoy: complex but unused transformation
def transform_metrics(raw):
    shifted = [x * 1.5 + 2 for x in raw]
    filtered = [x for x in shifted if x > 50]
    return list(map(lambda y: y ** 0.5, filtered))

# Misleading intermediate variable (looks important but unused)
baseline_efficiency = sum(task_durations) / len(task_durations) * 0.78

# Real computation begins here
processed_durations = [d for d in task_durations if d < 180]  # filter outliers
duration_zscore = [(d - sum(processed_durations)/len(processed_durations)) / (sum((x - sum(processed_durations)/len(processed_durations))**2 for x in processed_durations)/len(processed_durations))**0.5 for d in processed_durations]

# Node performance scoring
load_risk = [1 if load > 0.8 else 0 for load in node_loads]
high_risk_nodes = sum(load_risk)

# Hidden relevant logic: count consecutive high-loss intervals
consecutive_high_loss = 0
max_consecutive = 0
for rate in packet_loss_rates:
    if rate > 0.005:
        consecutive_high_loss += 1
        max_consecutive = max(max_consecutive, consecutive_high_loss)
    else:
        consecutive_high_loss = 0

# Construct feature vector using slicing and zip
loss_slice = packet_loss_rates[1::2]  # every other element
load_slice = node_loads[:len(loss_slice)]
combined_stress = [l1 * l2 for l1, l2 in zip(loss_slice, load_slice)]

# Use of enumerate to track positions
stress_with_index = []
for idx, stress in enumerate(combined_stress):
    if stress > 0.0015:
        stress_with_index.append((idx, stress))

# Build metrics dictionary
metrics = defaultdict(float)
metrics['avg_duration'] = sum(processed_durations) / len(processed_durations)
metrics['z_variance'] = sum(z**2 for z in duration_zscore) / len(duration_zscore)
metrics['risk_count'] = high_risk_nodes
metrics['max_loss_streak'] = max_consecutive
metrics['stress_peaks'] = len(stress_with_index)

# Weights for evaluation (some are distractions)
weights = {
    'avg_duration': 0.3,
    'z_variance': 0.1,
    'risk_count': -0.2,  # negative impact
    'max_loss_streak': -0.25,
    'stress_peaks': 0.15,
    'dummy_metric': 0.05  # weight assigned to non-existent metric — red herring
}

# Decoy data structure — looks like it's used
historical_trends = [
    {'timestamp': t, 'value': baseline_efficiency * (0.95 ** t)} for t in range(5)
]

# Critical function that computes the real answer
def evaluate_performance(met, wgt):
    score = 0.0
    for key in met:
        if key in wgt:  # ignore keys not in weights
            contribution = met[key] * wgt[key]
            score += contribution
    # Additional penalty if too many high-risk nodes
    if met['risk_count'] >= 3:
        score -= 5.0
    # Bonus for low variance
    if met['z_variance'] < 1.0:
        score += 2.5
    return round(score, 6)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")