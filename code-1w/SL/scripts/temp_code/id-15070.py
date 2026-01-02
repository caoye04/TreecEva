from collections import defaultdict

# Simulate a performance evaluation system with weighted feedback
def analyze_feedback(raw_responses):
    counts = defaultdict(int)
    for response in raw_responses:
        if response > 4:
            counts['positive'] += 1
        elif response < 3:
            counts['negative'] += 1
        else:
            counts['neutral'] += 1
    return counts

def calculate_trend(data):
    # Irrelevant trend analysis (distractor)
    diff = [data[i+1] - data[i] for i in range(len(data)-1)]
    avg_change = sum(diff) / len(diff) if diff else 0
    return avg_change

def filter_outliers(values, threshold=1):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def compute_baseline_adjustment(samples):
    # Dead code path — never used in final logic
    if len(samples) == 0:
        return 0
    temp_sum = 0
    for s in samples:
        temp_sum += s * 0.9 if s > 5 else s * 1.1
    return temp_sum / len(samples)

def evaluate_performance(ratings, importance_weights):
    # Core logic starts here
    filtered_ratings = filter_outliers(ratings)
    rating_counts = analyze_feedback(filtered_ratings)
    
    # Misleading intermediate computation
    total_impact = 0
    for w in importance_weights:
        total_impact += w ** 2
    scaling_factor = total_impact / len(importance_weights) if importance_weights else 1
    
    # Actual scoring logic
    base_score = 0
    if rating_counts['positive'] > 0:
        base_score += rating_counts['positive'] * 2
    if rating_counts['negative'] > 0:
        base_score -= rating_counts['negative'] * 3
    base_score += rating_counts['neutral']

    # Apply arbitrary offset (relevant only through indirect effect)
    adjustment = len(filtered_ratings) % 5
    
    # Final score calculation
    final_score = (base_score + adjustment) * scaling_factor
    return int(final_score)

# Main execution
if __name__ == '__main__':
    # Input data
    feedback_data = [5, 2, 4, 1, 5, 5, 3, 2, 4, 5, 1, 3]
    weights = [0.8, 1.2, 0.9, 1.1, 1.0]
    
    # Distractor variables and computations
    avg_rating = sum(feedback_data) / len(feedback_data)
    trend = calculate_trend(feedback_data)
    baseline_adj = compute_baseline_adjustment(feedback_data)
    summary_stats = {k: v for k, v in sorted(analyze_feedback(feedback_data).items())}
    
    # Key statement
    final_score = evaluate_performance(feedback_data, weights)
    
    print(f"Result: {final_score}")