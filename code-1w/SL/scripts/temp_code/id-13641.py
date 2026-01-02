def calculate_final_score(entries, importance_weights):
    total = 0
    base_offset = len(entries) % 7
    temp_cache = []

    for i, entry in enumerate(entries):
        if i % 2 == 0:
            adjusted_value = entry * 1.5
        else:
            adjusted_value = entry * 0.8

        # Irrelevant caching (distractor)
        temp_cache.append(adjusted_value * 0.1)

        scaling_factor = importance_weights[i % len(importance_weights)]
        contribution = adjusted_value * scaling_factor

        # Extra computation that doesn't affect final result
        outlier_check = contribution > 100
        if outlier_check:
            base_offset -= 1  # Red herring

        total += contribution

    # Additional logic with list comprehension and zip
    paired_data = list(zip(entries, importance_weights * (len(entries) // len(importance_weights) + 1)))
    correction_term = sum([val * weight for val, weight in paired_data if val > 50]) * 0.05

    # Final adjustment
    final_normalized = total - correction_term + base_offset
    return int(final_normalized)

# Main execution
raw_values = [45, 67, 23, 89, 54, 72]
weights = [0.9, 1.2, 0.8]

# Dead code path (distractor)
def unused_helper(arr):
    return [x ** 2 for x in arr if x % 2 == 0]

intermediate_sum = sum([x // 3 for x in raw_values])  # Semi-relevant but not used directly
flag = False
for v in raw_values:
    if v < 0:
        flag = True

final_score = calculate_final_score(raw_values, weights)
print(f"Target result: {final_score}")