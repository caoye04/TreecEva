def analyze_sequence(seq):
    total_weighted_index = 0
    base_offset = 7
    unused_counter = 0  # Irrelevant variable (minimal interference)

    for index, char in enumerate(seq):
        char_count = seq.count(char)  # Count occurrences of current character
        total_weighted_index += index * char_count
        
        # Some extra logic that doesn't affect the core computation
        if index % 2 == 0:
            unused_counter += 1

    scaling_factor = 1.0  # Unused in final result, slight distraction
    return total_weighted_index

sequence = "abracadabra"
total_weighted_index = analyze_sequence(sequence)
print(f"Result: {total_weighted_index}")