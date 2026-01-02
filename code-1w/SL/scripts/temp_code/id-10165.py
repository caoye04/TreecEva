def analyze_sequence(data, threshold, mode='strict'):
    # Simulate preprocessing steps with some irrelevant transformations
    normalized = [x / max(data) for x in data]
    squared_devs = [(x - sum(data)/len(data))**2 for x in data]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Distractor: secondary transformation not used later
    inverted = [round(1/(x + 1e-5)) for x in normalized]
    temp_offset = sum(inverted[:3]) if len(inverted) > 3 else 0

    # Core logic begins: extract subsequence based on slicing and filtering
    midpoint = len(data) // 2
    upper_half = data[midpoint:]  # Slice: second half
    lower_half = data[:midpoint]  # Slice: first half (unused)

    # Conditional branching with misleading path
    if mode == 'relaxed':
        candidate_set = upper_half
    else:
        candidate_set = [x for x in upper_half if x > threshold]  # strict mode filter

    # Additional distractor: unused accumulation
    cumulative = []
    running_total = 0
    for val in data:
        running_total += val
        cumulative.append(running_total)

    # Key slicing operation to isolate middle portion of filtered upper half
    if len(candidate_set) >= 3:
        relevant_subsequence = candidate_set[1:-1]  # Exclude first and last
    else:
        relevant_subsequence = candidate_set

    # Final computation dependent on prior steps
    filtered_sum = sum(relevant_subsequence)

    # Print required for deterministic traceability
    print(f"Result: {filtered_sum}")

    return filtered_sum

# Execute with realistic input
input_data = [8, 12, 3, 17, 9, 14, 6, 21]
threshold_value = 10
result = analyze_sequence(input_data, threshold_value)