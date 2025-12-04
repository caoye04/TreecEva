# Count occurrences of specific words in a text sample

text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Some potential words to analyze
target_words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
ignore_words = ["and", "was", "a", "an", "the"]

# Process text to lowercase for case-insensitive matching
processed_text = text.lower()

# Define counter function using lambda
filter_words = lambda word: word.lower() not in ignore_words
counter = lambda s: len(list(filter(filter_words, s.lower().replace(".", "").split())))

# Count words that aren't in the ignore list
word_count = counter(text)

# Display some statistics
print(f"Text length: {len(text)}")
print(f"Target result: {word_count}")