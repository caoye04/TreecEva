from itertools import combinations

def analyze_sensor_coverage(sensors, threshold=3):
    # Simulate sensor overlap analysis with red herrings
    active_zones = set()
    temp_margins = []
    for i, sensor in enumerate(sensors):
        margin = (sensor['range'] ** 2) % 7  # Irrelevant computation
        temp_margins.append(margin)
        if sensor['status'] == 'active':
            active_zones.add(sensor['zone'])
    
    # Distractor: complex but unused zone clustering
    zone_clusters = []
    for r in range(2, len(active_zones) + 1):
        for combo in combinations(active_zones, r):
            cluster_weight = sum([len(str(z)) for z in combo])
            zone_clusters.append(cluster_weight)

    # Actual relevant logic: count high-sensitivity active sensors
    sensitive_count = 0
    for sensor in sensors:
        if sensor['status'] == 'active' and sensor['sensitivity'] > threshold:
            sensitive_count += 1
    return sensitive_count


def calculate_network_flow(capacities, flow_constraints=True):
    base_flow = 0
    adjustments = []
    
    # Real logic: modular accumulation with filtering
    for cap in capacities:
        adjusted_cap = (cap * 11) % 19
        if adjusted_cap > 5:
            base_flow += adjusted_cap
        else:
            base_flow -= adjusted_cap
        
        # Distractor: dead path with no effect
        if adjusted_cap == 13:
            adjustments.append(cap // 3)

    # Another distractor: list comprehension that isn't used
    _ = [x**2 for x in adjustments if x < 10]

    # Final adjustment based on evenness
    if base_flow % 2 == 0:
        base_flow = (base_flow * 3) // 4
    else:
        base_flow = (base_flow * 5) // 6
        
    return base_flow

# Main execution
sensor_array = [
    {'zone': 'A7', 'range': 12, 'status': 'active', 'sensitivity': 4},
    {'zone': 'B3', 'range': 8, 'status': 'inactive', 'sensitivity': 6},
    {'zone': 'C5', 'range': 15, 'status': 'active', 'sensitivity': 3},
    {'zone': 'D2', 'range': 5, 'status': 'active', 'sensitivity': 5},
    {'zone': 'E9', 'range': 20, 'status': 'active', 'sensitivity': 2}
]

# Extract capacities from ranges using list comprehension (some distraction)
capacities_list = [s['range'] for s in sensor_array]

# Intermediate irrelevant transformation
efficiency_flags = {c: (c % 4 == 0) for c in capacities_list}

coverage_score = analyze_sensor_coverage(sensor_array, threshold=4)

# Key statement where answer is determined
final_capacity = calculate_network_flow(capacities_list, flow_constraints=True)

print(f"Target result: {final_capacity}")