def evaluate_performance(records, limits):
    # Preprocess: extract recent entries and apply filtering
    recent = records[-5:]  # Last 5 entries are relevant
    filtered = [x for x in recent if x > limits[0]]

    # Irrelevant transformation (distractor)
    squared_values = [x ** 2 for x in records if x < 0]  # No negative values, so this is dead logic
    temp_offset = sum(squared_values) // len(squared_values) if squared_values else 0

    # Bitwise normalization step (semi-relevant but masked)
    normalized = []
    for val in filtered:
        shifted = val >> 2  # Divide by 4 using bit shift
        adjusted = shifted ^ 3  # XOR with 3 for obfuscation
        normalized.append(adjusted)

    # Sorting for ranking (only the max matters)
    sorted_norm = sorted(normalized)

    # Secondary distractor: complex unused calculation
    cumulative = 0
    for i in range(len(normalized)):
        cumulative += normalized[i] * (i + 1)
    average_cumulative = cumulative / len(normalized) if normalized else 0

    # Key decision logic
    base_score = sorted_norm[-1] if sorted_norm else 0  # Max of normalized
    penalty = 0
    if len(filtered) < 3:
        penalty = 5
    elif len(filtered) == 4:
        penalty = 2

    # Final score computation
    final_score = base_score * 10 - penalty

    # Extra red herring: unrelated bitwise flag
    debug_flag = (base_score & 1) | (penalty << 1)

    return final_score

# Main execution context
raw_data = [12, 18, 24, 7, 9, 31, 42, 11]
config_thresholds = [8, 20, 30]

interim_result = sum(x for x in raw_data if x % 3 == 0)  # Distractor: divisible by 3
processed_slice = raw_data[2:6]  # Another slice not directly used

# Critical call
final_score = evaluate_performance(raw_data, config_thresholds)

print(f"Target result: {final_score}")