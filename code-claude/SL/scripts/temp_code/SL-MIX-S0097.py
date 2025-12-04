# Analysis of common words in two text samples
sample1 = "the quick brown fox jumps over the lazy dog"
sample2 = "a quick brown dog barks at the moon light"

# Extract all words from both samples
words_combined = sample1.split() + sample2.split()

# Some metadata about the samples
max_word = max(words_combined, key=len)
min_word = min(words_combined, key=len)

# Calculate lengths of all words
word_lengths = []
for i, word in enumerate(words_combined):
    # Store the length of each word
    word_lengths.append(len(word))

# Find common words between samples
common_set = set(sample1.split()) & set(sample2.split())
common_count = len(common_set)

# Find unique word lengths
unique_count = len(set(word_lengths))

# Display results
print(f"Common words: {common_set}")
print(f"Unique word lengths: {unique_count}")
print(f"Result: {unique_count}")