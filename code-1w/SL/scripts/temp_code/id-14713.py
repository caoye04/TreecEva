import math

# Network optimization simulation with decoy functions and irrelevant computations
def calculate_latency(hops, distance):
    # Irrelevant function - not used in final computation
    return (hops * 0.15) + (distance / 1000) * 0.3

def encrypt_packet(data, key):
    # Dead code path - never called
    return sum((d ^ key) % 256 for d in data)

def analyze_redundancy(paths):
    # Unused analysis function with misleading intermediate logic
    redundancy_score = 0
    for p in paths:
        if len(p) > 3:
            redundancy_score += 0.7
        else:
            redundancy_score += 0.2
    return redundancy_score

def generate_routing_table(nodes):
    # Distractor: generates table but not used
    table = {}
    for i, node in enumerate(nodes):
        table[node] = f'Route_{(i*17)%5}'
    return table

def simulate_congestion(flow_rates):
    # Red herring function: simulates but result ignored
    peak = max(flow_rates)
    avg = sum(flow_rates) / len(flow_rates)
    return (peak - avg) * 1.8

# Core parameters
traffic_load = [125, 200, 95, 300, 175]
link_matrix = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0]
]

topology_score = 0
for row in link_matrix:
    topology_score += sum(row) * 0.6  # Irrelevant accumulation

# Misleading intermediate calculation chain
candidate_peaks = [x * 1.1 for x in traffic_load if x > 150]
adjusted_peaks = []
for val in candidate_peaks:
    if val > 250:
        adjusted_peaks.append(val * 0.9)
    else:
        adjusted_peaks.append(val * 1.05)
aggregate_peak = sum(adjusted_peaks) / len(adjusted_peaks) if adjusted_peaks else 0

# Decoy variables with plausible names
efficiency_ratio = aggregate_peak / 350 if aggregate_peak else 0.0
normalization_factor = efficiency_ratio ** 0.5 if efficiency_ratio > 0 else 1.0
baseline_capacity = 1000 * normalization_factor  # Looks important, unused

# Real computation buried among distractions
active_links = 0
for i in range(len(link_matrix)):
    for j in range(len(link_matrix[i])):
        if link_matrix[i][j] == 1:
            active_links += 1

# Conditional expression determining effective load
max_load = max(traffic_load)
effective_load = max_load if max_load > 250 else (max_load * 1.3 if max_load > 100 else max_load * 1.5)

# Simulated packet loss adjustment (used in real logic)
packet_loss_rate = (active_links / 25) * 0.04
loss_adjustment = 1 - packet_loss_rate if packet_loss_rate < 0.1 else 0.9

# Optimization function combining multiple concepts
def optimize_bandwidth(matrix, load):
    total_connections = sum(sum(row) for row in matrix)
    peak_traffic = max(load)
    avg_traffic = sum(load) / len(load)
    
    # Determine redundancy multiplier using conditional expression
    redundancy_multiplier = 1.2 if any(sum(row) >= 3 for row in matrix) else 0.9
    
    # Apply traffic pattern factor
    burst_factor = 1.4 if peak_traffic > 2 * avg_traffic else 1.1
    
    # Compute base bandwidth
    base_bw = peak_traffic * burst_factor * redundancy_multiplier
    
    # Additional adjustment based on connection density
    density = total_connections / (len(matrix) ** 2)
    density_factor = 1.15 if density >= 0.4 else 0.95
    
    # Final bandwidth calculation
    bandwidth = base_bw * density_factor * loss_adjustment
    
    # Distractor: modify unused state
    global topology_score
    topology_score += bandwidth * 0.01  # Side effect, not relevant
    
    return bandwidth

# Execute main logic
final_bandwidth = optimize_bandwidth(link_matrix, traffic_load)

# Print result as required
print(f"Result: {final_bandwidth}")