from collections import Counter

def analyze_text_dominance(text_a, text_b):
    count_a = Counter(text_a.lower())
    count_b = Counter(text_b.lower())
    
    # Compute absolute frequency differences for shared characters
    all_chars = set(count_a.keys()).union(set(count_b.keys()))
    frequency_diff = {}
    
    for char in all_chars:
        freq_a = count_a.get(char, 0)
        freq_b = count_b.get(char, 0)
        frequency_diff[char] = abs(freq_a - freq_b)
    
    # Irrelevant distraction: unused variable (minimal interference)
    total_chars = len(text_a) + len(text_b)
    
    dominance_score = max(frequency_diff.values()) - min(frequency_diff.values())
    return dominance_score

result = analyze_text_dominance("algorithm", "logarithm")
print(f"Target result: {result}")