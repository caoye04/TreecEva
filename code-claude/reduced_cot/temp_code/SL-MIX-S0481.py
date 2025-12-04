from collections import Counter

text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Process the text
text = text.lower()
words = text.split()

# Count word frequency
word_frequency = Counter(words)

# Remove words that only appear once
for word in list(word_frequency.keys()):
    if word_frequency[word] == 1:
        del word_frequency[word]

# Number of words that appear multiple times
common_word_count = len(word_frequency)

# Create a dictionary with word lengths
word_lengths = {word: len(word) for word in word_frequency}

# Calculate average length of common words
avg_length = sum(word_lengths.values()) / common_word_count if common_word_count > 0 else 0

print(f"Result: {common_word_count}")