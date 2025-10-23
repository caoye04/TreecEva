from functools import reduce

def calculate_compatibility(package_ids):
    return reduce(lambda x, y: x ^ y, [pid * 3 + 7 for pid in package_ids], 0)

def find_optimal_combination(packages, capacity, current_load=0, index=0, selected=[]):
    if current_load > capacity:
        return -1, []
    if index == len(packages):
        score = calculate_compatibility(selected)
        return score, selected[:]
    
    # Exclude current package
    exclude_score, exclude_combo = find_optimal_combination(packages, capacity, current_load, index+1, selected)
    
    # Include current package
    selected.append(packages[index][0])
    include_score, include_combo = find_optimal_combination(packages, capacity, current_load + packages[index][1], index+1, selected)
    selected.pop()
    
    if include_score > exclude_score:
        return include_score, include_combo
    else:
        return exclude_score, exclude_combo

# Package data: (package_id, weight)
delivery_packages = [(101, 12), (102, 7), (103, 5), (104, 9), (105, 14), (106, 3)]
truck_capacity = 25

optimal_score, best_combo = find_optimal_combination(delivery_packages, truck_capacity)
print(f"Result: {optimal_score}")