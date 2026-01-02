def analyze_text_composition(text):
    words = text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Distractor: character frequency map (not used later)
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Distractor: unused complexity score
    complexity_score = len(set(word_lengths)) * avg_length
    
    return {'avg_word_len': avg_length, 'word_count': len(words)}


def extract_sentiment_indicators(text):
    positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'horrible'}
    
    words = text.lower().split()
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    
    sentiment_balance = pos_count - neg_count
    sentiment_ratio = (pos_count + 1) / (neg_count + 1)  # Avoid division by zero
    
    # Dead code path - never used
    if sentiment_balance > 5:
        warning_flag = True
    else:
        warning_flag = False
    
    return {'balance': sentiment_balance, 'ratio': sentiment_ratio}

# Lambda function for dynamic weighting
weight_function = lambda x, base: round((x + 1) ** 0.8 * base, 3)

# Simulated data processing pipeline
document = "The excellent team delivered amazing results with great effort and wonderful planning."

analysis_metrics = analyze_text_composition(document)
sentiment_metrics = extract_sentiment_indicators(document)

# Combine metrics into unified structure
metrics = {
    'length': analysis_metrics['avg_word_len'],
    'volume': analysis_metrics['word_count'],
    'sentiment': sentiment_metrics['balance'],
    'positivity': sentiment_metrics['ratio']
}

# Weight configuration
base_weights = {'length': 0.2, 'volume': 0.3, 'sentiment': 0.4, 'positivity': 0.1}

# Apply dynamic weighting using lambda
weights = {k: weight_function(metrics[k], base_weights[k]) for k in base_weights}

# Intermediate calculation with distractor variables
total_influence = 0.0
effective_metrics = {}
for key in metrics:
    effective_value = metrics[key] * weights[key]
    effective_metrics[key] = round(effective_value, 4)
    total_influence += effective_value

# Red herring normalization (unused)
max_possible = sum(w * (20 if k != 'sentiment' else 10) for k, w in weights.items())
normalized_total = total_influence / max_possible if max_possible > 0 else 0

# Key logic chain
adjusted_volume = metrics['volume'] * weights['volume']
bias_correction = (metrics['length'] > 4.5) * 1.1  # Minor boost if words are longer

# Final performance evaluation
evaluate_performance = lambda m, w: (
    (m['sentiment'] * w['sentiment']) +
    (m['positivity'] * w['positivity'] * 2) +
    bias_correction * adjusted_volume
)

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")