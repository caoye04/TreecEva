from itertools import compress

# System resource allocation simulation
def calculate_resource_allocation():
    node_limits = [15, 20, 25, 30]
    active_nodes = [True, False, True, True]
    
    # Filter active nodes using compress
    active_capacities = list(compress(node_limits, active_nodes))
    
    # Simulate matrix of resource blocks (each row is a tier)
    resource_matrix = [
        [5, 10, 15],
        [7, 14, 21],
        [9, 18, 27]
    ]
    
    # Add dummy operation: count how many tiers have sum > 30
    high_tier_count = 0
    tier_sums = []
    for tier in resource_matrix:
        s = sum(tier)
        tier_sums.append(s)
        if s > 30:
            high_tier_count += 1
    
    # Key computation: transpose and get last column sum
    total_capacity = sum(capacity for capacity in zip(*resource_matrix))[-1]
    
    # Dummy variable (irrelevant)
    avg_capacity = sum(active_capacities) / len(active_capacities) if active_capacities else 0
    
    return total_capacity

result = calculate_resource_allocation()
print(f"Result: {result}")