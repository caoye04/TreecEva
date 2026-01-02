def analyze_traffic(patterns):
    peak_load = sum([p['volume'] * p['weight'] for p in patterns if p['time'] in ['morning', 'evening']])
    off_peak = sum([p['volume'] for p in patterns if p['time'] == 'night'])
    normalized_load = peak_load / (off_peak + 1)
    return int(normalized_load)


def calculate_efficiency(nodes, redundancy_factor=1.5):
    active_nodes = len([n for n in nodes if n.status == 'ACTIVE'])
    total_capacity = sum([n.capacity for n in nodes])
    efficiency_score = (active_nodes / len(nodes)) * total_capacity
    adjusted = efficiency_score * redundancy_factor
    return round(adjusted, 2)


class NetworkNode:
    def __init__(self, capacity, status):
        self.capacity = capacity
        self.status = status


def optimize_allocation():
    # Simulate network node configuration
    nodes = [
        NetworkNode(100, 'ACTIVE'),
        NetworkNode(200, 'INACTIVE'),
        NetworkNode(150, 'ACTIVE'),
        NetworkNode(80, 'MAINTENANCE'),
        NetworkNode(120, 'ACTIVE')
    ]

    # Traffic pattern data
    traffic_patterns = [
        {'time': 'morning', 'volume': 450, 'weight': 1.8},
        {'time': 'afternoon', 'volume': 300, 'weight': 1.2},
        {'time': 'evening', 'volume': 500, 'weight': 2.0},
        {'time': 'night', 'volume': 100, 'weight': 0.5}
    ]

    # Irrelevant computation: dummy set operations (distractor)
    regions = {'north', 'south', 'east', 'west'}
    active_regions = {'north', 'east'}
    backup_regions = regions - active_regions
    region_count = len(regions | {'central'})  # unused

    # Misleading intermediate calculation
    baseline_threshold = 375
    fluctuation_index = sum([abs(p['weight'] - 1) for p in traffic_patterns])
    stability_flag = fluctuation_index < 2.5

    # Key computations
    load_metric = analyze_traffic(traffic_patterns)
    efficiency = calculate_efficiency(nodes)

    # Conditional expression usage (required Python feature)
    scaling_factor = 1.25 if stability_flag else 0.85

    # Core logic determining final answer
    raw_allocation = load_metric * efficiency
    adjusted_allocation = raw_allocation * scaling_factor

    # Final transformation with conditional logic
    final_bandwidth = int(adjusted_allocation) if adjusted_allocation > 0 else 0

    # Dead code path (distractor)
    if False:
        fallback = sum([n.capacity for n in nodes if n.status == 'INACTIVE'])
        final_bandwidth += fallback  # never reached

    return final_bandwidth

# Execute and print result
target_result = optimize_allocation()
print(f"Result: {target_result}")