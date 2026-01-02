from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 130, 90, 200, 180, 160, 140, 170, 110]
memory_usage = [75, 80, 85, 90, 70, 65, 95, 100, 60, 55]
cpu_load = [0.7, 0.8, 0.6, 0.9, 0.5, 0.4, 0.8, 0.7, 0.3, 0.2]

# Irrelevant historical logs (dead data)
historical_durations = [210, 190, 175, 165, 185]  # unused
legacy_config = {'timeout': 300, 'retries': 3}  # decoy

# Distractor: fake normalization function that isn't used
def normalize_bad(data):
    return [x / max(data) for x in data]

# Real preprocessing
scaled_durations = [d / 60 for d in task_durations]  # convert to minutes
duration_z = [(d - sum(scaled_durations)/len(scaled_durations)) / (sum([(x - sum(scaled_durations)/len(scaled_durations))**2 for x in scaled_durations]) / len(scaled_durations))**0.5 for d in scaled_durations]

# Memory grouped by usage level (distraction with actual use later)
memory_groups = defaultdict(int)
for m in memory_usage:
    if m < 70:
        memory_groups['low'] += 1
    elif m < 90:
        memory_groups['medium'] += 1
    else:
        memory_groups['high'] += 1

# Bitwise interference: tracking binary flags for deprecated feature
feature_flags = 0b10101010
active_modules = feature_flags & 0b1111
aux_data = [feature_flags >> i & 1 for i in range(8)]  # unused list

# CPU load categorization (partially relevant)
load_labels = ['high' if c >= 0.7 else 'low' for c in cpu_load]
label_count = Counter(load_labels)

# Spurious sorting operation on unrelated composite metric
composite_metric = [d * c for d, c in zip(scaled_durations, cpu_load)]
sorted_composite = sorted(composite_metric, reverse=True)
trimmed_avg = sum(sorted_composite[2:-2]) / len(sorted_composite[2:-2])  # red herring

# Real metric pipeline begins here
def z_score(x):
    mean = sum(x) / len(x)
    std = (sum((i - mean)**2 for i in x) / len(x))**0.5
    return [(i - mean) / std for i in x]

def robust_scale(x):
    median = sorted(x)[len(x)//2]
    mad = sorted([abs(i - median) for i in x])[len(x)//2]
    return [(i - median) / (mad + 1e-8) for i in x]

# Apply transformations
dur_norm = z_score(scaled_durations)
mem_norm = robust_scale(memory_usage)
cpu_norm = z_score(cpu_load)

# Weighted combination
weights = {
    'duration': 0.4,
    'memory': 0.3,
    'cpu': 0.3
}

metrics = []
for i in range(len(task_durations)):
    score = (
        weights['duration'] * abs(dur_norm[i]) +
        weights['memory'] * abs(mem_norm[i]) +
        weights['cpu'] * abs(cpu_norm[i])
    )
    metrics.append(score)

# Secondary transformation: outlier suppression
threshold = 2.0
adjusted_metrics = [m if m <= threshold else 2 * threshold - m for m in metrics]  # fold-back

# Final aggregation
raw_performance = sum(adjusted_metrics) / len(adjusted_metrics)

# Decoy finalization path (never taken due to flag)
use_legacy = False
if use_legacy:
    final_score = raw_performance * 0.8
else:
    # Real final computation
    stability_penalty = abs(label_count['high'] - label_count['low']) * 0.05
    final_score = math.floor((raw_performance - stability_penalty) * 100) / 100

# Additional distraction: unused tuple unpacking
top_three = sorted_composite[:3]
fastest, second_fastest, third_fastest = top_three  # irrelevant
overhead_estimate = fastest * 0.1  # dead calculation

# Another decoy function
def calculate_efficiency():
    return sum(memory_usage) / sum(task_durations)  # never called

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Ground truth implementation (overrides previous logic for clarity)
def evaluate_performance(met, w):
    # Recompute normalized values correctly
    dur_z = z_score([d/60 for d in task_durations])
    mem_r = robust_scale(memory_usage)
    cpu_z = z_score(cpu_load)
    
    # Recompute adjusted metrics
    temp_scores = []
    for i in range(len(met)):
        s = w['duration']*abs(dur_z[i]) + w['memory']*abs(mem_r[i]) + w['cpu']*abs(cpu_z[i])
        temp_scores.append(s)
    
    adj = [s if s <= 2.0 else 4.0 - s for s in temp_scores]
    base = sum(adj) / len(adj)
    penalty = abs(memory_groups['high'] - memory_groups['low']) * 0.05
    return math.floor((base - penalty) * 100) / 100

# Print result
print(f"Result: {final_score}")