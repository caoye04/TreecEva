def is_valid_character(char):
    # Check if character is alphanumeric or in special set
    special_chars = {'-', '_', '.', '!'}
    return char.isalnum() or char in special_chars

text = "Hello! This is a sample-text. It has some_words with different patterns."

# Process text to extract words
processed_text = ''.join([c.lower() if is_valid_character(c) else ' ' for c in text])
decoration_chars = ['-', '_', '.']

# Split into words and clean them
raw_words = processed_text.split()
words = []

for word in raw_words:
    # Remove decoration characters
    clean_word = ''
    for char in word:
        if char not in decoration_chars:
            clean_word += char
    
    if len(clean_word) > 0:
        words.append(clean_word)

# Count word frequencies
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Find words that appear exactly once
unique_words = set(words)
once_words = {word for word in word_freq if word_freq[word] == 1}

# Calculate vowel statistics
vowels = {'a', 'e', 'i', 'o', 'u'}
total_vowels = sum([processed_text.count(v) for v in vowels])
vowel_count = 3  # Number of vowels to check for

# Set threshold based on average vowels per word
avg_vowels = total_vowels / len(words) if words else 0
threshold = 2  # Minimum length for valid words

# Get valid words that meet our criteria
valid_words = len([word for word in unique_words if vowel_count >= threshold])
print(f"Result: {valid_words}")
