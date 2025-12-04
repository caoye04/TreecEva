# Word processing utility to analyze text data

text_samples = ["hello world", "python programming", "data analysis"]
processed_words = []

# Process each text sample
for i, sample in enumerate(text_samples):
    words = sample.split()
    # Add word index tuple pairs to processed list
    for j, word in enumerate(words):
        processed_words.append(word)

# Calculate some statistics
word_count = len(processed_words)
average_length = sum(len(word) for word in processed_words) / word_count

# Generate word-length pairs
word_length_pairs = [(word, len(word)) for word in processed_words]

# Count total characters across all processed words
total_characters = sum(len(word) for word in processed_words)

# Combine the first letter of each word
first_letters = ''.join(word[0] for word in processed_words)

print(f"Result: {total_characters}")