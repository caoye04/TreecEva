def preprocess_text(raw_input):
    cleaned = raw_input.strip().lower()
    tokenized = cleaned.split()
    word_count = len(tokenized)
    char_freq = {}
    for char in cleaned:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Distractor: unused statistical computation
    avg_word_length = sum(len(word) for word in tokenized) / word_count if word_count else 0
    entropy_proxy = sum(f * f for f in char_freq.values())  # Not actually used

    return {'words': tokenized, 'freq': char_freq, 'total_chars': len(cleaned)}


def analyze_sentiment(tokens):
    positive_words = {'good', 'great', 'excellent', 'amazing', 'awesome', 'outstanding'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'horrible'}
    score = 0
    for word in tokens:
        word_clean = word.strip('.,!?:;')
        if word_clean in positive_words:
            score += 1
        elif word_clean in negative_words:
            score -= 2
    return score


def compute_diversity_metric(freq_dict):
    unique_chars = len(freq_dict)
    total = sum(freq_dict.values())
    if total == 0:
        return 0.0
    # Shannon entropy approximation (not directly used in final logic path)
    import math
    diversity = -sum((count/total) * math.log(count/total) for count in freq_dict.values() if count > 0)
    normalized_diversity = diversity / math.log(26) if diversity > 0 else 0
    return round(normalized_diversity, 4)


def calculate_final_score(data):
    base_score = len(data['words'])
    frequency_bonus = sum(1 for count in data['freq'].values() if count > 2)
    sentiment_modifier = analyze_sentiment(data['words'])
    
    # Dummy nested structure with red herring computations
    temp_result = 0
    for i in range(2):
        for j in range(3):
            temp_result += i * j
    # temp_result is computed but irrelevant
    
    # Actual key calculation
    diversity_score = compute_diversity_metric(data['freq'])
    adjustment_factor = 1 + (diversity_score * 0.5)
    
    intermediate = base_score * adjustment_factor + frequency_bonus
    final_score = int(intermediate) + sentiment_modifier
    
    # Additional distraction: dead code path
    if False:
        debug_log = {'intermediate': intermediate, 'temp': temp_result}
    
    return final_score

# Main execution
raw_text = "Amazing good great excellent work! Truly outstanding and amazing effort in every aspect."
processed_data = preprocess_text(raw_text)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")