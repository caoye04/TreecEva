from collections import Counter

def analyze_sentiment(text):
    positive_words = {'great', 'good', 'excellent', 'amazing', 'wonderful'}
    negative_words = {'bad', 'poor', 'terrible', 'awful', 'horrible'}
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    return 'positive' if pos_count > neg_count else 'negative' if neg_count > pos_count else 'neutral'

# Simulated user feedback entries
feedback_entries = [
    "This is a great product, really wonderful!",
    "Terrible experience, very bad service.",
    "It's good but could be better, not excellent.",
    "Amazing quality, truly wonderful and excellent work",
    "Poor effort, feels awful and terrible overall"
]

# Extract key phrases (first two words) from each feedback
key_phrases = [" ".join(entry.lower().split()[:2]) for entry in feedback_entries]
phrase_counter = Counter(key_phrases)

dominant_phrase = phrase_counter.most_common(1)[0][0] if phrase_counter else ''

# Categorize each feedback by sentiment
sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}
sentiments = [sentiment_map[analyze_sentiment(entry)] for entry in feedback_entries]

# Compute rolling adjustment factor based on sentiment transitions
adjustment = 0
for i in range(1, len(sentiments)):
    if sentiments[i] == 1 and sentiments[i-1] == -1:
        adjustment += 0.5
    elif sentiments[i] == -1 and sentiments[i-1] == 1:
        adjustment -= 0.3

# Transform feedback into structured records
feedback_list = []
for idx, entry in enumerate(feedback_entries):
    char_count = len(entry.replace(' ', ''))
    word_count = len(entry.split())
    avg_word_length = char_count / word_count if word_count else 0
    is_flagged = 'bad' in entry.lower() or 'poor' in entry.lower()
    score_hint = (avg_word_length * 10) % 4
    
    # Irrelevant intermediate calculation (distractor)
    temp_weight = sum(ord(c) for c in entry[:5]) % 7 if entry else 0
    
    feedback_list.append({
        'id': idx,
        'length': len(entry),
        'sentiment_val': sentiments[idx],
        'score_hint': score_hint,
        'is_flagged': is_flagged
    })

# Misleading aggregation (not used in final logic)
cumulative_sum = sum(f['length'] * f['sentiment_val'] for f in feedback_list if f['sentiment_val'] > 0)

# Core evaluation logic
def evaluate_performance(feedbacks):
    base_score = 50
    penalty = 0
    bonus = 0
    
    flagged_count = sum(1 for f in feedbacks if f['is_flagged'])
    total_sentiment = sum(f['sentiment_val'] for f in feedbacks)
    
    # Bonus logic using hint values
    hints = [f['score_hint'] for f in feedbacks]
    hint_freq = Counter(hints)
    common_hint_value = hint_freq.most_common(1)[0][0]
    
    if common_hint_value > 2:
        bonus += 15
    
    # Penalty for negative trends
    negative_ratio = sum(1 for f in feedbacks if f['sentiment_val'] < 0) / len(feedbacks)
    if negative_ratio >= 0.4:
        penalty += 25
    
    # Adjustment from earlier transition analysis
    global adjustment
    adjusted_bonus = bonus + (adjustment * 10)
    
    # Final computation
    result = base_score + total_sentiment * 3 + adjusted_bonus - penalty
    
    # Dead code branch (distractor)
    if len(dominant_phrase) > 10:
        result *= 1.1
        
    return int(round(result))

# Key execution point
final_score = evaluate_performance(feedback_list)
print(f"Target result: {final_score}")