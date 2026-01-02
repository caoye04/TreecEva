def analyze_workload(demand_sequence, efficiency_curve):
    peak_load = max(demand_sequence)
    avg_load = sum(demand_sequence) / len(demand_sequence)
    stress_factor = (peak_load - avg_load) / avg_load
    
    # Irrelevant computation: system age effect (not used in final result)
    system_age_years = 7
    depreciation_rate = 0.85
    legacy_impact = system_age_years * (1 - depreciation_rate)
    
    adjusted_efficiency = []
    for i, eff in enumerate(efficiency_curve):
        if stress_factor > 0.5 and i % 2 == 0:
            adjusted_efficiency.append(eff * 0.92)
        else:
            adjusted_efficiency.append(eff * 1.03)
    
    return adjusted_efficiency, stress_factor


def calculate_system_capacity(resources, threshold):
    active_nodes = 0
    redundancy_pool = 0
    
    # Real capacity logic
    resource_matrix = [resources[i:i+3] for i in range(0, len(resources), 3)]
    
    for idx, row in enumerate(resource_matrix):
        if len(row) >= 2:
            base_power = row[0] * 1.5 + row[1] * 0.8
            if base_power > threshold * 25:
                active_nodes += 1
            else:
                redundancy_pool += base_power / 10
    
    # Distractor: unused health check simulation
    node_health = [True if x % 2 == 0 else False for x in range(len(resource_matrix))]
    failed_nodes = node_health.count(False)
    recovery_attempts = failed_nodes * 2
    
    # Critical capacity formula
    raw_capacity = active_nodes * 150 + int(redundancy_pool)
    scaling_factor = 1.1 if active_nodes > 2 else 0.95
    final_capacity = int(raw_capacity * scaling_factor)
    
    # Additional red herring: logging unrelated stats
    total_iterations = len(resource_matrix) * 3
    debug_checksum = sum([idx * val for idx, val in enumerate(resources)]) % 17
    
    return final_capacity

# Main execution
workload_demands = [120, 145, 130, 160, 110]
efficiency_profile = [0.88, 0.91, 0.76, 0.83, 0.94]

# Call analysis (result partially ignored)
_, stress_metric = analyze_workload(workload_demands, efficiency_profile)

resource_allocation = [40, 18, 22, 35, 28, 15, 50, 20]
activation_threshold = 3

# Key statement
final_capacity = calculate_system_capacity(resource_allocation, activation_threshold)

print(f"Result: {final_capacity}")