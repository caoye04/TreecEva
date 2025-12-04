from collections import Counter

text = "data science is the study of data extraction and data analysis"
words = text.split()

# Calculate average word length
avg_length = sum(len(word) for word in words) / len(words)
print(f"Average word length: {avg_length:.2f}")

# Find the most common word and its frequency
word_frequency = Counter(words).most_common(1)[0][1]
most_common = Counter(words).most_common(1)[0][0]

# Calculate number of unique words
unique_words = len(set(words))

# Find words longer than average
longer_words = [word for word in words if len(word) > avg_length]

print(f"Result: {word_frequency}")