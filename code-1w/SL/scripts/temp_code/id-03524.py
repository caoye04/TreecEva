from typing import Dict, Set

# Simulate a supply chain network with warehouses and transfer flows
def analyze_distribution_efficiency(inventory: Dict[str, int], thresholds: Set[int]) -> float:
    excess_count = 0
    total_capacity = sum(inventory.values())
    critical_threshold = max(thresholds)
    
    for level in inventory.values():
        if level > critical_threshold * 1.5:
            excess_count += 1

    efficiency_score = (len(inventory) - excess_count) / len(inventory)
    return round(efficiency_score, 4)

# Helper function to compute net flow across supply chain nodes
def calculate_net_flow(chain: Dict[str, Dict[str, int]]) -> int:
    inflow_counter = {}
    outflow_tracker = {node: 0 for node in chain}
    temp_aggregator = 0
    
    # Accumulate outflows from each node
    for source in chain:
        for target in chain[source]:
            if target not in inflow_counter:
                inflow_counter[target] = 0
            inflow_counter[target] += chain[source][target]
            outflow_tracker[source] += chain[source][target]
            temp_aggregator += 1  # Red herring counter

    # Compute net flow: (total inflow - total outflow) for central hub
    hub_in = inflow_counter.get('distribution_hub', 0)
    hub_out = outflow_tracker.get('distribution_hub', 0)
    net_flow = hub_in - hub_out
    
    # Irrelevant secondary calculation (distractor)
    phantom_delta = 0
    for i in range(3):
        for j in range(3):
            phantom_delta += (i * j - 1) ** 2  # Dead computation

    return net_flow

# Define supply chain topology
supply_chain = {
    'factory_a': {'warehouse_x': 15, 'distribution_hub': 25},
    'factory_b': {'warehouse_y': 20, 'distribution_hub': 30},
    'distribution_hub': {'retail_north': 35, 'retail_south': 20},
    'warehouse_x': {'retail_east': 10},
    'warehouse_y': {'retail_west': 15}
}

# Inventory levels at various sites
inventory_levels = {
    'warehouse_x': 120,
    'warehouse_y': 95,
    'distribution_hub': 80,
    'retail_north': 45,
    'retail_south': 30,
    'retail_east': 60,
    'retail_west': 50
}

# Thresholds for overstock detection
overstock_levels = {75, 100, 125}

# Analyze efficiency (irrelevant to final answer but adds interference)
efficiency = analyze_distribution_efficiency(inventory_levels, overstock_levels)

# Key computational step determining the answer
net_flow = calculate_net_flow(supply_chain)

# Additional distracting computations
lambda_offset = lambda x: x ** 2 - x
offset_correction = lambda_offset(7)  # 42, unused value

# Print final result
print(f"Result: {net_flow}")