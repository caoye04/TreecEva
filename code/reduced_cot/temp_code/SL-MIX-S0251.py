def validate_input(raw_data):
    # Misleading validation that doesn't affect main logic
    temp_check = sum(x % 2 for x in raw_data) if raw_data else 0
    return len(raw_data) > 3

def calculate_bonus(scores):
    # Dead code path - never actually used
    bonus = sum(scores) * 0.1 if len(scores) > 5 else 0
    return max(scores) * 2  # Misleading calculation

def filter_valid_entries(data, cutoff):
    # Irrelevant intermediate variable
    debug_counter = len([x for x in data if x > 100])
    
    # Main filtering logic with list comprehension
    valid_data = [x for x in data if x >= cutoff and x % 2 == 0]
    
    # Misleading intermediate result
    partial_sum = sum(valid_data) * 2 if len(valid_data) > 2 else 0
    
    return valid_data

def process_results(data_stream, threshold):
    # Multiple irrelevant operations
    dummy_var = [x * 3 for x in data_stream[:2]] if len(data_stream) > 1 else []
    temp_sum = sum(dummy_var) if dummy_var else 0
    
    # Core logic with nested calls
    if validate_input(data_stream):
        filtered_data = filter_valid_entries(data_stream, threshold)
        
        # Conditional expression for score calculation
        score = (sum(filtered_data) * 2) if len(filtered_data) > 1 else (filtered_data[0] * 3 if filtered_data else 0)
        
        # Irrelevant operation that doesn't affect result
        unused_bonus = calculate_bonus(filtered_data)
        
        # Final adjustment
        final_adjustment = score // len(filtered_data) if len(filtered_data) > 0 else score
        return final_adjustment
    else:
        # Unused dead code path
        return sum(data_stream) * 10

# Main execution
input_data = [12, 8, 15, 20, 6, 25, 18, 30]
threshold_value = 10

# Key statement
final_score = process_results(input_data, threshold_value)

print(f"Target result: {final_score}")