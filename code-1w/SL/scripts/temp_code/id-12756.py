def validate_pattern(seq, ref):
    # Precompute transformed slices for analysis
    left_segment = seq[:len(seq)//2]
    right_segment = seq[len(seq)//2:]
    reversed_ref = ref[::-1]

    # Misleading transformation - not used in final logic
    shifted_ref = [x + 1 for x in ref][1:] + [ref[0]]
    temp_sum = sum(shifted_ref) * 0.5  # Dead computation

    # Count matches with offset tracking
    match_count = 0
    offset = len(seq) % 4
    for i in range(len(left_segment)):
        if i + offset < len(right_segment) and left_segment[i] == right_segment[i + offset]:
            match_count += 1

    # Auxiliary check with distractor variables
    total_pairs = 0
    for i in range(len(ref) - 1):
        total_pairs += (ref[i] + ref[i+1]) % 3  # Irrelevant accumulation

    # Core logic: compare segment sums modulated by pattern
    left_sum = sum(left_segment) % 7
    right_sum = sum(right_segment) % 7
    
    # Reference-based validation
    ref_sum = sum(reversed_ref[:len(left_segment)]) % 7
    
    base_score = left_sum * 2 - right_sum
    adjustment = (ref_sum - left_sum) if match_count > 2 else 0
    
    result_score = base_score + adjustment

    # Unused state tracking
    status_log = {'valid': result_score > 0, 'peak': max(seq), 'length': len(seq)}

    return result_score

# Main execution
sequence = [3, 1, 4, 1, 5, 9, 2, 6]
reference = [6, 2, 9, 5, 1, 4, 1, 3]

# Extraneous preprocessing
norm_factor = sum(x**2 for x in sequence) ** 0.5
normalized_seq = [round(x / norm_factor, 3) for x in sequence]

result_score = validate_pattern(sequence, reference)
print(f"Target result: {result_score}")