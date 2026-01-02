def process_sequence(data):
    # Preprocessing: extract and transform relevant tokens
    raw_tokens = [x * 2 for x in data if x % 3 == 0]
    filtered = list(filter(lambda x: x > 10, raw_tokens))
    
    # Distractor: irrelevant transformation chain
    temp_shadow = [x ** 0.5 for x in data if x < 5]
    shadow_sum = sum(temp_shadow) * 0.1  # Not used later
    
    # Token categorization using slicing and conditions
    mid_point = len(filtered) // 2
    left_half = filtered[:mid_point]
    right_half = filtered[mid_point:]
    
    # Distractor: dead computation on right half
    magnitude = 0
    for val in right_half:
        magnitude += val << 2  # Bit-shift but unused

    # Actual signal: balance between halves
    left_weight = sum(left_half) if left_half else 0
    right_weight = sum(x for x in right_half if x % 2 == 1)  # Only odd values count

    adjustment_factor = len(data) - len(filtered)
    adjusted_left = left_weight + adjustment_factor * 1.5

    # Simulate recursive reduction for equilibrium
    def reduce_to_single(seq):
        if len(seq) <= 1:
            return seq[0] if seq else 0
        return reduce_to_single([seq[i] - seq[i+1] for i in range(0, len(seq)-1, 2)])
    
    synthetic_left = reduce_to_single(left_half) if left_half else 0
    synthetic_right = reduce_to_single([x for x in right_half if x > 15])

    # Core logic: equilibrium depends on conditional expression and lambda mapping
    spread = abs(synthetic_left - synthetic_right)
    modifier = (lambda x: x * 1.2 if x < 20 else x * 0.8)(spread)
    
    # Final score computed via multi-step reasoning
    base_score = adjusted_left + synthetic_right
    equilibrium_score = base_score - modifier

    # Irrelevant string distraction
    status_log = "Processing complete".split(' ')
    log_entry = " -> ".join(status_log)  # Unused

    # Output the required result
    return equilibrium_score

# Main execution
input_data = [3, 6, 9, 12, 15, 18, 21, 24]
tokens = input_data.copy()
equilibrium_score = process_sequence(tokens)
print(f"Target result: {equilibrium_score}")