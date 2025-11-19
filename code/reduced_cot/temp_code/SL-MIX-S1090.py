def optimize_truck_loading():
    # Package data: (priority, size)
    packages = [(9, 25), (8, 30), (7, 15), (6, 20), (5, 35), (4, 10), (3, 40), (2, 5), (1, 50)]
    truck_capacity = 100
    trucks_used = 0
    final_utilization = 0
    
    while packages:
        trucks_used += 1
        current_load = 0
        loaded_packages = []
        remaining_packages = []
        
        # Greedy loading by priority
        for priority, size in sorted(packages, reverse=True):
            if current_load + size <= truck_capacity:
                current_load += size
                loaded_packages.append((priority, size))
            else:
                remaining_packages.append((priority, size))
        
        # If greedy approach left space, use DP for optimization
        if current_load < truck_capacity and remaining_packages:
            dp = [0] * (truck_capacity - current_load + 1)
            dp_items = [[] for _ in range(truck_capacity - current_load + 1)]
            
            for priority, size in remaining_packages:
                if size > truck_capacity - current_load:
                    continue
                for j in range(truck_capacity - current_load, size - 1, -1):
                    if dp[j] < dp[j - size] + priority:
                        dp[j] = dp[j - size] + priority
                        dp_items[j] = dp_items[j - size] + [(priority, size)]
            
            # Add DP optimized items
            for _, size in dp_items[truck_capacity - current_load]:
                current_load += size
        
        final_utilization += current_load
        
        # Remove loaded packages from the main list
        loaded_set = set(loaded_packages)
        dp_loaded = set(dp_items[truck_capacity - current_load] if current_load < truck_capacity and remaining_packages else [])
        packages = [p for p in packages if p not in loaded_set and p not in dp_loaded]
    
    return final_utilization

final_utilization = optimize_truck_loading()
print(f"Result: {final_utilization}")