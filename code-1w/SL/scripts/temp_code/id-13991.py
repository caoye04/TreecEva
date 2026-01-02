def calculate_efficiency(resources, demands):
    # Initialize tracking variables
    utilization_log = []
    peak_capacity = max(resources) * 1.5  # Distractor: not directly used in final calculation
    baseline_threshold = sum(demands) / len(demands)

    # Filter relevant resources above threshold (semi-relevant computation)
    filtered_resources = [r for r in resources if r > baseline_threshold * 0.8]

    total_utilized = 0
    temp_buffer = 0  # Irrelevant accumulator (dead variable)

    for i, demand in enumerate(demands):
        if i >= len(filtered_resources):  
            break
        allocation = min(filtered_resources[i], demand * 1.2)
        total_utilized += allocation

        # Logging step (distractor, no effect on output)
        temp_buffer += allocation * 0.1  
        utilization_log.append(temp_buffer)

    # Complex but irrelevant transformation
    adjustment_factor = 1.0
    if len(utilization_log) > 3:
        adjustment_factor = (utilization_log[-1] + 1) / (utilization_log[0] + 1)

    # Actual efficiency formula
    raw_efficiency = total_utilized / sum(demands)
    efficiency_with_adjustment = raw_efficiency * adjustment_factor  # adjustment_factor is always ~1 due to structure

    # Final normalization (constant factor)
    normalized_score = int(efficiency_with_adjustment * 100) / 100.0

    return normalized_score

# Main execution context
resource_pool = [45, 67, 23, 89, 56, 77]
demand_forecast = [50, 60, 30, 95]

# Setup overhead with misleading computations
cumulative_stress_test = sum([x**2 for x in demand_forecast]) / 1000  # Unused metric
projection_matrix = {i: resource_pool[i] * 1.1 for i in range(len(resource_pool))}  # Unused dict

# Key state variable being queried
efficiency_score = calculate_efficiency(resource_pool, demand_forecast)

# Print result as required
print(f"Result: {efficiency_score}")