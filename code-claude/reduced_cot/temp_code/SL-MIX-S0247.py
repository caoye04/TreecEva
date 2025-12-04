from collections import Counter

text = "the quick brown fox jumps over the lazy dog and the fox was quick"
words = text.lower().split()

# Count word frequencies
word_counts = Counter(words)

# Find words that appear exactly once
single_occurrence = {word for word, count in word_counts.items() if count == 1}

# Create a set of all words
word_set = set(words)

# Calculate metrics
unique_words = len(word_set)
total_words = len(words)

# Track some additional statistics
avg_word_length = sum(len(word) for word in word_set) / unique_words
max_frequency = word_counts.most_common(1)[0][1]

print(f"Result: {unique_words}")