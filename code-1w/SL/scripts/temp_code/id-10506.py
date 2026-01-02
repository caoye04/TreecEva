from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 135, 180, 90, 200, 165]
task_retries = [0, 1, 0, 2, 0, 3, 1]
node_loads = [0.65, 0.82, 0.71, 0.93, 0.54, 0.97, 0.76]
packet_loss_rate = [0.001, 0.003, 0.002, 0.006, 0.001, 0.012, 0.004]

# Irrelevant telemetry (distractor data)
disk_io_ops = [2300, 1950, 2100, 2700, 1800, 3100, 2400]
cpu_temps_c = [67, 72, 69, 75, 64, 78, 71]
uptime_hours = [1024, 892, 945, 768, 1103, 654, 987]

# Misleading preprocessing (dead path)
def analyze_health(loads, temps):
    return [1 if l > 0.9 or t > 75 else 0 for l, t in zip(loads, temps)]

health_flags = analyze_health(node_loads, cpu_temps_c)  # Unused

# Fake normalization function (decoy)
def normalize_to_hundred(data):
    m = min(data)
    M = max(data)
    return [(x - m) / (M - m) * 100 for x in data]

# Distractor: fake risk scoring
risk_scores = defaultdict(float)
for i, loss in enumerate(packet_loss_rate):
    if loss > 0.005:
        risk_scores[f'node_{i}'] = 3
    elif loss > 0.002:
        risk_scores[f'node_{i}'] = 2
    else:
        risk_scores[f'node_{i}'] = 1

# Real metric weighting system (hidden in noise)
def compute_efficiency(durations, retries):
    total_time = sum(d for d in durations)
    penalty = sum(r * 30 for r in retries)  # Each retry adds 30s overhead
    return total_time + penalty

# Auxiliary logic with list comprehension and filtering
successful_tasks = [t for i, t in enumerate(task_durations) if task_retries[i] == 0]
retry_cost_seconds = sum([r * 15 for r in task_retries])  # Not directly used

# Core evaluation metrics
base_latency = compute_efficiency(task_durations, task_retries) / len(task_durations)
success_rate = len(successful_tasks) / len(task_durations)
load_balance_score = 1 - (max(node_loads) - min(node_loads))

# Hidden transformation using Counter
load_buckets = Counter([int(load * 10) for load in node_loads])
peak_concentration = load_buckets.most_common(1)[0][1]  # How many nodes at peak decile

# Decoy metrics (irrelevant aggregations)
avg_disk_speed = sum(disk_io_ops) / len(disk_io_ops)
total_uptime = sum(uptime_hours)
median_temp = sorted(cpu_temps_c)[len(cpu_temps_c)//2]

# Real performance metrics (buried)
metrics = {
    'latency': base_latency,
    'success': success_rate,
    'balance': load_balance_score,
    'concentration': 1 / (1 + peak_concentration),  # Inverse impact
    'retry_rate': sum(task_retries) / len(task_retries)
}

# Weights for final score (some misleading ones included)
weights = {
    'latency': 0.3,
    'success': 0.25,
    'balance': 0.2,
    'concentration': 0.15,
    'throughput': 0.1  # Weight for non-existent metric (red herring)
}

# Final evaluation logic with conditional overrides
def evaluate_performance(met, wts):
    score = 0.0
    applied = 0.0
    
    # Only apply weights for existing metrics
    for key in wts:
        if key in met:
            score += met[key] * wts[key]
            applied += wts[key]
    
    # Normalize by applied weight sum
    if applied > 0:
        score = score / applied
    
    # Final nonlinear adjustment based on retry rate (critical but hidden)
    if 'retry_rate' in met and met['retry_rate'] > 1.0:
        score *= 0.85  # Penalty
    
    # More decoys below
    anomaly_count = 0
    for i in range(len(node_loads)):
        if node_loads[i] > 0.9 and packet_loss_rate[i] > 0.005:
            anomaly_count += 1
    # anomaly_count unused
    
    return round(score * 100, 4)

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")