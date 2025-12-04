def analyze_data_patterns():
    data_stream = [15, 23, 42, 8, 56, 31, 19, 4, 72, 11]
    threshold_check = 25
    pattern_count = 0
    running_total = 0
    
    # Distractor: calculate average but don't use it
    temp_avg = sum(data_stream) / len(data_stream)
    
    for idx, value in enumerate(data_stream):
        if idx % 2 == 0 and value > threshold_check:
            pattern_count += 1
            running_total += value
        
        # Distractor: calculate XOR but don't use it
        xor_check = value ^ idx
    
    # Main computation chain
    analysis_complete = pattern_count * running_total
    
    # Distractor: complex calculation that gets discarded
    unused_computation = (temp_avg * pattern_count) - (xor_check if 'xor_check' in locals() else 0)
    
    # Final assignment
    final_result = analysis_complete
    print(f"Target result: {final_result}")
    
analyze_data_patterns()