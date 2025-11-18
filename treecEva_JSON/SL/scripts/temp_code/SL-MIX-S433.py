from collections import Counter

document = "Hello world hello world hello"
tokens = document.lower().split()
word_counts = Counter(tokens)
unique_words = len(word_counts)
most_frequent_count = max(word_counts.values())
metric = unique_words * most_frequent_count
print(f'Result: {metric}')