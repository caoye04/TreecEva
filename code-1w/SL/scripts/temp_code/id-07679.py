def analyze_system_load(usage_data):
    # Irrelevant transformation: normalize timestamps
    normalized_times = [(t - min(usage_data)) / (max(usage_data) - min(usage_data) + 1e-9) for t in usage_data]
    
    # Distractor: unused statistical calculation
    mean_val = sum(usage_data) / len(usage_data)
    variance = sum((x - mean_val) ** 2 for x in usage_data) / len(usage_data)
    std_dev = variance ** 0.5

    # Relevant: count how many exceed threshold
    high_load_count = sum(1 for x in usage_data if x > 80)
    return high_load_count

# Unused decoy function with complex logic
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Simulated monitoring metrics (CPU, memory, disk, network)
metrics = [
    {'type': 'cpu', 'usage': 85, 'critical': True},
    {'type': 'memory', 'usage': 92, 'critical': True},
    {'type': 'disk_io', 'usage': 45, 'critical': False},
    {'type': 'network', 'usage': 60, 'critical': False}
]

# Weights for scoring (only some are actually used)
weights = {
    'cpu_weight': 0.4,
    'memory_weight': 0.3,
    'disk_weight': 0.1,  # Not used but looks important
    'network_weight': 0.1 # Also not used
}

# Auxiliary irrelevant list for distraction
maintenance_windows = ["02:00", "04:30", "15:10"]
disk_readings = [33, 47, 52, 61, 44, 55]

# Extract relevant usages and types using zip and enumerate (required features)
data_stream = [m['usage'] for m in metrics]
labels = [m['type'] for m in metrics]
indexed_metrics = []
for i, (label, value) in enumerate(zip(labels, data_stream)):
    indexed_metrics.append((i, label, value))

# Perform load analysis (irrelevant to final result but plausible)
high_load_nodes = analyze_system_load(data_stream)

# Distractor: set operations that look meaningful but don't affect outcome
active_components = set(label for label in labels)
target_components = set(['cpu', 'memory', 'gpu'])
overlapping = active_components & target_components  # {'cpu', 'memory'}
missing = target_components - active_components     # {'gpu'}

# Real computation begins here — only CPU and memory contribute
weighted_sum = 0.0
for entry in metrics:
    typ = entry['type']
    usage = entry['usage']
    if typ == 'cpu':
        weighted_sum += usage * 0.4
    elif typ == 'memory':
        weighted_sum += usage * 0.3

# Additional irrelevant aggregation
average_usage = sum(m['usage'] for m in metrics) / len(metrics)
utilization_rate = average_usage / 100

# Final performance score based on key components
penalty = 0
if high_load_nodes >= 2:
    penalty = 15  # deduction for multiple overloaded systems

final_score = int(weighted_sum - penalty)

# Print result as required
print(f"Target result: {final_score}")