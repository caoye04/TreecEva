from collections import defaultdict

# Simulate warehouse inventory optimization with demand forecasting
inventory_levels = [120, 150, 90, 200, 80]
demand_projection = [130, 140, 100, 190, 85]

# Irrelevant historical data (distractor)
historical_sales = [110, 145, 95, 195, 78]
avg_growth_rate = 0.03
projected_revenue = sum(historical_sales) * (1 + avg_growth_rate)

# Misleading capacity metric (not used in final calculation)
theoretical_max_capacity = max(inventory_levels) * len(inventory_levels)

# Helper function to compute optimal redistribution efficiency
def assess_stability(inv, dem):
    differences = [abs(i - d) for i, d in zip(inv, dem)]
    return sum(differences) / len(differences)

# Another helper that seems relevant but is unused in critical path
def calculate_waste_estimate(inventory, demand):
    waste = 0
    for i, d in zip(inventory, demand):
        if i > d:
            waste += (i - d) * 0.1  # 10% spoilage rate
    return waste

# Core logic: optimize distribution based on supply-demand gap
def optimize_distribution(inv, dem):
    # Create balanced allocation plan
    allocation_plan = [(i + d) // 2 for i, d in zip(inv, dem)]
    
    # Track deficit areas using defaultdict (semi-relevant)
    deficit_map = defaultdict(int)
    for idx, (i, d) in enumerate(zip(inv, dem)):
        if d > i:
            deficit_map[idx] = d - i
    
    # Compute adjustment factor based on average surplus/deficit
    net_buffer = sum(inv) - sum(dem)
    adjustment_factor = abs(net_buffer) // len(inv) if inv else 0
    
    # Apply adjustment only if overall surplus
    effective_capacity = sum(allocation_plan)
    if net_buffer > 0:
        effective_capacity += adjustment_factor * 2
    
    # Additional logic: penalize instability
    stability_score = assess_stability(inv, dem)
    if stability_score > 10:
        effective_capacity -= 5
    
    # Dead code branch - never executed due to data values
    emergency_reserve = 0
    if any(d > 200 for d in dem):
        emergency_reserve = 25
    
    # Final computation
    final_capacity = effective_capacity + emergency_reserve
    return final_capacity

# Execute main calculation
final_capacity = optimize_distribution(inventory_levels, demand_projection)

# Print result as required
print(f"Result: {final_capacity}")