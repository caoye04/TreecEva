def analyze_sentiment(texts):
    sentiment_scores = []
    neutral_count = 0
    for text in texts:
        clean_text = text.strip().lower()
        if 'excellent' in clean_text or 'great' in clean_text:
            sentiment_scores.append(2)
        elif 'poor' in clean_text or 'bad' in clean_text:
            sentiment_scores.append(-1)
        elif 'average' in clean_text or 'ok' in clean_text:
            sentiment_scores.append(0)
            neutral_count += 1
        else:
            sentiment_scores.append(1)  # default positive nuance
    return sentiment_scores, neutral_count

# Simulated user feedback data
feedback_strings = [
    "  Excellent service overall!  ",
    "The experience was average, nothing special.",
    "Great product quality and fast delivery",
    "It was ok, could be improved",
    "Poor support response time"
]

base_rating = 3.5
adjustment_factor = 0.7
outlier_detect_flag = False
running_total = 0

# Secondary metric: character frequency analysis (mostly irrelevant)
distinct_chars = set()
char_frequency_map = {}
for entry in feedback_strings:
    for char in entry.lower():
        if char.isalpha():
            distinct_chars.add(char)
            char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

# Compute sentiment and process ratings
sentiments, ignored_neutrals = analyze_sentiment(feedback_strings)
sentiment_sum = sum(sentiments)
sentiment_avg = sentiment_sum / len(sentiments)

# Dummy clustering logic (dead path - doesn't affect final result)
if len(distinct_chars) > 15 and sentiment_sum > 0:
    outlier_detect_flag = True  # unused downstream

# Weighted score computation with redundant intermediate steps
raw_influence = sentiment_avg * adjustment_factor
baseline_adjusted = base_rating + 0.5  # red herring adjustment
temp_offset = baseline_adjusted - raw_influence
intermediate_result = (base_rating + raw_influence) / 2

# Final performance evaluation
final_score = base_rating + (raw_influence * 0.8)

# Extra unrelated list processing to increase cognitive load
word_lengths = [len(s.split()) for s in feedback_strings]
max_words = max(word_lengths)
length_penalty = 0.1 if max_words > 5 else 0

# Additional distraction: string transformation chain
processed_feedback = []
for s in feedback_strings:
    step1 = s.strip().replace('!', '').replace('?', '')
    step2 = ''.join([c for c in step1 if c.isalnum() or c == ' '])
    step3 = step2.title()  # visually significant but unused
    processed_feedback.append(step3)

# Final irrelevant dictionary aggregation
diagnostic_summary = {
    'total_entries': len(feedback_strings),
    'positive_signals': sum(1 for s in sentiments if s > 0),
    'negative_signals': sum(1 for s in sentiments if s < 0),
    'effective_chars': len(distinct_chars),
    'computed_offset': temp_offset  # included but not used
}

Result: {final_score}