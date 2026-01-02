import itertools

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 85, 200, 90, 150, 110, 95]
task_failures = [0, 1, 0, 2, 0, 1, 0]
node_loads = [0.65, 0.88, 0.45, 0.92, 0.73, 0.80, 0.50]
packet_loss_rate = [0.001, 0.003, 0.002, 0.012, 0.005, 0.004, 0.001]

# Irrelevant telemetry (distractor data)
gpu_temperatures = [68, 72, 65, 80, 70, 75, 69]  # unused
disk_io_ops = [1200, 1500, 1100, 1800, 1300, 1400, 1250]  # unused
timestamps = list(range(1000, 1007))  # unused

# Misleading preprocessing (dead path)
def analyze_health(metrics):
    return sum(m ** 2 for m in metrics if m > 0.5)  # never called

# Decoy weight set (red herring)
decoy_weights = {'latency': 0.1, 'failures': 0.7, 'load': 0.1, 'loss': 0.1}

# Real performance weights
weights = {
    'latency': 0.4,
    'failures': 0.3,
    'load': 0.2,
    'loss': 0.1
}

# Auxiliary function using enumerate and zip (relevant)
def normalize(series):
    mean_val = sum(series) / len(series)
    return [(val - mean_val) / mean_val for val in series]

# Complex transformation with lambda and itertools (mixed relevance)
smoothed_durations = list(map(lambda x: x * 0.9 + 10, task_durations))
expanded_pairs = list(itertools.product([1], smoothed_durations[:3]))  # partial use

# Generate index-aligned normalized metrics
norm_durations = normalize(smoothed_durations)
norm_failures = normalize([f + 0.1 for f in task_failures])
norm_loads = normalize(node_loads)
norm_loss = normalize(packet_loss_rate)

# Spurious aggregation (irrelevant)
peak_metrics = [max(vals) for vals in zip(task_durations, node_loads)]  # unused

# Core evaluation logic
metrics = []
for i, (dur, fail, load, loss) in enumerate(zip(norm_durations, norm_failures, norm_loads, norm_loss)):
    # Artificial complexity with conditional scaling
    adjustment = 1.1 if i % 2 == 0 else 0.95
    score_components = {
        'latency': abs(dur) * adjustment,
        'failures': abs(fail) * 1.5,
        'load': abs(load),
        'loss': abs(loss) * 2.0
    }
    metrics.append(score_components)

# Secondary red herring: incorrect aggregation method
total_risk = 0
for m in metrics:
    total_risk += m['failures'] * m['loss']  # looks important but unused

# Correct scoring using proper weights
def evaluate_performance(performance_metrics, w):
    total = 0.0
    for entry in performance_metrics:
        # Weighted sum with non-linear penalty
        base = sum(entry[k] * w[k] for k in w)
        penalty = (entry['load'] ** 2) * 0.1
        total += base + penalty
    return int(total * 100)  # deterministic integer output

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")