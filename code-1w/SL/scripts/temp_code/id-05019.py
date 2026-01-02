def analyze_sentiment(text):
    positive_words = {'great', 'good', 'excellent', 'amazing', 'wonderful'}
    negative_words = {'bad', 'poor', 'terrible', 'awful', 'horrible'}
    words = text.lower().split()
    pos_count = len([w for w in words if w in positive_words])
    neg_count = len([w for w in words if w in negative_words])
    return pos_count - neg_count


def process_feedback(entries):
    stats = {}
    total_entries = 0
    sentiment_sum = 0
    
    for entry in entries:
        category = entry['category']
        feedback = entry['comment']
        score = entry['rating']

        if category not in stats:
            stats[category] = {'count': 0, 'total_rating': 0, 'sentiment_total': 0}
        
        sentiment_val = analyze_sentiment(feedback)
        stats[category]['count'] += 1
        stats[category]['total_rating'] += score
        stats[category]['sentiment_total'] += sentiment_val
        total_entries += 1
        sentiment_sum += sentiment_val

    avg_sentiment = sentiment_sum / total_entries if total_entries else 0
    
    # Irrelevant aggregation
    redundant_data = {k: (v['total_rating'] / v['count']) for k, v in stats.items()}
    
    return stats, avg_sentiment, redundant_data


def compute_weights(categories):
    weights = {}
    base_weight = 0.5
    for i, cat in enumerate(categories):
        weights[cat] = base_weight + (i * 0.1)
        base_weight *= 0.9
    return weights


def assess_performance(log, min_threshold):
    processed_stats, avg_sent, _ = process_feedback(log)
    weight_map = compute_weights(processed_stats.keys())
    
    composite_score = 0
    debug_values = []
    
    for cat, data in processed_stats.items():
        norm_rating = data['total_rating'] / data['count']
        norm_sentiment = data['sentiment_total'] / data['count']
        
        # Weighted combination
        weighted_component = norm_rating * weight_map[cat] + norm_sentiment * 0.3
        composite_score += weighted_component
        
        # Distractor computation
        temp_flag = 'high' if norm_rating >= 4 else 'low'
        debug_values.append((cat, temp_flag, weighted_component))

    # Additional irrelevant filtering
    filtered_debug = [d for d in debug_values if 'h' in d[1]]
    size_hint = len(filtered_debug) * 10
    
    # Final adjustment based on threshold
    adjustment_factor = 1.2 if avg_sent > min_threshold else 0.8
    final_score = (composite_score + size_hint) * adjustment_factor
    
    # Key assignment point
    final_score = int(final_score)

    return final_score

# Input data
feedback_log = [
    {'category': 'service', 'comment': 'Great and excellent service!', 'rating': 5},
    {'category': 'food', 'comment': 'The food was bad and terrible.', 'rating': 2},
    {'category': 'ambiance', 'comment': 'Wonderful atmosphere, really amazing!', 'rating': 5},
    {'category': 'service', 'comment': 'Poor customer support.', 'rating': 3},
    {'category': 'food', 'comment': 'Good taste but poor presentation.', 'rating': 4}
]

threshold = 0.5

# Execution
final_score = assess_performance(feedback_log, threshold)
print(f"Result: {final_score}")