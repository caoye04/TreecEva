def analyze_sequence(raw_input):
    # Irrelevant transformation: case conversion with no impact
    inverted_case = ''.join(c.lower() if c.isupper() else c.upper() for c in raw_input)

    # Decoy list - looks important but unused in final result
    decoy_values = [len(inverted_case) * 2, len(inverted_case) + 100, -999]
    decoy_sum = sum(decoy_values) // 3

    # Core data extraction - hidden among distractions
    numeric_stream = [ord(c) - ord('0') for c in raw_input if c.isdigit()]

    # Bit manipulation red herring
    shifted_flags = []
    for x in numeric_stream:
        flag = (x << 3) ^ 0b1010
        shifted_flags.append(flag)

    # Actual relevant processing begins here
    transformed = [x ** 2 for x in numeric_stream if x % 2 == 1]  # Only odd digits squared

    # Slicing operation (required feature) - reverse and take first half
    mid = len(transformed) // 2
    processed_data = transformed[::-1][:mid]  # Reverse and slice

    # Dead code path: looks like filtering but unused
    temp_filtered = [y for y in transformed if y > 10]
    temp_filtered.append(42)  # Misleading append

    # Key assignment
    filtered_sum = sum(processed_data)

    # Distractor: unrelated floating-point calculation
    avg_entropy = (sum(shifted_flags) / len(shifted_flags)) if shifted_flags else 0.0
    derived_metric = round(avg_entropy * 0.017, 4)

    # Output only the target result
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Simulate input
input_str = "A7B2C5D9E1F"
analyze_sequence(input_str)