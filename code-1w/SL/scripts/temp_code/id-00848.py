def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
    return count


def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for freq in freq_map.values():
        p = freq / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def calculate_final_score(data_set, thresholds):
    # Step 1: Filter valid entries based on threshold rules
    valid_entries = [x for x in data_set if x > thresholds['min_val']]
    
    # Step 2: Apply transformation using bitwise and arithmetic ops
    transformed = []
    temp_sum = 0
    for val in valid_entries:
        shifted = (val << 1) ^ 5  # Left shift and XOR
        adjusted = shifted % 100 + (val & 7)  # Mod and bitwise AND
        transformed.append(adjusted)
        temp_sum += adjusted

    # Step 3: Analyze pattern repetition in transformed data
    repeat_count = analyze_pattern(transformed)
    
    # Step 4: Compute statistical dispersion (mock entropy)
    dispersion = compute_entropy(transformed)
    
    # Step 5: Use string slicing to extract control flag from metadata
    meta_flag_str = "threshold_adjustment_enabled"
    flag_substring = meta_flag_str[10:20]  # 'tment_enab'
    use_correction = 'ent' in flag_substring  # True
    
    # Step 6: Conditional correction based on flag and repetition
    if repeat_count > 2 and use_correction:
        temp_sum -= int(dispersion * 10)
    else:
        temp_sum += int(repeat_count / 2)
    
    # Irrelevant helper computations (distractors)
    unused_stats = {
        'max_raw': max(data_set),
        'sorted_half': sorted(data_set)[len(data_set)//2:],
        'unique_count': len(set(data_set))
    }
    
    shadow_value = 0
    for k in range(3):
        shadow_value = (shadow_value * 2) ^ k  # Dead computation
    
    # Final score calculation
    base_score = sum(transformed) // len(transformed) if transformed else 0
    penalty = len([x for x in transformed if x < 10])
    final_score = base_score * 3 - penalty + temp_sum % 7
    
    return final_score

# Main execution
raw_data = [12, 15, 15, 8, 23, 12, 9, 34, 45, 15]
config = {'min_val': 10}
processed_set = [x + 2 for x in raw_data if x % 3 != 0]  # Further filtering and adjustment

intermediate_result = [x * 2 for x in processed_set]  # Unused but plausible

# Key execution point
final_score = calculate_final_score(processed_set, config)

print(f"Result: {final_score}")