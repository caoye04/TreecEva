from collections import Counter, defaultdict

def analyze_text(text):
    # Count characters in the text
    char_freq = Counter(text.lower())
    
    # Remove spaces and punctuation from counting
    for char in [' ', '.', ',', '!', '?']:
        if char in char_freq:
            char_freq.pop(char)
    
    # Calculate some statistics about the text
    total_chars = sum(char_freq.values())
    most_common = char_freq.most_common(1)[0][0] if char_freq else ''
    
    # Track vowels and consonants
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = sum(char_freq[v] for v in vowels if v in char_freq)
    consonant_count = total_chars - vowel_count
    
    # Create a ratio dictionary (not used in final result)
    char_ratios = defaultdict(float)
    for char, count in char_freq.items():
        char_ratios[char] = count / total_chars if total_chars else 0
    
    # Calculate uniqueness score (not used in final result)
    uniqueness_score = len(char_freq) / total_chars if total_chars else 0
    
    # Count unique characters
    unique_chars = len(char_freq)
    
    return unique_chars, total_chars, vowel_count, consonant_count

# Sample text to analyze
sample = "hello world"

# Process text and get results
unique_result, total_result, vowels_result, consonants_result = analyze_text(sample)

# Calculate a complexity factor (not used in final calculation)
complexity = (total_result * 0.8) + (unique_result * 1.5)

# Print the number of unique characters
print(f"Result: {unique_result}")