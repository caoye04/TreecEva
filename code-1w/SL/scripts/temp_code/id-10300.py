def analyze_data_stream(raw_input):
    # Irrelevant transformation: case manipulation and splitting
    processed_chars = [c.upper() for c in raw_input if c.isalpha()]
    token_segments = ''.join(processed_chars).split('X')
    decoy_value = len(token_segments) * 7

    # Misleading numeric aggregation
    ascii_total = sum([ord(c) for c in processed_chars])
    fake_checksum = (ascii_total % 97) + 3

    # Real data path begins: extract and filter digits
    digit_candidates = [int(c) for c in raw_input if c.isdigit()]
    shifted_digits = [d ** 2 for d in digit_candidates]  # Transform digits

    # Distractor: unused list comprehension with bit operations
    ignored_results = [(d << 2) ^ 5 for d in digit_candidates if d % 2 == 0]

    # Slicing operation to skip first and last potential outliers
    trimmed_slice = shifted_digits[1:-1] if len(shifted_digits) > 2 else shifted_digits

    # Conditional logic with early return red herring
    if len(trimmed_slice) == 0:
        return 0  # Dead end - won't trigger with this input

    # Core filtering logic: only values divisible by 3 after adjustment
    adjusted_values = [v + 2 for v in trimmed_slice]
    relevant_values = [v for v in adjusted_values if v % 3 == 0]

    # Critical assignment point
    filtered_sum = sum(relevant_values)

    # Decoy accumulation using string joining
    dummy_concat = ''.join([str(v) for v in ignored_results][:3])
    phantom_ratio = (len(dummy_concat) / (filtered_sum or 1)) * 100

    # Output target result
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Simulate realistic input stream
input_stream = "a3b9cXm4n7o2p8qR5s1t"
result = analyze_data_stream(input_stream)