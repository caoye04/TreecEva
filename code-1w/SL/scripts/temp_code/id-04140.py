from collections import defaultdict, Counter

# Simulated system metrics from a distributed task scheduler
task_durations = [2.3, 1.8, 4.5, 3.1, 2.9, 5.2, 3.3, 3.7, 4.0, 3.0]
node_load = {'n1': 87, 'n2': 65, 'n3': 92, 'n4': 45, 'n5': 76}
completed_tasks = ['t1', 't3', 't4', 't7', 't8']
pending_tasks = ['t2', 't5', 't6', 't9', 't10']

# Irrelevant statistical counters (distractor)
duration_stats = defaultdict(int)
for d in task_durations:
    if d < 3.0:
        duration_stats['fast'] += 1
    elif d < 4.0:
        duration_stats['medium'] += 1
    else:
        duration_stats['slow'] += 1

# Fake anomaly detection (dead code path)
def detect_anomaly(logs):
    return False  # Never used

# Misleading performance indicator (decoy)
current_throughput = len(task_durations) / sum(task_durations)
anomaly_flag = detect_anomaly(task_durations)

# Core evaluation logic masked by noise
baseline = {"latency": 3.5, "success_rate": 0.8, "load_balance": 75}
metrics = {
    "latency": sum(task_durations) / len(task_durations),
    "success_rate": len(completed_tasks) / (len(completed_tasks) + len(pending_tasks)),
    "load_variance": max(node_load.values()) - min(node_load.values()),
    "peak_load": max(node_load.values())
}

# Auxiliary helper with red herring (appears important but isn't critical)
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

# Unused normalization table (distractor)
normalized_metrics = {}
for key, val in metrics.items():
    if key == "latency":
        normalized_metrics[key] = normalize(val, 1.0, 6.0)
    elif key == "success_rate":
        normalized_metrics[key] = normalize(val, 0.5, 1.0)

# Real scoring logic buried in conditional complexity
def calculate_efficiency(latency, success_rate):
    base = 100 if latency <= 3.5 else 70
    bonus = 30 if success_rate >= 0.7 else 0
    penalty = -20 if latency > 4.0 else 0
    return base + bonus + penalty

def assess_load_balance(load_values):
    sorted_loads = sorted(load_values)
    balanced_threshold = (max(load_values) - min(load_values)) < 30
    return 20 if balanced_threshold else -10

# Secondary decoy function (never called)
def simulate_recovery():
    recovery_time = 0
    for i in range(5):
        recovery_time += i * 0.5
    return recovery_time

# Main evaluation with layered logic and conditionals
def evaluate_performance(met, base):
    # Step 1: Compute efficiency score
    eff_score = calculate_efficiency(met["latency"], met["success_rate"])
    
    # Step 2: Assess load distribution
    load_list = list(node_load.values())
    balance_score = assess_load_balance(load_list)
    
    # Step 3: Latency deviation penalty
    latency_deviation = abs(met["latency"] - base["latency"]) * 10
    dev_penalty = -int(latency_deviation * 5) if latency_deviation > 0.5 else 0
    
    # Step 4: Success rate multiplier (conditional expression)
    multiplier = 1.2 if met["success_rate"] >= base["success_rate"] else 0.8
    
    # Step 5: Load variance penalty (additional distractor logic)
    high_load_nodes = [k for k, v in node_load.items() if v > 80]
    critical_count = len(high_load_nodes)
    load_var_penalty = -5 * critical_count
    
    # Step 6: Aggregate final raw score before adjustment
    raw_score = eff_score + balance_score + dev_penalty + load_var_penalty
    
    # Step 7: Adjustment based on pending tasks (hidden relevance)
    task_backlog_factor = len(pending_tasks) * -2
    
    # Step 8: Final adjustment with conditional expression
    adjusted_score = raw_score * multiplier
    final_score = int(adjusted_score) + task_backlog_factor
    
    # Irrelevant print debug (distractor)
    # print(f'Debug - raw: {raw_score}, mult: {multiplier}, adj: {adjusted_score}')
    
    return final_score

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")