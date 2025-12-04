def analyze_text_complexity(text_samples):
    # Irrelevant initialization for distraction
    baseline_score = 42
    temp_cache = [i * 2 for i in range(10)]
    unused_metric = sum(temp_cache) / len(temp_cache)
    
    # Main logic with multiple steps
    processed_data = []
    for sample in text_samples:
        # Character counting and string operations
        char_count = len(sample)
        vowel_count = sum(1 for c in sample.lower() if c in 'aeiou')
        
        # Conditional expression with multiple conditions
        complexity_factor = (char_count * 2 + vowel_count) if char_count > 5 else (vowel_count - char_count)
        
        # Bitwise operations as distractor
        bit_shift = complexity_factor << 2
        unused_bit = bit_shift & 0xFF
        
        # String method operations
        processed_text = sample.upper().replace(' ', '_')
        text_length = len(processed_text)
        
        # Composite calculation with misleading intermediate
        temp_value = (complexity_factor + text_length) * 3
        misleading_result = temp_value // 2 + baseline_score
        
        # Actual relevant calculation
        if text_length % 2 == 0:
            metric = complexity_factor + vowel_count
        else:
            metric = complexity_factor - vowel_count
            
        processed_data.append(metric)
    
    # Dead code path that's never executed
    if baseline_score > 100:
        unused_result = sum(processed_data) * 2
    
    # Final computation with early return logic
    processed_data.sort()
    if len(processed_data) > 3:
        processed_data = processed_data[1:-1]
    
    # Key statement - this is what we're tracking
    final_metric = processed_data[-1]
    
    # Print the target result
    print(f"Target result: {final_metric}")
    return final_metric

# Test execution
text_samples = ["hello world", "python programming", "code analysis", "benchmark evaluation"]
result = analyze_text_complexity(text_samples)