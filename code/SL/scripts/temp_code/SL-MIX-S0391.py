def process_data(text, pattern_dict):
    # Initial setup with irrelevant computations
    base_offset = len(text) * 3 - 7
    temp_sum = sum([ord(c) for c in text[:5]]) if len(text) >= 5 else 100
    
    # Misleading intermediate calculation (dead code path)
    if base_offset > 50:
        misleading_count = base_offset // 2
    else:
        misleading_count = base_offset * 2
    
    # Actual processing logic with lambda and list comprehension
    pattern_checker = lambda s, p: sum(1 for char in s if char in p)
    relevant_chars = pattern_dict.get('target', '')
    
    # Distractor operations
    char_frequency = {char: text.count(char) for char in set(text)}
    total_unique = len(char_frequency)
    
    # Main computation with slicing and conditional logic
    processed_sections = [text[i:i+3] for i in range(0, len(text), 3)]
    valid_sections = [section for section in processed_sections 
                     if len(section) == 3 and pattern_checker(section, relevant_chars) >= 1]
    
    # More irrelevant calculations
    weighted_sum = sum(ord(c) * (i+1) for i, c in enumerate(text[:8])) if len(text) >= 8 else 0
    
    # Final result computation
    final_count = len(valid_sections) * 2 - (total_unique % 3)
    
    # Dead code that doesn't affect final_count
    unused_result = misleading_count + weighted_sum // 10
    
    return final_count

# Main execution with misleading setup
text_input = "abracadabra_pattern_test"
pattern_data = {'target': 'abc', 'ignore': 'xyz', 'weight': 2.5}

# Irrelevant preprocessing
input_length = len(text_input)
pattern_length = len(pattern_data['target'])
ratio = input_length / pattern_length if pattern_length > 0 else 0

# Key statement
result = process_data(text_input, pattern_data)

# Print final answer
print(f"Result: {result}")