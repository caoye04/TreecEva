from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis
def collect_readings():
    raw_samples = [
        (0.88, 'A'), (0.91, 'B'), (0.76, 'A'), (0.85, 'C'),
        (0.94, 'B'), (0.77, 'C'), (0.89, 'A'), (0.90, 'B')
    ]
    readings = defaultdict(list)
    for val, node in raw_samples:
        readings[node].append(val)
    return readings

def compute_stability_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    stability = math.exp(-variance)
    return round(stability, 6)

def generate_noise_patterns():
    # Irrelevant function: simulates noise but not used in final calculation
    return [math.sin(i * 0.5) for i in range(10)]

def deprecated_calibration_sequence():
    # Dead code path: never called
    calib_vals = [0.1 * j for j in range(5)]
    return sum(math.cos(x) for x in calib_vals)

# Misleading intermediate diagnostic (decoy)
initial_diagnostic = sum([0.91, 0.88, 0.76]) / 3

# Main processing pipeline
sensor_data = collect_readings()

# Compute node reliability scores (only A and B contribute to final result)
reliability_scores = {}
for node, samples in sensor_data.items():
    if node == 'C':
        continue  # Exclude C from final analysis
    idx = compute_stability_index(samples)
    reliability_scores[node] = idx

# Aggregation phase with distractor operations
aggregated_metrics = []
sum_temp = 0.0
for k in ['A', 'B']:
    if k in reliability_scores:
        sum_temp += reliability_scores[k]
        aggregated_metrics.append(reliability_scores[k])

# Add irrelevant transformation on unused metric
buffer_snapshot = [x * x + 0.1 for x in aggregated_metrics]  # Not used later

# Threshold logic with red herring condition
threshold_map = defaultdict(lambda: 0.75)
thresh_adjust = {'A': 0.02, 'B': -0.01}
for key in threshold_map:
    if key in thresh_adjust:
        threshold_map[key] += thresh_adjust[key]

# Unused statistical moment calculations (distractors)
moment_2 = sum(x**2 for x in aggregated_metrics) / len(aggregated_metrics)
moment_3 = sum(x**3 for x in aggregated_metrics) / len(aggregated_metrics)

# Core decision logic hidden among noise
convergence_flag = False
if len(aggregated_metrics) >= 2:
    diff = abs(aggregated_metrics[0] - aggregated_metrics[1])
    if diff < 0.05:
        convergence_flag = True

# Final pattern analysis (key statement)
def analyze_pattern(metrics, thresholds):
    base_score = sum(metrics)
    penalty = 0
    contrib_count = 0
    
    # Element-wise evaluation with side tracking
    tracking_log = Counter()
    for idx, score in enumerate(metrics):
        node = ['A', 'B'][idx]
        if score >= thresholds[node]:
            contrib_count += 1
            tracking_log['valid'] += 1
        else:
            penalty += 0.05
            tracking_log['invalid'] += 1
    
    # Unused log statistics (misdirection)
    log_ratio = tracking_log['valid'] / max(1, tracking_log['invalid'])
    
    # Actual result computation
    raw_result = base_score * contrib_count - penalty
    
    # Apply convergence bonus if applicable (only if both are stable and close)
    if convergence_flag and contrib_count == 2:
        raw_result *= 1.1  # 10% boost
    
    return int(round(raw_result * 100))  # Scale to integer

final_diagnostic = analyze_pattern(aggregated_metrics, threshold_map)
print(f"Result: {final_diagnostic}")