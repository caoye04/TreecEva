def analyze_traffic_flow(bandwidth, usage):
    if bandwidth <= 0:
        return 0
    utilization = (usage / bandwidth) * 100
    return utilization if utilization <= 100 else 100

# Simulate network node configurations
topology_nodes = [10, 15, 20, 25, 30]
base_bandwidths = [100, 120, 140, 160, 180]
current_usage = [85, 95, 130, 150, 175]

# Irrelevant metric: latency simulation (dead computation)
latency_shift = sum([abs(base_bandwidths[i] - current_usage[i]) for i in range(len(base_bandwidths))]) // 5

# Compute per-node traffic analysis
traffic_metrics = [
    analyze_traffic_flow(base_bandwidths[i], current_usage[i]) 
    for i in range(len(topology_nodes))
]

# Initialize system state with decoy variables
event_log = {'timestamp': 12345, 'status': 'active', 'mode': 'debug'}
system_health = 98.5
baseline_offset = 2.3  # Unused in final logic

# Threshold configuration map (used later)
threshold_map = {
    'critical': 90,
    'high': 75,
    'normal': 50
}

# Network load aggregation with conditional weighting
network_load = 0
for i, metric in enumerate(traffic_metrics):
    weight = 1.2 if metric > threshold_map['high'] else 0.8
    adjusted_load = metric * weight
    # Misleading update - doesn't affect final result
    if i % 2 == 0:
        network_load += adjusted_load * 0.9
    else:
        network_load += adjusted_load

# Red herring: cache simulation with no impact
cache_pool = set()
for val in traffic_metrics:
    normalized = int(val // 10)
    cache_pool.add(normalized)
    cache_pool.discard(10)  # Pointless operation

# Real computation begins: equilibrium calculation
def calculate_equilibrium(load, thresholds):
    surge_factor = 1.1
    if load > thresholds['critical'] * 1.5:
        surge_factor = 1.3
    elif load > thresholds['high'] * 1.2:
        surge_factor = 1.2
    
    # Apply surge and dampening
    amplified = load * surge_factor
    dampened = amplified * 0.95
    
    # Final adjustment based on even/odd characteristic of integer part
    int_part = int(dampened)
    parity_correction = 0.9 if int_part % 2 == 0 else 1.05
    return dampened * parity_correction

# Execute key statement
temp_diagnostic = sum(traffic_metrics) / len(traffic_metrics)  # Distractor
final_load = calculate_equilibrium(network_load, threshold_map)
print(f"Result: {final_load}")