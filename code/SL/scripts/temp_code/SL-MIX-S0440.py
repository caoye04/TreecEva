def analyze_text_complexity(text):
    # Irrelevant string transformations
    temp_upper = text.upper()
    temp_reversed = text[::-1]
    char_count = lambda s: sum(1 for c in s if c.isalpha())
    
    # Distractor computations
    vowel_count = sum(1 for c in text if c.lower() in 'aeiou')
    space_count = text.count(' ')
    irrelevant_sum = len(text) * 3 - vowel_count + space_count
    
    # Main logic path
    words = text.split()
    avg_word_len = sum(len(word) for word in words) / max(len(words), 1)
    
    # Misleading intermediate result
    complexity_factor = (avg_word_len * 10) % 7
    
    # Unused dead code path
    if len(text) > 50:
        compression_ratio = len(text) / avg_word_len
    else:
        compression_ratio = avg_word_len / len(text)
    
    # Actual computation
    unique_chars = len(set(text.lower()))
    compression_score = round((unique_chars * avg_word_len) / (len(text) + 1), 2)
    
    # More distractions
    fake_result = compression_score * 2 - complexity_factor
    dummy_var = fake_result + irrelevant_sum
    
    return compression_score

# Main execution
sample_text = "The quick brown fox jumps over the lazy dog"
unrelated_data = [1, 2, 3, 4, 5]
processed_list = list(map(lambda x: x * 2 - 1, unrelated_data))

final_result = analyze_text_complexity(sample_text)
print(f"Target result: {final_result}")