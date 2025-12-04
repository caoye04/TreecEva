from collections import Counter

document = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Clean the text by removing punctuation and converting to lowercase
clean_text = ""
for char in document:
    if char.isalnum() or char.isspace():
        clean_text += char.lower()
    else:
        clean_text += " "

# Split into words and create word frequency counter
words = clean_text.split()
word_counts = Counter(words)

# Calculate statistics
total_words = len(words)
word_set = set(words)
unique_words_count = len(word_set)
most_common_word = word_counts.most_common(1)[0][0]

# Calculate average word frequency
avg_frequency = total_words / unique_words_count if unique_words_count > 0 else 0

print(f"Result: {unique_words_count}")