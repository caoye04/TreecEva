def analyze_text_metrics(text_data):
    char_count = len(text_data)
    word_list = text_data.split()
    word_count = len(word_list)
    
    # Irrelevant statistic: average consonant count per word (not used later)
    vowels = 'aeiou'
    total_consonants = sum(len([c for c in word.lower() if c.isalpha() and c not in vowels]) for word in word_list)
    avg_consonants_per_word = total_consonants / word_count if word_count else 0
    
    # Frequency map of word lengths
    length_freq = {}
    for word in word_list:
        length = len(word)
        length_freq[length] = length_freq.get(length, 0) + 1
    
    # Use enumerate and zip: get weighted score based on position and length
    positional_length_bonus = sum(i * len(word) for i, word in enumerate(word_list))
    
    # Conditional expression: reward longer texts, cap at 1000
    size_bonus = 100 if char_count > 500 else (50 if char_count > 200 else 10)
    
    # Lambda function to compute redundancy penalty based on repeated word lengths
    max_freq = max(length_freq.values()) if length_freq else 1
    penalty_factor = lambda freq, max_f: 0.9 if freq / max_f > 0.7 else 1.0
    normalized_penalty = sum(penalty_factor(freq, max_freq) for freq in length_freq.values())
    
    # Real metric: content density score
    content_density = (word_count * 10 + char_count) / 100.0
    
    # Distractor: unused complexity involving sorted frequency items
    sorted_freq = sorted(length_freq.items(), key=lambda x: x[1], reverse=True)
    most_common_length = sorted_freq[0][0] if sorted_freq else 0
    high_freq_count = len([f for f in length_freq.values() if f == max_freq])
    
    # Final aggregation using only selected components
    base_score = content_density + positional_length_bonus
    adjusted_score = base_score * normalized_penalty  # Apply uniform penalty
    final_score = adjusted_score + size_bonus  # Add bonus
    
    return final_score

# Simulated document input
document = "The algorithm processes data efficiently using advanced techniques. Performance improves with optimized logic and careful analysis. Redundant patterns should be minimized."

result = analyze_text_metrics(document)
final_score = round(result, 2)
print(f"Result: {final_score}")