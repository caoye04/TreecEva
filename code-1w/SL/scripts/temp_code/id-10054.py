def evaluate_data_compliance():
    raw_samples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    offset = 2
    processed = [x + offset for x in raw_samples if x % 2 == 0]
    
    # Apply slicing to extract middle portion
    trimmed = processed[1:-1]
    
    # Define valid range using set comprehension
    valid_range = {x for x in range(5, 12)}
    
    # Perform set difference to isolate outliers
    outlier_buffer = {3, 4, 12}
    extended_valid = valid_range | outlier_buffer
    
    # Final compliance check
    final_set = set(trimmed)
    threshold_met = final_set.issubset(valid_range)
    
    # Irrelevant tracking variable (minimal distraction)
    sample_count = len(raw_samples)
    
    print(f"Result: {threshold_met}")

evaluate_data_compliance()