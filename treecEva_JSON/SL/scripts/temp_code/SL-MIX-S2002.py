from functools import reduce
from collections import namedtuple

def transform_word(word, depth=0):
    if len(word) <= 1:
        return word
    mid = len(word) // 2
    left = transform_word(word[:mid], depth + 1)
    right = transform_word(word[mid:], depth + 1)
    return right + left  # Swap halves recursively

def tokenize_and_process(text):
    tokens = text.split()
    transformed_tokens = list(map(transform_word, tokens))
    return transformed_tokens

def count_pattern_occurrences(tokens, pattern):
    count = 0
    for token in tokens:
        count += token.count(pattern)
    return count

class AnalysisResult:
    def __init__(self, score):
        self.score = score

# Ciphered input message
message = "enigma mystery riddle puzzle"

# Process the message
processed_tokens = tokenize_and_process(message)

# Count occurrences of specific letter combinations
pattern_count_a = count_pattern_occurrences(processed_tokens, 'l')
pattern_count_b = count_pattern_occurrences(processed_tokens, 'e')

# Calculate weighted score using functional approach
weights = [2, 3]
scores = [pattern_count_a, pattern_count_b]
weighted_sum = reduce(lambda acc, pair: acc + pair[0] * pair[1], zip(scores, weights), 0)

# Apply final transformation
final_score = weighted_sum * len(processed_tokens) + sum(map(len, processed_tokens))

print(f"Result: {final_score}")