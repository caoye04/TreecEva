def process_text_data(text_samples):
    # Distractor: irrelevant string operations
    temp_upper = lambda x: x.upper() if len(x) > 3 else x.lower()
    temp_lower = lambda x: x.lower() if x.isalpha() else x.upper()
    
    # Main logic with misleading intermediate results
    char_sets = []
    processed_values = []
    
    for text in text_samples:
        # Distractor: unused operation
        reversed_text = text[::-1]
        
        # Relevant: character set operations
        char_set = set(text)
        char_sets.append(char_set)
        
        # Misleading calculation
        temp_sum = sum(ord(c) for c in text) % 100
        
        # Actual processing with conditionals
        if len(text) % 2 == 0:
            processed = len(char_set) * 10
        else:
            processed = len(char_set) * 5
        
        # Distractor: dead code path
        if processed > 100:
            processed = processed - 50  # Never reached with given data
        
        processed_values.append(processed)
    
    # More distractors: irrelevant set operations
    union_set = set()
    for cs in char_sets:
        union_set = union_set.union(cs)
    
    # Dead variable
    intersection_size = len(char_sets[0].intersection(char_sets[1])) if len(char_sets) > 1 else 0
    
    # Final calculation with string methods
    base_value = sum(processed_values)
    unique_chars = len(union_set)
    
    # Key statement: the actual answer
    result = base_value - unique_chars * 2
    
    # More irrelevant operations
    dummy_var = len(''.join(text_samples)) // 10
    unused_result = dummy_var * 3 + 7
    
    return result

# Main execution with realistic data
text_samples = ['algorithm', 'processing', 'benchmark', 'reasoning']
final_output = process_text_data(text_samples)
print(f"Result: {final_output}")