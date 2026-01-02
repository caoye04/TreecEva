from collections import defaultdict, Counter
import math

# Simulated system metrics over time
timestamped_metrics = [
    (100, {'cpu': 75, 'mem': 80, 'disk': 30}),
    (101, {'cpu': 82, 'mem': 85, 'disk': 32}),
    (102, {'cpu': 90, 'mem': 92, 'disk': 35}),
    (103, {'cpu': 88, 'mem': 87, 'disk': 34}),
    (104, {'cpu': 95, 'mem': 94, 'disk': 38})
]

# Irrelevant historical backup data (distractor)
historical_backups = {
    'weekly': [45, 50, 52],
    'monthly': [300, 310]
}

# Misleading auxiliary function (dead path)
def calculate_backup_load(snaps):
    total = 0
    for s in snaps:
        total += sum(s) * 0.1
    return total

# Decoy metric transformation (not used in final logic)
transformed = []
for ts, vals in timestamped_metrics:
    transformed.append({
        'time_norm': ts - 100,
        'load': math.sqrt(vals['cpu']**2 + vals['mem']**2) / 141.4
    })

# Extract sequences for analysis
cpu_sequence = [m[1]['cpu'] for m in timestamped_metrics]
mem_sequence = [m[1]['mem'] for m in timestamped_metrics]
disk_sequence = [m[1]['disk'] for m in timestamped_metrics]

def analyze_trend(data_seq):
    trend_scores = []
    for i in range(1, len(data_seq)):
        if data_seq[i] > data_seq[i-1]:
            trend_scores.append(1)
        elif data_seq[i] < data_seq[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return Counter(trend_scores)

# Analyze trends (some used, some not)
cpu_trend = analyze_trend(cpu_sequence)  # Used later
mem_trend = analyze_trend(mem_sequence)  # Partially used
disk_trend = analyze_trend(disk_sequence)  # Unused (distractor)

# Auxiliary scoring with red herring variables
base_weighting = defaultdict(float)
base_weighting['cpu_up'] = cpu_trend.get(1, 0) * 1.2
base_weighting['mem_stable'] = mem_trend.get(0, 0) * 0.8
base_weighting['disk_down'] = disk_trend.get(-1, 0) * 0.5  # Not actually impactful

# Complex multi-stage filtering process
filtered_peaks = []
critical_moments = []
temp_accumulator = 0

for i, val in enumerate(cpu_sequence):
    if val >= 85:
        temp_accumulator += val
        filtered_peaks.append(val)
        if val >= 90:
            critical_moments.append(i)

# Secondary structure with misleading aggregation
aggregated_diagnostics = {
    'peak_avg': temp_accumulator / len(filtered_peaks) if filtered_peaks else 0,
    'critical_count': len(critical_moments),
    'warning_flags': sum(1 for v in mem_sequence if v > 90),
    'ghost_metric': sum(1 for v in disk_sequence if v < 20)  # Always zero, distractor
}

# Core evaluation logic buried among noise
metric_data = {
    'peaks': filtered_peaks,
    'trend_bias': cpu_trend.get(1, 0) - cpu_trend.get(-1, 0),
    'stability': 5 - len([x for x in cpu_sequence if x > 90 and x != max(cpu_sequence)])
}

base_threshold = 3.5

# Key irrelevant intermediate (misleads with complex formula)
phantom_score = 0
for k, v in aggregated_diagnostics.items():
    phantom_score += v * 0.37

# Real but non-obvious answer computation path
def evaluate_performance(metrics, threshold):
    score = 0
    if metrics['trend_bias'] > 0:
        score += 10 * metrics['trend_bias']
    if len(metrics['peaks']) >= 3:
        score += 25
    # Hidden dependency on exact peak values
    sorted_peaks = sorted(metrics['peaks'], reverse=True)
    if len(sorted_peaks) >= 2:
        peak_diff = sorted_peaks[0] - sorted_peaks[1]
        score += 5 * (peak_diff // 5)  # Integer division bonus
    # Threshold modulation
    mod_factor = int(threshold * 2)
    score -= mod_factor
    return score

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Target result: {final_score}")