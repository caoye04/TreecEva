def analyze_text(text1, text2):
    # Process first text
    words1 = set(text1.lower().split())
    unique_chars1 = {c for c in text1 if c.isalpha()}
    
    # Process second text
    words2 = set(text2.lower().split())
    unique_chars2 = {c for c in text2 if c.isalpha()}
    
    # Calculate letter statistics
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count1 = len(unique_chars1.intersection(vowels))
    vowel_count2 = len(unique_chars2.intersection(vowels))
    
    # Find common words (case insensitive)
    common_words = words1.intersection(words2)
    
    # Filter words with certain properties
    long_words = {w for w in common_words if len(w) > 5}
    short_words = {w for w in common_words if len(w) <= 3}
    
    # Calculate metrics
    word_ratio = len(words1) ^ len(words2)
    char_factor = (vowel_count1 + vowel_count2) * 2
    
    # Apply bitwise operations to create a complexity factor
    complexity = (len(long_words) << 2) | (len(short_words) & 0x7)
    
    # This is the key value we want to track
    intersection_count = len(common_words)
    
    # Apply transformations that don't affect the result
    if vowel_count1 > vowel_count2:
        word_ratio += 10
    else:
        complexity += 5
    
    print(f"Text similarity metrics:")
    print(f"Common word count: {intersection_count}")
    print(f"Word ratio: {word_ratio}")
    print(f"Complexity factor: {complexity}")
    
    return intersection_count

# Sample texts
text_a = "The quick brown fox jumps over the lazy dog."
text_b = "A quick animal jumps over obstacles while the dog watches."
text_c = "Python programming is fun and rewarding to learn."

# Calculate metrics for different text combinations
result1 = analyze_text(text_a, text_b)
result2 = analyze_text(text_a, text_c)

# Final result (the one we want)
final_result = analyze_text(text_b, text_c)
print(f"Result: {final_result}")