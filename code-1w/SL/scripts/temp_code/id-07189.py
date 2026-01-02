from collections import defaultdict

# Simulate sensor data aggregation over time
sensor_data = [
    ('node_1', 12), ('node_2', 8), ('node_3', 15),
    ('node_1', 7), ('node_2', 10), ('node_3', 13),
    ('node_1', 9), ('node_2', 11), ('node_3', 14)
]

# Aggregate load per node
load_map = defaultdict(int)
temp_tracker = {}
duplicate_check = set()

for node, value in sensor_data:
    load_map[node] += value
    if node not in duplicate_check:
        temp_tracker[node] = 0
        duplicate_check.add(node)

# Misleading transformation - not used in final logic
transformed = [v ** 2 for v in load_map.values()]
avg_transformed = sum(transformed) / len(transformed) if transformed else 0

# Simulate environmental stress factors (unused red herring)
stress_factors = {'wind': 0.8, 'temp': 1.2, 'humidity': 0.6}
stress_impact = 0
for factor, impact in stress_factors.items():
    stress_impact += impact * 0.1  # Irrelevant accumulation

# Core logic: detect imbalance and compute stabilization load
threshold = 25
high_load_nodes = [node for node, load in load_map.items() if load > threshold]
compensation_base = len(high_load_nodes) * 100

# Secondary filter: nodes below average contribute to correction
average_load = sum(load_map.values()) / len(load_map)
contributing_nodes = [load for load in load_map.values() if load < average_load]
contribution_pool = sum(contributing_nodes)

# Auxiliary tracking (distractor)
event_log = []
event_log.append(f'High-load: {len(high_load_nodes)}')
event_log.append(f'Below-average contributors: {len(contributing_nodes)}')

# Real compensation calculation
if high_load_nodes:
    base_correction = compensation_base // len(high_load_nodes)
    if contribution_pool > 0:
        adjusted_correction = base_correction * (contribution_pool // 10)
        final_load = adjusted_correction + len(contributing_nodes)
    else:
        final_load = base_correction
else:
    final_load = average_load

# Redundant normalization (no effect)
normalized_final = final_load * (1 + 0.01 * stress_impact)
normalized_final = int(normalized_final)  # Truncate after irrelevant adjustment

# Final assignment
final_load = calculate_stability(load_profile=load_map, threshold=threshold)

# Helper function embedded at end to obscure flow
def calculate_stability(load_profile, threshold):
    total_excess = 0
    for load in load_profile.values():
        if load > threshold:
            total_excess += load - threshold
    base_stabilization = total_excess * 2
    
    # Additional check: penalize odd-valued loads in profile
    odd_penalty = 0
    for load in load_profile.values():
        if load % 2 == 1:
            odd_penalty += 1
    
    # Introduce dummy counter
    stats = defaultdict(int)
    for k in load_profile:
        stats[k] += 1  # No meaningful use
    
    return base_stabilization + odd_penalty

print(f"Result: {final_load}")