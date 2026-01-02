def calculate_final_score(raw_data, limits):
    # Preprocessing: Normalize data using conditional expressions
    normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data)) if max(raw_data) != min(raw_data) else 0 for x in raw_data]

    # Irrelevant transformation: ASCII sum of lowercase letters in description (distractor)
    description = "performance metrics q4"
    ascii_sum = sum(ord(c) for c in description if c.islower())
    magic_offset = ascii_sum % 10

    # Apply threshold filtering using set operations
    valid_set = {i for i, val in enumerate(normalized) if val >= limits.get('upper', 0.7)}
    warning_set = {i for i, val in enumerate(normalized) if limits.get('lower', 0.3) <= val < limits.get('upper', 0.7)}
    outlier_indices = {i for i in range(len(normalized)) if i not in valid_set and i not in warning_set}

    # Secondary scoring with lambda-based weight function
    dynamic_weight = lambda idx: 1.5 if idx in valid_set else (0.5 if idx in warning_set else 0.1)
    weighted_scores = [normalized[i] * dynamic_weight(i) for i in range(len(normalized))]

    # Compute aggregate metrics (some are red herrings)
    avg_weighted = sum(weighted_scores) / len(weighted_scores) if weighted_scores else 0
    peak_index = max(range(len(normalized)), key=lambda i: normalized[i])
    stability_factor = abs(sum(normalized[i] - normalized[i-1] for i in range(1, len(normalized))))

    # Simulate environmental interference (unused variable)
    env_noise = [0.01 * i for i in range(len(raw_data))]  
    adjusted_stability = stability_factor - magic_offset * 0.01

    # Final composition: only avg_weighted and peak_index contribute
    base_score = avg_weighted * 100
    bonus = 10 if peak_index == 0 else 5 if peak_index < len(raw_data) // 2 else 0
    penalty = 5 if len(outlier_indices) > 1 else 0

    final_score = base_score + bonus - penalty

    return final_score

# Main execution context
raw_input = [85, 92, 78, 90, 88]
threshold_config = {'lower': 0.25, 'upper': 0.85}

intermediate_total = sum(x ** 0.5 for x in raw_input)  # Distractor computation
placeholder_list = [0] * len(raw_input)  # Unused data structure

final_score = calculate_final_score(raw_input, threshold_config)
print(f"Result: {final_score}")