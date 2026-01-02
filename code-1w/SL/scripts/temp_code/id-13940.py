from collections import defaultdict

# Simulate employee feedback analysis with distraction variables
def analyze_feedback(reviews):
    sentiment_count = defaultdict(int)
    total_entries = 0
    
    for review in reviews:
        words = review.lower().split()
        if 'excellent' in words:
            sentiment_count['positive'] += 1
        elif 'poor' in words:
            sentiment_count['negative'] += 1
        else:
            sentiment_count['neutral'] += 1
        total_entries += 1

    # Distractor computation: irrelevant word length stats
    avg_word_length = sum(len(word) for review in reviews for word in review.split()) / sum(len(review.split()) for review in reviews)
    complexity_flag = avg_word_length > 5.0
    
    return dict(sentiment_count), total_entries

# Evaluate performance based on adjusted metrics
def evaluate_performance(feedback_data, base):
    adjustments = []
    shift_factor = 0.87
    
    for category, count in feedback_data.items():
        if category == 'positive':
            adjustments.append(count * 1.5)
        elif category == 'negative':
            adjustments.append(-count * 2.0)
        else:
            adjustments.append(count * 0.2)
    
    # Distractor: unused helper calculation
    outlier_check = [x for x in adjustments if abs(x) > 10]
    adjustment_sum = sum(adjustments)
    
    # Real logic path
    base_modifier = len(feedback_data) if adjustment_sum > 0 else -len(feedback_data)
    temp_result = base + adjustment_sum + base_modifier
    
    # Secondary distractor: conditional expression that doesn't alter flow
    status_label = 'optimal' if temp_result >= 0 else ('suboptimal' if temp_result < -5 else 'marginal')
    
    # Final score computed here
    final_score = int(temp_result * shift_factor)
    return final_score

# Main execution
if __name__ == "__main__":
    # Input data
    feedback_reviews = [
        "The team performed excellent work this quarter",
        "Poor communication affected delivery timelines",
        "Results were acceptable but could improve",
        "excellent leadership shown by management",
        "standard performance, nothing exceptional"
    ]
    
    baseline_value = 42
    
    # Analyze feedback (partial use of result)
    parsed_feedback, entry_count = analyze_feedback(feedback_reviews)
    
    # Key computation step
    final_score = evaluate_performance(parsed_feedback, baseline_value)
    
    # Print result as required
    print(f"Target result: {final_score}")