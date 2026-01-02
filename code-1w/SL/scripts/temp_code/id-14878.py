def analyze_dataset():
    raw_data = [15, 23, 9, 34, 28, 46, 12, 38, 41, 27]
    threshold = 25
    
    # Filter data above threshold
    filtered_data = [x for x in raw_data if x > threshold]
    
    # Irrelevant distraction: sorting (not used in final computation)
    sorted_data = sorted(filtered_data)
    
    # Compute sum of values above threshold
    base_sum = sum(filtered_data)
    
    # Apply adjustment based on set difference with another range
    upper_set = set(range(30, 50))
    data_set = set(filtered_data)
    excess_values = data_set - upper_set  # Values >= 25 but < 30
    adjustment = len(excess_values) * 2
    
    adjusted_sum = base_sum - adjustment
    
    # Key statement
    final_score = adjusted_sum + len(filtered_data)
    
    # Additional slicing distraction (not affecting result)
    sample_slice = raw_data[::2]
    slice_sum = sum(sample_slice)
    
    print(f"Result: {final_score}")

analyze_dataset()