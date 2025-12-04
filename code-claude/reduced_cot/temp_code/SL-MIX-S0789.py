from collections import Counter

text = "The quick brown fox jumped over the lazy dog. The fox was very quick!"
stop_words = {"the", "was", "over", "very"}

# Convert to lowercase and remove punctuation
processed_text = "".join(c.lower() if c.isalpha() else " " for c in text)

# Split into words
words = processed_text.split()

# Filter out stop words
filtered_words = [word for word in words if word not in stop_words]

# Count word frequencies
word_frequency = dict(Counter(filtered_words))

# Get most common word
most_common = max(word_frequency.items(), key=lambda x: x[1])
most_common_word = most_common[0]

# Calculate average word length
total_length = sum(len(word) for word in filtered_words)
avg_length = total_length / len(filtered_words) if filtered_words else 0

print(f"Result: {len(word_frequency)}")