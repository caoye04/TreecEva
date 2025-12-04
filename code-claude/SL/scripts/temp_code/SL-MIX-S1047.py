import itertools

def is_valid_configuration(configuration):
    # Check if the configuration satisfies the network constraints
    server_a, server_b, server_c = configuration
    
    # Servers cannot be identical (must have different loads)
    if server_a == server_b or server_b == server_c or server_a == server_c:
        return False
    
    # Server A must have higher load than Server C
    if server_a <= server_c:
        return False
        
    # Total load must be less than 15
    total_load = server_a + server_b + server_c
    max_allowed = 15
    if total_load >= max_allowed:
        return False
    
    return True

# Available server load configurations
load_options = [2, 3, 4, 5, 6, 7]

# Generate all possible combinations of 3 servers
all_combinations = list(itertools.combinations_with_replacement(load_options, 3))

# Temporary calculation that doesn't affect final result
temp_metric = sum(sum(combo) for combo in all_combinations)
debug_ratio = temp_metric / len(all_combinations)

# Calculate average load across all possible combinations
avg_load = sum(sum(c) for c in all_combinations) / len(all_combinations)

# Filter combinations that meet the initial capacity requirement
min_capacity = 8
filter_combinations = [combo for combo in all_combinations if sum(combo) > min_capacity]

# Tracking variables for debugging (not used in final calculation)
rejected_same_load = 0
rejected_a_vs_c = 0
rejected_overload = 0

# Count valid configurations where server loads are all different
for combo in filter_combinations:
    if combo[0] == combo[1] or combo[1] == combo[2] or combo[0] == combo[2]:
        rejected_same_load += 1
    elif combo[0] <= combo[2]:  # Server A not greater than Server C
        rejected_a_vs_c += 1
    elif sum(combo) >= 15:  # Total load exceeds maximum
        rejected_overload += 1

# Calculate valid configurations that meet all constraints
valid_combinations = len([combo for combo in filter_combinations if is_valid_configuration(combo)])

# Alternative calculation that gives wrong answer (distraction)
incorrect_valid = len(filter_combinations) - (rejected_same_load + rejected_a_vs_c + rejected_overload)

# Calculate efficiency ratio (not used in final answer)
efficiency = valid_combinations / len(all_combinations) if len(all_combinations) > 0 else 0

print(f"Result: {valid_combinations}")