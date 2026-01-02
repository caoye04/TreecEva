from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant in part)
telemetry = [12, 45, 23, 67, 89, 34, 56, 78, 90, 11]
running_avg = sum(telemetry) / len(telemetry)
spike_count = sum(1 for x in telemetry if x > 50)

def analyze_pattern(seq):
    # Irrelevant pattern analyzer (dead-end function)
    freq = defaultdict(int)
    for i in range(len(seq) - 1):
        freq[(seq[i], seq[i+1])] += 1
    return dict(freq)

# Unused but plausible-looking analysis
temporal_patterns = analyze_pattern(telemetry)

# Core logic begins: performance evaluation system
assessment_log = {
    'latency': 42,
    'throughput': 85,
    'consistency': 67,
    'reliability': 76,
    'scalability': 58
}

# Misleading secondary log with decoy values
decoy_log = {
    'latency': 91,
    'throughput': 22,
    'consistency': 33,
    'reliability': 44,
    'scalability': 55
}

weights = {
    'latency': 0.2,
    'throughput': 0.3,
    'consistency': 0.15,
    'reliability': 0.25,
    'scalability': 0.1
}

# Auxiliary computation: normalization factor (partially relevant)
norm_base = sum(weights.values())
scaling_factor = math.log(running_avg + 1) if running_avg > 0 else 0

# Distraction: unused weight adjustment based on spike count
adjusted_weights = {}
for k, v in weights.items():
    if spike_count > 5:
        adjusted_weights[k] = v * 1.1
    else:
        adjusted_weights[k] = v * 0.9

# Secondary distraction: fake calibration using decoy_log
calibration_shift = 0
temp_sum = 0
for metric, value in decoy_log.items():
    temp_sum += value
fake_avg = temp_sum / len(decoy_log)
calibration_shift = abs(fake_avg - running_avg)

# Real processing function
def process_metrics(log, w):
    total = 0.0
    applied_norm = 0.0
    
    # First apply weights
    for metric, score in log.items():
        if metric == 'latency':
            # Invert latency since lower is better
            normalized = 100 - score
        else:
            normalized = score  # higher is better
        total += normalized * w[metric]
        applied_norm += w[metric]
    
    # Apply base normalization
    if applied_norm != 0:
        total /= applied_norm
    
    # Conditional bonus logic (short-circuit)
    throughput_ok = log['throughput'] >= 80
    reliability_ok = log['reliability'] >= 70
    if throughput_ok and reliability_ok:
        total += 5.0  # Bonus for high perf & reliability
    
    # Hidden adjustment: consistency outlier penalty
    consistency = log['consistency']
    if consistency < 60:
        total -= 3.0
    
    # Return rounded final score
    return round(total, 4)

# Execution point of interest
final_score = process_metrics(assessment_log, weights)

# Irrelevant aggregation of telemetry patterns
pattern_counter = Counter(telemetry)
dominant_values = [k for k, v in pattern_counter.items() if v > 1]

# Output the target result
print(f"Result: {final_score}")