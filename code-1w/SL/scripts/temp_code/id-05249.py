from collections import Counter

def analyze_text_patterns(text):
    char_count = Counter(text.lower())
    vowels = 'aeiou'
    vowel_freq = sum(char_count[char] for char in vowels if char in char_count)
    consonant_freq = len(text) - vowel_freq - text.count(' ')
    
    # Irrelevant distraction: counting special characters (minimal interference)
    special_chars = sum(1 for c in text if c not in 'abcdefghijklmnopqrstuvwxyz ')
    
    return vowel_freq, consonant_freq

def calculate_diversity_index(freq_tuple):
    vowel_freq, consonant_freq = freq_tuple
    if consonant_freq == 0:
        return 0.0
    diversity_index = round(vowel_freq / consonant_freq, 3) if vowel_freq > consonant_freq else round(consonant_freq / vowel_freq, 3)
    return diversity_index

def calculate_final_score(data):
    pattern_analysis = analyze_text_patterns(data)
    diversity_metric = calculate_diversity_index(pattern_analysis)
    base_score = len(data.split())  # Word count as base score
    adjustment = 1.5 if diversity_metric > 1.0 else 0.8
    final_score = int(base_score * diversity_metric * adjustment)
    return final_score

text_data = "Dynamic programming solves complex problems by breaking them into simpler subproblems."
final_score = calculate_final_score(text_data)
print(f"Result: {final_score}")