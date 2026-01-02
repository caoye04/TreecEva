def process_feedback(feedback_list, importance_weights):
    total_entries = len(feedback_list)
    weighted_sum = 0
    adjustment_factor = 0.85
    temp_buffer = []
    ignored_count = 0

    # Preprocess: filter invalid entries and normalize case
    cleaned_feedback = []
    for entry in feedback_list:
        text = entry['comment'].strip()
        if not text:
            ignored_count += 1
            continue
        normalized = text.lower()
        cleaned_feedback.append({
            'comment': normalized,
            'sentiment': entry['sentiment'],
            'length': len(normalized)
        })

    # Extract keywords using slicing and string methods
    keywords = set()
    for item in cleaned_feedback:
        words = item['comment'].split()
        for word in words:
            clean_word = word.strip('.,!?"')
            if len(clean_word) > 4:
                keywords.add(clean_word[:4])  # First 4 chars as keyword hash

    # Compute sentiment density with distraction logic
    positive_count = 0
    neutral_count = 0
    negative_count = 0
    for item in cleaned_feedback:
        sent = item['sentiment']
        if sent == 'positive':
            positive_count += 1
        elif sent == 'neutral':
            neutral_count += 1
        else:
            negative_count += 1

    # Dummy statistical analysis (irrelevant)
    avg_length = sum(item['length'] for item in cleaned_feedback) / max(len(cleaned_feedback), 1)
    length_variance = sum((item['length'] - avg_length)**2 for item in cleaned_feedback) / max(len(cleaned_feedback), 1)

    # Core scoring logic with enumerate and zip
    scores = []
    for i, item in enumerate(cleaned_feedback):
        base_score = len(item['comment'].split())
        bonus = 1 if item['sentiment'] == 'positive' else (-2 if item['sentiment'] == 'negative' else 0)
        dynamic_weight = importance_weights[i % len(importance_weights)]
        weighted_score = (base_score + bonus) * dynamic_weight
        scores.append(weighted_score)

    aggregate = sum(scores)
    decay_factor = 0.95 ** len(keywords)

    # Secondary adjustment based on sentiment balance (distraction)
    sentiment_balance = (positive_count - negative_count) / max(positive_count + negative_count, 1)
    balance_correction = adjustment_factor if sentiment_balance > 0 else 0.5

    # Final computation
    raw_result = aggregate * decay_factor * balance_correction
    final_score = int(round(raw_result))

    # Dead code path - never executed due to structure
    if len(temp_buffer) > 100:
        final_score += sum(ord(c) for c in 'phantom')

    return final_score

# Input data
reviews = [
    {'comment': 'Excellent service and very friendly staff', 'sentiment': 'positive'},
    {'comment': 'It was okay, nothing special', 'sentiment': 'neutral'},
    {'comment': 'Poor experience, will not return', 'sentiment': 'negative'},
    {'comment': 'Outstanding quality and fast delivery', 'sentiment': 'positive'},
    {'comment': '', 'sentiment': 'neutral'},
    {'comment': 'Good value for money', 'sentiment': 'positive'}
]
weights = [1.2, 0.8, 1.5, 0.9]

result = process_feedback(reviews, weights)
print(f"Result: {result}")