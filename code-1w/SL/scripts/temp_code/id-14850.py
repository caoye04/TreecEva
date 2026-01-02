def analyze_data_stream():
    raw_readings = [12, 15, 22, 8, 33, 41, 19, 27]
    calibration_offset = 3
    processed_values = [x + calibration_offset for x in raw_readings]
    
    # Irrelevant statistical distraction
    mean_value = sum(processed_values) / len(processed_values)
    variance_proxy = sum((x - mean_value) ** 2 for x in processed_values)
    normalized_data = [(x - mean_value) / (variance_proxy ** 0.5) for x in processed_values]

    # Real logic begins: detect rising sequences
    rising_pairs = 0
    for i in range(len(processed_values) - 1):
        if processed_values[i] < processed_values[i + 1]:
            rising_pairs += 1

    # Secondary processing with zip and enumerate (core concept)
    indexed_deltas = []
    for idx, (a, b) in enumerate(zip(processed_values, processed_values[1:])):
        delta = b - a
        indexed_deltas.append((idx, delta))

    # Filter significant jumps using lambda (required feature)
    significant_increases = list(filter(lambda pair: pair[1] > 7, indexed_deltas))
    
    # Distractor: unused complex transformation
    transformed_spectrum = [abs(val * (i % 5 + 1)) for i, val in enumerate(normalized_data)]
    spectral_peak = max(transformed_spectrum) if transformed_spectrum else 0

    # Scoring logic
    base_score = len(significant_increases) * 10
    bonus = rising_pairs // 3 * 5
    penalty = 0
    
    for _, delta in indexed_deltas:
        if delta < -6:
            penalty += 3

    temp_result = base_score + bonus - penalty

    # Another red herring: character analysis from numbers
    digit_chars = ''.join([str(x) for x in raw_readings])
    vowel_count_in_digits = len([c for c in digit_chars if c in '02468'])  # Misleading name

    # Final computation chain
    adjustment_factor = 1.5 if len(significant_increases) >= 3 else 0.8
    adjusted_score = temp_result * adjustment_factor

    # Final answer variable
    final_score = int(adjusted_score + 0.5)  # Round to nearest integer

    return final_score

# Key statement
final_score = analyze_data_stream()
print(f"Result: {final_score}")