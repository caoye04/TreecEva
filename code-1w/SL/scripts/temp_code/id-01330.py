def analyze_pattern(sequence, threshold=3):
    char_count = {}
    position_map = {char: idx for idx, char in enumerate(sequence)}
    temp_sum = 0

    for char in sequence:
        char_count[char] = char_count.get(char, 0) + 1
        temp_sum += ord(char) % 7

    # Irrelevant transformation (dead-end computation)
    transformed_vals = [v * 2 + 1 for v in char_count.values()]
    ignored_result = sum(x for x in transformed_vals if x > threshold * 2)

    unique_chars = set(char_count.keys())
    repeated_chars = [ch for ch, cnt in char_count.items() if cnt > 1]

    # Semi-relevant filtering based on positional criteria
    valid_positions = [pos for ch, pos in position_map.items() if pos % 2 == 1 and ch in repeated_chars]

    adjustment_factor = len(valid_positions) - len(repeated_chars) + 1

    # Core logic disguised among distractions
    base_score = sum(ord(ch) for ch in unique_chars)
    penalty = len(sequence) - len(unique_chars)

    intermediate = base_score // (penalty + 1) if penalty else base_score

    # Use of zip and enumerate together (required Python feature)
    indexed_sequence = list(enumerate(zip(sequence, sequence[1:])))
    transition_bonus = 0
    for i, (curr, next_char) in indexed_sequence:
        if curr < next_char and i % 3 == 0:
            transition_bonus += 1

    final_score = (intermediate + transition_bonus) * adjustment_factor

    # Red herring: complex tuple unpacking that doesn't affect result
    stats_summary = {
        'length': len(sequence),
        'repeats': len(repeated_chars),
        'entropy_proxy': intermediate
    }
    
    metadata_bundle = (stats_summary, transformed_vals, ignored_result)
    extra_analysis = {**{f'raw_{k}': v*0.5 for k,v in stats_summary.items()}, 'flag': False}

    return final_score


def compute_aggregate(data_stream, mask):
    filtered_stream = [c for c, m in zip(data_stream, mask) if m]
    secondary_filter = [c for c in filtered_stream if c.isalpha()]
    
    # Distractor: unused frequency map
    freq_debug = {}
    for item in secondary_filter:
        freq_debug[item] = freq_debug.get(item, 0) + 1
    
    # Actual processing
    reversed_stream = ''.join(reversed(secondary_filter))
    return analyze_pattern(reversed_stream, threshold=2)

# Main execution
input_seq = "abracadabra"
mask_pattern = [True, False, True, True, False, True, True, False, True, True, False]

result = compute_aggregate(input_seq, mask_pattern)
print(f"Target result: {result}")