import functools

def calculate_priority_score(weight, distance):
    return weight * distance

def load_packages_greedy(truck_capacity, package_list):
    # Sort packages by priority score descending (greedy)
    scored_packages = [(pkg[0], pkg[1], calculate_priority_score(pkg[0], pkg[1])) for pkg in package_list]
    scored_packages.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize data structures
    loaded_stack = []
    pending_queue = scored_packages[:]
    current_load = 0
    
    # Process using greedy + backtracking approach
    def backtrack_load(remaining_capacity, index):
        if index >= len(pending_queue):
            return 0
        
        weight, _, _ = pending_queue[index]
        
        # Try loading current package (if fits)
        if weight <= remaining_capacity:
            loaded_stack.append(weight)
            taken = 1 + backtrack_load(remaining_capacity - weight, index + 1)
            loaded_stack.pop()
        else:
            taken = 0
            
        # Skip current package
        skipped = backtrack_load(remaining_capacity, index + 1)
        
        return max(taken, skipped)
    
    # Execute greedy loading first
    for pkg in scored_packages:
        if current_load + pkg[0] <= truck_capacity:
            current_load += pkg[0]
            loaded_stack.append(pkg[0])
    
    # Refine with backtracking
    final_load_count = backtrack_load(truck_capacity, 0)
    return final_load_count

# Define truck specs and packages
max_capacity = 50
packages = [
    (10, 5),   # (weight, delivery_distance)
    (20, 3),
    (15, 4),
    (12, 6),
    (8, 2),
    (25, 1),
    (5, 8)
]

# Compute optimized loading
final_load_count = load_packages_greedy(max_capacity, packages)
print(f"Result: {final_load_count}")