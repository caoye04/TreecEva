def analyze_performance(feedback, limit):
    base_scores = {i for i in range(1, len(feedback) + 1) if feedback[i-1] > 0.7}
    adjustment = 0
    temp_sum = 0
    
    # Irrelevant accumulation (distractor)
    for val in feedback:
        temp_sum += val * 0.1  # Not used in final logic

    outlier_count = 0
    for val in feedback:
        if val < 0.3 or val > 0.9:
            outlier_count += 1

    # Semi-relevant transformation
    adjusted_threshold = limit * 0.8 if len(base_scores) > 3 else limit * 1.2
    
    # Core logic: count how many meet adjusted threshold
    qualified = 0
    for val in feedback:
        if val >= adjusted_threshold:
            qualified += 1

    # Additional distraction: unused helper calculation
    def compute_entropy(data):
        from math import log
        return -sum(p * log(p) for p in data if p > 0)
    
    entropy_proxy = sum(1 for x in feedback if x > 0.5) / len(feedback)  # Simplified stand-in

    # Final score computation (key path)
    scaling_factor = 2 if outlier_count < 4 else 1
    final_score = (qualified * len(base_scores)) + scaling_factor * 10
    
    # Dead code branch (distractor)
    if limit < 0:
        final_score = -1  # Never reached

    return final_score

# Input setup
feedback_data = [0.85, 0.72, 0.88, 0.29, 0.91, 0.76]
threshold = 0.75

# Execution point
final_score = analyze_performance(feedback_data, threshold)
print(f"Result: {final_score}")