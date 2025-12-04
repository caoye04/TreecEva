from collections import Counter

def calculate_word_value(word):
    # Calculate a value based on letter frequencies and positions
    letter_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    consonant_value = 2
    total = 0
    
    # Count letter frequencies
    letter_count = Counter(word.lower())
    vowel_count = sum(letter_count[vowel] for vowel in 'aeiou' if vowel in letter_count)
    
    # This calculation doesn't affect the result
    average_ascii = sum(ord(c) for c in word) / len(word) if word else 0
    normalized_ascii = int(average_ascii) % 10
    
    # Process each character
    for i, char in enumerate(word.lower()):
        # Position factor (not used in final calculation)
        position_factor = (i + 1) / len(word)
        
        if char in letter_values:
            total += letter_values[char] * (i + 1)
        elif char.isalpha():
            total += consonant_value * (i + 1)
    
    # Some additional processing that doesn't affect the result
    potential_bonus = len(set(word)) - vowel_count
    complexity_score = len(word) * 0.5
    
    return total

# Sample text for processing
text = "The quick brown fox jumps over the lazy dog"
words = text.split()

# Some preprocessing that doesn't affect the final answer
word_lengths = [len(word) for word in words]
max_length = max(word_lengths) if word_lengths else 0
min_length = min(word_lengths) if word_lengths else 0

# Find words with specific properties
long_words = [word for word in words if len(word) >= 4]
short_words = [word for word in words if len(word) < 4]

# Select an important word
important_word = "fox"
backup_word = "jumps"

# Calculate various word values
long_word_value = calculate_word_value(long_words[2]) if len(long_words) > 2 else 0
short_word_value = calculate_word_value(short_words[0]) if short_words else 0

# Calculate the target value
word_value = calculate_word_value(important_word)

print(f"Result: {word_value}")