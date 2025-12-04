# Text analysis of most frequent words in a paragraph
text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy. Brown foxes are known to be quick."

# Convert to lowercase for case-insensitive counting
text = text.lower()

# Clean the text by removing punctuation
punctuation = ['.', ',', '!', '?', ';', ':']
for p in punctuation:
    text = text.replace(p, '')

# Split into words
words = text.split()

# Count word frequencies
word_frequencies = {}
for word in words:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

# Calculate statistics
total_words = len(words)
unique_words = len(word_frequencies)
average_frequency = total_words / unique_words if unique_words > 0 else 0

# Sort words by frequency (most frequent first)
sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

# Find the top 3 most frequent words
top_words = sorted_words[:3]

# Calculate a frequency threshold based on average
frequency_threshold = average_frequency * 0.8

# Extract words with frequency higher than threshold
frequency_indicator = sum(1 for w in word_frequencies.values() if w > 2)
common_word_set = {word for word, freq in word_frequencies.items() if freq > frequency_threshold}

# Count how many words exceed our threshold
filtered_word_count = len([w for w in word_frequencies if word_frequencies[w] > frequency_threshold])

# Calculate a complexity score (not used in the final answer)
complexity_score = unique_words * average_frequency / (total_words * 0.1)

# Print some results
print(f"Total words: {total_words}")
print(f"Unique words: {unique_words}")
print(f"Top 3 words: {top_words}")
print(f"Frequency threshold: {frequency_threshold}")
print(f"Number of words above threshold: {filtered_word_count}")
print(f"Result: {filtered_word_count}")