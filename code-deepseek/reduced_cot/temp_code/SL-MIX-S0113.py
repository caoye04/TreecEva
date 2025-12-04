def compute_storage_capacity(base_units):
    # Initialize storage metrics
    total_units = base_units * 2
    allocated_units = base_units // 3
    
    # Slicing operations on data segments
    data_segments = [10, 25, 40, 55, 70, 85]
    primary_segment = data_segments[1:4]
    secondary_segment = data_segments[2:5]
    
    # Calculate capacity metrics
    base_capacity = sum(primary_segment) - 15
    overflow_buffer = len(secondary_segment) * 8
    
    # Distractor calculations (not used in final result)
    temp_utilization = base_capacity * 0.75
    projected_growth = temp_utilization + overflow_buffer
    
    # Core logic with conditional branches
    if base_capacity > 80:
        current_capacity = base_capacity - 20
        scaling_factor = 1.5
    else:
        current_capacity = base_capacity + 10
        scaling_factor = 1.25
    
    # Final calculation
    final_capacity = current_capacity * scaling_factor
    
    # Print result
    print(f"Result: {final_capacity}")
    return final_capacity

# Execute the function
compute_storage_capacity(15)