def optimize_storage(capacity, items):
    # Calculate base efficiency
    base_efficiency = len(items) * 2 if capacity > 10 else len(items)
    
    # Distractor computation - not used in final result
    temp_calc = (capacity * 3) // 2
    
    # Conditional expression for efficiency adjustment
    adjusted_efficiency = base_efficiency + 5 if capacity % 2 == 0 else base_efficiency - 3
    
    # Recursive helper function
    def calculate_utilization(current_cap, item_set):
        if current_cap <= 0 or not item_set:
            return current_cap
        # Simple recursion with set operations
        remaining_items = item_set - {min(item_set)}
        return calculate_utilization(current_cap - 1, remaining_items)
    
    # Main optimization logic
    final_utilization = calculate_utilization(capacity, items)
    
    # Final result computation with conditional
    result = final_utilization + adjusted_efficiency if final_utilization > 0 else adjusted_efficiency
    
    # Unused intermediate variable
    unused_var = temp_calc + len(items)
    
    return result

# Initialize storage parameters
initial_capacity = 15
items_set = {3, 7, 12, 5, 8}

# Pre-computation that doesn't affect final result
preliminary_analysis = sum(items_set) * 2

# Execute main optimization
final_capacity = optimize_storage(initial_capacity, items_set)

# Distractor print statement
print(f"Analysis complete: {preliminary_analysis}")

# Final target result
print(f"Target result: {final_capacity}")