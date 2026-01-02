def analyze_text_patterns(text_data):
    # Distractor: Text analysis that isn't directly related to final score
    char_count = len(text_data)
    word_list = text_data.split()
    avg_word_length = sum(len(word) for word in word_list) / len(word_list) if word_list else 0
    palindrome_count = sum(1 for word in word_list if word == word[::-1])
    
    # Irrelevant transformation
    encoded = ''.join([chr(ord(c) + 1) for c in text_data[:10]]) if text_data else ''

    # Red herring: complex but unused calculation
    entropy = 0
    from math import log2
    for c in set(text_data):
        p = text_data.count(c) / len(text_data)
        entropy -= p * log2(p) if p > 0 else 0

    # Unused recursive function (decoy)
    def get_depth(s):
        return 1 + get_depth(s[1:-1]) if len(s) > 2 else 0
    
    nesting_depth = get_depth(text_data) if text_data else 0

    # Actual relevant metric extraction (buried in distractors)
    vowel_ratio = sum(1 for c in text_data.lower() if c in 'aeiou') / len(text_data) if text_data else 0
    
    # Return only what's needed later
    return {'vowel_ratio': vowel_ratio, 'length': len(text_data)}


def transform_metrics(raw):
    # Another layer of distraction
    if not raw:
        return {'processed': 0}
    
    # Some irrelevant list operations
    temp_array = [i for i in range(int(raw['length'])) if i % 7 == 0]
    shifted = [(x << 2) ^ 5 for x in temp_array]
    
    # Dead code path
    if len(temp_array) > 100:
        return {'overflow': True}
    
    # Real transformation
    normalized_vowels = round(raw['vowel_ratio'] * 100, 3)
    size_class = 3 if raw['length'] > 50 else (2 if raw['length'] > 20 else 1)
    
    # This is actually used later
    return {
        'norm_vowels': normalized_vowels,
        'size_rating': size_class,
        'complexity_proxy': normalized_vowels * size_class
    }


def calculate_weights(factor_set):
    # Weight calculation with distractions
    base_factors = ['norm_vowels', 'size_rating']
    extra_noise = [x**2 for x in range(15) if x % 3 == 0]
    
    # Fake weight mapping
    decoy_weights = {f'f{x}': (x*2.5) for x in range(8)}
    
    # The actual weights used in computation
    real_weights = {
        'norm_vowels': 0.65,
        'size_rating': 0.35
    }
    
    # Misleading intermediate
    weighted_sum = sum(factor_set.get(f, 0) * decoy_weights[f'f{i}'] for i, f in enumerate(base_factors) if f in factor_set)
    
    # But we return the correct ones
    return real_weights


def evaluate_performance(metrics, weights):
    # Core logic buried under noise
    initial_check = metrics.get('complexity_proxy', 0) > 10
    fallback_value = 42
    
    # Multiple conditionals as red herrings
    if metrics.get('norm_vowels', 0) < 5:
        if metrics.get('size_rating', 0) == 1:
            fallback_value = 15
    elif len([x for x in weights.values() if x > 0.5]) == 2:
        fallback_value = 75
    else:
        fallback_value = 30

    # Actual calculation (hard to trace due to surrounding noise)
    score = 0
    for key, weight in weights.items():
        if key in metrics:
            score += metrics[key] * weight * 10  # Scaling factor hidden here
    
    # Final adjustment
    final_adjusted = int(round(score)) + (5 if initial_check else 0)
    
    return final_adjusted

# Main execution flow
raw_text = "Intelligence requires reasoning, memory, and linguistic pattern recognition."

# Step 1: Extract features from text (looks like NLP but used numerically)
data_metrics = analyze_text_patterns(raw_text)

# Step 2: Transform into evaluation metrics
processed_metrics = transform_metrics(data_metrics)

# Step 3: Generate weighting schema
weights = calculate_weights(processed_metrics)

# Key statement: compute final score
final_score = evaluate_performance(processed_metrics, weights)

print(f"Result: {final_score}")