from collections import defaultdict, Counter

# Simulate system resource allocation and usage audit
def analyze_resource_utilization(config_matrix):
    # Irrelevant pre-processing (distractor)
    temp_weights = [config_matrix[i][i % len(config_matrix[0])] for i in range(len(config_matrix))]
    normalization_factor = sum(w ** 0.5 for w in temp_weights if w > 0) or 1
    adjusted_weights = [w / normalization_factor for w in temp_weights]

    # Actual data of interest
    resource_map = defaultdict(lambda: 'unknown')
    resource_map.update({
        'disk_io': 'storage',
        'net_bandwidth': 'network',
        'gpu_load': 'compute',
        'ram_swap': 'memory'
    })

    usage_log = [
        ('disk_io', 120), ('net_bandwidth', 45), ('disk_io', 180),
        ('gpu_load', 95), ('ram_swap', 60), ('net_bandwidth', 30),
        ('disk_io', 210), ('gpu_load', 105)
    ]

    # Misleading intermediate calculation (dead path)
    peak_usage = max([record[1] for record in usage_log])
    avg_latency = sum([x[1] * 0.03 for x in usage_log]) / len(usage_log)
    theoretical_capacity = peak_usage * len(resource_map) * 0.75

    # Core logic: count valid high-usage events per category
    usage_counter = Counter()
    for resource, usage in usage_log:
        category = resource_map[resource]
        if usage > 100 and category in ['compute', 'storage']:
            usage_counter[category] += 1
        elif usage > 50 and category == 'network':
            usage_counter[category] += 0.5  # partial credit for network

    # Calculate efficiency score based on thresholds
    raw_score = sum(
        val * (1.5 if key == 'compute' else 1.0)
        for key, val in usage_counter.items()
    )

    # Secondary adjustment using config_matrix (only some rows matter)
    bonus_factor = 0
    for i in range(len(config_matrix)):
        if sum(config_matrix[i]) > 10:
            bonus_factor += 0.1

    # Final efficiency score computation
    efficiency_score = int(raw_score * 10 + bonus_factor * 10)

    # Dead code branch (never executed, but looks relevant)
    if __debug__:
        debug_trace = [f"{k}:{v}" for k, v in sorted(usage_counter.items())]
        print(f"Debug info: {debug_trace}")

    return efficiency_score

# Input configuration matrix (simulated hardware profile)
config_matrix = [
    [2, 3, 5],
    [8, 1, 4],
    [6, 7, 2],
    [1, 1, 1],
    [4, 4, 4]
]

# Execute main logic
efficiency_score = analyze_resource_utilization(config_matrix)
print(f"Result: {efficiency_score}")