def analyze_redundancy(elements):
    # Irrelevant function: analyzes redundancy but not used in main logic
    unique_set = set(elements)
    duplicates = len(elements) - len(unique_set)
    return duplicates * 2 if duplicates > 0 else -1

def preprocess_constraints(raw):
    # Distractor preprocessing: transforms data but result unused
    adjusted = {k: v + 10 for k, v in raw.items()}
    normalized = {k: v / (sum(adjusted.values()) + 1e-6) for k, v in adjusted.items()}
    return normalized

def evaluate_threshold(value, base=5.0):
    # Dead code path: never called in execution
    return value >= base * 1.5

def generate_combinations(n):
    # Misleading combinatorics function: computes combinations but not used
    if n <= 1:
        return 1
    return generate_combinations(n-1) * n

def decode_segments(signal_tuple):
    # Decodes tuple input; actually used in critical path
    a, b, c = signal_tuple
    decoded = (a ^ b) | c  # Bit manipulation
    scale = (a + b + c) / 3.0
    return decoded, scale

def validate_integrity(check_data):
    # Unused validation routine with side effects
    temp_flags = []
    for x in check_data:
        if x % 3 == 0:
            temp_flags.append(True)
        elif x % 7 == 0:
            temp_flags.clear()
    return len(temp_flags) > 0

def optimize_allocation(pool, rules):
    # Core function with multiple concepts and distractors
    
    # Irrelevant variables
    backup_pool = pool.copy()
    audit_log = []
    max_theoretical = 0
    
    # Real computation begins
    active_resources = [x for x in pool if x > 0]
    sorted_resources = sorted(active_resources, reverse=True)
    
    # Apply rule-based filtering (only even indices matter)
    filtered = []
    for i, val in enumerate(sorted_resources):
        if i % 2 == 0:
            filtered.append(val)
    
    # Set operation to remove duplicates conceptually
    filtered_set = set(filtered)
    adjustment_factor = len(filtered_set.intersection({x for x in range(10, 100, 5)}))
    
    # Tuple unpacking from helper function
    signal = (filtered[0], filtered[-1], adjustment_factor)
    decoded_value, scaling = decode_segments(signal)
    
    # Conditional logic with early return red herring
    if decoded_value < 0:
        return -1  # Never reached due to unsigned operations
    
    # Actual capacity calculation
    base_capacity = sum(filtered) * scaling
    penalty = 0
    for r in filtered:
        if r < 20:
            penalty += r // 4
    
    # Final adjustment using bitwise and arithmetic mix
    final_shift = (base_capacity - penalty) + (decoded_value & 255)
    
    # Unused transformation
    hypothetical = [x * scaling for x in filtered if x in filtered_set]
    
    # Critical assignment
    final_capacity = int(final_shift)
    
    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Main execution
if __name__ == "__main__":
    # Setup data
    resource_pool = [15, 40, 25, 40, 30, 12, 8, 22]
    constraints = {'limit': 100, 'threshold': 15, 'tolerance': 5}
    
    # Call distractor functions to increase interference
    _ = analyze_redundancy(resource_pool)
    _ = preprocess_constraints(constraints)
    _ = validate_integrity(resource_pool)
    _ = generate_combinations(6)
    
    # Key statement
    final_capacity = optimize_allocation(resource_pool, constraints)