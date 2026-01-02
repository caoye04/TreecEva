from collections import defaultdict, Counter
import math

# Simulated system performance monitoring with decoy data
def generate_noise_data(size):
    return [((i * 17 + 257) % 1000) for i in range(size)]

def deprecated_analysis(data):
    # Unused function - red herring
    return sum(x ** 0.5 for x in data if x % 3 == 0)

def parse_legacy_format(raw_entry):
    # Legacy parser - never called
    parts = raw_entry.split('-')
    return {'id': parts[0], 'val': int(parts[1])}

# Irrelevant sensor simulation (avoided theme: sensor; renamed to 'activity')
activity_levels = [x % 128 for x in generate_noise_data(50)]
baseline_readings = [abs(math.sin(i / 10)) * 100 for i in range(30)]

# Core logic disguised among distractions
def normalize(values):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.5] * len(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def calculate_entropy(weights):
    total = 0.0
    for w in weights:
        if w > 0:
            total -= w * math.log(w + 1e-9)
    return total

def validate_sequence(seq):
    # Complex validation with early returns - partially relevant
    if len(seq) < 5:
        return False
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            return False
    return True

def filter_outliers(data, factor=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in data if low <= x <= high]

# Decoy statistical analysis
temp_stats = defaultdict(int)
for val in activity_levels:
    temp_stats['bin_' + str(val // 16)] += 1

# Unused transformation chain
cumulative_shift = 0
for i in range(len(baseline_readings)):
    cumulative_shift = (cumulative_shift + int(baseline_readings[i])) % 7

# Real input data - metrics log with multiple dimensions
metrics_log = [
    {'time': 1, 'cpu': 85, 'mem': 70, 'disk': 45, 'net': 20},
    {'time': 2, 'cpu': 90, 'mem': 75, 'disk': 50, 'net': 25},
    {'time': 3, 'cpu': 95, 'mem': 80, 'disk': 60, 'net': 30},
    {'time': 4, 'cpu': 87, 'mem': 77, 'disk': 55, 'net': 35},
    {'time': 5, 'cpu': 83, 'mem': 72, 'disk': 50, 'net': 28}
]

base_threshold = 85
penalty_weights = {'cpu': 0.4, 'mem': 0.3, 'disk': 0.2, 'net': 0.1}
dynamic_adjustment = 0.0

# Flag to control execution path - set based on irrelevant condition
if sum(activity_levels[:10]) > 500:
    dynamic_adjustment = 0.05
else:
    dynamic_adjustment = -0.05

# Main evaluation logic buried in complexity
def evaluate_performance(log_entries, threshold):
    recent_entries = log_entries[-3:]  # Focus on last 3
    
    # Extract metric trends
    trends = defaultdict(list)
    for entry in log_entries:
        for k, v in entry.items():
            if k != 'time':
                trends[k].append(v)
    
    # Normalize each metric series
    normalized_trends = {}
    for key, values in trends.items():
        norm_vals = normalize(values)
        normalized_trends[key] = norm_vals
    
    # Calculate violation scores
    violation_counts = defaultdict(int)
    for entry in recent_entries:
        for resource, usage in entry.items():
            if resource != 'time' and usage > threshold:
                violation_counts[resource] += 1
    
    # Compute weighted penalty
    total_penalty = 0.0
    for resource, count in violation_counts.items():
        total_penalty += count * penalty_weights[resource] * 10
    
    # Entropy-based unpredictability bonus/penalty
    all_cpu = [e['cpu'] for e in log_entries]
    filtered_cpu = filter_outliers(all_cpu)
    normalized_cpu = normalize(filtered_cpu)
    cpu_entropy = calculate_entropy(normalized_cpu)
    
    # Bonus decreases penalty if entropy is high (unpredictable load)
    unpredictability_factor = (cpu_entropy - 0.5) * 2
    
    # Apply dynamic adjustment from above (only depends on activity_levels)
    adjusted_penalty = total_penalty - unpredictability_factor + dynamic_adjustment
    
    # Final score calculation
    raw_score = 100 - adjusted_penalty
    
    # Dead code branch - never executed due to data
    if validate_sequence([1, 1, 2, 3, 5]):
        raw_score *= 1.1
    
    # Key execution point
    final_score = round(raw_score, 4)
    return final_score

# Misleading intermediate computation
aggregate_load = sum(sum(d[k] for k in d if k != 'time') for d in metrics_log)
system_stability_index = len([x for x in baseline_readings if x > 50])

# Critical statement
final_score = evaluate_performance(metrics_log, base_threshold)

# Print result
print(f"Result: {final_score}")