def analyze_sequence_pattern(text_corpus, pattern_key):
    # Distractor: multiple irrelevant variables
    initial_offset = 15
    temp_buffer = [0] * 20
    dummy_sum = sum(range(10))
    
    # Relevant: string slicing and pattern analysis
    core_segment = text_corpus[3:15]
    pattern_matches = 0
    
    # Misleading intermediate computation
    fake_count = len(core_segment) * 2 + initial_offset
    
    # Dead code path
    if fake_count > 100:
        unused_result = fake_count // 2
    else:
        unused_result = fake_count * 3
    
    # Actual pattern analysis
    for i in range(len(core_segment) - len(pattern_key) + 1):
        window = core_segment[i:i+len(pattern_key)]
        if window == pattern_key:
            pattern_matches += 1
    
    # More distractors
    intermediate_value = pattern_matches * 7
    redundant_calc = (intermediate_value + 5) % 13
    
    # Key computation with bitwise operations
    pattern_factor = (pattern_matches << 2) | 1
    
    # Final relevant calculation
    valid_sequences = pattern_matches * 3 - 1
    final_count = valid_sequences * pattern_factor
    
    # Unused computation
    misleading_total = final_count + dummy_sum + redundant_calc
    
    print(f"Result: {final_count}")
    return final_count

# Main execution with realistic scenario
text_data = "abxypatternqrwpatternzvpatternmnopattern"
target_pattern = "pattern"
result = analyze_sequence_pattern(text_data, target_pattern)
