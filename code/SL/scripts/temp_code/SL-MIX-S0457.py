from collections import Counter

def analyze_word_patterns(text):
    words = text.lower().split()
    word_counts = Counter(words)
    
    # Calculate pattern score (main logic)
    unique_words = len(word_counts)
    total_words = len(words)
    pattern_density = unique_words / total_words
    
    # Some intermediate calculations (partially relevant)
    char_count = sum(len(word) for word in words)
    avg_word_length = char_count / total_words
    
    # Key computation (main path)
    base_score = int(pattern_density * 100)
    length_factor = int(avg_word_length * 10)
    
    # Adjustment calculations (somewhat relevant but not used in final)
    vowel_counts = sum(1 for word in words for char in word if char in 'aeiou')
    consonant_ratio = (char_count - vowel_counts) / char_count if char_count > 0 else 0
    
    # Distractor operations (irrelevant to final result)
    temp_adjust = base_score & length_factor
    cyclic_check = (base_score << 2) | (length_factor >> 1)
    
    # Core result computation
    result = base_score + length_factor
    adjustment = result % 7
    
    # Final computation
    final_result = result ^ adjustment
    
    print(f"Target result: {final_result}")

# Execute the function
text_sample = "data science machine learning artificial intelligence data analysis"
analyze_word_patterns(text_sample)