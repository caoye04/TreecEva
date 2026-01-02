def calculate_distribution(efficiency, resources):
    total_capacity = 0
    adjustment_factor = 0.85
    temp_buffer = []
    
    for key in resources:
        if key in efficiency:
            # Relevant calculation: accumulate weighted capacity
            weighted = resources[key] * efficiency[key]
            total_capacity += weighted
            temp_buffer.append(weighted)

    # Irrelevant sorting and buffer processing (distractor)
    temp_buffer.sort(reverse=True)
    smoothed_values = [val * adjustment_factor for val in temp_buffer]
    average_smoothed = sum(smoothed_values) / len(smoothed_values) if smoothed_values else 0

    # Another irrelevant computation (misleading)
    outlier_threshold = average_smoothed * 1.5
    filtered_count = len([v for v in temp_buffer if v < outlier_threshold])

    # Key normalization step (semi-relevant but overridden later)
    if total_capacity > 100:
        total_capacity = total_capacity * 0.95

    # Simulate load redistribution based on efficiency peaks
    peak_efficiency = max(efficiency.values())
    efficiency_ratio = peak_efficiency / sum(efficiency.values())

    # Final computation - only this matters
    final_load = int(total_capacity * efficiency_ratio)
    
    return final_load

# Setup data
resource_pool = {
    'node_a': 40,
    'node_b': 30,
    'node_c': 50,
    'node_d': 20
}

efficiency_map = {
    'node_a': 0.9,
    'node_b': 0.7,
    'node_c': 1.2,
    'node_d': 0.6
}

# Execution point of interest
final_load = calculate_distribution(efficiency_map, resource_pool)

print(f"Result: {final_load}")