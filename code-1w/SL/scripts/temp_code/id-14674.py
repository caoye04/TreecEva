from collections import defaultdict, Counter

# Simulated system metrics over time
timestamps = [100, 101, 102, 103, 104]
raw_metrics = [
    {'cpu': 75, 'mem': 80, 'disk': 40},
    {'cpu': 80, 'mem': 82, 'disk': 45},
    {'cpu': 90, 'mem': 85, 'disk': 50},
    {'cpu': 85, 'mem': 90, 'disk': 60},
    {'cpu': 95, 'mem': 95, 'disk': 70}
]

# Irrelevant historical cache (distractor)
cache_hits = [120, 125, 130]
cache_misses = [8, 10, 12]
historical_efficiency = {t: (h / (h + m)) for t, h, m in zip(timestamps[:3], cache_hits, cache_misses)}

# Data structure transformation pipeline
transformed = []
for i, metric in enumerate(raw_metrics):
    entry = defaultdict(float)
    entry['time'] = timestamps[i]
    entry['load'] = (metric['cpu'] + metric['mem']) / 2
    entry['stress'] = metric['cpu'] * 0.6 + metric['mem'] * 0.4
    entry['disk_util'] = metric['disk']
    transformed.append(entry)

# Compute rolling average (irrelevant for final result)
rolling_stress = []
window_size = 2
for i in range(len(transformed)):
    if i >= window_size - 1:
        avg = sum(transformed[j]['stress'] for j in range(i - window_size + 1, i + 1)) / window_size
        rolling_stress.append(avg)

# Misleading anomaly detection (dead path)
def detect_anomaly(data_list):
    anomalies = []
    for d in data_list:
        if d['cpu'] > 88 and d['mem'] > 88:
            anomalies.append(d['time'])
    return anomalies

# Unused function call (decoy)
anomalies_detected = detect_anomaly(raw_metrics)  # Not used later

# Aggregate stress levels by load bracket (distraction)
load_brackets = defaultdict(list)
for entry in transformed:
    bracket = (int(entry['load'] // 10) * 10)
    load_brackets[bracket].append(entry['stress'])

average_by_bracket = {k: sum(v)/len(v) for k, v in load_brackets.items()}

# Critical data preparation
metric_data = [entry['stress'] for entry in transformed]
baseline = 85.0

# Decoy statistical analysis
frequencies = Counter([round(md) for md in metric_data])
total_frequency = sum(frequencies.values())
mode_value = frequencies.most_common(1)[0][0]

# Dummy string processing (irrelevant but plausible)
system_log = "Performance check at multiple intervals: STRESS_HIGH, LOAD_MEDIUM, DISK_OK"
flags = system_log.lower().split()
trigger_words = [word for word in flags if '_' in word]

# Core evaluation logic buried in noise
def evaluate_performance(stress_values, threshold):
    above_count = 0
    cumulative = 0.0
    peak_penalty = 0

    for idx, val in enumerate(stress_values):
        if val > threshold:
            above_count += 1
            cumulative += val
        # Hidden logic: penalize if high stress follows another high stress
        if idx > 0 and stress_values[idx-1] > threshold and val > threshold:
            peak_penalty += 1

    # Complex scoring formula
    if above_count == 0:
        score = 50
    else:
        base = cumulative / above_count
        adjustment = above_count * 3
        penalty_factor = peak_penalty * 2.5
        score = base + adjustment - penalty_factor

    # Additional red herring: unused rounding branch
    if len(str(score).split('.')[1]) > 4 if '.' in str(score) else False:
        score = round(score, 4)
    
    return score

# Final computation — key execution point
final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Target result: {final_score}")