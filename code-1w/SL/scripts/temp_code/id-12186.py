def analyze_balance(data_sequence):
    total_passes = 0
    temp_buffer = [0] * len(data_sequence)
    cumulative_shift = 0

    # Initialize derived arrays
    reversed_data = data_sequence[::-1]  # slicing operation
    shifted_peaks = []

    for i in range(len(data_sequence)):
        if data_sequence[i] % 3 == 0 and data_sequence[i] > 5:
            shifted_peaks.append(data_sequence[i] * 2)

    # Misleading transformation pass (dead computation)
    for x in temp_buffer:
        cumulative_shift += x * 0.5  # No effect on result

    left_sum = 0
    right_sum = 0
    even_elements = []

    midpoint = len(data_sequence) // 2

    # Left half accumulation
    for j in range(midpoint):
        left_sum += data_sequence[j]
        if data_sequence[j] % 2 == 0:
            even_elements.append(data_sequence[j])

    # Right half accumulation with slice offset
    for k in range(midpoint, len(reversed_data)):
        right_sum += reversed_data[k - midpoint]
        if reversed_data[k - midpoint] % 2 == 0:
            even_elements.append(reversed_data[k - midpoint])

    # Key statement: equilibrium score calculation
    equilibrium_score = abs(left_sum - right_sum) // 2 + len(even_elements)

    # Irrelevant post-processing (distractor)
    normalization_factor = max(data_sequence) / (min(data_sequence) + 1)
    adjusted_score = equilibrium_score * normalization_factor  # Not used

    return equilibrium_score

# Input data
input_seq = [4, 7, 6, 9, 10, 3, 8, 5]
result = analyze_balance(input_seq)
print(f"Target result: {result}")