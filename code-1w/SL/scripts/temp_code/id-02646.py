import math

# Simulated system metrics from a distributed computing environment
cpu_load = [0.78, 0.82, 0.91, 0.65, 0.77]
memory_usage = [0.64, 0.71, 0.88, 0.59, 0.73]
disk_iops = [1200, 1400, 1350, 1100, 1500]
network_latency_ms = [23, 19, 27, 21, 18]

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def compute_efficiency(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.exp(-variance)  # Higher homogeneity -> higher efficiency

def analyze_outliers(data):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return len(outliers)

# Irrelevant diagnostic function (dead code path)
def legacy_diagnostics(mode="basic"):
    history_log = {"errors": 0, "warnings": 3, "info": 12}
    checksum = sum(ord(c) for c in str(history_log)) % 1000
    return False  # Never used

# Unused auxiliary variables (distractors)
baseline_threshold = 0.65
redundant_flag = True
temp_buffer = [0] * 5
aggregated_metrics = []

# Simulate corrupted data flag (misleading intermediate)
data_corruption_flag = any(x < 0 for x in disk_iops)  # Always False

# Begin relevant processing chain
normalized_cpu = [normalize(x, 0.5, 1.0) for x in cpu_load]
efficient_cpu_pattern = compute_efficiency(normalized_cpu)

# Memory normalized differently
normalized_memory = [normalize(x, 0.5, 0.95) for x in memory_usage]
efficient_memory_pattern = compute_efficiency(normalized_memory)

# Disk IOPS transformed via logarithmic scaling
log_iops = [math.log(x) for x in disk_iops]
avg_log_iops = sum(log_iops) / len(log_iops)

# Network latency: lower is better, invert and scale
inverted_latency = [100 / (1 + x) for x in network_latency_ms]
scaled_latency = [normalize(x, 80, 100) for x in inverted_latency]

# Construct performance feature set
feature_vector = [
    efficient_cpu_pattern,
    efficient_memory_pattern,
    avg_log_iops / 10,  # scaled down
    sum(scaled_latency) / len(scaled_latency)
]

# Define evaluation logic with conditional expression and lambda
metric_set = set(feature_vector)

# Misleading transformation (not used in final score)
phantom_metric = list(map(lambda x: x ** 2 + 0.1, feature_vector))

# Benchmark weight schema (simulated)
benchmark_weights = {
    'efficiency': 0.4,
    'throughput': 0.3,
    'responsiveness': 0.2,
    'stability': 0.1
}

# Evaluate performance using weighted combination
# Only specific indices map to actual weights
def evaluate_performance(metrics, weights):
    sorted_vals = sorted(metrics)
    
    # Extract meaningful components by position
    a = sorted_vals[0]  # lowest: stability proxy
    b = sorted_vals[1]  # responsiveness
    c = sorted_vals[2]  # throughput
    d = sorted_vals[3]  # efficiency
    
    # Apply weights based on rank-mapped roles
    w_stability = weights['stability']
    w_resp = weights['responsiveness']
    w_thr = weights['throughput']
    w_eff = weights['efficiency']
    
    composite = (
        d * w_eff +         # efficiency (highest)
        c * w_thr +         # throughput
        b * w_resp +        # responsiveness
        a * w_stability     # stability
    )
    
    # Red herring: adjust for phantom outlier penalty (never applied)
    outlier_count = analyze_outliers(disk_iops)  # returns 0
    if outlier_count > 1:
        composite *= 0.95
    
    # Final nonlinear calibration
    calibrated = 100 * (1 - math.exp(-composite))
    
    return round(calibrated, 4)

# Critical execution point
final_score = evaluate_performance(metric_set, benchmark_weights)

# Print result as required
print(f"Result: {final_score}")