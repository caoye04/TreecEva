def analyze_text_patterns(input_texts):
    char_frequencies = {}
    total_chars = 0
    uppercase_count = 0

    for text in input_texts:
        temp_upper = 0
        for char in text:
            if char.isalpha():
                total_chars += 1
                key = char.lower()
                char_frequencies[key] = char_frequencies.get(key, 0) + 1
            if char.isupper():
                temp_upper += 1
                uppercase_count += 1
        
        # Distractor: irrelevant smoothing logic
        if temp_upper > len(text) / 2:
            smoothed_value = sum(char_frequencies.values()) * 0.95

    avg_length = sum(len(t) for t in input_texts) / len(input_texts) if input_texts else 0

    # Distractor: dead code path (never executed due to condition)
    special_factor = 0
    if False and avg_length > 10:
        special_factor = 1000

    return char_frequencies, total_chars, uppercase_count, avg_length


def rank_characters(freq_dict, threshold=2):
    ranked = []
    for char, count in freq_dict.items():
        if count >= threshold:
            score = count * (ord(char) - 96)  # a=1, b=2, etc.
            ranked.append((char, score))
    
    # Use of enumerate and conditional expression
    ranked_with_index = [(i, item[0], 'high' if item[1] > 10 else 'low') 
                         for i, item in enumerate(ranked)]
    
    # Distractor: unused sorting
    ranked.sort(key=lambda x: x[1], reverse=True)
    
    return [r[1] for r in ranked]  # return only scores


def calculate_diversity_metric(frequencies, total):
    if total == 0:
        return 0.0
    
    unique_letters = len(frequencies)
    entropy = 0.0
    for count in frequencies.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log(p)
    
    # Irrelevant intermediate calculation
    max_freq = max(frequencies.values())
    redundancy_penalty = (max_freq / total) * 0.1
    
    return round(entropy - redundancy_penalty, 4)


def calculate_final_score(data_tuple):
    frequencies, total_chars, upper_count, avg_len = data_tuple
    raw_scores = rank_characters(frequencies, threshold=1)
    
    base_score = sum(raw_scores)
    diversity_bonus = calculate_diversity_metric(frequencies, total_chars)
    
    # Conditional expression with distractor variables
    adjustment = 1.1 if avg_len > 5 else 0.9
    
    # Key logic step
    normalized_upper = upper_count / total_chars if total_chars > 0 else 0
    case_penalty = 5 if normalized_upper > 0.3 else 0
    
    # Final computation
    final_score = (base_score + diversity_bonus * 100) * adjustment - case_penalty
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    sample_texts = [
        "Hello World",
        "Python Code",
        "Statement Level Reasoning"
    ]
    
    # Intermediate processing with distractor variables
    processed_result = analyze_text_patterns(sample_texts)
    frequency_map = processed_result[0]
    total_character_count = processed_result[1]
    
    # Unused variable - red herring
    ignored_summary = {
        'texts_processed': len(sample_texts),
        'total_upper': processed_result[2],
        'average_len': processed_result[3]
    }
    
    # Key statement
    final_score = calculate_final_score(processed_result)