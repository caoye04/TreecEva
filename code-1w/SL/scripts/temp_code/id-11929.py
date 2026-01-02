from itertools import combinations

# Simulate hourly network load across data centers with failover logic
def compute_network_capacity():
    base_loads = [120, 150, 130, 160, 145, 138, 170]
    redundancy_factor = 1.25
    maintenance_mode = False
    peak_capacity = 0
    
    # Auxiliary tracking variables (some not directly used)
    cumulative_stress = 0
    stress_history = []
    fallback_engaged = False
    temp_shadow_loads = [x * 0.9 for x in base_loads]  # Distractor: shadow simulation
    
    # Generate all possible two-node failure scenarios
    failure_scenarios = list(combinations(range(len(base_loads)), 2))
    usage_tracker = []
    
    for hour in range(8):  # Simulate 8-hour operational window
        hourly_shift = (hour ** 2) % 7
        shifted_loads = [base_loads[(i + hourly_shift) % len(base_loads)] for i in range(len(base_loads))]
        
        # Apply dynamic scaling based on time-of-day
        scaled_loads = [load * (1.1 + 0.1 * (hour % 3)) for load in shifted_loads]
        
        # Simulate failover redistribution if any two nodes are down
        for f1, f2 in failure_scenarios[:5]:  # Only test first 5 scenarios (not all)
            active_loads = scaled_loads.copy()
            failed_load = active_loads[f1] + active_loads[f2]
            active_loads[f1] = active_loads[f2] = 0
            # Redistribute half of failed load across remaining nodes
            per_node_addition = (failed_load * 0.5) / (len(active_loads) - 2)
            active_loads = [load + per_node_addition if load > 0 else 0 for load in active_loads]
        
        # Final capacity check with redundancy
        total_capacity = sum(scaled_loads) * redundancy_factor
        capped_capacity = min(total_capacity, 950)  # Hard cap due to safety limits
        usage_tracker.append(capped_capacity)
        
        # Update cumulative stress (distractor metric)
        hour_stress = sum([load ** 0.5 for load in scaled_loads])
        cumulative_stress += hour_stress
        stress_history.append(hour_stress)
        
        # Misleading conditional – appears important but doesn't affect outcome
        if cumulative_stress > 100 and not fallback_engaged:
            fallback_engaged = True
            temp_recovery_boost = 1.05  # Unused except here
            usage_tracker[-1] *= temp_recovery_boost  # Minor adjustment

    # Critical execution point
    peak_capacity = max(usage_tracker)
    
    # Irrelevant summary statistics (dead-end computation)
    avg_usage = sum(usage_tracker) / len(usage_tracker)
    variance = sum((x - avg_usage) ** 2 for x in usage_tracker) / len(usage_tracker)
    normalized_risk = (variance / avg_usage) if avg_usage > 0 else 0
    
    print(f"Result: {peak_capacity}")

compute_network_capacity()