from collections import defaultdict
from itertools import cycle

# Simulate time-series resource allocation across nodes
def balance_distribution(flow_data, threshold):
    cumulative = defaultdict(float)
    peak_moments = []
    temp_buffer = 0
    adjustment_factor = 1.0
    decay_rate = 0.9

    for tick, (node, load) in enumerate(flow_data):
        if load > threshold * 1.5:
            peak_moments.append(tick)
        if load > threshold:
            adjusted_load = load * decay_rate
        else:
            adjusted_load = load + temp_buffer * 0.1

        cumulative[node] += adjusted_load

        # Irrelevant tracking of buffer drift (distractor)
        temp_buffer = (temp_buffer + load) % 7

        # Extra logic that doesn't affect final result
        if tick % 5 == 0:
            adjustment_factor *= 0.98

    # Secondary processing: normalize by node count (misleading)
    node_count = len(cumulative)
    if node_count > 3:
        scaling = sum(cumulative.values()) / node_count
        for node in cumulative:
            cumulative[node] -= scaling * 0.1  # Minor perturbation

    # Final aggregation into single metric
    total = sum(value for value in cumulative.values() if value > 0.5)
    stability_penalty = len(peak_moments) * 0.2
    return int(total - stability_penalty)

# Generate synthetic input flow
phases = ['alpha', 'beta', 'gamma', 'delta']
base_loads = [12, 18, 15, 22, 14, 10, 25, 19, 16, 21]

resource_ticks = []
for i, load in enumerate(base_loads):
    phase = phases[i % len(phases)]
    resource_ticks.append((phase, load))

    # Dead code branch – never executed but adds cognitive load
    if False:
        resource_ticks.append(('unknown', 0))

# Unused helper (distractor)
def analyze_fragmentation(seq):
    return {x: seq.count(x) for x in set(seq)}

threshold = 16
intermediate_snapshot = [x for x in resource_ticks if x[1] > threshold]

# Key execution point
final_load = balance_distribution(resource_ticks, threshold)
print(f"Result: {final_load}")