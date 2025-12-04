def calculate_storage_capacity(containers):
    # Calculate base capacities using list comprehension
    base_capacities = [container * 2 for container in containers]
    
    # Distractor: Calculate average (not used in final result)
    avg_capacity = sum(base_capacities) / len(base_capacities)
    
    # Apply capacity adjustment using lambda
    adjuster = lambda x: x * 0.75 if x > 15 else x * 1.25
    adjusted_capacities = [adjuster(cap) for cap in base_capacities]
    
    # Filter capacities above threshold
    threshold = 20
    filtered_capacities = [cap for cap in adjusted_capacities if cap >= threshold]
    
    # Distractor: Calculate maximum (not used in final result)
    max_capacity = max(adjusted_capacities) if adjusted_capacities else 0
    
    # Sort filtered capacities
    sorted_capacities = sorted(filtered_capacities)
    
    # Count filtered items
    filtered_count = len(filtered_capacities)
    
    # Distractor: Calculate median (not used in final result)
    if sorted_capacities:
        mid_index = len(sorted_capacities) // 2
        median_capacity = sorted_capacities[mid_index] if len(sorted_capacities) % 2 != 0 else (sorted_capacities[mid_index - 1] + sorted_capacities[mid_index]) / 2
    else:
        median_capacity = 0
    
    # Critical execution point
    final_capacity = sorted_capacities[filtered_count - 1] if filtered_count > 0 else 0
    
    print(f"Target result: {final_capacity}")

# Initial container sizes
container_sizes = [8, 12, 18, 22, 14, 25]
calculate_storage_capacity(container_sizes)