text_data = """Machine learning algorithms analyze patterns in data to make predictions and decisions without being explicitly programmed for each task."""

# Count all words in the text
all_words = text_data.split()
word_count = len(all_words)

# Extract unique words using set comprehension
unique_words_set = {word.lower() for word in all_words}

# Calculate distinct words count
distinct_words = len(unique_words_set)

# Some additional processing for reference
char_count = sum(len(word) for word in all_words)

print(f"Result: {distinct_words}")