from collections import Counter

text = "The quick brown fox jumps over the lazy dog. The fox is quick and the dog is lazy."

# Preprocessing the text
processed_text = text.lower().replace('.', '').replace(',', '')
words = processed_text.split()

# Count word frequencies
word_counter = Counter(words)

# Find words that appear more than once
repeated_words = [word for word, count in word_counter.items() if count > 1]
print(f"Repeated words: {repeated_words}")

# Get the 3 most common words
common_word_count = len(word_counter.most_common(3))

# Check if any word appears exactly twice
twice_words = [word for word, count in word_counter.items() if count == 2]
twice_count = len(twice_words)

print(f"Result: {common_word_count}")