def process_text(text):
    # Remove punctuation and convert to lowercase
    clean_text = ''.join(c.lower() if c.isalnum() else ' ' for c in text)
    # Split into words
    words = clean_text.split()
    return words

# Sample text from a book review
review = "The book was excellent! I enjoyed the plot and characters. The ending, however, was somewhat predictable."

# Process the text
processed_text = process_text(review)

# Calculate statistics
word_count = len(processed_text)
average_length = sum(len(word) for word in processed_text) / word_count if word_count > 0 else 0

# Find unique words
unique_words = len(set(processed_text))

# Print results
print(f"Total words: {word_count}")
print(f"Average word length: {average_length:.2f}")
print(f"Unique words: {unique_words}")
