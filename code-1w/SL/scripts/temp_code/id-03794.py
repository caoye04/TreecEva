from collections import defaultdict

# Simulate user feedback analysis for a training module
def analyze_feedback(responses):
    word_count = defaultdict(int)
    positive_keywords = {'good', 'great', 'excellent', 'well', 'improved'}
    negative_keywords = {'bad', 'poor', 'worse', 'difficult', 'confusing'}
    
    total_comments = len(responses)
    sentiment_score = 0
    
    for response in responses:
        words = response.lower().split()
        for word in words:
            word_count[word] += 1
            if word in positive_keywords:
                sentiment_score += 1
            elif word in negative_keywords:
                sentiment_score -= 1

    # Irrelevant aggregation
    long_words = [w for w in word_count.keys() if len(w) > 6]
    diversity_metric = len(set(word_count.values()))
    
    return sentiment_score, total_comments

# Process rating distribution
def normalize_ratings(raw_ratings):
    adjusted = [r + 0.1 for r in raw_ratings if 1 <= r <= 5]
    avg = sum(adjusted) / len(adjusted) if adjusted else 0
    variance = sum((x - avg) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    
    # Dead computation - not used later
    normalized_ranks = [int((r - min(adjusted)) / (max(adjusted) - min(adjusted)) * 10) 
                        for r in adjusted] if adjusted else []
    
    return avg, variance

# Main evaluation logic
def evaluate_performance(feedback, scores):
    base_sentiment, comment_count = analyze_feedback(feedback)
    mean_rating, spread = normalize_ratings(scores)
    
    # Weighted combination
    weighted_component = base_sentiment * 1.5
    adjustment_factor = 0 if mean_rating < 3 else (mean_rating - 3) * 2
    
    # Distractor variables
    temp_correction = sum(1 for s in scores if s >= 4)
    auxiliary_metric = comment_count / (spread + 1) if spread != 0 else 0
    
    final_score = int(weighted_component + (mean_rating * 10) + adjustment_factor)
    
    # Additional unused tracking
    performance_tier = 'High' if final_score > 30 else 'Medium' if final_score > 15 else 'Low'
    
    return final_score

# Input data
feedback_set = [
    "The module was excellent and very well structured",
    "I found it confusing and difficult to follow",
    "Great improvement over last version",
    "Well done, good job!",
    "Poor content, worse delivery"
]
ratings = [4, 5, 3, 4, 2, 5, 4]

# Execution point of interest
final_score = evaluate_performance(feedback_set, ratings)
print(f"Target result: {final_score}")