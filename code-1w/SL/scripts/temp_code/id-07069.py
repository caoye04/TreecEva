from itertools import combinations
from math import log

# Simulate sensor data analysis with noise filtering and performance scoring
def analyze_sensor_readings(readings):
    raw_peaks = [i for i, x in enumerate(readings) if x > 80]
    smoothed = [x for x in readings if x > 20]
    peak_pairs = list(combinations(raw_peaks, 2))
    distances = [abs(p1 - p2) for p1, p2 in peak_pairs]
    
    # Irrelevant intermediate: entropy-like measure (not used in final)
    entropy_approx = sum(log(d) if d > 0 else 0 for d in distances) / len(distances) if distances else 0
    
    # Key metric: average distance between high peaks
    avg_distance = sum(distances) / len(distances) if distances else 0
    
    # Distractor: unused transformation
    transformed = [round(x ** 0.5 * 1.5) for x in smoothed]
    
    return avg_distance, entropy_approx, transformed

# Evaluate system performance based on metric set and baseline threshold
def evaluate_performance(metrics, base):
    score = 0
    adjustments = []
    
    for m in metrics:
        if m > base:
            score += int(m // 3)
            adjustments.append(m * 0.1)
        else:
            score -= int(base % 4)
    
    # Dead code path: never executed due to fixed condition
    if len(metrics) < 0:  # Always false
        score = -1
    
    # Additional distraction: complex but unused calculation
    temp_grid = [[i * j for j in range(3)] for i in range(3)]
    trace_sum = sum(temp_grid[i][i] for i in range(3))
    
    return score + len(adjustments)

# Sensor input data (simulated)
sensor_data = [15, 85, 30, 90, 25, 40, 95, 60, 88, 70, 22]

# Extract key features
avg_dist, info_metric, filtered = analyze_sensor_readings(sensor_data)

# Construct metric set with irrelevant additions
metric_set = {
    avg_dist,
    info_metric,
    len(sensor_data),
    sum(filtered[:5]) // 5
}

baseline = 35

# Unused helper: misleading function suggesting deeper processing
def refine_calibration(data):
    return sorted(set((x + 2) * 3 for x in data))

# Critical statement
temp_result = tuple(round(x) for x in metric_set)
final_score = evaluate_performance(metric_set, baseline)

print(f"Target result: {final_score}")