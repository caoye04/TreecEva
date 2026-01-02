def analyze_text_quality(text):
    if not text:
        return 0
    words = text.split()
    word_length_sum = sum(len(word.strip('.,!?"')) for word in words)
    avg_word_length = word_length_sum / len(words) if words else 0
    
    # Distractor: sentence analysis (not directly used)
    sentences = text.split('.')
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    complexity_proxy = avg_word_length * avg_sentence_length

    # Relevance metric based on character diversity
    unique_chars = len(set(text.lower()))
    char_diversity_ratio = unique_chars / len(text) if text else 0

    # Intermediate score with multiple factors
    lexical_score = (avg_word_length * 10) + (char_diversity_ratio * 100)
    return round(lexical_score, 2)


def validate_and_transform(entries):
    cleaned = []
    invalid_count = 0
    for entry in entries:
        stripped = entry.strip()
        if stripped.islower() and stripped.isalpha():
            cleaned.append(stripped[::-1])  # reverse valid lowercase alphabetic strings
        elif stripped.replace(' ', '').isalpha():
            cleaned.append(stripped.title())
        else:
            invalid_count += 1
    # Distractor: transformation log
    transform_log = {'original_count': len(entries), 'cleaned_count': len(cleaned), 'invalid': invalid_count}
    return cleaned


def calculate_final_score(data_list):
    raw_scores = []n    temp_adjustment = 0
    
    for item in data_list:
        base_score = len(item) * 0.5
        vowel_count = sum(1 for c in item if c in 'aeiou')
        vowel_bonus = vowel_count * 1.2
        
        # String method usage: counting uppercase as distraction
        uppercase_penalty = sum(1 for c in item if c.isupper()) * 0.3
        
        # Actual scoring component
        normalized_score = (base_score + vowel_bonus - uppercase_penalty) * (1 + item.count('e') * 0.05)
        raw_scores.append(normalized_score)
        
        # Distractor: running adjustment not used later
        temp_adjustment += len(item) % 3
    
    # Final aggregation logic
    mean_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    peak_score = max(raw_scores) if raw_scores else 0
    final_score = int(mean_raw + (peak_score * 0.1))  # deterministic integer result
    
    # Dead code path (never executed under current logic)
    if temp_adjustment > 100:
        final_score -= 5
        
    return final_score

# Main execution
raw_input_data = [
    "hello world programming test",
    "algorithmic thinking required here",
    "data processing evaluation",
    "reasoning capability benchmark"
]

# Preprocessing phase with string manipulation
processed_texts = validate_and_transform(raw_input_data)

# Extract key features using text analysis
processed_data = [analyze_text_quality(txt) for txt in processed_texts]

# Introduce distractor variable
auxiliary_metrics = [txt.upper().replace(' ', '_') for txt in processed_texts]

# Key computation step
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")