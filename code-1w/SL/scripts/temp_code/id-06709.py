def analyze_trends(data, threshold_func):
    high_performers = set()
    low_performers = set()
    temp_sum = 0

    for item in data:
        temp_sum += item * 0.5
        if threshold_func(item):
            high_performers.add(item)
        else:
            low_performers.add(item)

    # Irrelevant aggregation
    avg_val = sum(data) / len(data) if data else 0
    outlier_count = len([x for x in data if abs(x - avg_val) > 2 * avg_val])

    return high_performers

# Simulated user feedback ratings
customer_feedback = [8, 9, 5, 7, 10, 4, 8, 9, 6]

# Misleading preprocessing
normalized_feedback = [round(x * 1.1) for x in customer_feedback]
discounted_feedback = [x - 1 for x in normalized_feedback if x > 5]

feedback_set = set(customer_feedback)

# Dead code path - never executed but looks relevant
def legacy_evaluation(data):
    return len([x for x in data if x >= 6])

# Secondary distractor computation
efficiency_metrics = {}
efficiency_metrics['peak'] = max(customer_feedback)
efficiency_metrics['volatility'] = sum(abs(a - b) for a, b in zip(customer_feedback, customer_feedback[1:]))
efficiency_metrics['trend'] = 'increasing' if efficiency_metrics['peak'] > 7 else 'stable'

# Core logic obscured by context
final_score = 0
def evaluate_performance(feedbacks, condition):
    result_set = set()
    for fb in feedbacks:
        if condition(fb):
            result_set.add(fb)
    
    # Additional irrelevant transformation
    squared_mapping = {x: x**2 for x in feedbacks}
    total_contrib = sum(squared_mapping[x] for x in result_set)
    
    base_score = len(result_set) * 10
    bonus = 5 if len(result_set) > 3 else 0
    
    # Unused metric
    coverage_ratio = len(result_set) / len(feedbacks) if feedbacks else 0
    
    return base_score + bonus

final_score = evaluate_performance(feedback_set, lambda x: x > 7)
print(f"Result: {final_score}")