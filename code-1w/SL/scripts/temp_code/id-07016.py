def analyze_feedback(reviews):
    positive_count = 0
    total_length = 0
    
    for review in reviews:
        cleaned = review.strip().lower()
        if 'excellent' in cleaned or 'great' in cleaned:
            positive_count += 1
        total_length += len(cleaned)
    
    avg_length = total_length / len(reviews) if reviews else 0
    return positive_count, avg_length

feedback_list = [
    "  Excellent service and great experience!  ",
    "Great staff, very helpful.",
    "Average, nothing special",
    "Great food but slow delivery",
    "Excellent! Will recommend."
]

positive_reviews, average_review_length = analyze_feedback(feedback_list)

# Secondary metric: count how many words are in reviews that contain 'great' or 'excellent'
keyword_word_count = 0
for review in feedback_list:
    words = review.strip(' .!').lower().split()
    if 'great' in words or 'excellent' in words:
        keyword_word_count += len(words)

baseline_score = positive_reviews * 10
length_bonus = int(average_review_length // 5)
engagement_factor = keyword_word_count // 3

initial_score = baseline_score + length_bonus

# Final performance rating calculation
final_score = calculate_performance_rating = lambda: initial_score + engagement_factor
final_score = final_score()