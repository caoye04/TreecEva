def analyze_sentiment(texts):
    sentiment_scores = {'positive': 0, 'negative': 0, 'neutral': 0}
    word_sentiment = {
        'excellent': 3, 'good': 2, 'fine': 1,
        'poor': -2, 'bad': -3, 'awful': -4,
        'okay': 1, 'average': 0
    }
    
    total_intensity = 0
    for text in texts:
        words = text.lower().split()
        for word in words:
            if word in word_sentiment:
                score = word_sentiment[word]
                if score > 0:
                    sentiment_scores['positive'] += 1
                elif score < 0:
                    sentiment_scores['negative'] += 1
                else:
                    sentiment_scores['neutral'] += 1
                total_intensity += abs(score)
    
    # Distractor: unused computation
    avg_sentiment = sum(word_sentiment.values()) / len(word_sentiment) if word_sentiment else 0
    
    return sentiment_scores, total_intensity


def transform_ratings(ratings):
    transformed = []
    offset = 5
    multiplier = 2
    
    for r in ratings:
        adjusted = (r + offset) * multiplier
        if adjusted > 20:
            adjusted = 20
        elif adjusted < 0:
            adjusted = 0
        transformed.append(adjusted)
    
    # Dead code path - never executed due to logic above
    if False and any(x > 30 for x in transformed):
        transformed = [x // 2 for x in transformed]
    
    return transformed


def calculate_weighted_sum(data, weights):
    # Unused function - red herring
    result = 0
    for i in range(len(data)):
        result += data[i] * weights[i % len(weights)]
    return result


def build_feedback_summary(records):
    feedback_map = {}
    category_count = {}
    
    for record in records:
        user_id = record['user']
        category = record['category']
        feedback = record['feedback']
        rating = record['rating']
        
        if category not in category_count:
            category_count[category] = 0
        category_count[category] += 1
        
        sentiment_key = 'neutral'
        if rating >= 4:
            sentiment_key = 'positive'
        elif rating <= 2:
            sentiment_key = 'negative'
        
        if user_id not in feedback_map:
            feedback_map[user_id] = {'ratings': [], 'feedbacks': [], 'sentiment': []}
        
        feedback_map[user_id]['ratings'].append(rating)
        feedback_map[user_id]['feedbacks'].append(feedback)
        feedback_map[user_id]['sentiment'].append(sentiment_key)
    
    # Irrelevant aggregation
    total_entries = sum(category_count.values())
    unique_users = len(feedback_map)
    
    # Misleading intermediate: looks important but unused later
    completeness_score = unique_users / (total_entries + 1) * 100
    
    return feedback_map


def evaluate_performance(feedback_map, threshold):
    base_score = 0
    bonus_count = 0
    penalty_count = 0
    
    user_contribution = []
    
    for user_id, data in feedback_map.items():
        user_rating_avg = sum(data['ratings']) / len(data['ratings']) if data['ratings'] else 0
        
        # Real scoring logic
        if user_rating_avg >= threshold:
            base_score += 15
            bonus_count += 1
        else:
            base_score -= 5
            penalty_count += 1
        
        # Tuple unpacking distraction
        feedbacks = data['feedbacks']
        sentiments = data['sentiment']
        for f, s in zip(feedbacks, sentiments):
            if len(f) > 10 and s == 'positive':
                base_score += 2
            elif len(f) < 5 and s == 'negative':
                base_score -= 3
        
        user_contribution.append((user_id, user_rating_avg))
    
    # Final adjustment based on bonus/penalty ratio
    if bonus_count > 0 and penalty_count == 0:
        final_multiplier = 1.5
    elif bonus_count == 0 and penalty_count > 0:
        final_multiplier = 0.5
    else:
        final_multiplier = 1.0
    
    # The actual answer computation
    final_score = int((base_score * final_multiplier) + (bonus_count * 10) - (penalty_count * 5))
    
    # Unused complex structure - set operations as required
    seen_ratings = set()
    for data in feedback_map.values():
        seen_ratings.update(data['ratings'])
    high_performers = {uid for uid, d in feedback_map.items() 
                       if sum(d['ratings']) / len(d['ratings']) >= threshold}
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    raw_texts = [
        "The service was excellent and fast",
        "Poor quality and bad attitude",
        "It's okay, nothing special"
    ]
    
    # Distractor call - result not used
    sentiment_analysis = analyze_sentiment(raw_texts)
    
    ratings_data = [3, 4, 5, 2, 1]
    transformed_ratings = transform_ratings(ratings_data)
    
    # Build realistic input
    feedback_records = [
        {'user': 'U001', 'category': 'service', 'feedback': 'Great help!', 'rating': 5},
        {'user': 'U002', 'category': 'usability', 'feedback': 'Too complex', 'rating': 2},
        {'user': 'U003', 'category': 'service', 'feedback': 'Good support', 'rating': 4},
        {'user': 'U004', 'category': 'performance', 'feedback': 'Fine for now', 'rating': 3},
        {'user': 'U005', 'category': 'usability', 'feedback': 'Awful UI', 'rating': 1}
    ]
    
    feedback_map = build_feedback_summary(feedback_records)
    final_score = evaluate_performance(feedback_map, 7)
