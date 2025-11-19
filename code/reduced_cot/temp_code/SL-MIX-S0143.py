from collections import defaultdict
import math

def calculate_optimal_loading(weights, capacity):
    # Sort packages by weight in descending order (greedy approach)
    sorted_weights = sorted(weights, reverse=True)
    
    # Initialize tracking variables
    loaded_weight = 0.0
    loaded_packages_count = 0
    
    # Greedily load packages
    for weight in sorted_weights:
        if loaded_weight + weight <= capacity:
            loaded_weight += weight
            loaded_packages_count += 1
        else:
            # Apply a correction factor using floating point operations
            correction = math.log(loaded_weight + 1.5) * 0.1
            loaded_weight = round(loaded_weight - correction, 2)
            break
    
    # Apply string transformation to create a report identifier
    report_id = f"LOAD-{str(loaded_packages_count).zfill(3)}-{str(int(loaded_weight*100)).zfill(5)}"
    
    # Use dictionary comprehension to create a weight distribution map
    weight_distribution = {f"pkg_{i}": w for i, w in enumerate(sorted_weights[:loaded_packages_count])}
    
    # Merge with default values using dictionary merging
    default_weights = defaultdict(lambda: 0.0, {"base": 5.0})
    final_distribution = default_weights | weight_distribution
    
    # Calculate a checksum using bit operations
    checksum = 0
    for w in weight_distribution.values():
        checksum ^= int(w * 100)  # Convert to cents to avoid floating point issues
    
    return loaded_packages_count, loaded_weight, report_id, dict(final_distribution), checksum

# Package weights in kilograms
package_weights = [12.5, 8.3, 15.7, 6.2, 22.1, 9.8, 18.4, 5.6, 14.9, 7.7]
truck_capacity = 65.0  # Maximum load capacity in kilograms

# Execute the loading optimization
loaded_packages_count, total_loaded_weight, report_identifier, distribution_map, validation_checksum = calculate_optimal_loading(package_weights, truck_capacity)

# Print the result
print(f"Result: {loaded_packages_count}")