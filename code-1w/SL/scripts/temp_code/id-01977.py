def process_timestamps(ts_list):
    # Irrelevant function: processes timestamps but not used in main logic
    return [t % 86400 for t in ts_list if t > 0]


def deprecated_calc(v):
    # Dead code path: never called
    return (v ** 2 + 3 * v + 1) // 2

# Misleading intermediate constants
temp_offset = 45.6
correction_factor = 0.987
baseline_threshold = 127

# Distractor data structures
auxiliary_map = {i: i * 3 + 1 for i in range(10)}
decoys = [0] * 5
for k in range(len(decoys)):
    decoys[k] = k * 100 + 23

# Real data used in computation
raw_data = [18, 25, 34, 12, 47, 29, 33]

# Dictionary operations with relevant and irrelevant keys
metric_weights = {
    'accuracy': 0.4,
    'latency': 0.2,
    'throughput': 0.25,
    'reliability': 0.15,
    'bandwidth': 0.0,  # Unused weight (red herring)
    'jitter': 0.0       # Unused metric
}

# Lambda functions for dynamic filtering
outlier_filter = lambda x: 20 <= x <= 40
filtered_data = list(filter(outlier_filter, raw_data))

# Secondary transformation with distraction
adjusted_values = []
for val in raw_data:
    temp_val = val + 5
    if temp_val > 45:
        temp_val -= 10
    adjusted_values.append(temp_val)  # Computed but not used

# Simulated recursion (not directly used in final answer but looks important)
def recursive_sum(n):
    return n + recursive_sum(n - 1) if n > 1 else 1

# Unused nested structure
data_cube = [[[i+j+k for k in range(2)] for j in range(2)] for i in range(3)]

# Core logic disguised among distractions
effective_metrics = []
for key, weight in metric_weights.items():
    if weight > 0:  # Filters out decoy metrics
        if key == 'accuracy':
            effective_metrics.append(weight * sum(filtered_data))
        elif key == 'latency':
            effective_metrics.append(weight * min(filtered_data))
        elif key == 'throughput':
            effective_metrics.append(weight * len(filtered_data))
        elif key == 'reliability':
            # Complex expression to distract
            base = 10
            for _ in range(2):
                base *= 2
            effective_metrics.append(weight * base)

# Linear search for no effect (distractor)
def find_peak(lst):
    if not lst:
        return -1
    peak = lst[0]
    for item in lst:
        if item > peak:
            peak = item
    return peak

# Unused set operation
unique_set = set(raw_data)
unique_set.add(baseline_threshold)

# Actual answer derivation buried in logic
def evaluate_performance(weights, data):
    # Step 1: filter valid data points
    valid_points = [x for x in data if x >= 25]
    # Step 2: compute weighted components
    w_acc = weights['accuracy'] * sum(valid_points)
    w_latency = weights['latency'] * max(data)
    w_throughput = weights['throughput'] * len([d for d in data if d < 30])
    w_reliability = weights['reliability'] * 40  # Fixed contribution
    # Step 3: aggregate
    total = w_acc + w_latency + w_throughput + w_reliability
    # Step 4: apply hidden offset (from distractor constant)
    result = total - temp_offset  # Uses misleading global
    return int(result)

# Key execution point
final_score = evaluate_performance(metric_weights, raw_data)

# Output the target result
print(f"Result: {final_score}")