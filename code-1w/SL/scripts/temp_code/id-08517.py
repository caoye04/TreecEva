def calculate_efficiency(data, limit):
    total_elements = len(data)
    valid_count = 0
    temp_sum = 0
    outlier_count = 0  # distractor: not used in final logic

    for val in data:
        if val > limit * 2:
            outlier_count += 1  # tracked but irrelevant
        elif val >= limit:
            valid_count += 1
            temp_sum += val

    average_valid = temp_sum / valid_count if valid_count > 0 else 0
    
    # Simulated efficiency formula
    scaling_factor = 1.5 if average_valid > limit else 1.0
    efficiency = (valid_count / total_elements) * average_valid * scaling_factor
    
    # Additional noise variables
    debug_info = {'processed': total_elements, 'kept': valid_count, 'discarded_est': outlier_count}
    intermediate_diag = [x for x in data if x % 2 == 0]  # distractor list

    return efficiency

# Main execution
raw_input = [12, 15, 3, 22, 8, 45, 13, 7, 30, 25]
filter_threshold = 10

# Preprocessing: remove duplicates conceptually, but list has none
filtered_data = [x for x in raw_input if x >= 5]
processed_data = sorted(filtered_data, reverse=True)

# Secondary distraction: simulate metadata analysis
count_stats = {
    'high': sum(1 for x in processed_data if x > 20),
    'medium': sum(1 for x in processed_data if 10 <= x <= 20),
    'low': sum(1 for x in processed_data if x < 10)
}

peak_value = max(processed_data)  # distractor
threshold_ratio = peak_value / filter_threshold if filter_threshold else 0  # unused path

# Key computation
efficiency_score = calculate_efficiency(processed_data, filter_threshold)

# Print result as required
print(f"Result: {efficiency_score}")