from collections import defaultdict, Counter

# Simulate sensor readings from a water distribution network
def analyze_water_flow():
    sensor_readings = [
        ('A', 'in', 12), ('B', 'out', 8), ('A', 'in', 5), ('C', 'in', 15),
        ('B', 'out', 3), ('D', 'in', 7), ('C', 'out', 9), ('A', 'in', 6),
        ('D', 'out', 4), ('B', 'in', 10), ('C', 'in', 3), ('D', 'out', 5)
    ]

    # Track inflows and outflows per node
    inflows = defaultdict(int)
    outflows = defaultdict(int)

    # Aggregation using list comprehensions and filtering
    valid_inflows = [(node, amount) for node, direction, amount in sensor_readings if direction == 'in']
    valid_outflows = [(node, amount) for node, direction, amount in sensor_readings if direction == 'out']

    # Accumulate values
    for node, amount in valid_inflows:
        inflows[node] += amount

    for node, amount in valid_outflows:
        outflows[node] += amount

    # Misleading intermediate calculations (distractors)
    total_events = len(sensor_readings)
    node_counts = Counter([node for node, _, _ in sensor_readings])
    avg_events_per_node = total_events / len(node_counts)
    flow_variance = sum((inflows[n] - outflows[n])**2 for n in set(inflows) | set(outflows))  # Not used later

    # Secondary analysis on redundancy (irrelevant to final answer)
    redundant_nodes = [n for n in node_counts if node_counts[n] > 3]
    stability_score = len(redundant_nodes) * avg_events_per_node

    # Core logic: compute total inflow and outflow sums
    inflow_sum = sum(inflows.values())
    outflow_sum = sum(outflows.values())

    # Key statement: net system flow
    net_flow = inflow_sum - outflow_sum

    # Additional red herring computation
    theoretical_capacity = max(inflows.values()) * 2 - min(outflows.values())
    efficiency_ratio = inflow_sum / (outflow_sum + 1e-9)

    # Print result as required
    print(f"Result: {net_flow}")

    return net_flow

analyze_water_flow()