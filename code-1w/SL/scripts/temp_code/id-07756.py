def evaluate_performance(feedback):
    base_score = 0
    adjustments = {'positive': 3, 'neutral': 0, 'negative': -2}
    
    for category, comment in feedback.items():
        if 'exceeds' in comment.lower():
            base_score += adjustments['positive']
        elif 'meets' in comment.lower():
            base_score += adjustments['neutral']
        elif 'needs_improvement' in comment.lower():
            base_score += adjustments['negative']
    
    multiplier = len(feedback) // 2 + 1
    final_score = base_score * multiplier
    
    # Irrelevant tracking variable (minor distraction)
    review_count = len(feedback)
    return final_score

# Input data
feedback_map = {
    'communication': 'Performance exceeds expectations',
    'punctuality': 'meets standard requirements',
    'teamwork': 'needs_improvement in collaboration',
    'initiative': 'exceeds typical engagement'
}

final_score = evaluate_performance(feedback_map)
print(f"Result: {final_score}")