def analyze_text_metrics(text_data):
    char_count = len(text_data)
    word_list = text_data.split()
    word_count = len(word_list)
    upper_case_count = sum(1 for c in text_data if c.isupper())
    digit_count = sum(1 for c in text_data if c.isdigit())
    
    # Distractor: irrelevant frequency analysis
    freq_map = {}
    for c in text_data:
        freq_map[c] = freq_map.get(c, 0) + 1
    
    # Semi-relevant transformation (not used later but looks important)
    reversed_words = [word[::-1] for word in word_list]
    palindrome_count = sum(1 for word in word_list if word == word[::-1])

    # Key metrics for scoring
    unique_words = len(set(w.lower() for w in word_list))
    avg_word_length = sum(len(w) for w in word_list) / word_count if word_count > 0 else 0

    # Dummy threshold checks that don't affect final logic
    has_long_words = any(len(w) > 8 for w in word_list)
    has_special_chars = any(not c.isalnum() and not c.isspace() for c in text_data)

    return {
        'char_count': char_count,
        'word_count': word_count,
        'unique_words': unique_words,
        'avg_word_length': round(avg_word_length, 3),
        'palindrome_count': palindrome_count,
        'digit_count': digit_count
    }


def evaluate_performance(data_str, threshold=5):
    metrics = analyze_text_metrics(data_str)
    
    # Intermediate derived values
    base_score = metrics['unique_words'] * 2
    length_bonus = 10 if metrics['char_count'] > 100 else 5
    
    # Conditional expression (required python feature)
    complexity_factor = 1.5 if metrics['avg_word_length'] > 4.5 else 1.0
    
    # Another conditional expression based on palindromes
    palindrome_impact = -3 if metrics['palindrome_count'] > 0 else 0

    # Distractor computation: unused linguistic score
    linguistic_richness = (metrics['unique_words'] / metrics['word_count']) * 100 if metrics['word_count'] > 0 else 0
    normalized_richness = max(0, min(linguistic_richness, 100))

    # Core calculation chain
    raw_score = base_score + length_bonus
    adjusted_score = raw_score * complexity_factor
    final_score = int(adjusted_score + palindrome_impact)
    
    # Early termination condition that may or may not trigger (but won't here)
    if metrics['digit_count'] > 20:
        return -1
    
    return final_score

# Main execution
input_text = "The ReFeReNCe strinG conta1ns MIXED case and 7 digits with level eveL radar racecar"
result_metrics = analyze_text_metrics(input_text)
final_score = evaluate_performance(input_text, threshold=6)
print(f"Target result: {final_score}")