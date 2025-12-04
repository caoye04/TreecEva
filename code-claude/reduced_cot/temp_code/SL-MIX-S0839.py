def find_vowels(word):
    vowels = 'aeiou'
    return [c for c in word.lower() if c in vowels]

def calculate_length_factor(text):
    words = text.split()
    avg_len = sum(len(word) for word in words) / len(words) if words else 0
    # This factor isn't used in the final calculation
    complexity_factor = len([w for w in words if len(w) > 5]) / len(words) if words else 0
    return avg_len

def calculate_word_score(text):
    words = text.split()
    # Track some metrics that won't be used directly
    longest_word = max(words, key=len) if words else ''
    shortest_word = min(words, key=len) if words else ''
    
    # Core calculation
    base_score = sum(len(find_vowels(word)) * 2 + len(word) for word in words)
    
    # Apply length factor
    length_factor = calculate_length_factor(text)
    adjusted_score = base_score * (1 + length_factor / 10)
    
    # Apply bonus for words with more than 2 vowels
    vowel_rich_words = len([w for w in words if len(find_vowels(w)) > 2])
    bonus = vowel_rich_words * 5
    
    # These operations don't affect the final result
    consonants = sum(len(word) - len(find_vowels(word)) for word in words)
    word_density = len(words) / len(text) if text else 0
    
    return round(adjusted_score + bonus, 2)

# Input text processing
text = "Python is an interpreted high-level programming language"
text_length = len(text)
words_count = len(text.split())

# Apply some transformations that don't affect the result
text_reversed = text[::-1]
text_upper = text.upper()

# This filter doesn't actually change the text
filter_words = lambda s: s.replace('xyz', '')
filtered_text = filter_words(text)

# Calculate the word score
word_score = calculate_word_score(filtered_text)

# Extra calculation that isn't used
alternate_score = lambda t: sum(ord(c) % 10 for c in t) / 10
alt_value = alternate_score(text)

print(f"Result: {word_score}")