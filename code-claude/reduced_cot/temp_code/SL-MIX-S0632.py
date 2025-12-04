from collections import Counter

# Process text data from a language analysis dataset
text = "The quick brown fox jumps over the lazy dog while the dog barks at the fox"

# Initial text processing
words = text.lower().split()
total_chars = sum(len(word) for word in words)
avg_length = total_chars / len(words)

# Create frequency analysis
word_count = Counter(words)
most_common = word_count.most_common(1)[0][0]
unique_words = set(words)

# Filter words based on conditions
filtered_words = []
for word in unique_words:
    score = len(word) * word_count[word]
    if 'o' in word or word.startswith('t'):
        filtered_words.append(word)
    elif score > 10:
        # This condition never triggers but adds complexity
        filtered_words.append(word + 's')

# Calculate statistics on filtered words
total_filtered = len(filtered_words)
filtered_chars = sum(len(w) for w in filtered_words)

# Create word pairs for analysis (not used in final result)
pairs = list(zip(words[:-1], words[1:]))
distinct_pairs = len(set(pairs))

# Count words with more than 3 characters
word_frequency = len([w for w in filtered_words if len(w) > 3])

# Calculate alternate metric (not used in final answer)
alternate_metric = sum(1 for w in filtered_words if w in most_common)

print(f"Result: {word_frequency}")