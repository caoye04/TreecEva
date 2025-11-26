from collections import Counter

def analyze_text_patterns(text_samples):
    char_frequencies = Counter()
    processed_total = 0
    temp_storage = []
    
    for sample in text_samples:
        char_frequencies.update(sample)
        temp_storage.extend([ord(c) for c in sample if c.isalpha()])
    
    # Distractor: Calculate but don't use
    max_freq_char = char_frequencies.most_common(1)[0] if char_frequencies else ('', 0)
    
    # Relevant processing
    vowel_counts = sum(1 for char, count in char_frequencies.items() 
                      if char.lower() in 'aeiou')
    consonant_counts = sum(1 for char, count in char_frequencies.items() 
                          if char.isalpha() and char.lower() not in 'aeiou')
    
    # Distractor: Intermediate calculation that's not used in final result
    ratio_calc = vowel_counts * 3 if consonant_counts > 0 else 0
    
    processed_total = vowel_counts + consonant_counts
    
    # Final relevant computation
    final_count = processed_total // 2
    
    print(f"Result: {final_count}")
    return final_count

# Test data
text_data = ["programming", "benchmark", "evaluation", "reasoning"]
analyze_text_patterns(text_data)