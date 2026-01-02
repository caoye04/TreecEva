from collections import defaultdict
import math

# Simulate system health monitoring with performance metrics
def collect_metrics():
    data = defaultdict(float)
    data['cpu_load'] = 78.2
    data['memory_usage'] = 65.4
    data['disk_iops'] = 1200
    data['network_latency_ms'] = 45.6
    data['error_rate'] = 0.034
    data['throughput_tps'] = 230
    data['temperature_c'] = 67.1
    return data

# Secondary irrelevant metric collector (distractor)
def gather_logs():
    logs = []
    for i in range(5):
        logs.append(f"Log entry {i}: operational")
    # This function returns nothing useful
    return None

# Auxiliary calculation: efficiency ratio (semi-relevant)
def compute_efficiency(cpu, memory, tps):
    return (tps / (cpu + memory + 1)) * 100

# Heuristic to determine stability class (not used in final score but looks important)
def classify_stability(latency, errors):
    if latency < 50 and errors < 0.05:
        return 'STABLE'
    elif latency < 100 and errors < 0.1:
        return 'CAUTIOUS'
    else:
        return 'UNSTABLE'

# Core evaluation logic
metrics = collect_metrics()

# Irrelevant intermediate transformation (dead code path)
shadow_copy = {k: v * 1.0 for k, v in metrics.items()}
shadow_copy['checksum'] = sum(len(k) for k in shadow_copy.keys())

# Define weighting scheme for performance score
weights = defaultdict(float)
weights['cpu_load'] = 0.1
weights['memory_usage'] = 0.1
weights['throughput_tps'] = 0.3
weights['disk_iops'] = 0.2
weights['network_latency_ms'] = -0.1  # Inverse impact
weights['error_rate'] = -0.2

# Lambda-based normalization function (used)
normalize = lambda x, ideal: 1 - abs(x - ideal) / (ideal + 1)

# Initialize accumulator
raw_sum = 0.0
weight_sum = 0.0

# Main scoring loop with filtering
for key in metrics:
    if key not in weights:
        continue  # Skip unweighted metrics
    
    raw_value = metrics[key]
    weight = weights[key]
    
    # Normalize critical metrics
    if key == 'network_latency_ms':
        normalized = normalize(raw_value, 20)
    elif key == 'error_rate':
        normalized = normalize(raw_value, 0.01)
    elif key == 'throughput_tps':
        normalized = min(raw_value / 300, 1.0)  # Cap at 300 TPS
    else:
        normalized = raw_value / 100.0  # Scale to 0-1
    
    contribution = normalized * abs(weight)
    raw_sum += contribution
    weight_sum += abs(weight)
    
    # Early termination heuristic (never triggers due to data)
    if raw_value > 1000 and key == 'disk_iops':
        raw_sum *= 0.9
        break

# Compute weighted average
if weight_sum > 0:
    base_score = raw_sum / weight_sum
else:
    base_score = 50.0

# Bonus calculation based on efficiency (semi-relevant)
efficiency = compute_efficiency(metrics['cpu_load'], metrics['memory_usage'], metrics['throughput_tps'])
bonus = 0.0
if efficiency > 200:
    bonus = 5.0
elif efficiency > 150:
    bonus = 2.5

# Stability classification (completely irrelevant to final score)
stability_class = classify_stability(metrics['network_latency_ms'], metrics['error_rate'])

gather_logs()  # Call with no side effect

# Final score computation
final_score = int(base_score * 100 + bonus)

# Print result as required
Target result: {final_score}