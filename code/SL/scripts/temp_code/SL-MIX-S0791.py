from collections import Counter

# Analyze word frequency in a small text passage
text_passage = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text_passage.split()
word_counts = Counter(words)

# Find words that appear more than once
repeated_words = [word for word, count in word_counts.items() if count > 1]

# Use enumerate to process repeated words with their positions
enumerate_results = []
for index, word in enumerate(repeated_words):
    if index % 2 == 0:
        enumerate_results.append(len(word) + index)
    else:
        enumerate_results.append(len(word) - index)

final_count = sum(enumerate_results)
print(f"Result: {final_count}")