from collections import Counter

text = "The quick brown fox jumped over the lazy dog. The fox was very quick!"

# Convert to lowercase for better matching
text_lower = text.lower()

# Split into words and remove punctuation
words = [word.strip('.,!?;:') for word in text_lower.split()]

# Filter out short words (less than 3 characters)
filtered_words = [word for word in words if len(word) >= 3]

# Find common words to exclude
common_words = ['the', 'and', 'was']

# Remove common words from our filtered list
filtered_words = [word for word in filtered_words if word not in common_words]

# Calculate word frequencies
word_frequency = Counter(filtered_words).most_common(1)[0][1]

# Display result
print(f"Result: {word_frequency}")