# Count unique words in a text exceeding a minimum length

text = "The quick brown fox jumps over the lazy dog while the dog barks"
min_length = 3
all_words = len(text.split())

# Filter for words longer than minimum length
long_words = [word for word in text.split() if len(word) >= min_length]

# Count unique words exceeding the minimum length
unique_words = len(set([word.lower() for word in text.split() if len(word) > min_length]))

# Calculate average word length for comparison
avg_length = sum(len(word) for word in text.split()) / all_words

# Apply a weighting factor based on average length
weighted_factor = lambda x: x * (avg_length / 5)
weighted_count = weighted_factor(unique_words)

print(f"Result: {unique_words}")