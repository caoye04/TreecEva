import math

# Simulated network node performance data (irrelevant to final result)
node_stability_log = [0.98, 0.99, 0.97, 0.95, 0.96]
stability_threshold = 0.90

def calculate_jitter_score(records):
    # Dead function - never called
    return sum((1 - r) ** 2 for r in records if r < stability_threshold)

# Core system parameters
base_frequency = 2400
modulation_levels = 64
packet_size_bits = 1500 * 8
overhead_ratio = 0.12

# Irrelevant diagnostic counters
diag_counter_a = 0
diag_counter_b = 0
diag_counter_c = 0

# Simulated flow matrix between network nodes (key input)
flow_matrix = [
    [0, 120, 85, 0],
    [95, 0, 150, 60],
    [70, 130, 0, 110],
    [0, 55, 95, 0]
]

# Latency map in milliseconds (key input)
latency_map = [
    [0, 12, 8, 999],
    [14, 0, 6, 10],
    [9, 16, 0, 7],
    [999, 11, 13, 0]
]

# Red herring: unused but plausible-looking weight matrix
weight_matrix = [[1/(latency_map[i][j] + 1) if latency_map[i][j] != 999 else 0 
                  for j in range(4)] for i in range(4)]

# Misleading intermediate calculation (never used)
effective_throughput = (base_frequency * math.log2(modulation_levels)) * (1 - overhead_ratio)
theoretical_max = effective_throughput * 0.75  # Assumed efficiency cap

# Auxiliary functions that appear important but are distractions
def analyze_congestion(flows):
    global diag_counter_a, diag_counter_b
    total_load = sum(sum(row) for row in flows)
    avg_load = total_load / len(flows)**2
    diag_counter_a += 1
    return [row[:] for row in flows if sum(row) > avg_load]

def compute_hop_efficiency(latencies):
    global diag_counter_c
    clean_latencies = []
    for row in latencies:
        filtered = [x for x in row if x < 50]
        if filtered:
            clean_latencies.append(sum(filtered)/len(filtered))
    diag_counter_c += 1
    return clean_latencies

# Key optimization function - only this affects the final answer
def optimize_routing(flows, latencies):
    n = len(flows)
    total_utilization = 0.0
    
    # Compute direct utilization from flows and inverse latency weighting
    for i in range(n):
        for j in range(n):
            if i != j and flows[i][j] > 0 and latencies[i][j] < 999:
                # Weight each flow by inverse latency (higher latency = lower weight)
                weight = 1 / latencies[i][j]
                total_utilization += flows[i][j] * weight
    
    # Apply nonlinear scaling based on modulation and packet size
    scaling_factor = math.log2(modulation_levels) * (1 - overhead_ratio)
    raw_bandwidth = total_utilization * scaling_factor
    
    # Secondary adjustment using set operations to filter high-latency paths
    critical_paths = set()
    for i in range(n):
        for j in range(n):
            if latencies[i][j] >= 10:
                critical_paths.add((i, j))
    
    # Reduce bandwidth proportionally to number of critical paths
    penalty_rate = len(critical_paths) / (n * n)
    adjusted_bandwidth = raw_bandwidth * (1 - penalty_rate)
    
    # Final nonlinear transformation
    final = int(adjusted_bandwidth // 1)  # Integer division
    
    # Dead assignment - looks important but unused
    peak_capacity = base_frequency * 12  # GHz-scale distraction
    
    return final

# Execution path with multiple side computations
active_flows = [row[:] for row in flow_matrix]  # Copy

# Spurious transformations (distractors)
scaled_flows = []
for row in active_flows:
    scaled_row = []
    for x in row:
        if x > 100:
            scaled_row.append(x * 0.95)
        elif x > 50:
            scaled_row.append(x * 0.98)
        else:
            scaled_row.append(x)
    scaled_flows.append(scaled_row)

# Unused but plausible analysis
topology_density = sum(1 for row in flow_matrix for x in row if x > 0) / (4*4)

# Another red herring function call
congested_segments = analyze_congestion(flow_matrix)
hop_efficiency_stats = compute_hop_efficiency(latency_map)

# Critical execution point
final_bandwidth = optimize_routing(flow_matrix, latency_map)

# Print required output
print(f"Result: {final_bandwidth}")