from collections import defaultdict, Counter
import math

# Simulated system metrics over time (real data)
timestamped_metrics = [
    {'time': 1, 'cpu': 75, 'mem': 60, 'disk': 20, 'active_users': 150},
    {'time': 2, 'cpu': 80, 'mem': 65, 'disk': 25, 'active_users': 160},
    {'time': 3, 'cpu': 90, 'mem': 70, 'disk': 30, 'active_users': 170},
    {'time': 4, 'cpu': 85, 'mem': 75, 'disk': 35, 'active_users': 165},
    {'time': 5, 'cpu': 70, 'mem': 55, 'disk': 15, 'active_users': 140}
]

# Irrelevant telemetry (distractor data)
sensor_noise = [0.12, 0.33, 0.05, 0.88, 0.41, 0.99, 0.01, 0.76, 0.22, 0.54]
fake_checksums = {f'log_{i}': (i * 17) % 256 for i in range(20)}
metadata_cache = defaultdict(lambda: 'unknown')
for i in range(5):
    metadata_cache[f'node_{i}'] = f'state_{i % 3}'

# Real processing begins here
metric_data = []
for entry in timestamped_metrics:
    normalized_load = (entry['cpu'] * 0.5 + entry['mem'] * 0.3 + entry['disk'] * 0.2) / 100
    metric_data.append({
        'load_index': round(normalized_load, 3),
        'user_scale': math.log(entry['active_users'], 10),
        'efficiency': entry['cpu'] / (entry['mem'] + 1) if entry['mem'] > 50 else 0
    })

# Decoy transformation chain (dead path)
efficiency_stats = defaultdict(list)
for md in metric_data:
    efficiency_stats['values'].append(md['efficiency'])
efficiency_stats['avg'] = sum(efficiency_stats['values']) / len(efficiency_stats['values'])

# Secondary distraction: set operations on irrelevant tags
tags_a = {f'host{i}' for i in range(10) if i % 2 == 0}
tags_b = {f'host{i}' for i in range(10) if i < 7}
overlap_hosts = tags_a & tags_b  # unused later

# Conditional logic with red herring branches
penalty_factor = 0
if len(metric_data) > 4:
    peak_load = max(md['load_index'] for md in metric_data)
    if peak_load > 0.8:
        penalty_factor = 0.9
    elif peak_load > 0.7:
        penalty_factor = 0.95
    else:
        penalty_factor = 1.0
else:
    penalty_factor = 1.0  # unreachable but present

# Bonus calculation with misleading intermediate steps
raw_bonus = 0
for i, md in enumerate(metric_data):
    if md['user_scale'] > 2.1:
        raw_bonus += md['load_index'] * (i + 1)
    else:
        raw_bonus -= 0.05  # minor penalty

bonus_multiplier = math.ceil(raw_bonus * 10) / 10  # rounds to nearest 0.1

# Core evaluation function (relevant)
def evaluate_performance(metrics, bonus_mult):
    base_score = 0
    load_trend = []
    for m in metrics:
        base_score += m['load_index'] * m['user_scale']
        load_trend.append(m['load_index'])
    
    # Trend analysis distraction (partially used)
    increasing = 0
    for i in range(1, len(load_trend)):
        if load_trend[i] > load_trend[i-1]:
            increasing += 1
    trend_boost = 1.05 if increasing >= 3 else 1.0
    
    # Final composition
    raw_final = base_score * bonus_mult * trend_boost * penalty_factor
    
    # Apply artificial cap (distractor)
    if raw_final > 100:
        raw_final = 95  # never triggered
    
    return int(round(raw_final * 10)) / 10.0

# Critical execution point
final_score = evaluate_performance(metric_data, bonus_multiplier)

# Output requirement
print(f"Target result: {final_score}")