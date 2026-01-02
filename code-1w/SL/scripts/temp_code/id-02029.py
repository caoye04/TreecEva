def analyze_sentiment(text_blocks):
    sentiment_scores = {'positive': 0, 'negative': 0, 'neutral': 0}
    word_count = 0
    for block in text_blocks:
        words = block.lower().split()
        word_count += len(words)
        for word in words:
            if word in ['excellent', 'great', 'good', 'amazing']:
                sentiment_scores['positive'] += 1
            elif word in ['terrible', 'bad', 'awful', 'horrible']:
                sentiment_scores['negative'] += 1
            else:
                sentiment_scores['neutral'] += 1
    avg_length = word_count / len(text_blocks) if text_blocks else 0
    return sentiment_scores, avg_length


def normalize_data(raw_values):
    min_val = min(raw_values)
    max_val = max(raw_values)
    if max_val == min_val:
        return [0.5 for _ in raw_values]
    return [(x - min_val) / (max_val - min_val) for x in raw_values]


def evaluate_performance(feedback, threshold):
    base_points = 0
    bonus = 0
    penalties = 0
    
    # Real logic path
    category_weights = {'service': 3, 'food': 4, 'ambiance': 2, 'wait_time': -1}
    temp_result = {}
    for category, comments in feedback.items():
        score = 5
        if category in category_weights:
            weight = category_weights[category]
            if weight > 0:
                score += weight
            else:
                penalties += abs(weight)
        
        # Simulated analysis
        comment_text = ' '.join(comments)
        if 'not bad' in comment_text:
            score += 1
        if 'could be better' in comment_text:
            score -= 2
        if len(comments) > 3:
            bonus += 1
        
        temp_result[category] = score
    
    base_points = sum(temp_result.values())
    
    # Irrelevant computation - distractor
    inverted_map = {v: k for k, v in category_weights.items()}
    sorted_inverted = sorted(inverted_map.keys(), reverse=True)
    phantom_value = 0
    for key in sorted_inverted:
        if key > 0:
            phantom_value += key * 2
    
    # Another distraction: unused normalization
    dummy_list = [len(comments) for comments in feedback.values()]
    normalized_counts = normalize_data(dummy_list)
    
    final_score = base_points - penalties + bonus
    return final_score

# Main execution
feedback_data = {
    'service': [
        'The service was great and fast',
        'Excellent staff behavior',
        'Good overall experience',
        'Satisfactory but not outstanding'
    ],
    'food': [
        'Amazing flavors and great presentation',
        'Food was excellent',
        'Could be better in terms of spice'
    ],
    'ambiance': [
        'Ambiance is terrible',
        'Not bad for a weekday evening'
    ],
    'wait_time': [
        'Wait time was horrible',
        'Too long for a simple order'
    ]
}

# Extract sentiment for distraction
sentiment_analysis, average_words = analyze_sentiment(feedback_data['service'])

# Key execution point
final_score = evaluate_performance(feedback_data, 8)

print(f"Result: {final_score}")