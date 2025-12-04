from collections import Counter
import itertools

def analyze_text_patterns(text):
    # Convert to lowercase for case-insensitive analysis
    processed_text = text.lower()
    
    # Count words that meet our criteria
    words = processed_text.split()
    word_counts = Counter(words)
    
    # Track some metrics that seem important
    total_chars = sum(len(word) for word in words)
    avg_word_length = total_chars / max(1, len(words))
    unique_words = len(word_counts)
    
    # Find words with alternating vowels and consonants
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # These variables track our alternating pattern search
    valid_words = []
    invalid_words = []
    
    for word in words:
        if len(word) < 4:  # Skip short words
            continue
            
        # Track alternation pattern
        alternating = True
        starts_with_vowel = word[0] in vowels
        
        # This variable doesn't affect the result but seems important
        expected_pattern = itertools.cycle([True, False]) if starts_with_vowel else itertools.cycle([False, True])
        
        # Check if word follows alternating pattern
        for i, char in enumerate(word):
            if char not in vowels and char not in consonants:
                alternating = False
                break
                
            is_vowel = char in vowels
            # Compare with expected pattern
            if is_vowel != (i % 2 == 0 if starts_with_vowel else i % 2 == 1):
                alternating = False
                break
        
        # Collect results
        if alternating:
            valid_words.append(word)
        else:
            invalid_words.append(word)
    
    # Calculate various metrics
    valid_count = len(valid_words)
    invalid_count = len(invalid_words)
    total_words = len(words)
    
    # Calculate the primary metric we're interested in
    frequency_ratio = valid_count / max(1, total_words)
    
    # This doesn't affect our result but seems like it might be important
    weighted_score = valid_count * 2 - invalid_count
    
    return {
        'valid_words': valid_words,
        'frequency_ratio': frequency_ratio,
        'weighted_score': weighted_score,
        'avg_word_length': avg_word_length
    }

# Sample text to analyze
sample_text = "The quick brown fox jumps over a lazy dog while the moon shines brightly"

result = analyze_text_patterns(sample_text)
print(f"Result: {result['frequency_ratio']}")