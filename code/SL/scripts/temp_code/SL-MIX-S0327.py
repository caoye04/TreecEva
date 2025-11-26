def analyze_text_patterns(text_corpus):
    word_lengths = [len(word) for word in text_corpus]
    irrelevant_count = sum(1 for length in word_lengths if length > 8)
    
    char_frequencies = {}
    for word in text_corpus:
        for char in word:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1
    
    # Distractor operations
    temp_sum = sum(word_lengths) * 3
    unused_var = temp_sum // len(text_corpus) + 7
    
    # Main logic chain
    max_length = max(word_lengths)
    min_length = min(word_lengths)
    length_difference = max_length - min_length
    
    # Bitwise operations for distraction
    bit_shift = length_difference << 2
    bit_mask = bit_shift & 0b1111
    
    # Enumerate and zip usage
    indexed_lengths = list(enumerate(word_lengths))
    paired_values = list(zip(word_lengths, [l*2 for l in word_lengths]))
    
    # Core computation path
    product_pairs = [a * b for a, b in paired_values]
    total_product = sum(product_pairs)
    target_value = total_product // (length_difference + 1)
    
    # More distractors
    misleading_calc = (target_value * 3) % 17
    dead_branch = misleading_calc if misleading_calc > 10 else misleading_calc * 2
    
    modifier = len([pair for pair in paired_values if pair[0] > pair[1] // 2])
    divisor = max(1, len(char_frequencies) - 12)
    
    final_product = target_value * modifier // divisor
    
    # Print result
    print(f"Result: {final_product}")
    return final_product

# Execute with sample data
text_samples = ["python", "programming", "benchmark", "evaluation", "complexity", "reasoning", "algorithms"]
analyze_text_patterns(text_samples)