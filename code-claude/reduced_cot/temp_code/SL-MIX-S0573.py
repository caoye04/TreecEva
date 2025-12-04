import itertools

# Text processing for a word frequency analyzer
text = "The quick brown fox jumps over the lazy dog"
words = text.lower().split()

# Track word frequencies
unique_words = set(words)
word_stats = {}

# Process words and their properties
for i, word in enumerate(words):
    # Remove any punctuation
    clean_word = word.strip('.,!?;:')
    # Update statistics
    if clean_word in word_stats:
        word_stats[clean_word] += 1
    else:
        word_stats[clean_word] = 1

# Extract words and their counts for analysis
words = list(word_stats.keys())
counts = list(word_stats.values())

# Calculate number of valid words (longer than 3 characters and appear at least once)
valid_words = sum(1 for w, c in zip(words, counts) if len(w) > 3 and c > 0)

# Display results
print(f"Result: {valid_words}")