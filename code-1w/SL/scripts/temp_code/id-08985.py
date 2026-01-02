def preprocess_input(data):
    # Irrelevant preprocessing with decoy transformations
    temp_a = (data ** 2 + 3) % 19
    temp_b = sum((data + i) % 5 for i in range(6))
    return temp_a if temp_b > 10 else data * 2

# Unused but plausible-looking helper function
def obsolete_filter(x):
    return x & (x - 1) == 0  # Checks if power of two (not used in logic)

# Distractor set: irrelevant category codes
invalid_codes = {1, 4, 7, 13, 16, 19, 22}
category_flags = {'A': 3, 'B': 7, 'C': 11}

# Real logic begins: recursive root finder
memo = {}
def find_root(n):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    
    # Complex branching with red herring calculations
    if n % 3 == 0:
        branch_offset = (n // 3) ** 2
        result = find_root(n - 2) + (branch_offset % 7)
    elif n % 5 == 0:
        fake_reduction = n // 5
        noise_term = sum(i * fake_reduction for i in range(3)) % 4
        result = find_root(n - 1) + noise_term
    else:
        # Core path: Fibonacci-like recurrence
        result = find_root(n - 1) + find_root(n - 2) - (n % 2)
    
    memo[n] = result
    return result

# Decoy accumulation loop with no effect
junk_accumulator = 0
for k in range(1, 5):
    junk_accumulator += (k * k) ^ 7

# Set-based validation with partial relevance
allowed_roots = {find_root(i) for i in range(1, 6)}  # Only values 1-5 matter

aux_data = [1, 1, 2, 3, 5, 8]
overlap_set = allowed_roots.intersection(aux_data)

# Main analysis with conditional bypass
threshold_map = {0: 5, 1: 8, 2: 13}
def analyze_path(root_value):
    base_score = root_value * 3
    
    # Distractor: unused scoring branches
    if base_score < 0:
        return base_score * -2
    elif base_score in invalid_codes:
        return -1
    
    # Real transformation
    adjusted = base_score + len(overlap_set)
    
    # Conditional early exit that looks important but isn't triggered
    if adjusted > 100:
        sentinel = sum(threshold_map.values())
        return sentinel % adjusted
    
    # Key operation
    final_shift = adjusted ^ 7  # Bitwise red herring
    post_shift = final_shift + (final_shift % 4)
    
    # Final filtering using set membership
    if root_value in allowed_roots:
        post_shift += 5
    
    return post_shift

# Irrelevant global counter
execution_count = 0
for _ in range(3):
    execution_count += 1

# Critical execution point
temp_input = preprocess_input(7)
root_result = find_root(7)
final_diagnostic = analyze_path(find_root(7))
print(f"Result: {final_diagnostic}")