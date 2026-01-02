def analyze_sentiment(texts):
    positive_keywords = ['excellent', 'great', 'outstanding', 'good', 'well']
    negative_keywords = ['poor', 'bad', 'terrible', 'awful', 'weak']
    scores = []
    for text in texts:
        lower_text = text.lower()
        pos_count = sum(1 for word in positive_keywords if word in lower_text)
        neg_count = sum(1 for word in negative_keywords if word in lower_text)
        score = pos_count - neg_count
        scores.append(score)
    return scores

feedback = [
    "The model performed excellently on all tasks.",
    "Poor reasoning and bad logic flow.",
    "Great job overall, well done!",
    "Outstanding work with excellent attention to detail."
]

sentiment_scores = analyze_sentiment(feedback)

# Irrelevant transformation (distractor)
word_lengths = [len(text.split()) for text in feedback]
avg_word_length = sum(word_lengths) / len(word_lengths)

# Dummy normalization (not used later)
normalized_scores = [round(s * 1.5, 2) for s in sentiment_scores]

threshold = 1

# Misleading filtering based on string patterns
long_feedback_mask = [len(f) > 40 for f in feedback]
filtered_indices = [i for i, mask in enumerate(long_feedback_mask) if mask]

# Actual evaluation logic
def evaluate_performance(scores, min_threshold):
    adjusted = [max(s, 0) for s in scores]  # Only positive contributions
    bonus = 0
    for s in scores:
        if s >= min_threshold:
            bonus += 2
    base_total = sum(adjusted)
    final_value = base_total + bonus
    
    # Dead code branch (distractor)
    if False:
        correction = len(scores) // 2
        final_value -= correction
    
    return int(final_value)

# Key statement
final_score = evaluate_performance(sentiment_scores, threshold)

# Additional irrelevant computation
char_count_map = {i: sum(1 for c in fb if c.isalpha()) for i, fb in enumerate(feedback)}
total_chars = sum(char_count_map.values())

# Print required output
print(f"Result: {final_score}")