from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def analyze_text_pattern(text):
    # Normalize text and count character frequencies
    cleaned = ''.join(ch.lower() for ch in text if ch.isalpha())
    frequency_map = Counter(cleaned)
    
    # Calculate entropy as a measure of letter distribution uniformity
    total_entropy = calculate_entropy(frequency_map)
    
    # Auxiliary metric: redundancy (not used in final result)
    unique_chars = len(frequency_map)
    redundancy = 1 - (total_entropy / math.log2(len(cleaned))) if len(cleaned) > 1 else 0
    
    # Return only entropy for this task
    return total_entropy

text_sample = "The quick brown fox jumps over the lazy dog"
total_entropy = analyze_text_pattern(text_sample)
print(f"Result: {total_entropy}")