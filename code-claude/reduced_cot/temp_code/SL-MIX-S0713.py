import itertools

text = "programming challenges require logical thinking"

# Extract words with length greater than 5
long_words = [word for word in text.split() if len(word) > 5]

# Process the first long word
first_word = long_words[0] if long_words else ""

# Get only alphabetic characters from the word
processed_word = ''.join(c for c in first_word if c.isalpha())

# Apply some transformations
alpha_word = processed_word.lower()
reversed_word = alpha_word[::-1]

# Filter characters based on position
filtered_word = ''
for i, char in enumerate(reversed_word):
    if i % 2 == 0:
        filtered_word += char

# Count unique characters
unique_count = len(set(filtered_word))

# Generate additional statistics
avg_ascii = sum(ord(c) for c in filtered_word) / len(filtered_word) if filtered_word else 0

print(f"Result: {unique_count}")