import itertools

def min_containers_greedy(capacities, target):
    # Sort capacities in descending order for greedy selection
    sorted_caps = sorted(capacities, reverse=True)
    count = 0
    current_sum = 0
    
    for cap in sorted_caps:
        if current_sum + cap <= target:
            current_sum += cap
            count += 1
            if current_sum == target:
                break
    
    return count if current_sum == target else -1  # Return -1 if not possible

# Ingredient quantities needed
containers_available = [10, 7, 3, 2, 1]
target_quantity = 15

# Greedily select minimum containers
minimum_containers_needed = min_containers_greedy(containers_available, target_quantity)
print(f"Result: {minimum_containers_needed}")