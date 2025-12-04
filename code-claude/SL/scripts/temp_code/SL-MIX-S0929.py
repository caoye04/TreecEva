from collections import Counter

text = "the quick brown fox jumps over the lazy dog but the fox was too quick for the dog"
words = text.lower().split()

# Count word frequencies
word_counts = Counter(words)

# Some text analysis
total_words = len(words)
max_word = word_counts.most_common(1)[0][0]
max_count = word_counts.most_common(1)[0][1]

# Find unique words
unique_words = len(word_counts)

# Calculate average word frequency
avg_frequency = total_words / unique_words if unique_words > 0 else 0

print(f"Result: {unique_words}")