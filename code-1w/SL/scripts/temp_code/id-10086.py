from collections import defaultdict

# Simulate system performance metrics over time
time_logs = [
    {'cpu': 75, 'mem': 80, 'disk': 40, 'net': 30},
    {'cpu': 85, 'mem': 82, 'disk': 45, 'net': 35},
    {'cpu': 90, 'mem': 85, 'disk': 50, 'net': 40},
    {'cpu': 92, 'mem': 88, 'disk': 55, 'net': 42}
]

# Irrelevant backup configuration (distractor)
backup_schedule = defaultdict(lambda: 'daily')
backup_schedule['critical'] = 'hourly'
backup_schedule['archival'] = 'weekly'

# Weighted scoring system for performance evaluation
weights = {'cpu': 0.4, 'mem': 0.3, 'disk': 0.2, 'net': 0.1}

# Historical thresholds (mostly unused - distraction)
historical_max = {resource: 0 for resource in weights}
for log in time_logs:
    for k in log:
        if k in historical_max and log[k] > historical_max[k]:
            historical_max[k] = log[k]

# Compute rolling averages
rolling_avg = defaultdict(float)
for resource in weights:
    total = sum(log[resource] for log in time_logs)
    rolling_avg[resource] = total / len(time_logs)

# Normalize values to a base-100 scale with offset
normalized = {r: int((rolling_avg[r] / 100) * 100) for r in rolling_avg}

# Apply bitwise adjustment based on even/odd pattern (semi-relevant)
adjusted = {}
for r, v in normalized.items():
    if v % 2 == 0:
        adjusted[r] = v ^ 3  # XOR with 3 for even values
    else:
        adjusted[r] = v | 1   # Ensure odd stays odd

# Dummy transformation function (not used in final path)
def transform_value(x, method='linear'):
    if method == 'quadratic':
        return x ** 2
    elif method == 'logarithmic':
        from math import log
        return log(x + 1)
    return x + 10  # default case (dead code)

# Core evaluation logic
metrics = {r: adjusted[r] for r in weights}  # Use adjusted metrics

# Secondary adjustment: shift based on index (irrelevant but looks important)
dummy_shift = 0
for i, val in enumerate(metrics.values()):
    dummy_shift += (val >> i) & 1  # bit-shift distraction

# Final performance score calculation
effective_metrics = {r: metrics[r] + (i % 2) for i, r in enumerate(metrics)}  # minor tweak

# Evaluate weighted performance
weighted_sum = 0.0
for resource, base_val in effective_metrics.items():
    weight = weights[resource]
    weighted_sum += base_val * weight

# Final scaling with ceiling
final_score = int(weighted_sum * 1.1)  # Boost by 10%

# Print result as required
print(f"Result: {final_score}")