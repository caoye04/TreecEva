from collections import Counter

text = "The quick brown fox jumps over the lazy dog while the dog barks at the fox"

# Clean and split the text
words = text.lower().split()

# Initial processing
total_words = len(words)
unique_words = len(set(words))

# Count word frequencies
word_freq = Counter(words)
most_common_word = word_freq.most_common(1)[0][0]

# Process word lengths
word_lengths = Counter([len(word) for word in words])
most_common_word_length = word_lengths.most_common(1)[0][0]

# Calculate average word length for comparison
avg_length = sum(len(word) for word in words) / total_words

# Additional metrics
max_length = max(len(word) for word in words)
min_length = min(len(word) for word in words)

print(f"Result: {most_common_word_length}")