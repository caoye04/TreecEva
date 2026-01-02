def calculate_final_score(data, limit):
    # Preprocessing: filter and transform data
    processed = [x for x in data if x > 0]
    squared_values = [x**2 for x in processed]
    
    # Irrelevant distraction: string processing with no impact on result
    status_log = "Processing complete. Entries: " + str(len(processed))
    log_upper = status_log.upper()
    log_chars = set(log_upper)  # Set operation (required)
    char_count = len(log_chars)

    # Actual logic begins: determine valid entries above threshold
    filtered = [x for x in squared_values if x > limit]
    if not filtered:
        return 0
    
    # Compute statistics (some used, some not)
    avg_val = sum(filtered) / len(filtered)
    max_val = max(filtered)
    min_val = min(filtered)  # Not used but computed
    range_val = max_val - min_val  # Distractor computation

    # Apply weighting based on size and average
    size_factor = len(filtered) if len(filtered) < 10 else 10
    weighted_score = avg_val * size_factor

    # Secondary distraction: unused recursive helper
    def useless_recursion(n):
        if n <= 1:
            return 1
        return n + useless_recursion(n-2)  # Dead code path
    
    temp_result = useless_recursion(7)  # Computed but not used

    # Final adjustment using string method (required)
    key_suffix = "_score".replace("_", "*")  # String method usage
    adjustment = len(key_suffix)  # equals 6

    final_value = int(weighted_score + adjustment)  # Deterministic integer result
    return final_value

# Main execution
raw_data = [1, -3, 4, 2, -5, 6, 0, 3]
threshold = 8
data_set = [x * 2 for x in raw_data]  # Transform input

# Extraneous variable tracking
execution_phase = "stage_1"
phase_complete = True
update_available = False

final_score = calculate_final_score(data_set, threshold)
print(f"Result: {final_score}")