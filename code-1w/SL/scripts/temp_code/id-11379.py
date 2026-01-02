def analyze_resource_distribution():
    # Simulate resource distribution across zones with validation
    zones = ['alpha', 'beta', 'gamma', 'delta']
    resources_initial = [120, 200, 150, 180]
    allocation_factor = [0.85, 0.90, 0.75, 0.88]
    maintenance_cost_per_zone = [12, 15, 10, 14]

    # Intermediate derived data
    adjusted_resources = [init * factor for init, factor in zip(resources_initial, allocation_factor)]
    
    # Distractor: unused efficiency metrics
    efficiency_score = [factor * 100 for factor in allocation_factor]
    avg_efficiency = sum(efficiency_score) / len(efficiency_score)
    efficiency_threshold = 85.0
    high_efficiency_zones = [z for z, e in zip(zones, efficiency_score) if e >= efficiency_threshold]

    # Primary flow computation
    inflows = []
    outflows = []

    for i, zone in enumerate(zones):
        base_inflow = adjusted_resources[i]
        maintenance_out = maintenance_cost_per_zone[i] * 4  # quarterly cost
        tax_rate = 0.05 + (i * 0.01)
        tax_out = base_inflow * tax_rate

        # Real contributions
        inflows.append(base_inflow)
        outflows.append(maintenance_out)
        outflows.append(tax_out)

        # Distractor: logging irrelevant intermediate stats
        projected_growth = base_inflow * 0.03
        growth_cap = 5.0
        capped_growth = min(projected_growth, growth_cap)

    # Critical execution point
    net_flow = sum(inflows) - sum(outflows)

    # Additional red herring computations
    surplus_ratio = net_flow / sum(inflows) if sum(inflows) > 0 else 0
    normalized_surplus = round(surplus_ratio * 100, 2)

    # Final output
    print(f"Result: {net_flow}")

analyze_resource_distribution()