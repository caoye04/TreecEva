from itertools import combinations

def analyze_pattern(sequence):
    length = len(sequence)
    total_pairs = 0
    xor_accum = 0
    temp_sum = 0  # distractor

    for i, val in enumerate(sequence):
        for j in range(i + 1, length):
            if sequence[j] > val:
                total_pairs += 1
            xor_accum ^= (val & sequence[j])

    # Distractor block: irrelevant combinatorics
    redundant_calc = 0
    if length > 3:
        for combo in combinations(sequence, 3):
            redundant_calc += combo[0] - combo[2]

    return total_pairs, xor_accum

def compute_aggregate(data_string, threshold=4):
    chars = list(data_string)
    ascii_vals = [ord(c) for c in chars]
    upper_count = sum(1 for c in chars if c.isupper())
    lower_count = sum(1 for c in chars if c.islower())
    
    # Slicing and transformation
    mid_section = ascii_vals[1:-1]
    shifted = [v >> 1 for v in mid_section]
    
    # Real computation starts
    base_score = 0
    adjustment = 0
    for i, v in enumerate(shifted):
        if i % 2 == 0:
            base_score += v * 2
        else:
            base_score -= v

    # Secondary logic path with partial relevance
    paired_data = list(zip(ascii_vals, ascii_vals[1:]))
    edge_sum = sum(abs(a - b) for a, b in paired_data)

    # Dummy tracking state
    state_tracker = {'init': True, 'count': 0}
    for _ in range(upper_count):
        state_tracker['count'] += 1
        if state_tracker['count'] > threshold:
            break

    # Actual key step
    trend_value = edge_sum // (len(paired_data) or 1)
    adjustment = (trend_value ^ lower_count) & 0xFF

    # Call helper function with partial result
    aux_pairs, aux_xor = analyze_pattern(ascii_vals)

    final_score = base_score + adjustment + (aux_pairs % 100)
    
    # Red herring: unused complex expression
    if len(chars) % 2 == 0:
        phantom = sum(v ** 0.5 for v in ascii_vals if v % 3 == 0)
        phantom_floor = int(phantom)

    return final_score

# Main execution
input_str = "CodeEval"
result = compute_aggregate(input_str)
print(f"Target result: {result}")