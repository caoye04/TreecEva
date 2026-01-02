def analyze_sentiment(text_blocks):
    sentiment_scores = []
    for block in text_blocks:
        words = block.lower().split()
        positive = len([w for w in words if w in ['excellent', 'good', 'great', 'outstanding']])
        negative = len([w for w in words if w in ['poor', 'bad', 'terrible', 'awful']])
        sentiment_scores.append(max(positive - negative, -2))
    return sentiment_scores


def calculate_weights(n):
    # Irrelevant helper function - dead code path
    return [i**0.5 for i in range(1, n+1)]


def filter_extremes(scores, threshold=1):
    # Semi-relevant: used to sanitize inputs but not critical
    return [s for s in scores if abs(s) >= threshold]


def evaluate_performance(feedback, multiplier):
    raw_scores = analyze_sentiment(feedback)
    filtered_scores = filter_extremes(raw_scores, threshold=0)  # Includes all
    
    # Distraction: unnecessary transformations
    squared_sum = sum([s**2 for s in filtered_scores])
    avg_square = squared_sum / len(filtered_scores) if filtered_scores else 0
    rms_value = avg_square ** 0.5  # Not used later
    
    # Key logic chain starts here
    adjustment_factor = 1.0
    if len(filtered_scores) > 3:
        adjustment_factor += 0.2
    if sum(filtered_scores) > 5:
        adjustment_factor += 0.3
    
    base_total = sum(filtered_scores)
    adjusted_total = base_total * adjustment_factor
    
    # Misleading intermediate
    temp_result = adjusted_total * 1.5  # Never used
    final_score = int(adjusted_total * multiplier)
    
    return final_score

# Main execution
base_multiplier = 10
project_feedback = [
    "The work was excellent and outstanding overall",
    "Good effort but could improve",
    "Terrible execution and poor management",
    "Great progress, truly outstanding",
    "Excellent results again this quarter"
]

irrelevant_matrix = [[i*j for j in range(5)] for i in range(5)]  # Distractor data
unused_stats = {"max": 99, "min": 3, "range": 96}  # Dead variable

feedback_list = project_feedback

# Critical statement
final_score = evaluate_performance(feedback_list, base_multiplier)
print(f"Result: {final_score}")