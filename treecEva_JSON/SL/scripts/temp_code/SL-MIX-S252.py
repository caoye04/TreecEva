from collections import defaultdict
import itertools

def calculate_max_packages(weights, capacity):
    memo = {}
    n = len(weights)
    
    def backtrack(index, current_weight, package_count, bitmask):
        if current_weight > capacity:
            return -1
        
        if index == n:
            return package_count
        
        if (index, current_weight) in memo:
            return memo[(index, current_weight)]
        
        # Skip current package (short-circuit if weight exceeds capacity)
        skip = backtrack(index + 1, current_weight, package_count, bitmask)
        
        # Take current package (only if it doesn't exceed capacity)
        take = -1 if current_weight + weights[index] > capacity else backtrack(index + 1, current_weight + weights[index], package_count + 1, bitmask | (1 << index))
        
        result = max(skip, take)
        memo[(index, current_weight)] = result
        return result
    
    return backtrack(0, 0, 0, 0)

# Package weights in kilograms
package_weights = [3, 1, 4, 2, 2, 5, 1]
truck_capacity = 10  # Maximum load capacity in kilograms

# Calculate optimized loading sequence
optimized_load_count = calculate_max_packages(package_weights, truck_capacity)

# Adjust for special logistics rules
heavy_items = sum(1 for w in package_weights if w > 3)
fragile_items = sum(1 for w in package_weights if w < 2)

optimized_load_count = optimized_load_count + (1 if heavy_items > fragile_items else 0) - (1 if heavy_items < fragile_items else 0)

# Apply company policy modifier
policy_modifier = 1 if (optimized_load_count & 1) == 0 else -1
optimized_load_count += policy_modifier if optimized_load_count > 0 else 0

print(f"Result: {optimized_load_count}")