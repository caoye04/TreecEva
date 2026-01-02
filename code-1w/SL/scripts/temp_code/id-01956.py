from collections import defaultdict, Counter
import math

# Simulated sensor health data with redundant fields
data_source = [
    {'id': 'A', 'temp': 36.8, 'pulse': 70, 'noise': 0.003, 'status': 'active', 'backup_flag': False},
    {'id': 'B', 'temp': 39.1, 'pulse': 110, 'noise': 0.001, 'status': 'active', 'backup_flag': True},
    {'id': 'C', 'temp': 37.0, 'pulse': 68, 'noise': 0.002, 'status': 'inactive', 'backup_flag': False},
    {'id': 'D', 'temp': 40.3, 'pulse': 125, 'noise': 0.005, 'status': 'active', 'backup_flag': False},
    {'id': 'E', 'temp': 36.5, 'pulse': 60, 'noise': 0.001, 'status': 'active', 'backup_flag': True}
]

# Irrelevant preprocessing: noise filtering (never actually used)
filtered_noise = [entry['noise'] * math.exp(-0.1 * i) for i, entry in enumerate(data_source)]
smoothed_noise = sum(filtered_noise) / len(filtered_noise) if filtered_noise else 0

# Threshold configuration map with red herring keys
threshold_map = {
    'temp': {'normal': (36.1, 37.5), 'high_risk': 39.5},
    'pulse': {'tachy': 100, 'brady': 65},
    'dummy_scale': {'alpha': 0.8, 'beta': 1.2},  # decoy values
    'weights': {'temp': 0.6, 'pulse': 0.4}
}

# Extract relevant patient metrics (with extra baggage)
health_data = []
for record in data_source:
    temp = record['temp']
    pulse = record['pulse']
    status = record['status']
    flag = record['backup_flag']

    # Compute derived indices (some irrelevant)
    fever_score = (temp - 36.5) * 10
    stress_index = pulse / (temp + 1) if temp > 0 else 0
    risk_level = 'elevated' if temp > 37.5 or pulse > 100 else 'normal'

    # Store extended features including unused ones
    health_data.append({
        'node': record['id'],
        't': temp,
        'p': pulse,
        'risk': risk_level,
        'fever_score': fever_score,
        'stress': stress_index,
        'active': status == 'active',
        'flagged': flag or (temp > 38 and pulse > 90),
        'metadata': f"sensor_{record['id'].lower()}"
    })

# Decoy function: looks important but unused
def analyze_trend(data):
    trend_vector = []
    for i in range(1, len(data)):
        delta_t = data[i]['t'] - data[i-1]['t']
        delta_p = data[i]['p'] - data[i-1]['p']
        trend_vector.append((delta_t, delta_p))
    return [math.hypot(dx, dy) for dx, dy in trend_vector]

# Auxiliary structure with misleading aggregation
counter_decoy = Counter([pt['risk'] for pt in health_data])
status_breakdown = {k: v for k, v in counter_decoy.items()}

# Real processing begins: categorize by thresholds
abnormal_nodes = []
critical_count = 0

for pt in health_data:
    is_critical = False
    if pt['t'] >= threshold_map['temp']['high_risk']:
        is_critical = True
    if pt['p'] > 120:
        is_critical = True
    if pt['t'] > threshold_map['temp']['normal'][1] and pt['p'] > threshold_map['pulse']['tachy']:
        abnormal_nodes.append(pt['node'])
        if is_critical:
            critical_count += 1

# Secondary analysis with conditional expression distraction
alert_summary = [
    (pt['node'], 'RED' if pt['t'] > 38.5 and pt['p'] > 110 else 'AMBER' if pt['risk'] == 'elevated' else 'GREEN')
    for pt in health_data if pt['active']
]

# Dummy transformation using defaultdict (unused path)
summary_log = defaultdict(int)
for node, level in alert_summary:
    summary_log[level] += 1
    summary_log['total_alerts'] += 1  # Increment total

# Core logic: compute weighted deviation score only for active, abnormal nodes
valid_entries = [pt for pt in health_data if pt['active'] and pt['node'] in abnormal_nodes]

if valid_entries:
    temp_dev = sum((pt['t'] - 37.5) for pt in valid_entries)
    pulse_dev = sum((pt['p'] - 80) for pt in valid_entries)
    weight_t = threshold_map['weights']['temp']
    weight_p = threshold_map['weights']['pulse']
    composite_deviation = weight_t * temp_dev + weight_p * pulse_dev
else:
    composite_deviation = 0.0

# Final diagnostic computation incorporating dead code check
baseline_adjustment = math.log(smoothed_noise + 1) if smoothed_noise > 0 else 0  # Always near zero

# Key statement
final_diagnostic = process_metrics(health_data, threshold_map)

# Supporting function with nested logic and distractors
def process_metrics(data, config):
    # Unused intermediate calculations
    inactive_set = {d['node'] for d in data if not d['active']}
    flagged_only = [d for d in data if d['flagged'] and d['node'] not in inactive_set]

    # Real signal: count how many exceed both primary thresholds
    primary_risk = 0
    temp_high = config['temp']['normal'][1]
    pulse_high = config['pulse']['tachy']

    for entry in data:
        t_val = entry['t']
        p_val = entry['p']
        isActive = entry['active']

        # Compound condition with short-circuit potential
        if isActive and (t_val > temp_high) and (p_val > pulse_high):
            primary_risk += 1

    # Additional constraint: must NOT be flagged as backup to count
    filtered_risk = 0
    for entry in data:
        if (entry['active'] and 
            entry['t'] > temp_high and 
            entry['p'] > pulse_high and 
            not entry['flagged']):
            filtered_risk += 1

    # Distractor: complex tuple unpacking with no effect
    extremes = [(d['t'], d['p']) for d in data if d['t'] > 38 or d['p'] > 110]
    if extremes:
        max_temp, max_pulse = max(extremes, key=lambda x: x[0])
        scaled_peak = math.sqrt(max_temp**2 + max_pulse**2) // 10
    else:
        scaled_peak = 0

    # Critical formula: (filtered_risk * 100) + (scaled_peak * 10) + baseline from deviation
    raw_base = int(composite_deviation)
    result = (filtered_risk * 100) + (scaled_peak * 10) + raw_base

    # Dead code branch (never reached due to structure)
    if len(inactive_set) > 100:
        fallback = sum(len(d['metadata']) for d in data)
        result = fallback % 1000

    return result

# Print final result
print(f"Result: {final_diagnostic}")