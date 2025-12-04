def count_word_frequency(text):
    # Count frequency of words in text
    words = text.lower().split()
    frequency = {}
    for word in words:
        # Remove punctuation
        clean_word = ''.join(c for c in word if c.isalnum())
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    return frequency

# Sample texts from two documents
doc1 = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
doc2 = "A quick brown dog jumps over the fence. The dog was brown and energetic."

# Calculate word frequencies
word_freq1 = count_word_frequency(doc1)
word_freq2 = count_word_frequency(doc2)

# Find common words between documents
common_words = set(word_freq1.keys()) & set(word_freq2.keys())

# Calculate potential similarity score (not used in final result)
similarity_score = len(common_words) / (len(word_freq1) + len(word_freq2)) * 100

# Create combined frequency dictionary
word_freq = {}
for word in set(word_freq1.keys()) | set(word_freq2.keys()):
    # For common words, use the sum of frequencies
    if word in common_words:
        word_freq[word] = word_freq1.get(word, 0) + word_freq2.get(word, 0)
    # For words only in doc1, use frequency * 2
    elif word in word_freq1:
        word_freq[word] = word_freq1[word] * 2
    # For words only in doc2, use frequency * 3
    else:
        word_freq[word] = word_freq2[word] * 3

# Calculate weighted frequency for all words (distraction)
weighted_freq = sum(len(word) * freq for word, freq in word_freq.items())

# Filter common words by length and sum their frequencies
filtered_sum = sum(word_freq[word] for word in common_words if len(word) > 3)

# Calculate alternative metrics (distractions)
avg_word_length = sum(len(word) for word in word_freq) / len(word_freq)
unique_ratio = len(common_words) / len(word_freq) * 100

print(f"Result: {filtered_sum}")