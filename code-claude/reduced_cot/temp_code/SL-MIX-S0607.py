import itertools
from functools import reduce

# Text analysis function to count valid words
def analyze_text(text, min_length=4):
    # Clean and split the text
    words = text.lower().replace(',', ' ').replace('.', ' ').split()
    
    # Some statistics that might be useful later
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(words) if words else 0
    
    # Extract unique characters for analysis
    all_chars = ''.join(words)
    unique_chars = set(all_chars)
    char_frequency = {char: all_chars.count(char) for char in unique_chars}
    
    # Filter words based on various criteria
    contains_vowel = lambda w: any(c in 'aeiou' for c in w)
    starts_with_consonant = lambda w: w and w[0] not in 'aeiou'
    
    # Apply filters - we only care about certain words
    potential_words = [w for w in words if contains_vowel(w)]
    filtered_words = list(filter(starts_with_consonant, potential_words))
    
    # Count words meeting our length requirement
    valid_word_count = sum(1 for word in filtered_words if len(word) >= min_length)
    
    # Calculate a quality score (not used in final result)
    quality_score = valid_word_count * 10 - len(words) // 2
    
    # Generate word pairs for later analysis (not used for now)
    word_pairs = list(itertools.combinations(filtered_words[:3], 2)) if len(filtered_words) >= 2 else []
    
    return valid_word_count

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog while watching carefully."
result = analyze_text(sample_text, 5)
print(f"Result: {result}")