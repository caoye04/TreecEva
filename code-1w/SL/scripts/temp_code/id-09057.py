def analyze_data_stream(raw_input):
    # Simulate preprocessing steps with distractions
    temp_buffer = [x * 2 for x in raw_input if x % 3 == 0]
    checksum = sum(temp_buffer) % 1000

    # Irrelevant transformation chain (dead path)
    transformed = ''.join([chr((x + checksum) % 256) for x in temp_buffer])
    decoy_value = len(transformed.replace('a', '').replace('e', ''))

    # Real processing begins: filter and shift logic
    shifted_view = [x >> 1 for x in raw_input if x > 0]  # Bit manipulation
    masked_data = [x for x in shifted_view if bin(x).count('1') % 2 == 1]  # Keep odd parity only

    # Conditional filtering using slicing and string methods as red herrings
    control_flag = 'active' if sum(masked_data) > 100 else 'standby'
    metadata_tag = f"STATUS:{control_flag}".lower().strip('status:')

    # Distractor: unused recursive function
    def calculate_entropy(data, depth=0):
        if depth > 5 or len(data) == 0:
            return 0.0
        mid = len(data) // 2
        return 1 + calculate_entropy(data[:mid], depth + 1)

    entropy_score = calculate_entropy(raw_input)  # Not used later

    # Core logic hidden among noise
    candidate_pool = [x for x in raw_input if x % 2 == 1 and x < 500]  # Odd values under 500
    extended_pool = candidate_pool + [x * -1 for x in candidate_pool[:3]]  # Mirror first three negatives

    # Final filtering based on index position and magnitude
    relevant_values = []
    for idx, val in enumerate(extended_pool):
        if idx % 2 == 0:  # Only even indices
            adjusted = abs(val) + (idx ** 2)
            if str(adjusted).startswith('1') or str(adjusted).endswith('7'):
                relevant_values.append(adjusted)

    filtered_sum = sum(relevant_values)

    # Dead code branches with misleading prints
    if decoy_value > 10:
        debug_log = "Event triggered at level ".upper() + str(checksum)
        _ = debug_log.split()  # Unused

    return filtered_sum

# Main execution
input_sequence = [123, 456, 111, 789, 102, 303, 404, 505]
result = analyze_data_stream(input_sequence)
print(f"Result: {result}")