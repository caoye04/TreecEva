def process_segments(sequence, threshold):
    segment_a = sequence[:threshold]
    segment_b = sequence[threshold:]
    
    # Irrelevant transformation (distractor)
    temp_sum = sum(x ** 2 for x in segment_a if x % 2 == 0)
    temp_filtered = [x for x in segment_b if x > len(segment_a)]

    # Semi-relevant computation: count pairs with modular condition
    pair_count = 0
    for i in range(len(segment_a)):
        for j in range(i + 1, len(segment_a)):
            if (segment_a[i] + segment_a[j]) % 5 == 0:
                pair_count += 1

    # Core logic: product of indices where value exceeds index, mod length
    relevant_indices = []
    for idx, val in enumerate(segment_a):
        if val > idx:
            relevant_indices.append(idx)
    
    # Secondary distraction: unused helper list
    dummy_stats = []
    for x in segment_b:
        if x % 3 == 0:
            dummy_stats.append(x * 1.5)

    # Actual answer derivation: sum of relevant indices, then multiplied by pair_count
    base_value = sum(relevant_indices)
    final_mod = (base_value * pair_count) % 987

    # Dead code path (never executed but looks meaningful)
    if len(dummy_stats) > 100:
        final_mod -= len(temp_filtered)

    return final_mod

# Main execution
raw_data = [4, 6, 2, 8, 3, 1, 9, 5]
pivot = 5
dummy_flag = False

# Misleading pre-processing (no effect on result)
processed_copy = [x + 2 for x in raw_data]
sorted_version = sorted(processed_copy, reverse=True)

result = process_segments(raw_data, pivot)
print(f"Target result: {result}")