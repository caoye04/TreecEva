import math
import statistics
from itertools import combinations

def tokenize(sentence):
    return [word.strip('.,!?;') for word in sentence.split()]

def word_entropy_frequency(words):
    unique_words = set(words)
    freq_dict = {word: words.count(word) for word in unique_words}
    frequencies = list(freq_dict.values())
    return statistics.variance(frequencies) if len(frequencies) > 1 else 0

class TextProcessor:
    def __init__(self, text):
        self.tokens = tokenize(text)
        self.entropy = word_entropy_frequency(self.tokens)
    
    @property
    def combinatorial_density(self):
        if len(self.tokens) < 3:
            return 0
        return len(list(combinations(self.tokens, 3)))

sample_text = "The quick brown fox jumps over the lazy dog. The dog was really lazy and very sleepy."

processor = TextProcessor(sample_text)
encoded_values = {word: sum(ord(c) for c in word) for word in processor.tokens}
filtered_values = {k: v for k, v in encoded_values.items() if v % 2 == 0}

partition_point = len(filtered_values) // 2
left_partition = dict(list(filtered_values.items())[:partition_point])
right_partition = dict(list(filtered_values.items())[partition_point:])

merged_dict = {**left_partition, **right_partition}
if 'lazy' in merged_dict:
    merged_dict['lazy'] *= 2

linguistic_score = int(sum(merged_dict.values()) * processor.entropy * processor.combinatorial_density)
print(f"Result: {linguistic_score}")