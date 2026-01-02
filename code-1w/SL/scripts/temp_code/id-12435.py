from collections import Counter

# Employee performance evaluation system
def evaluate_performance(feedback_list):
    word_count = Counter(word.lower() for word in ' '.join(feedback_list).split())
    
    positive_terms = ['excellent', 'outstanding', 'improved', 'reliable']
    negative_terms = ['delayed', 'error', 'complaint', 'missed']
    
    pos_score = sum(word_count[term] * 3 for term in positive_terms)
    neg_score = sum(word_count[term] * 2 for term in negative_terms)
    
    base_performance = pos_score - neg_score
    adjustment = len(feedback_list) % 4  # minor cycle adjustment
    performance_points = base_performance + adjustment
    
    if performance_points > 10:
        final_bonus = 25
    else:
        final_bonus = 10
    
    total_score = final_bonus + performance_points
    return total_score

feedback = [
    "Excellent work on the project",
    "Outstanding improvement in reliability",
    "No complaints or errors reported"
]

result = evaluate_performance(feedback)
print(f"Result: {result}")