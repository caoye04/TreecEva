def calculate_statistics(values):
    # Irrelevant statistical calculations
    temp_sum = sum(values)
    temp_avg = temp_sum / len(values)
    temp_squared = [x**2 for x in values]
    irrelevant_stat = sum(temp_squared) - temp_avg * 2
    
    # Misleading intermediate operations
    fake_median = (max(values) + min(values)) / 2
    bogus_variance = sum([(x - fake_median)**3 for x in values])
    
    # Actual relevant operation
    unique_count = len(set(values))
    return unique_count

def filter_patterns(data_stream):
    # Dead code path with misleading operations
    if len(data_stream) > 100:
        unused_filter = [x for x in data_stream if x % 7 == 0]
        fake_result = sum(unused_filter) * 2
    
    # Red herring computations
    pattern_sum = sum(data_stream)
    pattern_avg = pattern_sum / len(data_stream)
    
    # Key operation using lambda
    threshold_check = lambda x: x > pattern_avg
    filtered_data = list(filter(threshold_check, data_stream))
    
    # More irrelevant calculations
    unnecessary_set = {x % 10 for x in data_stream}
    misleading_count = len(unnecessary_set) * 3
    
    return filtered_data

def process_data_filter(input_data):
    # Set operations with relevant logic
    primary_set = set(input_data)
    secondary_set = {x * 2 for x in input_data}
    
    # Misleading intersection that doesn't affect result
    fake_intersection = primary_set & secondary_set
    irrelevant_union = primary_set | secondary_set
    
    # Key statistical analysis
    stats_result = calculate_statistics(input_data)
    
    # Filter operation with actual relevance
    filtered_stream = filter_patterns(input_data)
    
    # Core computation
    if len(filtered_stream) > 0:
        final_value = (stats_result * len(filtered_stream)) // 2
    else:
        final_value = stats_result * 3
    
    # Final adjustments with logical operations
    if final_value > 50 and len(primary_set) < 10:
        final_value += 7
    elif final_value <= 50 or len(secondary_set) > 15:
        final_value -= 3
    
    return final_value

# Main execution with distractor data
sample_data = [8, 12, 8, 15, 20, 12, 25, 8, 30, 15]
distractor_data = [5, 10, 15, 20, 25, 30, 35, 40]

# Irrelevant preprocessing
combined_data = sample_data + [x % 8 for x in distractor_data]
unused_analysis = sum(combined_data) - min(combined_data)

# Key execution point
final_analysis_result = process_data_filter(combined_data)

print(f"Target result: {final_analysis_result}")