import re
from collections import defaultdict
from statistics import mean

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

corpus_text = "The quick brown fox jumps over the lazy dog while the dog sleeps peacefully"
stops = frozenset(['the', 'over', 'while', 'sleeps'])

words = tokenize(corpus_text)
filtered_words = [word for word in words if word not in stops]
word_lengths = list(map(len, filtered_words))
length_frequency = defaultdict(int)

for length in word_lengths:
    length_frequency[length] += 1

unique_lengths = set(length_frequency.keys())
max_freq = max(length_frequency.values())
common_lengths = {k for k, v in length_frequency.items() if v == max_freq}
avg_length = mean(word_lengths)

lexical_density_score = int(avg_length * len(common_lengths) + sum(unique_lengths))
print(f"Result: {lexical_density_score}")