import itertools
from collections import defaultdict

def tokenize_sentences(document):
    return [sentence.strip() for sentence in document.split('.') if sentence]

def calculate_word_stats(words):
    length_sum = 0
    char_set = set()
    for word in words:
        length_sum += len(word)
        char_set.update(word.lower())
    return length_sum, len(char_set)

def compute_complexity(sentences):
    stats = []
    for sentence in sentences:
        words = sentence.split()
        if not words:
            continue
        length_sum, unique_chars = calculate_word_stats(words)
        avg_length = length_sum / len(words)
        diversity_ratio = unique_chars / 26.0
        stats.append((avg_length, diversity_ratio))
    
    if not stats:
        return 0
    
    total_avg = sum(s[0] for s in stats) / len(stats)
    total_diversity = sum(s[1] for s in stats) / len(stats)
    
    return round(total_avg * total_diversity * 100)

def process_document(document):
    sentences = tokenize_sentences(document)
    if not sentences:
        return 0
    
    complexity_scores = []
    for i in range(min(3, len(sentences))):  # Process up to 3 sentences
        subset = sentences[i:]
        score = compute_complexity(subset)
        complexity_scores.append(score)
        if score > 50:  # Early termination condition
            break
    
    if not complexity_scores:
        return 0
    
    # Calculate final score using weighted average
    weights = [3, 2, 1][:len(complexity_scores)]
    weighted_sum = sum(score * weight for score, weight in zip(complexity_scores, weights))
    total_weight = sum(weights)
    
    return round(weighted_sum / total_weight)

document = "The quick brown fox jumps over the lazy dog. Python programming is fun and versatile. Natural language processing opens new possibilities."
sentences = tokenize_sentences(document)
complexity_score = compute_complexity(sentences[:2])
if complexity_score > 40:
    final_score = process_document(document)
else:
    final_score = complexity_score + 10

print(f"Result: {final_score}")