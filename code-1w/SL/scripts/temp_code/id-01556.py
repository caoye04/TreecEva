from collections import defaultdict, Counter

def analyze_frequencies(text_list):
    char_freq = defaultdict(int)
    total_chars = 0
    for text in text_list:
        for char in text.lower():
            if char.isalpha():
                char_freq[char] += 1
                total_chars += 1
    return char_freq, total_chars

def compute_redundancy_score(freq_dict, threshold=2):
    redundant_count = 0
    for count in freq_dict.values():
        if count > threshold:
            redundant_count += 1
    return redundant_count

def normalize_scores(raw_scores, multiplier=1.0):
    normalized = {}
    sum_vals = sum(raw_scores.values())
    for k, v in raw_scores.items():
        normalized[k] = (v / sum_vals) * multiplier if sum_vals != 0 else 0
    return normalized

def calculate_final_score(data):
    score = 0
    temp_result = []
    for item in data:
        if len(item) % 2 == 0:
            score += 3
        else:
            score -= 1
        temp_result.append(len(item))
    
    # Irrelevant aggregation
    avg_len = sum(temp_result) / len(temp_result) if temp_result else 0
    length_penalty = 0
    if avg_len < 4:
        length_penalty = -2
    
    # Actual contribution to score
    unique_lengths = set(temp_result)
    diversity_bonus = len(unique_lengths) * 1.5
    
    # Dummy computation with string methods
    joined = ''.join(data).lower()
    vowel_count = sum(joined.count(v) for v in 'aeiou')
    consonant_count = len(joined) - vowel_count
    ratio_metric = vowel_count / consonant_count if consonant_count != 0 else 0
    
    # Final calculation
    final_score = score + diversity_bonus + length_penalty
    return round(final_score, 4)

data_input = ["hello", "world", "test", "ai", "benchmark", "py"]

# Preprocessing steps
freq_analysis, total_char_count = analyze_frequencies(data_input)
normalized_freq = normalize_scores(freq_analysis)
redundancy = compute_redundancy_score(freq_analysis, threshold=3)
processed_data = [s.upper().strip() for s in data_input]

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")