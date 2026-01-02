from collections import defaultdict

# Simulated system metrics over time
time_logs = [
    {'cpu': 70, 'mem': 45, 'disk': 20, 'network': 30},
    {'cpu': 85, 'mem': 60, 'disk': 25, 'network': 35},
    {'cpu': 90, 'mem': 80, 'disk': 30, 'network': 40},
    {'cpu': 65, 'mem': 50, 'disk': 35, 'network': 45},
    {'cpu': 95, 'mem': 85, 'disk': 40, 'network': 50}
]

# Thresholds for performance grading
thresholds = defaultdict(lambda: 80)
thresholds['disk'] = 35  # Disk has a lower threshold
thresholds['network'] = 42

# Weighting factors for each metric
weights = {'cpu': 0.4, 'mem': 0.3, 'disk': 0.2, 'network': 0.1}

# Auxiliary tracking (distractor variables)
cpu_spike_count = 0
degradation_warnings = []
baseline_shift = 0.0

# Historical averages (not used in final logic but looks relevant)
historical_avg = defaultdict(float)
for key in ['cpu', 'mem', 'disk', 'network']:
    historical_avg[key] = sum(entry[key] for entry in time_logs) / len(time_logs)

# Compute rolling window peaks (irrelevant but plausible)
peak_values = defaultdict(int)
for log in time_logs:
    for k, v in log.items():
        if v > peak_values[k]:
            peak_values[k] = v

# Misleading normalization attempt
normalized_offsets = {}
for k in weights.keys():
    normalized_offsets[k] = round((peak_values[k] - historical_avg[k]) / historical_avg[k], 3)

# Real processing begins here
exceedance_count = defaultdict(int)
for log in time_logs:
    for metric, value in log.items():
        if value > thresholds[metric]:
            exceedance_count[metric] += 1

# Calculate penalty points based on exceedances
penalty_points = 0
for metric, count in exceedance_count.items():
    penalty_points += count * 10

# Performance grade per metric (only cpu and mem matter in final score)
effective_grade = 0
effective_grade += (100 - exceedance_count['cpu'] * 5) * weights['cpu']
effective_grade += (100 - exceedance_count['mem'] * 5) * weights['mem']

# Unused intermediate calculations (distractors)
marginal_loss = (exceedance_count['disk'] + exceedance_count['network']) * 2.5
compounded_risk_factor = max(normalized_offsets.values()) * penalty_points / 10

# Final evaluation function
def evaluate_performance(data):
    base = effective_grade
    adjustment = 10 if exceedance_count['cpu'] < 3 else -5
    resilience_bonus = 5 if peak_values['network'] > 45 else 0  # Not triggered
    stability_penalty = -10 if cpu_spike_count > 2 else 0      # cpu_spike_count is never updated
    return int(base + adjustment + stability_penalty)

# Critical execution point
final_score = evaluate_performance(time_logs)

print(f"Result: {final_score}")