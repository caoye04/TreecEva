from itertools import combinations

# Network node performance data (latency in ms, throughput in Mbps)
nodes = [(12, 85), (23, 64), (15, 90), (19, 70), (11, 95)]

# Extract throughputs and latencies using zip
throughputs, latencies = zip(*nodes)

# Calculate average latency (distractor computation)
avg_latency = sum(latencies) / len(latencies)
fluctuation_score = max(latencies) - min(latencies)

# Identify high-performing nodes: throughput > 80 and latency < 16
high_perf_nodes = [node for node in nodes if node[1] > 80 and node[0] < 16]

# Generate all possible pairs of high-performing nodes (semi-relevant)
perf_pairs = list(combinations(high_perf_nodes, 2))

# Total raw capacity from all nodes
raw_capacity = sum(throughputs)

# Apply load distribution efficiency: modeled as harmonic mean
inv_sum = sum(1 / t for t in throughputs)
harmonic_mean = len(throughputs) / inv_sum
load_efficiency_factor = harmonic_mean / 100  # Normalize to [0,1]

# Effective aggregate capacity after efficiency tuning
aggregate_capacity = int(raw_capacity * load_efficiency_factor)

# Simulate congestion events based on latency variance
latency_variance = sum((l - avg_latency) ** 2 for l in latencies) / len(latencies)
congestion_events = int(latency_variance // 5)  # Events per monitoring window

# Throttling offset based on event count and fixed penalty
base_throttle = 12
throttling_offset = congestion_events * base_throttle + len(perf_pairs)  # Minor influence from pair count

# Critical assignment: final available bandwidth
final_bandwidth = aggregate_capacity - throttling_offset

# Print result for verification
print(f"Result: {final_bandwidth}")