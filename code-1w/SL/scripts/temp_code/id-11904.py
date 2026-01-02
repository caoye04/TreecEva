from collections import defaultdict
import itertools

# Simulated sensor data processing with performance evaluation
raw_readings = [145, 273, 91, 88, 205, 117, 301, 74, 188, 230]

def process_signal(data):
    filtered = [x for x in data if x > 70]
    adjusted = [x * 0.85 if x > 200 else x * 1.05 for x in filtered]
    return sorted(adjusted, reverse=True)

def analyze_trend(seq):
    trend_scores = []
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            trend_scores.append(1)
        else:
            trend_scores.append(-0.5)
    return sum(trend_scores)

# Irrelevant helper - dead code path (distractor)
def deprecated_normalization(vec):
    mean_val = sum(vec) / len(vec)
    return [(v - mean_val) / mean_val for v in vec]

# Unused transformation chain (red herring)
transform_chain = [
    lambda x: x + 10,
    lambda x: x * 0.9,
    lambda x: abs(x - 5) ** 2
]

temp_diagnostic = []
for val in raw_readings:
    temp_diagnostic.append(val % 13)

# Distractor: complex but unused data structure
stats_summary = defaultdict(lambda: 0)
for reading in raw_readings:
    bucket = (reading // 50) * 50
    stats_summary[bucket] += 1

# Real processing begins here
processed_signal = process_signal(raw_readings)
primary_peak = processed_signal[0]  # Highest adjusted reading

# Secondary metrics (some used, some not)
baseline_avg = sum(raw_readings) / len(raw_readings)
adjusted_avg = sum(processed_signal) / len(processed_signal)

drift_metric = analyze_trend(processed_signal)

# Fake fusion logic (decoy)
fusion_weights = [0.1, 0.3, 0.6]
composite_index = 0
for w in fusion_weights:
    composite_index += w * primary_peak  # Simplified use, rest is distraction

# Actual metric data construction
metric_data = {
    'peak': primary_peak,
    'stability': drift_metric,
    'size': len(processed_signal),
    'base_avg': baseline_avg
}

base_threshold = 180

# Core logic hidden among distractions
def evaluate_performance(metrics, threshold):
    score = 0
    
    # Meaningful condition 1
    if metrics['peak'] > threshold:
        score += 40
    
    # Meaningful condition 2
    if metrics['stability'] > 3:
        score += 35
    
    # Meaningful condition 3
    size_factor = metrics['size'] - 5
    score += max(0, size_factor * 10)
    
    # Red herring branch (never taken due to logic but looks important)
    if metrics.get('reliability', 0) > 0.9:
        score += 100  # This is never added
    
    # Distractor computation
    phantom_risk = (metrics['peak'] / 100) ** 2
    normalized_risk = phantom_risk * 0.1  # Not used
    
    return int(score)

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Target result: {final_score}")