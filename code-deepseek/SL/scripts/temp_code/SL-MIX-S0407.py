def analyze_data_patterns(input_set):
    # Distractor: complex set operations that aren't used in final result
    primary_set = {x % 7 for x in input_set if x > 10}
    secondary_set = {x * 2 for x in input_set if x % 3 == 0}
    union_set = primary_set | secondary_set
    intersection_set = primary_set & secondary_set
    
    # Relevant computation path
    filtered_data = [x for x in input_set if 5 <= x <= 25]
    unique_count = len(set(filtered_data))
    
    # More distractions
    temp_calc = sum(x ** 2 for x in input_set if x % 2 == 0)
    unused_metric = len(intersection_set) * 3
    
    # Dead code path
    if len(union_set) > 10:
        dead_result = min(union_set) * max(union_set)
    else:
        dead_result = sum(union_set) // len(union_set)
    
    # Misleading intermediate variable
    intermediate_value = unique_count + len(primary_set)
    
    # Key logic with set operations
    processed_set = {x + 2 for x in filtered_data if x % 4 != 0}
    actual_count = len(processed_set) - 1 if processed_set else 0
    
    # Final computations
    result_metrics = {
        'unique_count': unique_count,
        'actual_count': actual_count,
        'temp_value': intermediate_value
    }
    
    # Distractor calculation
    bonus_value = (len(filtered_data) - actual_count) if len(filtered_data) > actual_count else 0
    
    # Critical execution point
    final_result = result_metrics.get('actual_count', 0) + bonus_value
    
    print(f"Result: {final_result}")

# Main execution
sample_data = [3, 8, 15, 22, 8, 17, 9, 24, 15, 11, 6, 19, 22, 5, 12]
analyze_data_patterns(sample_data)