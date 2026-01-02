def calculate_route_efficiency(distance, fuel_used):
    if distance <= 0:
        return 0.0
    return (distance / fuel_used) * 0.85

# Simulate warehouse logistics optimization
base_storages = [150, 300, 250, 400]
distance_map = {i: base_storages[i] * 0.75 for i in range(len(base_storages))}
fuel_estimates = {i: distance_map[i] / 12.5 for i in range(len(distance_map))}

# Efficiency scores (distractor computations)
efficiency_scores = {}
for route in distance_map:
    efficiency = calculate_route_efficiency(distance_map[route], fuel_estimates[route])
    efficiency_scores[route] = round(efficiency, 2)

# Real computation begins: resource allocation simulation
stock_levels = {i: base_storages[i] for i in range(4)}
allocation_sequence = [(0, 50), (1, 75), (2, 100), (3, 60), (0, 25), (1, 50)]
logistics_map = {
    'capacity': {idx: val for idx, val in enumerate(base_storages)},
    'utilization': {0: 0, 1: 0, 2: 0, 3: 0},
    'maintenance_required': False
}

# Auxiliary tracking variables (some irrelevant)
total_dispatched = 0
historical_peak = 0
transfer_logs = []

for location, amount in allocation_sequence:
    if stock_levels[location] >= amount:
        stock_levels[location] -= amount
        logistics_map['utilization'][location] += amount
        total_dispatched += amount
        transfer_logs.append(f'Dispatched {amount} to Zone-{location}')
    else:
        # Over-allocation triggers maintenance flag (not actually used later)
        logistics_map['maintenance_required'] = True

# Secondary loop: normalize utilization into percentage (semi-relevant)
normalized_util = {}
max_capacity = sum(base_storages)
total_used = sum(logistics_map['utilization'].values())
for k in logistics_map['utilization']:
    normalized_util[k] = (logistics_map['utilization'][k] / logistics_map['capacity'][k]) * 100

# Distractor: simulate diagnostic check
consistency_flag = True
for cap_key in logistics_map['capacity']:
    if logistics_map['capacity'][cap_key] < 0:
        consistency_flag = False

# Critical function: compute remaining system capacity
def calculate_remaining_capacity(logistics_map, sequence):
    used_total = sum(logistics_map['utilization'].values())
    cap_total = sum(logistics_map['capacity'].values())
    temp_buffer = 0
    for _, amt in sequence:
        temp_buffer += amt * 0.1  # Simulate buffer usage (red herring)
    net_available = cap_total - used_total - temp_buffer
    return int(net_available)

# Final computation step
final_capacity = calculate_remaining_capacity(logistics_map, allocation_sequence)
print(f"Result: {final_capacity}")