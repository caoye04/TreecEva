from collections import defaultdict

def calculate_network_load():
    # Simulate packet counts per node in a network segment
    traffic_data = [
        ('router_A', 120), ('switch_B', 85), ('router_A', 200),
        ('firewall_X', 60), ('switch_B', 95), ('firewall_X', 140),
        ('router_A', 80)
    ]

    # Aggregate traffic using defaultdict for cleaner accumulation
    packet_count = defaultdict(int)
    for node, count in traffic_data:
        packet_count[node] += count

    # Calculate total load and apply efficiency factor
    base_load = sum(packet_count.values())
    efficiency_factor = 0.85
    adjusted_load = base_load * efficiency_factor

    # Secondary metric: number of high-traffic nodes (for distraction)
    high_traffic_nodes = [node for node, count in packet_count.items() if count > 150]
    node_count = len(high_traffic_nodes)

    # Final load includes adjustment and small overhead per high-traffic node
    overhead_per_node = 10
    total_load = adjusted_load + (node_count * overhead_per_node)

    return total_load

# Execute computation
total_load = calculate_network_load()
print(f"Result: {total_load}")