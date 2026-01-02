from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

def analyze_text_pattern(text):
    char_counts = Counter(text)
    filtered_chars = {k: v for k, v in char_counts.items() if k.isalpha()}
    normalized_counts = {k.lower(): v for k, v in filtered_chars.items()}
    frequency_map = Counter(normalized_counts)
    
    # Irrelevant distraction: character length tracking (minimal interference)
    unused_length_metric = sum(1 for c in text if c.isupper())
    
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

text_corpus = "MachineLearningModelsOftenRelyOnDataDistribution"
total_entropy = analyze_text_pattern(text_corpus)
print(f"Result: {total_entropy}")