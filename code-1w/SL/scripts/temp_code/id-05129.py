def analyze_sequence(data, threshold, mode):
    # Count elements above threshold
    count_above = sum(1 for x in data if x > threshold)
    total_elements = len(data)
    
    # Determine filter condition using conditional expression
    is_sparse = count_above < (total_elements * 0.3)
    
    # Compute filtered subset using slicing based on mode
    if mode == 'head':
        filtered_data = data[:total_elements//2]
    else:
        filtered_data = data[total_elements//2:]
    
    # Count odd numbers in filtered segment
    filtered_count = sum(1 for x in filtered_data if x % 2 == 1)
    
    # Dummy variable - irrelevant to final result (minor distraction)
    temp_scale = len(filtered_data) // 4 + 2
    
    # Adjustment factor based on sparsity and mode
    adjustment_factor = 2 if is_sparse else 1.5
    
    # Key computation point
    result = filtered_count * adjustment_factor
    
    # Print final result as required
    print(f"Target result: {result}")

# Input data
input_data = [12, 7, 9, 14, 3, 8, 11, 5]

# Execute function
analyze_sequence(input_data, threshold=10, mode='tail')