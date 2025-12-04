def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return sum(1 for char in text.lower() if char in consonants)

# Text analysis for a linguistics study
text = "The quick brown fox jumps over the lazy dog"
debug_mode = False
case_sensitive = False  # Not used in final calculation

# Remove spaces for character frequency analysis
no_spaces = text.replace(" ", "")
char_count = len(no_spaces)

# Apply filters based on character position
filter_factor = 3
filtered_text = ""
for i, char in enumerate(no_spaces):
    # Keep characters at positions divisible by filter_factor
    if i % filter_factor == 0 or char.isupper():
        filtered_text += char

# Calculate letter frequencies for debugging
if debug_mode:
    letter_freq = {}
    for char in filtered_text.lower():
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1

# Lambda functions for scoring
consonant_value = lambda c: ord(c.lower()) - ord('a') + 1 if c.lower() in 'bcdfghjklmnpqrstvwxyz' else 0
vowel_value = lambda c: (ord(c.lower()) - ord('a')) * 2 if c.lower() in 'aeiou' else 0

# Calculate linguistic score based on character types
def calculate_word_score(word):
    consonant_score = sum(consonant_value(c) for c in word)
    vowel_score = sum(vowel_value(c) for c in word)
    
    # Special case handling for 'q' without 'u'
    q_count = word.lower().count('q')
    u_after_q = 0
    for i in range(len(word) - 1):
        if word[i].lower() == 'q' and word[i+1].lower() == 'u':
            u_after_q += 1
    
    # Final scoring formula
    word_score = consonant_score + vowel_score - (q_count - u_after_q) * 5
    print(f"Result: {word_score}")
    return word_score

# Process the filtered text
word_score = calculate_word_score(filtered_text)

# Additional statistics (not used in final result)
char_density = len(filtered_text) / len(text) if text else 0
vowel_count = count_vowels(filtered_text)
consonant_count = count_consonants(filtered_text)

print(f"Result: {word_score}")