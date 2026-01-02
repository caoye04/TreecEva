def analyze_redundancy(components):
    critical = set()
    for comp in components:
        if comp['reliability'] < 0.95:
            critical.add(comp['id'])
    return critical

components_list = [
    {'id': 'C1', 'reliability': 0.98, 'type': 'sensor'},
    {'id': 'C2', 'reliability': 0.87, 'type': 'actuator'},
    {'id': 'C3', 'reliability': 0.96, 'type': 'controller'},
    {'id': 'C4', 'reliability': 0.82, 'type': 'sensor'}
]

# Irrelevant computation - simulates system latency but unused
latency_simulation = sum([i * 0.05 for i in range(10)])
baseline_offset = 12.8
adjusted_metrics = [0.98, 0.87, 0.96, 0.82]
smoothed = [x + baseline_offset for x in adjusted_metrics]

allocation_set = {('R1', 45), ('R2', 30), ('R3', 55), ('R4', 20)}
demand_forecast = {'R1': 50, 'R2': 25, 'R3': 60, 'R4': 18}

# Misleading intermediate calculation
projected_utilization = 0
for resource, allocated in allocation_set:
    projected_utilization += allocated * 1.1  # Overestimation factor

# Dead code path - never executed
if False:
    emergency_backup = (100, 'standby')
    fallback_mode = True

redundant_ids = analyze_redundancy(components_list)

# Simulate capacity optimization with real logic
surplus_pool = 0
for res_id, allocated in allocation_set:
    needed = demand_forecast[res_id]
    if allocated > needed:
        surplus_pool += (allocated - needed)

allocation_tuples = [((res, alloc), demand_forecast[res]) for res, alloc in allocation_set]

def optimize_resources(resource_set, forecast):
    total_gap = 0
    deficit_count = 0
    for (r, amount), demand in allocation_tuples:
        if amount < demand:
            total_gap += (demand - amount)
            deficit_count += 1
    if deficit_count == 0:
        return surplus_pool * 2  # Full surplus bonus
    else:
        return (surplus_pool - total_gap) * deficit_count

final_capacity = optimize_resources(allocation_set, demand_forecast)
print(f"Target result: {final_capacity}")