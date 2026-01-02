def analyze_sentiment(text):
    positive_words = {'great', 'good', 'excellent', 'outstanding', 'superb'}
    negative_words = {'poor', 'bad', 'terrible', 'awful', 'worst'}
    words = text.lower().split()
    pos_count = len([w for w in words if w in positive_words])
    neg_count = len([w for w in words if w in negative_words])
    return pos_count - neg_count

# Simulate system health check (distractor)
def compute_health_status(loads):
    avg_load = sum(loads) / len(loads)
    threshold = 75
    status = 'OK' if avg_load < threshold else 'CRITICAL'
    penalty = 10 if status == 'CRITICAL' else 0
    return penalty  # Not used in final logic

# Main evaluation pipeline
def extract_keywords(feedback):
    clean_text = feedback.strip().lower()
    tokens = clean_text.replace('.', ' ').replace('!', ' ').replace('?', ' ').split()
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at'}
    keywords = [t for t in tokens if t not in stopwords and len(t) > 2]
    freq_map = {}
    for k in keywords:
        freq_map[k] = freq_map.get(k, 0) + 1
    return freq_map

def calculate_relevance_score(word_freq, target_theme):
    theme_keywords = {
        'performance': 3,
        'efficiency': 2.5,
        'speed': 2,
        'accuracy': 3.5,
        'response': 1.5
    }
    score = 0.0
    for word, count in word_freq.items():
        if word in theme_keywords:
            score += theme_keywords[word] * count
    return round(score, 3)

def evaluate_performance(feedback_str, base_metrics):
    # Step 1: Sentiment analysis
    sentiment_val = analyze_sentiment(feedback_str)
    
    # Step 2: Keyword extraction
    keywords = extract_keywords(feedback_str)
    
    # Step 3: Relevance scoring
    relevance = calculate_relevance_score(keywords, 'performance')
    
    # Step 4: Combine with base metrics
    base_performance = base_metrics.get('base_score', 0)
    adjustment = base_metrics.get('adjustment_factor', 1.0)
    
    # Distractor: unused health computation
    system_loads = [68, 72, 70, 80, 75]
    _ = compute_health_status(system_loads)  # Dead call, no effect
    
    # Step 5: Apply complex weighting
    if sentiment_val > 0:
        multiplier = 1.2 + (sentiment_val * 0.1)
    elif sentiment_val < 0:
        multiplier = 0.8
    else:
        multiplier = 1.0
    
    # Final integration
    raw_score = (base_performance + relevance) * adjustment * multiplier
    
    # Extra distraction: character analysis (not influencing result)
    char_count = len(feedback_str)
    upper_ratio = sum(1 for c in feedback_str if c.isupper()) / char_count if char_count > 0 else 0
    _ = round(upper_ratio * 100, 2)  # Unused metric
    
    # Final discretization
    final_score = int(round(raw_score))
    
    return final_score

# Execution block
if __name__ == '__main__':
    user_feedback = "The performance was excellent! Great speed and outstanding accuracy."
    initial_metrics = {
        'base_score': 45,
        'adjustment_factor': 1.1,
        'ignored_param': 999  # Irrelevant
    }
    final_score = evaluate_performance(user_feedback, initial_metrics)
    print(f"Result: {final_score}")