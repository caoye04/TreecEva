from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9]
humidity_readings = [45, 47, 50, 52, 48, 55, 60]
pressure_readings = [1013, 1015, 1012, 1009, 1010, 1014, 1016]

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
offset_map = {k: v for v, k in enumerate(dummy_labels)}

# Data transformation pipeline (mixed relevance)
smoothed_temps = [round(t * 1.02 + 0.1, 2) for t in temperature_readings]  # slight correction
normalized_humidity = [h / 100.0 for h in humidity_readings]

# Bit manipulation red herring
def transform_value(x):
    shifted = (x << 3) ^ 0xFF
    return shifted & 0xFFFF

decoy_values = [transform_value(int(t)) for t in temperature_readings]

# Statistical baseline metrics (some used, some not)
mean_temp = sum(smoothed_temps) / len(smoothed_temps)
median_temp = sorted(smoothed_temps)[len(smoothed_temps)//2]
mode_humidity = Counter(humidity_readings).most_common(1)[0][0]

# Dead function - never called (dead code path)
def deprecated_analysis(data):
    return sum(d ** 2 for d in data) / len(data)

# Control flow with conditional aggregation
data_bins = defaultdict(list)
for i, temp in enumerate(smoothed_temps):
    label = dummy_labels[i % len(dummy_labels)]
    data_bins[label].append(temp)

# Unused binning result (distractor)
binned_stats = {k: (sum(v), len(v)) for k, v in data_bins.items()}

# Core logic embedded within noise
def calculate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0

stability_metric = calculate_stability(smoothed_temps)

# Boolean logic chain with short-circuiting distraction
temp_in_range = all(22 < t < 27 for t in smoothed_temps)
humid_critical = any(h > 58 for h in humidity_readings)
alert_flag = temp_in_range and not humid_critical or (False and True)  # Short-circuit decoy

# Decoy threshold calculation (unused)
baseline_offset = math.log(1 + mean_temp, 2) * transform_value(10)

# Real threshold, but obscured
base_threshold = 0.35 if alert_flag else 0.45

# Linear search for anomaly pattern (partially relevant)
def has_sequential_rise(data, n=3):
    for i in range(len(data) - n + 1):
        if all(data[i+j] < data[i+j+1] for j in range(n-1)):
            return True
    return False

rising_pattern = has_sequential_rise(temperature_readings, 3)

# Main metric construction
metric_data = {
    'stability': stability_metric,
    'trend_rising': rising_pattern,
    'valid_labels': len([lbl for lbl in dummy_labels if lbl < 'D']),  # arbitrary filter
    'scale_factor': 2.718
}

# Core evaluation logic buried in abstraction
def evaluate_performance(metrics, threshold):
    score = 100.0
    
    # Step 1: penalize instability
    if metrics['stability'] > threshold:
        score -= 40
    
    # Step 2: reward rising trend under conditions
    if metrics['trend_rising'] and metrics['valid_labels'] >= 2:
        score += 15
    
    # Step 3: scaling adjustment
    scaled_penalty = (metrics['stability'] * 100) * 0.1
    score -= scaled_penalty
    
    # Step 4: final nonlinear adjustment
    score = math.floor(score * metrics['scale_factor']) % 85
    
    # Irrelevant string operation (distraction)
    log_tag = f"PERF-{metrics['valid_labels']}:{''.join([c.lower() for c in 'ScoreCalc' if c.isupper()])}"
    
    return score

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output the target result
print(f"Target result: {final_score}")