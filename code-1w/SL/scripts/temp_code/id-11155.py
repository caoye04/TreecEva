def analyze_trend(values):
    if len(values) < 2:
        return 0
    slope = sum(values[i+1] - values[i] for i in range(len(values)-1)) / (len(values) - 1)
    return slope if abs(slope) > 0.5 else 0

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log(count/total, 2) for count in freq.values())
    return round(entropy, 3)

# Unused but plausible transformation
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(round((signal[i-1] + signal[i] + signal[i+1]) / 3, 2))
    smoothed.append(signal[-1])
    return smoothed

# Distractor variables
temp_threshold = 42.5
activation_flag = False
buffer_cache = [0] * 100

# Real computation begins
baseline_metrics = [3, 7, 11, 15, 19]
adjustment_factor = 1.25
offset_correction = lambda x: x + 2 if x % 2 == 0 else x + 1

# Simulated sensor readings (irrelevant but looks important)
sensor_log = {
    'A': [1.1, 2.3, 1.9],
    'B': [5.6, 5.1, 5.8],
    'C': [9.2, 8.7, 9.0]
}

# Another red herring: checksum calculation
checksum = 0
for key, vals in sensor_log.items():
    for v in vals:
        checksum += int(v * 10) % 7
checksum = (checksum * 3) % 17

# Core logic disguised among distractions
metric_data = [offset_correction(x * 2) for x in baseline_metrics]
baseline_ref = sum(baseline_metrics) // len(baseline_metrics)

# Misleading intermediate calculation
dummy_aggregate = 0
for idx, val in enumerate(metric_data):
    if idx % 2 == 0:
        dummy_aggregate += val ** 0.5
    else:
        dummy_aggregate -= val // 3

def evaluate_performance(metrics, base):
    trend = analyze_trend(metrics)
    deviation = sum(abs(m - base) for m in metrics)
    # Key decision point with conditional expression
    penalty = deviation // 3 if trend < 2 else deviation // 5
    # Critical computation hidden in abstraction
    primary_score = base * 3 + int(trend * 10)
    secondary_score = len([m for m in metrics if m > base]) * 7
    # Actual answer determined here
    final = primary_score + secondary_score - penalty
    
    # Dead code path (never executed due to logic)
    if activation_flag and temp_threshold > 50:
        final += compute_entropy(buffer_cache[:10])
    
    return final

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline_ref)

# Noise: unused list comprehension with zip
auxiliary_pairs = [(a, b) for a, b in zip(baseline_metrics, metric_data) if a % 3 == 0]

# Output the required result
print(f"Result: {final_score}")