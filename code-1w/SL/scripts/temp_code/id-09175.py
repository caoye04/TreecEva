from collections import defaultdict, Counter
import math

# Simulate system performance metrics over time
timestamps = [100, 105, 110, 115, 120, 125, 130]
raw_data = [
    {'cpu': 70, 'mem': 45, 'disk': 200, 'req': 15},
    {'cpu': 85, 'mem': 50, 'disk': 180, 'req': 20},
    {'cpu': 90, 'mem': 60, 'disk': 160, 'req': 25},
    {'cpu': 88, 'mem': 62, 'disk': 170, 'req': 23},
    {'cpu': 92, 'mem': 75, 'disk': 150, 'req': 28},
    {'cpu': 94, 'mem': 80, 'disk': 140, 'req': 30},
    {'cpu': 96, 'mem': 82, 'disk': 130, 'req': 32}
]

# Extraneous tracking variables (distractors)
peak_cpu_window = 0
avg_disk_latency = 0.0
data_volume = []
transfer_rates = defaultdict(float)

# Process raw data into structured metrics
processed = defaultdict(list)
for entry in raw_data:
    processed['cpu_load'].append(entry['cpu'])
    processed['memory_usage'].append(entry['mem'])
    processed['disk_io'].append(entry['disk'])
    processed['request_rate'].append(entry['req'])

# Misleading intermediate calculations (not directly used)
for i, rate in enumerate(processed['disk_io']):
    if rate > 150:
        transfer_rates[timestamps[i]] = rate * 0.001

# Compute derived statistics (some are red herrings)
disk_trend = [processed['disk_io'][i+1] - processed['disk_io'][i] for i in range(len(processed['disk_io'])-1)]
request_growth = [processed['request_rate'][i] - processed['request_rate'][i-1] for i in range(1, len(processed['request_rate']))]

# Calculate moving average of CPU (unused but plausible)
cpu_moving_avg = []
window_size = 3
for i in range(len(processed['cpu_load']) - window_size + 1):
    window = processed['cpu_load'][i:i+window_size]
    cpu_moving_avg.append(sum(window) / window_size)

# Baseline thresholds for evaluation
baseline = {
    'cpu_threshold': 85,
    'mem_threshold': 70,
    'min_requests': 22
}

# Performance counter (key variable)
metrics = Counter()
for entry in raw_data:
    if entry['cpu'] > baseline['cpu_threshold']:
        metrics['high_cpu'] += 1
    if entry['mem'] > baseline['mem_threshold']:
        metrics['high_mem'] += 1
    if entry['req'] >= baseline['min_requests']:
        metrics['high_req'] += 1

# Auxiliary function with plausible but partially irrelevant logic
def analyze_trends(data_list):
    trend_changes = 0
    for i in range(1, len(data_list)):
        if (data_list[i] - data_list[i-1]) * (data_list[i-1] - data_list[i-2]) < 0 if i > 1 else False:
            trend_changes += 1
    return trend_changes

# Call to misleading function (distractor)
total_trend_shifts = analyze_trends(processed['cpu_load'])

# Core evaluation logic
overload_periods = 0
for i in range(len(raw_data)):
    if (raw_data[i]['cpu'] > baseline['cpu_threshold'] and 
        raw_data[i]['mem'] > baseline['mem_threshold'] and 
        raw_data[i]['req'] >= baseline['min_requests']):
        overload_periods += 1

# Final scoring function
def evaluate_performance(counts, base):
    # Complex formula with some dummy terms
    base_score = counts['high_cpu'] * 1.5
    bonus = counts['high_req'] * 0.8
    penalty = counts['high_mem'] * 0.5
    adjustment = math.log(overload_periods + 1)  # Depends on outer scope
    
    # Dummy calculation that looks important but isn't used
    hypothetical_max = len(timestamps) * 3
    efficiency_ratio = (counts['high_cpu'] + counts['high_req']) / hypothetical_max if hypothetical_max else 0
    
    # Actual score computation
    raw_score = base_score + bonus - penalty + adjustment
    normalized = int(round(raw_score * 2))  # Final transformation
    return normalized

# Critical execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")