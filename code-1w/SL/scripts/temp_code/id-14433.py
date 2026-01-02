def analyze_feedback(reviews):
    sentiment_scores = []
    neutral_count = 0
    temp_multiplier = 1.5  # unused distraction
    offset = 10  # misleading constant

    for review in reviews:
        cleaned = review.strip().lower()
        if 'excellent' in cleaned or 'great' in cleaned:
            sentiment_scores.append(4)
        elif 'good' in cleaned or 'satisfactory' in cleaned:
            sentiment_scores.append(3)
        elif 'poor' in cleaned or 'bad' in cleaned:
            sentiment_scores.append(-2)
        else:
            sentiment_scores.append(1)
            neutral_count += 1

    # Distractor computation: not used later
    avg_length = sum(len(r) for r in reviews) / len(reviews) if reviews else 0
    adjusted_avg = avg_length * 0.75 + 5

    return sentiment_scores, neutral_count


def calculate_weighted_average(scores):
    weights = [1.0] * len(scores)
    decay = 0.9
    for i in range(1, len(weights)):
        weights[i] = weights[i-1] * decay

    weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight != 0 else 0


def filter_outliers(data, threshold=2):
    if len(data) < 3:
        return data
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered or data  # ensure non-empty


def evaluate_performance(feedback, base):
    raw_scores, _ = analyze_feedback(feedback)
    
    # Simulate some irrelevant state tracking
    session_log = []
    for idx, sc in enumerate(raw_scores):
        session_log.append(f"item_{idx}: {sc}")
    
    # Meaningful processing chain
    cleaned_scores = filter_outliers(raw_scores)
    trend = [cleaned_scores[i+1] - cleaned_scores[i] for i in range(len(cleaned_scores)-1)]
    improvement = sum(1 for t in trend if t > 0)
    regression = sum(1 for t in trend if t < 0)
    
    net_progress = improvement - regression  # semi-relevant
    
    # Core calculation
    base_modifier = 1.2 if net_progress > 0 else 0.8
    adjusted_base = base * base_modifier
    
    average_rating = calculate_weighted_average(cleaned_scores)
    
    # Final integration
    final_score = adjusted_base + average_rating
    
    # Red herring variables
    normalization_factor = 100 / (sum(abs(x) for x in raw_scores) or 1)
    scaled_log = [len(entry) * normalization_factor for entry in session_log]

    return int(round(final_score))

# Input data
feedback_list = [
    "  Excellent service and great staff!  ",
    "Good overall experience.",
    "Poor communication and bad follow-up.",
    "Satisfactory but could improve.",
    "This was excellent work!",
    "Absolutely terrible.",
    "Great attention to detail."
]
baseline = 45

# Execution point
final_score = evaluate_performance(feedback_list, baseline)
print(f"Result: {final_score}")