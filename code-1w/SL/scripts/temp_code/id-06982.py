def analyze_sentiment(texts):
    sentiments = []
    for i, text in enumerate(texts):
        char_count = len(text.strip())
        word_count = len(text.split())
        avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0
        
        # Distractor computation: not used later
        uppercase_ratio = sum(1 for c in text if c.isupper()) / len(text) if len(text) > 0 else 0
        
        sentiment_score = (avg_word_length * 1.5) + (1 if '!' in text else 0) * 2
        sentiments.append(sentiment_score)
    return sentiments

# Simulate feedback processing with mixed data types
raw_feedback = [
    "Great service!",
    "  Poor quality  ",
    "Excellent and fast!",
    "Not good.",
    "Outstanding performance!!!"
]

# Preprocessing with slicing and string methods
cleaned = [f.lower().strip("!. ") for f in raw_feedback]
sentiment_values = analyze_sentiment(raw_feedback)

# Weight configuration (some are red herrings)
weights = {
    'relevance': 0.4,
    'tone': 0.35,
    'clarity': 0.25,
    'length_penalty': 0.1  # unused distractor
}

# Additional distraction: irrelevant dictionary mapping
feedback_stats = {}
for idx, txt in enumerate(cleaned):
    feedback_stats[f'entry_{idx}'] = {
        'chars': len(txt),
        'syllables_approx': sum(1 for c in txt if c in 'aeiou'),
        'has_repeat_vowels': any(txt[i] == txt[i+1] for i in range(len(txt)-1) if txt[i] in 'aeiou')
    }

# Real computation begins: zipping sentiment with artificial relevance scores
relevance_scores = [0.9, 0.4, 0.95, 0.3, 0.8]
combined = list(zip(sentiment_values, relevance_scores))

# State tracking with intermediate variables
aggregated = 0
normalization_factor = 0

for s_val, r_score in combined:
    weighted_sentiment = s_val * weights['tone']
    relevance_contribution = r_score * weights['relevance']
    
    # Use bitwise to mask every other entry (artificial logic)
    entry_index = combined.index((s_val, r_score))
    if entry_index & 1:  # XOR pattern via bitwise AND with 1
        weighted_sentiment *= 0.9  # slight reduction
    
    total_component = weighted_sentiment + relevance_contribution
    aggregated += total_component
    normalization_factor += 1

# Final aggregation using distractor-free subset of logic
def aggregate_performance(data, w):
    base = aggregated / normalization_factor if normalization_factor > 0 else 0
    clarity_boost = weights['clarity'] * 10  # constant boost factor
    return int(base * 10 + clarity_boost)  # scale and discretize

final_score = aggregate_performance(feedback_data=None, weights=weights)
print(f"Result: {final_score}")