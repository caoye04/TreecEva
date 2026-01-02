def optimize_allocation(resources, demands):
    # Simulate resource allocation under fluctuating demand
    peak_utilization = 0
    temp_buffer = 0
    adjustment_factor = 0.85
    decay_rate = 0.92
    
    # Irrelevant pre-processing: normalize resource names (distractor)
    normalized_names = [r.lower().strip() for r in resources.keys()]
    name_hash = sum([hash(n) % 100 for n in normalized_names])

    # Real logic begins: track rolling capacity adjustments
    capacity_history = []
    surplus_tracker = []
    
    for day, demand in enumerate(demands):
        daily_cap = sum([resources[r] for r in resources])
        
        # Apply artificial decay every 3 days (semi-relevant)
        if (day + 1) % 3 == 0:
            daily_cap = int(daily_cap * decay_rate)

        # Compute utilization and update peak
        utilization = demand / daily_cap if daily_cap > 0 else 0
        peak_utilization = max(peak_utilization, utilization)
        
        # Surplus calculation with red herring condition
        surplus = daily_cap - demand
        if surplus > 0:
            adjusted_surplus = surplus * adjustment_factor
            surplus_tracker.append(adjusted_surplus)
            temp_buffer += adjusted_surplus // 2
        else:
            temp_buffer = max(0, temp_buffer - 10)  # Distractor state

        # Record history for later analysis (not used directly)
        capacity_history.append({'day': day, 'cap': daily_cap, 'util': utilization})

        # Hidden key: reset buffer if high surplus streak
        if len([s for s in surplus_tracker[-3:] if s > 20]) >= 2:
            temp_buffer = int(temp_buffer * 1.5)

    # Secondary computation: efficiency score (distractor)
    efficiency_score = lambda x, y: round(x * 100 / (y + 1), 2)
    score = efficiency_score(len([c for c in capacity_history if c['util'] > 0.7]), len(demands))

    # Critical decision point: reallocate based on peak
    base_realloc = int(sum(resources.values()) * (1 + peak_utilization))
    final_capacity = base_realloc - temp_buffer  # Actual answer depends on this

    # Dead code path: never executed due to fixed condition (distractor)
    emergency_override = False
    if sum(demands) > 10000:
        final_capacity *= 0.9
        emergency_override = True

    return final_capacity

# Input setup
resource_pool = {
    'CPU': 40,
    'GPU': 24,
    'RAM_MB': 128,
    'STORAGE_GB': 50
}

demand_schedule = [68, 73, 85, 92, 78, 105, 95, 88, 80]

# Execute
final_capacity = optimize_allocation(resource_pool, demand_schedule)
print(f"Target result: {final_capacity}")