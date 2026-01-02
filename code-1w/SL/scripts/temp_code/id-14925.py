from collections import defaultdict, Counter
import math

# Simulated system performance metrics (irrelevant data structure)
system_logs = [
    {'timestamp': 1, 'cpu': 75, 'mem': 80, 'disk_io': 30},
    {'timestamp': 2, 'cpu': 85, 'mem': 82, 'disk_io': 35},
    {'timestamp': 3, 'cpu': 90, 'mem': 85, 'disk_io': 40},
    {'timestamp': 4, 'cpu': 88, 'mem': 83, 'disk_io': 38}
]

# Irrelevant helper function (dead code path)
def analyze_disk_usage(logs):
    total_io = sum(entry['disk_io'] for entry in logs)
    avg_io = total_io / len(logs)
    return 'High' if avg_io > 35 else 'Normal'

# Unused but plausible transformation
disk_pattern = [entry['disk_io'] * 1.5 for entry in system_logs if entry['cpu'] > 80]

# Core data for evaluation (plausible but partially irrelevant)
raw_metrics = [88, 92, 76, 85, 90, 82, 89, 84, 77, 91]

# Distractor: complex normalization with unused result
normalized = [(x - 70) / 30 for x in raw_metrics]
scaled_normalized = [round(n * 100) for n in normalized]

# Actual relevant metric preprocessing
metric_data = [x for x in raw_metrics if x >= 80]  # Filter high performers

# Secondary distractor: frequency count (not used in final logic)
frequency = Counter(raw_metrics)
common_values = frequency.most_common(3)

# Complex but irrelevant transformation chain
transformed = []
for val in metric_data:
    temp = val ** 0.5
    temp = temp * math.pi
    temp = int(temp + 0.5)
    transformed.append(temp)

# Fake aggregation that looks important
effective_sum = sum(transformed[i] * (i + 1) for i in range(len(transformed)))
weight_factor = len(transformed) / (effective_sum % 50 + 1)

# Real threshold logic buried in noise
base_threshold = 85

def adjust_threshold(base, factor=1.05):
    # Seemingly important adjustment, never actually called
    return base * factor

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Key function with embedded distractions
def evaluate_performance(metrics, threshold):
    # Real computation steps
    above_threshold = [m for m in metrics if m >= threshold]
    below_threshold = [m for m in metrics if m < threshold]
    
    # Distractor variables
    outlier_count = len([m for m in metrics if m < 75 or m > 95])
    peak_value = max(metrics) if metrics else 0
    decay_weights = [0.9**i for i in range(len(metrics))]
    weighted_avg = sum(metrics[i] * decay_weights[i] for i in range(len(metrics)))
    
    # Critical intermediate calculation
    score_component_a = len(above_threshold) * 15
    score_component_b = sum(below_threshold) // (len(below_threshold) + 1)  # Avoid zero div
    
    # More red herrings
    histogram = defaultdict(int)
    for m in metrics:
        bucket = (m // 5) * 5
        histogram[bucket] += 1
    
    trend_analysis = []
    for i in range(1, len(metrics)):
        trend_analysis.append(1 if metrics[i] > metrics[i-1] else 0)
    
    # The actual answer computation (non-obvious)
    raw_score = score_component_a + score_component_b
    penalty = abs(len(above_threshold) - len(below_threshold)) * 2
    final_score = raw_score - penalty
    
    # Dead assignment (looks like scaling but isn't needed)
    final_score = final_score * 1.0  # No-op
    
    return int(final_score)

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Additional distraction: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Unused list comprehension with bit manipulation
analysis_flags = [fibonacci(i) | (1 << (i % 4)) for i in range(5)]

# Output the target result
print(f"Result: {final_score}")