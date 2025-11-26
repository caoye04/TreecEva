from collections import Counter

text_corpus = "python programming language data analysis machine learning"
words = text_corpus.split()
word_counts = Counter(words)

# Process the word frequency data
unique_words = len(word_counts)
total_words = len(words)

# Calculate final score
final_score = sum(word_counts.values())
print(f"Result: {final_score}")