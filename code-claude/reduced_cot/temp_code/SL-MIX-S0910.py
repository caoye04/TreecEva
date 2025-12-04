from collections import Counter

# Analyzing text from a book review
text = "The book was fantastic and engaging. The plot was well-crafted and the characters were fantastic. I would recommend this book to anyone who enjoys a well-crafted story."

# Clean and process the text
text = text.lower()
punctuation = ".,!?;:()"
for p in punctuation:
    text = text.replace(p, "")
    
# Split into words and remove common words
words = text.split()
common_words = {"the", "and", "was", "to", "a", "i", "this"}
processed_words = [word for word in words if word not in common_words]

# Count unique words
unique_word_count = len(set(processed_words))

# Find most frequent word for analysis
word_counts = Counter(processed_words)
most_common = word_counts.most_common(1)[0][0]

print(f"Result: {unique_word_count}")