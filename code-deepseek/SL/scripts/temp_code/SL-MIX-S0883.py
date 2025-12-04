def process_data_entries(raw_inputs, filter_criteria):
    processed = []
    temp_cache = []
    irrelevant_counter = 0
    
    for entry in raw_inputs:
        temp_cache.append(entry * 2)  # Misleading computation
        if len(str(entry)) > filter_criteria:
            processed.append(entry)
            irrelevant_counter += 3  # Distractor
        else:
            temp_cache.pop()  # Dead code path
    
    # Red herring calculation
    dummy_sum = sum(temp_cache) * 0.5
    return processed, irrelevant_counter

def calculate_quality_score(samples, threshold):
    relevant_data, unused_var = process_data_entries(samples, threshold)
    
    # String manipulation - actual core logic
    quality_strings = [str(x).replace('7', '1').replace('9', '4') for x in relevant_data]
    
    # Distractor operations
    misleading_list = [int(s[-1]) if len(s) > 1 else int(s) for s in quality_strings]
    fake_metric = sum(misleading_list) // len(misleading_list) if misleading_list else 0
    
    # Real calculation path
    numeric_values = []
    for s in quality_strings:
        digits = [int(ch) for ch in s if ch.isdigit()]
        if digits:
            numeric_values.append(sum(digits) * len(s))
    
    # Final computation with bitwise operation
    if numeric_values:
        base_value = sum(numeric_values) % 256
        final_metric = (base_value ^ 0b10101010) // 3
    else:
        final_metric = fake_metric  # Fallback path (not taken)
    
    return final_metric

# Main execution
threshold_value = 2
data_samples = [42, 789, 156, 23, 971, 8, 345]

# Misleading intermediate variables
preliminary_check = [x for x in data_samples if x > 100]
shadow_calc = len(preliminary_check) * 25

result = calculate_quality_score(data_samples, threshold_value)
print(f"Result: {result}")