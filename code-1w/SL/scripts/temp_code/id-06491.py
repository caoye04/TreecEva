from collections import defaultdict, Counter
import math

# Simulated system performance metrics over time
timestamped_logs = [
    {'time': 1, 'cpu': 75, 'mem': 80, 'io': 30, 'err': 0},
    {'time': 2, 'cpu': 60, 'mem': 85, 'io': 35, 'err': 1},
    {'time': 3, 'cpu': 90, 'mem': 90, 'io': 50, 'err': 0},
    {'time': 4, 'cpu': 95, 'mem': 92, 'io': 60, 'err': 2},
    {'time': 5, 'cpu': 40, 'mem': 70, 'io': 25, 'err': 0}
]

# Irrelevant auxiliary function - dead code path (distractor)
def analyze_security_threats(logs):
    threat_level = 0
    for entry in logs:
        if entry['err'] > 1:
            threat_level += 10
    return threat_level

# Misleading intermediate computation (red herring)
security_risk = analyze_security_threats(timestamped_logs)
baseline_anomaly_score = sum([log['err'] * 100 for log in timestamped_logs])

# Data transformation pipeline with distractors
def normalize(value, max_val=100):
    return value / max_val

def moving_average(data, window=2):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

# Extract raw metric sequences
cpu_loads = [log['cpu'] for log in timestamped_logs]
memory_usage = [log['mem'] for log in timestamped_logs]
disk_io = [log['io'] for log in timestamped_logs]
error_count = [log['err'] for log in timestamped_logs]

# Apply irrelevant smoothing (distractor)
cpu_smooth = moving_average(cpu_loads)
mem_smooth = moving_average(memory_usage)

# Create composite health indicators (some irrelevant)
health_flags = []
for i, log in enumerate(timestamped_logs):
    critical = log['cpu'] > 90 and log['mem'] > 85
    health_flags.append(1 if critical else 0)

# Another decoy structure
critical_moments = [t['time'] for t in timestamped_logs if t['cpu'] > 90 and t['mem'] > 85]
emergency_responses = len(critical_moments) * 5

# Real processing begins here: aggregate base metrics per timestamp
def compute_stability_index(logs):
    index = []
    for log in logs:
        instability = (
            normalize(log['cpu'], 100) * 0.4 +
            normalize(log['mem'], 100) * 0.4 +
            normalize(log['io'], 100) * 0.2
        )
        index.append(round(1 - instability, 4))
    return index

stability_over_time = compute_stability_index(timestamped_logs)

# Weighted scoring model with red herring variables
weights = {
    'stability': 0.6,
    'reliability': 0.3,
    'rarity_bonus': 0.1  # unused weight - misleading
}

# Compute reliability score based on error frequency
error_freq = sum(error_count) / len(error_count)
reliability_score = math.exp(-error_freq)  # higher with fewer errors

# Compute stability score as average of normalized stability index
base_stability = sum(stability_over_time) / len(stability_over_time)
stability_score = base_stability  # direct pass-through

# Spurious calculation using zip and enumerate (distraction)
spurious_trend = 0
detailed_analysis = defaultdict(float)
for i, (cpu, mem) in enumerate(zip(cpu_loads, memory_usage)):
    diff = abs(cpu - mem)
    detailed_analysis[f'gap_{i}'] = diff
    if i > 0:
        cpu_change = cpu - cpu_loads[i-1]
        mem_change = mem - memory_usage[i-1]
        spurious_trend += cpu_change * mem_change

# Another decoy: rare event detection
frequencies = Counter(disk_io)
rare_io_events = sum(1 for count in frequencies.values() if count == 1)

# Actual metric aggregation happens here — only stability and reliability matter
metrics = {
    'stability': stability_score,
    'reliability': reliability_score
}

# Key statement: evaluation using only defined metrics despite distractions
def evaluate_performance(met, wgt):
    total = 0.0
    for key in met:
        if key in wgt:  # skip keys not in weights
            total += met[key] * wgt[key]
    # Normalize to a 0-100 scale
    return int(total * 100)

final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")