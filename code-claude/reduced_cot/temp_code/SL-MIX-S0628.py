from collections import Counter

def calculate_word_score(text):
    # Count character frequencies
    char_count = Counter(text.lower())
    
    # Remove spaces from consideration
    if ' ' in char_count:
        del char_count[' ']
    
    # Calculate primary score based on unique characters
    unique_chars = len(char_count)
    primary_score = unique_chars * 10
    
    # Calculate secondary score based on vowel ratio
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    vowel_count = sum(char_count[v] for v in vowels if v in char_count)
    consonant_count = sum(char_count[c] for c in consonants if c in char_count)
    
    # Avoid division by zero
    if consonant_count == 0:
        vowel_ratio = 100  # Arbitrary high value
    else:
        vowel_ratio = vowel_count / consonant_count
    
    # This calculation isn't used in final result
    special_chars = sum(char_count[c] for c in char_count if c not in vowels and c not in consonants)
    special_factor = special_chars * 2
    
    # Calculate word length metrics (distraction)
    words = text.split()
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    max_word_length = max(len(word) for word in words) if words else 0
    
    # Calculate final score
    word_score = int(primary_score + (vowel_ratio * 15))
    
    return word_score

# Sample text to analyze
text = "The quick brown fox jumps over the lazy dog"

# Process text (distraction)
processed_text = text.replace('!', '').replace('.', '')
reversed_text = processed_text[::-1]  # This isn't used

# Calculate the score
word_score = calculate_word_score(processed_text)

# Some additional calculations that don't affect the result
bonus_points = len(processed_text) // 5
penalty = 3 if 'z' in processed_text.lower() else 0

print(f"Result: {word_score}")