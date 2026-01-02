from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 85, 93, 150, 78, 112, 99, 134, 67, 108]
node_failures = [0, 1, 0, 2, 1, 0, 0, 3, 1, 0]
memory_usage_gb = [3.2, 5.6, 4.1, 6.8, 2.9, 4.4, 5.0, 7.1, 3.0, 4.9]

def compute_efficiency(durations):
    avg = sum(durations) / len(durations)
    peak = max(durations)
    return (avg / peak) * 100

def calculate_reliability(failures):
    total_failures = sum(failures)
    # Misleading: this function computes something but isn't used in final path
    reliability_score = 100 - (total_failures * 2.5)
    return reliability_score if reliability_score > 0 else 0

def assess_memory_stress(usage_list):
    stress_levels = []
    for usage in usage_list:
        if usage < 3.5:
            stress_levels.append('low')
        elif usage < 5.5:
            stress_levels.append('moderate')
        else:
            stress_levels.append('high')
    counter = Counter(stress_levels)
    high_ratio = counter['high'] / len(usage_list)
    return high_ratio * 100

def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def bitwise_diagnostic(value):
    # Red herring function: looks important but unused
    result = value
    for _ in range(3):
        result = (result ^ 0xAA) & 0xFF
        result = (result << 1) | (result >> 7)
    return result

def filter_outliers(data, threshold=1.5):
    # Dead code path - never called
    median = sorted(data)[len(data)//2]
    iqr = sorted(data)[int(0.75*len(data))] - sorted(data)[int(0.25*len(data))]
    lower, upper = median - threshold * iqr, median + threshold * iqr
    return [x for x in data if lower <= x <= upper]

def generate_report(tasks, failures, memory):
    # Complex but irrelevant aggregation
    report = defaultdict(dict)
    for i in range(len(tasks)):
        status = 'critical' if failures[i] >= 2 else 'stable'
        load = 'high' if memory[i] > 6.0 else 'normal'
        report[i]['status'] = status
        report[i]['load'] = load
        report[i]['efficiency_hint'] = tasks[i] * 0.01
    return report

# Irrelevant intermediate transformations
efficiency_raw = compute_efficiency(task_durations)
reliability_raw = calculate_reliability(node_failures)
memory_stress_pct = assess_memory_stress(memory_usage_gb)

# Normalized metrics (only some are actually used later)
norm_durations = normalize(task_durations)
norm_memory = normalize(memory_usage_gb)

# Fake diagnostic check
system_key = 0x1A3B
for val in task_durations[:3]:
    system_key ^= val
    system_key &= 0xFFFF

# Actual relevant computation begins here
base_metrics = [
    efficiency_raw,                    # from durations
    (100 - (sum(node_failures) / len(node_failures)) * 15),  # availability proxy
    100 - memory_stress_pct,           # memory headroom
    (sum(1 for m in memory_usage_gb if m > 5.0) / len(memory_usage_gb)) * -20 + 100  # penalty logic
]

# Weight assignment with red herring
weights = [0.4, 0.3, 0.2, 0.1]
dummy_weights = [0.25, 0.25, 0.25, 0.25]  # unused

# Misleading comment: "Adjust for network jitter"
jitter_correction = 0.0
for t in task_durations:
    jitter_correction += (t % 10) * 0.01
jitter_correction = round(jitter_correction, 2)

# Core evaluation function
def evaluate_performance(metrics, w):
    adjusted = []
    for i, m in enumerate(metrics):
        if i == 0:
            # Apply non-linear boost to efficiency
            adjusted.append(100 * (1 - math.exp(-m / 100)))
        elif i == 3:
            # Extra penalty if last metric below threshold
            raw = m * w[i]
            adjusted.append(raw - 5 if m < 80 else raw)
        else:
            adjusted.append(m * w[i])
    
    # Final aggregation with distractor logic
    temp_sum = sum(adjusted)
    bonus = 10 if all(m > 60 for m in metrics[:3]) else 0  # bonus not actually added
    penalty = 15 if memory_stress_pct > 40 else 0
    
    # ACTUAL final score
    final = temp_sum - penalty
    
    # DEAD CODE: unreachable due to return
    if final < 50:
        final *= 1.1  # supposed recovery boost
    
    return final

# Execute key statement
temp_var_x = generate_report(task_durations, node_failures, memory_usage_gb)
final_score = evaluate_performance(base_metrics, weights)
print(f"Target result: {final_score}")