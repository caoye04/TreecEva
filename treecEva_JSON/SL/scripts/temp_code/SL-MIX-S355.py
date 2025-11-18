from collections import defaultdict
from functools import reduce

def count_vowels(word):
    return sum(1 for char in word.lower() if char in 'aeiou')

def calculate_word_score(word):
    vowel_count = count_vowels(word)
    length = len(word)
    if length == 0:
        return 0
    # Recursive component for compound words with hyphens
    if '-' in word:
        parts = word.split('-')
        return sum(calculate_word_score(part) for part in parts)
    # Base scoring logic
    base_score = length * (vowel_count + 1)
    return base_score if vowel_count > 0 else length

def process_text_corpus(corpus):
    word_scores = defaultdict(int)
    for sentence in corpus:
        words = sentence.split()
        for word in words:
            score = calculate_word_score(word)
            # Logical operations to filter and accumulate scores
            if len(word) >= 4 and count_vowels(word) > 1:
                word_scores[word] += score
            elif not (len(word) < 3 or count_vowels(word) == 0):
                word_scores[word] += score // 2
    return word_scores

def compute_final_score(score_dict):
    # Using functional programming to aggregate scores
    high_scores = list(filter(lambda x: x > 10, score_dict.values()))
    if not high_scores:
        return 0
    # Apply reduction with a multiplier based on count of high scores
    multiplier = 2 if len(high_scores) > 3 else 1
    return reduce(lambda a, b: a + b, high_scores, 0) * multiplier

text_corpus = [
    "The quick brown fox jumps over the lazy dog",
    "Python programming language has powerful features",
    "Recursive functions can be challenging to master",
    "Data structures and algorithms are fundamental",
    "Natural language processing requires understanding"
]

processed_scores = process_text_corpus(text_corpus)
final_score = compute_final_score(processed_scores)
print(f"Result: {final_score}")