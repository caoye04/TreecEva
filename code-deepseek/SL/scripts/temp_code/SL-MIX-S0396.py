def analyze_text_data(text_samples):
    # Initialize data processing variables
    base_count = len(text_samples)
    char_total = sum(len(sample) for sample in text_samples)
    
    # Calculate character density (distractor - not used in final result)
    density_metric = char_total / base_count if base_count > 0 else 0
    
    # Process each text sample
    processed_values = []
    for i, sample in enumerate(text_samples):
        # Clean and process text (distractor operations)
        cleaned = sample.strip().lower()
        
        # Calculate weighted score based on position and length
        position_weight = i + 1
        length_factor = len(cleaned) % 10
        weighted_score = position_weight * length_factor
        
        processed_values.append(weighted_score)
    
    # Calculate main processing metrics
    processed_data = sum(processed_values)
    adjustment_factor = base_count * 2
    normalization_constant = max(processed_values) if processed_values else 1
    
    # Final computation (this is the key statement)
    final_result = processed_data * adjustment_factor // normalization_constant
    
    # Print result for verification
    print(f"Result: {final_result}")
    return final_result

# Test data
text_samples = ["Hello World", "Python Code", "Data Analysis", "Benchmark Test"]
result = analyze_text_data(text_samples)