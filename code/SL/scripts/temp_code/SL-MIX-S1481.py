from collections import defaultdict

def calculate_truck_loading():
    # Package weights in order of arrival
    package_weights = [23, 45, 12, 67, 34, 89, 56, 78, 91, 23, 45, 67]
    truck_capacity = 150
    
    # Track loaded weights per truck using modular indexing
    truck_loads = defaultdict(int)
    current_truck = 0
    
    # Greedy loading algorithm
    for i, weight in enumerate(package_weights):
        # Calculate which truck to use with modular arithmetic
        truck_index = i % 4
        
        # If adding this package would exceed capacity, move to next truck
        if truck_loads[truck_index] + weight > truck_capacity:
            # Find next available truck using greedy approach
            next_truck = (truck_index + 1) % 4
            while truck_loads[next_truck] + weight > truck_capacity:
                next_truck = (next_truck + 1) % 4
                if next_truck == truck_index:  # All trucks full
                    break
            truck_index = next_truck
        
        # Load package onto selected truck
        truck_loads[truck_index] += weight
    
    # Calculate total weight on third truck (index 2)
    third_truck_total = truck_loads[2]
    return third_truck_total

# Execute the loading calculation
final_loaded_weight = calculate_truck_loading()
print(f"Result: {final_loaded_weight}")