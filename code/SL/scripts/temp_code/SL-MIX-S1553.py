import re
from functools import lru_cache

def tokenize(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())

def is_valid_pattern(words, index=0):
    if index >= len(words):
        return True
    if words[index] in {'the', 'a', 'an'}:
        return is_valid_pattern(words, index + 2) if index + 1 < len(words) else False
    return is_valid_pattern(words, index + 1)

@lru_cache(maxsize=None)
def calculate_structure_score(word_tuple):
    if not word_tuple:
        return 0
    first_char_hash = hash(word_tuple[0][0]) % 100
    rest_score = calculate_structure_score(word_tuple[1:])
    return first_char_hash + rest_score if first_char_hash % 2 == 0 else rest_score - first_char_hash

sentence = "The quick brown fox jumps over the lazy dog"
word_sequence = tuple(tokenize(sentence))
valid_structure = is_valid_pattern(list(word_sequence))
linguistic_score = calculate_structure_score(word_sequence) if valid_structure else -1
print(f"Result: {linguistic_score}")