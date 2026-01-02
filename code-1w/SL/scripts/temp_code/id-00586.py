def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0:
            count += 1
            temp_sum += sequence[i]
    avg_even = temp_sum / count if count > 0 else 0
    return avg_even


def validate_string_format(s):
    if not isinstance(s, str):
        return False
    stripped = s.strip().lower()
    if not stripped.startswith('data'):
        return False
    return stripped.isalnum()


def calculate_final_score(data_set, threshold):
    # Irrelevant helper computation (distractor)
    auxiliary_values = [x ** 2 + 3 * x + 1 for x in data_set if x > 5]
    filtered_data = [x for x in data_set if x >= threshold]
    
    # Set operations to remove duplicates (relevant)
    unique_filtered = list(set(filtered_data))
    
    # Secondary filtering based on bitwise condition (semi-relevant)
    processed = []
    for val in unique_filtered:
        if val & 1:  # keep only odd numbers
            processed.append(val)
    
    # String-based tagging (mostly irrelevant but uses string method)
    tags = []
    for num in processed:
        tag_str = f"score_{num}".upper()
        if '5' in tag_str:
            tags.append(tag_str.replace('5', 'X'))
    
    # Core logic: sum of processed values with modular adjustment
    raw_total = sum(processed)
    mod_adjustment = raw_total % 7
    adjusted_total = raw_total - mod_adjustment
    
    # Additional state tracking (distractor)
    state_log = []
    for v in auxiliary_values:
        state_log.append(f"Processed: {v}")
    
    # Final score calculation (key result)
    final_score = adjusted_total + len(tags)
    
    return final_score

# Main execution
if __name__ == "__main__":
    raw_input = [12, 15, 15, 8, 9, 10, 11, 11, 7, 6]
    config_threshold = 8
    metadata_tag = "DataRun2024"
    
    # Validate tag (irrelevant to final score)
    is_valid = validate_string_format(metadata_tag)
    
    # Extract pattern statistic (distractor)
    pattern_stat = analyze_pattern(raw_input)
    
    # Key computation
    final_score = calculate_final_score(raw_input, config_threshold)
    
    print(f"Result: {final_score}")