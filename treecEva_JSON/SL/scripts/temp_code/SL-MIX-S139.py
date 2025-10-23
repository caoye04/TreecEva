from functools import reduce

def calculate_package_checksum(loaded_packages):
    # Dynamic programming approach to calculate checksum
    checksum_history = [0] * len(loaded_packages)
    total_checksum = 0
    
    for i in range(1, len(loaded_packages)):
        # Sum weights of all previous packages that are lighter
        lighter_sum = sum(weight for weight in loaded_packages[:i] if weight < loaded_packages[i])
        checksum_history[i] = lighter_sum
        total_checksum += lighter_sum
    
    return total_checksum

# Package weights in kg
package_weights = [320, 150, 480, 210, 90, 370, 180, 420]

# Sort packages by weight in descending order (greedy approach)
package_weights.sort(reverse=True)

# Truck loading simulation
truck_capacity = 1000
loaded_packages = []
remaining_packages = package_weights.copy()

while remaining_packages and sum(loaded_packages) + remaining_packages[0] <= truck_capacity:
    next_package = remaining_packages.pop(0)
    loaded_packages.append(next_package)

# Calculate logistics checksum using dynamic programming
logistics_checksum = calculate_package_checksum(loaded_packages)

print(f"Result: {logistics_checksum}")