def calculate_final_score(data, limit):
    # Preprocessing: filter and transform data
    filtered_data = [x for x in data if x > limit]
    squared_values = [x ** 2 for x in filtered_data]
    
    # Irrelevant computation: character counting in dummy string
    dummy_text = "performance_metrics_analysis_2024"
    char_count = len(dummy_text.replace("_", ""))
    temp_offset = char_count % 7
    
    # Bitwise manipulation on sum of squares
    raw_total = sum(squared_values)
    masked_total = raw_total ^ 0xFF  # XOR mask for obfuscation
    
    # Conditional adjustment based on set properties
    unique_set = set(filtered_data)
    has_duplicates = len(filtered_data) != len(unique_set)
    
    # Dummy string operation with no effect
    status_flag = "valid" if has_duplicates else "clean"
    status_flag = status_flag.upper().strip() + "_END"
    
    # Core logic: apply conditional bonus using ternary-like expression
    bonus = 100 if all(x & 1 for x in unique_set) else 50
    adjusted_score = masked_total + bonus
    
    # Red herring: unused loop over irrelevant range
    debug_logs = []
    for i in range(3):
        debug_logs.append(f"Debug step {i}: no impact")
    
    # Final scoring with offset that doesn't affect result due to fixed logic
    final_score = adjusted_score - temp_offset
    return final_score

# Main execution
raw_input = [12, 15, 13, 12, 17, 14]
threshold = 10
data_set = sorted(raw_input, reverse=True)

# Extraneous list processing with strings
labels = [f"item_{i}" for i in range(len(data_set))]
normalized_labels = [label.upper().replace("_", "-") for label in labels]

# Key call that produces the answer
target_result = calculate_final_score(data_set, threshold)
print(f"Target result: {target_result}")