def analyze_sentiment(text_list):
    sentiment_scores = []
    for text in text_list:
        positive_words = len([w for w in text.split() if w.lower() in ['good', 'great', 'excellent', 'amazing']])
        negative_words = len([w for w in text.split() if w.lower() in ['bad', 'terrible', 'awful', 'poor']])
        net_score = positive_words - negative_words
        sentiment_scores.append(max(-1, min(1, net_score)))
    return sentiment_scores

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x - 5

# Another distraction: precompute meaningless stats
text_corpus = [
    "This product is amazing and excellent",
    "Terrible experience, very bad service",
    "It's okay, not great but not awful",
    "Absolutely poor quality, such a waste"
]

sentiments = analyze_sentiment(text_corpus)
word_count_stats = list(map(lambda t: len(t.split()), text_corpus))
avg_word_count = sum(word_count_stats) / len(word_count_stats)

# Misleading normalization factor (not used in final logic)
normalization_factor = max(word_count_stats) if word_count_stats else 1

# Real computation begins: weight adjustment based on position
def compute_final_score(data, weights):
    weighted_sum = 0
    temp_buffer = []
    
    for i, (val, w) in enumerate(zip(data, weights)):
        adjusted_w = w * (0.9 ** i)  # Exponential decay of weight importance
        contribution = val * adjusted_w
        temp_buffer.append(contribution)
        weighted_sum += contribution
    
    # Dummy tracking variables (distractors)
    total_contributions = len(temp_buffer)
    peak_contribution = max(temp_buffer) if temp_buffer else 0
    
    # Additional irrelevant calculation
    entropy_proxy = 0
    for x in temp_buffer:
        if x != 0:
            entropy_proxy -= x * __import__('math').log(abs(x))
    
    return round(weighted_sum, 4)

# Main data flow
raw_data = [50, 30, -20, 40]
weights = [0.1, 0.3, 0.5, 0.7]

# Preprocessing side track: scale data by average length (unused)
scaled_data = [x * avg_word_count / 10 for x in raw_data]

# Actual relevant assignment
data = [x + 10 for x in raw_data]  # Shift all values

# Final score computation
final_score = compute_final_score(data, weights)

print(f"Result: {final_score}")