import re
from collections import defaultdict

document = "The quick brown fox jumps over the lazy dog. The dog was really lazy."
stop_words = {'the', 'over', 'was', 'really'}

# Tokenize and normalize
tokens = re.findall(r'\b\w+\b', document.lower())

# Filter out stop words
filtered_tokens = [word for word in tokens if word not in stop_words]

# Count frequencies using defaultdict
freq_map = defaultdict(int)
for word in filtered_tokens:
    freq_map[word] += 1

# Create a dictionary of words with frequency 1 using dictionary comprehension
single_occurrence = {word: count for word, count in freq_map.items() if count == 1}

# Count unique words that occur exactly once
unique_word_count = len(single_occurrence)

print(f"Result: {unique_word_count}")