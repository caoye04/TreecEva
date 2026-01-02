from collections import defaultdict, Counter

def analyze_text_patterns(text):
    # Irrelevant frequency tracking (distractor)
    char_freq = defaultdict(int)
    for char in text:
        char_freq[char] += 1

    # Semi-relevant preprocessing
    words = text.lower().split()
    word_lengths = [len(word.strip('.,!?')) for word in words]

    # Use of set operations to filter unique length words
    unique_lengths = set(word_lengths)
    filtered_words = [w for w in words if len(w.strip('.,!?')) in unique_lengths and len(w) > 2]

    # Misleading statistical computation
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    length_variance = sum((x - avg_length) ** 2 for x in word_lengths) / len(word_lengths) if word_lengths else 0

    # Core logic disguised among distractions
    long_words = [w for w in filtered_words if len(w) > 5]
    duplicate_count = sum(Counter(filtered_words).values()) - len(Counter(filtered_words))

    return long_words, duplicate_count, avg_length

def calculate_final_score(input_text, bonus_factor=1.5):
    # Intermediate variables with partial relevance
    processed = input_text.replace('-', ' ').replace(',', ' ')
    tokens = processed.split()
    token_counter = Counter(tokens)

    # Dead code path (never executed due to condition)
    rare_words = []
    if len(tokens) > 1000:
        rare_words = [w for w, c in token_counter.items() if c == 1]

    # Nested logic with meaningful and irrelevant parts
    base_score = 0
    adjustments = defaultdict(float)
    for i, token in enumerate(tokens):
        if i % 3 == 0 and len(token) > 2:
            base_score += len(token)
            adjustments['length_bonus'] += 0.5
        if token.isupper() and any(c.isalpha() for c in token):
            adjustments['shout_penalty'] -= 0.3

    # Complex but partially redundant validation
    valid_tokens = [t for t in tokens if t.isalnum() or t in ['_', '-']]
    validity_ratio = len(valid_tokens) / len(tokens) if tokens else 0

    # Key computation mixed with noise
    pattern_result = analyze_text_patterns(input_text)
    long_word_score = len(pattern_result[0]) * 2
    repetition_penalty = pattern_result[1] * -0.4
    stability_metric = 1.0 if pattern_result[2] < 5.0 else 0.8

    # Final aggregation with distractor terms that cancel out
    dummy_offset = sum(1 for t in tokens if t.startswith('a')) * 0
    phantom_boost = len([t for t in tokens if t.endswith('z')]) * 0.0  # dead contribution

    final_score = (
        base_score + 
        long_word_score + 
        repetition_penalty + 
        bonus_factor + 
        sum(adjustments.values()) + 
        (stability_metric * 2) +
        dummy_offset + 
        phantom_boost
    )
    
    return int(round(final_score))

# Main execution
input_str = "The quick brown fox jumps over the lazy dog repeatedly. Very QUICK and BOLD moves! Fox fox action." \
             "JUMPS happened thrice. Lazy days, zany days, always crazy."

result = calculate_final_score(input_str, bonus_factor=2.0)
print(f"Target result: {result}")