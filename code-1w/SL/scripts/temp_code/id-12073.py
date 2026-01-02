from collections import defaultdict

# Simulate sensor data with some noise and redundancy
data = [
    {'type': 'temp', 'value': 23.5, 'status': 'ok'},
    {'type': 'pressure', 'value': 1013, 'status': 'ok'},
    {'type': 'temp', 'value': 24.1, 'status': 'ok'},
    {'type': 'humidity', 'value': 45, 'status': 'warning'},
    {'type': 'temp', 'value': 22.9, 'status': 'ok'},
    {'type': 'pressure', 'value': 1012, 'status': 'ok'},
    {'type': 'humidity', 'value': 47, 'status': 'ok'},
    {'type': 'temp', 'value': 24.3, 'status': 'ok'},
]

# Irrelevant helper to simulate preprocessing (adds distraction)
def smooth_values(values):
    if len(values) < 3:
        return values
    smoothed = []
    for i in range(len(values)):
        left = max(0, i-1)
        right = min(len(values), i+2)
        smoothed.append(sum(values[left:right]) / (right - left))
    return smoothed

# Misleading aggregation that isn't used later
redundant_stats = defaultdict(lambda: {'count': 0, 'total': 0})
for entry in data:
    redundant_stats[entry['type']]['count'] += 1
    redundant_stats[entry['type']]['total'] += entry['value']

# Unused transformation (dead code path)
if False:
    for key in redundant_stats:
        redundant_stats[key]['avg'] = (
            redundant_stats[key]['total'] / redundant_stats[key]['count']
        )

# Actual processing begins here
filtered_temps = [d['value'] for d in data if d['type'] == 'temp' and d['status'] == 'ok']
pressure_avg = sum(d['value'] for d in data if d['type'] == 'pressure') / len([d for d in data if d['type'] == 'pressure'])
humidity_warnings = len([d for d in data if d['type'] == 'humidity' and d['status'] == 'warning'])

# Apply smoothing to temperature (used in final calculation)
smoothed_temps = smooth_values(filtered_temps)

# Secondary distraction: unused frequency counter
type_counter = defaultdict(int)
for d in data:
    type_counter[d['type']] += 1

# Real logic: score based on temp stability, pressure baseline, and warnings
temp_variance = sum((t - pressure_avg/42)**2 for t in smoothed_temps) / len(smoothed_temps)
baseline_score = 100 - temp_variance * 2
adjustment_factor = (lambda x: 0.9 if x > 1012 else 1.1)(pressure_avg)
penalty = humidity_warnings * 15

# Final score computation
final_score = baseline_score * adjustment_factor - penalty

# Print result as required
print(f"Result: {final_score}")