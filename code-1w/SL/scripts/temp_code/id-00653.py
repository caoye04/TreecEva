from itertools import combinations

# Simulate pressure readings from a distributed network of nodes
node_pressures = [1024, 987, 1003, 995, 1012, 976, 1008]

# Irrelevant baseline calibration offset (not used in final logic)
calibration_offset = sum(node_pressures) // len(node_pressures) - 1000

# Track cumulative variance for diagnostic purposes (semi-relevant but not decisive)
cumulative_variance = 0
variance_log = []

# Compute pairwise absolute differences to detect instability
pairwise_deltas = []
for pair in combinations(node_pressures, 2):
    delta = abs(pair[0] - pair[1])
    pairwise_deltas.append(delta)
    cumulative_variance += delta ** 0.5
    variance_log.append(cumulative_variance)

# Misleading trend analysis with no impact on result
trend_flags = [1 if i > 0 and node_pressures[i] > node_pressures[i-1] else 0 for i in range(len(node_pressures))]
spike_count = sum([1 for d in pairwise_deltas if d > 30])

# Core logic: identify deltas between adjacent sorted pressures below threshold
sorted_pressures = sorted(node_pressures)
adjacent_deltas = [sorted_pressures[i+1] - sorted_pressures[i] for i in range(len(sorted_pressures)-1)]

# Filter for stable transitions (small changes)
stability_threshold = 15
filtered_deltas = [d for d in adjacent_deltas if d < stability_threshold]

# Key computation point
equilibrium_score = max(filtered_deltas) if filtered_deltas else 0

# Dead code path — never executed but adds cognitive load
if __debug__:
    debug_state = {"nodes": len(node_pressures), "max_delta": max(pairwise_deltas)}

# Print target result
print(f"Result: {equilibrium_score}")