def analyze_efficiency(data, threshold=0.75):
    """Irrelevant efficiency analysis function (dead code path)."""
    return sum(x > threshold for x in data) / len(data)

optimization_log = [0.6, 0.8, 0.9, 0.7]
def update_cache(value):
    """Unused side-effect function."""
    optimization_log.append(value)

baseline = {
    'latency': 120,
    'throughput': 850,
    'error_rate': 0.01,
    'memory': 256
}

# Irrelevant system monitoring variables
cpu_load = [0.4, 0.6, 0.8]
disk_io = {'read': 120, 'write': 80}

config_flags = {
    'enable_retry': True,
    'use_cache': False,
    'log_verbose': True
}

legacy_weights = [0.1, 0.3, 0.4, 0.2]  # Unused in final calculation

scaling_factor = 1.5
temp_offset = 22

metrics = [
    ('latency', 110, 120),
    ('throughput', 900, 850),
    ('error_rate', 0.008, 0.01),
    ('memory', 240, 256)
]

# Misleading intermediate transformation
transformed = list(map(lambda x: (x[0], (x[1] - x[2]) * scaling_factor + temp_offset), metrics))

# Decoy scoring with unused logic
raw_scores = []
for name, diff in transformed:
    if name == 'latency':
        raw_scores.append(max(0, 100 - abs(diff)))
    elif name == 'throughput':
        raw_scores.append(min(100, 50 + diff))
    else:
        raw_scores.append(75)  # default placeholder

# Actual relevant logic buried among distractions
weight_map = {
    'latency': 0.3,
    'throughput': 0.4,
    'error_rate': 0.2,
    'memory': 0.1
}

normalized = {key: (baseline[key] - val[1]) / baseline[key] for key, val in zip(weight_map.keys(), metrics)}

adjusted = {k: round(v * 100 * w, 2) for k, v in normalized.items() for w in [weight_map[k]]}

# Critical statement: this is where the answer is determined
final_score = int(sum(adjusted.values()) + 0.5)

# Red herring: unrelated aggregation
aggregate_health = sum([len(str(x)) for x in disk_io.values()]) + len(cpu_load)

# Another decoy function call
_ = analyze_efficiency([0.5, 0.8, 0.9])

# Output required result
print(f"Target result: {final_score}")