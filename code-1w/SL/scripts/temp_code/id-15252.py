from collections import defaultdict, Counter
import math

# Simulated sensor data: timestamp -> readings
timestamps = [100, 101, 102, 103, 104, 105]
raw_readings = [5.1, 4.8, 5.6, 6.2, 4.9, 5.3]

# Irrelevant auxiliary mapping (distractor)
status_map = {'OK': 1, 'WARN': 2, 'CRIT': 3}
code_names = {v: k for k, v in status_map.items()}

# Real health data aggregation
health_data = defaultdict(list)
for t, val in zip(timestamps, raw_readings):
    bucket = 'stable' if val < 5.5 else 'elevated'
    health_data[bucket].append(val)

# Multiple threshold sets – only one is used (red herring)
thresh_set_a = {'low': 4.5, 'high': 5.5}
thresh_set_b = {'min_alert': 5.0, 'max_normal': 5.7}  # Used
thresh_set_c = {'critical': 6.0}

def apply_filter(data, mode='none'):
    """Irrelevant filtering function (dead path)"""
    if mode == 'smooth':
        return [sum(data[i:i+3])/3 for i in range(len(data)-2)]
    return data

def rolling_average(values, window=2):
    """Another distractor function not used in final path"""
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

# Preprocessing with conditional expression (used)
normalized = [x if x >= 5.0 else 5.0 for x in raw_readings]

# Artificially complex counting (partially relevant)
reading_counts = Counter(['high' if x > 5.5 else 'normal' for x in normalized])

# Decoy statistical calculations
mean_val = sum(normalized) / len(normalized)
variance_proxy = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)
entropy_like = -sum((count / len(normalized)) * math.log(count / len(normalized)) 
                    for count in reading_counts.values())

# Threshold logic actually used
thresholds = thresh_set_b

# Simulated weight matrix for unused algorithm
weights = [[0.5, 0.5], [0.3, 0.7], [0.8, 0.2]]
weighted_sum = sum(w[0] * normalized[i % len(normalized)] for i, w in enumerate(weights))

# Core diagnostic logic buried among distractions
def evaluate_stability(items):
    score = 0
    for val in items:
        if val > thresholds['min_alert']:
            score += 1
        if val >= thresholds['max_normal']:
            score -= 2
    return score

def compute_urgency(data_list):
    total = 0
    factor = 1
    for entry in data_list:
        if isinstance(entry, list):
            total += sum(1 for x in entry if x > 5.2) * factor
            factor += 1
    return total

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def analyze_metrics(metrics, config):
    base = 0
    adjustment = 0
    
    # Real logic starts here — deeply nested and mixed with noise
    for key, values in metrics.items():
        if key == 'stable':
            base += len(values) * 3
            for v in values:
                if v > config['min_alert']:
                    adjustment += 1
        elif key == 'elevated':
            base += len(values) * 5
            for v in values:
                if v >= config['max_normal']:
                    adjustment -= 3
    
    # Final computation intertwined with decoy logic
    temp_result = base + adjustment
    
    # More irrelevant operations
    debug_trace = [fibonacci(4)] * 2  # Computationally expensive but unused
    metadata_log = {'entries': len(metrics), 'version': '2.1'}
    
    # Only this line matters
    final_score = temp_result * 100 // (len(raw_readings) or 1)
    
    return final_score

# Critical execution point
final_diagnostic = analyze_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")