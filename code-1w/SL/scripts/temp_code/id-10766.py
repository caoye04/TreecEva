from itertools import groupby

def calculate_remaining_capacity(storage, allocations):
    total_storage = sum(storage.values())
    reserved = 0
    
    # Process allocation requests by grouping consecutive blocks
    sorted_allocs = sorted(allocations)
    for size, group in groupby(sorted_allocs):
        count = len(list(group))
        reserved += size * (count // 2 + count % 2)  # Every block reserves ceiling(count/2) slots
    
    temp_var_junk = [x * 2 for x in range(3)]  # Irrelevant list comprehension (distractor)
    unused_dict = {'a': 1, 'b': 2}  # Unused variable (minimal interference)
    
    final_capacity = total_storage - reserved
    return final_capacity

# System configuration
capacity_map = {'sector_a': 250, 'sector_b': 180, 'sector_c': 120}
request_list = [40, 40, 30, 30, 30, 20]

result = calculate_remaining_capacity(capacity_map, request_list)
print(f"Target result: {result}")