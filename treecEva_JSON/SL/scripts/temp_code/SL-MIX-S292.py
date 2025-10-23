import math
from functools import reduce

def tokenize_sentences(text):
    return [sentence.strip() for sentence in text.split('.') if sentence.strip()]

def calculate_length_variance(sentences):
    lengths = [len(sentence.split()) for sentence in sentences]
    mean_length = sum(lengths) / len(lengths)
    variance = sum((x - mean_length) ** 2 for x in lengths) / len(lengths)
    return variance

def vocabulary_richness(words):
    unique_words = set(words)
    return len(unique_words) / len(words) if words else 0

corpus = "Advanced computational algorithms require precise implementation. These systems often involve complex data structures. Efficient processing demands optimized code execution. Mathematical models guide software development. Robust frameworks ensure reliable performance."

sentences = tokenize_sentences(corpus)
words = [word for sentence in sentences for word in sentence.split()]

length_variance = calculate_length_variance(sentences)
vocab_diversity = vocabulary_richness(words)

complexity_base = length_variance * 10 + vocab_diversity * 100
sentence_count = len(sentences)
word_count = len(words)

adjustment_factor = 1.5 if sentence_count > 3 else 0.8
adjusted_complexity = complexity_base * adjustment_factor

log_transform = math.log(adjusted_complexity + 1)
exp_modifier = math.exp(log_transform * 0.1)

scores = [adjusted_complexity, log_transform, exp_modifier]
mean_score = reduce(lambda a, b: a + b, scores) / len(scores)

normalized_score = round((mean_score - min(scores)) / (max(scores) - min(scores)) * 100) if max(scores) != min(scores) else 0

print(f"Result: {normalized_score}")