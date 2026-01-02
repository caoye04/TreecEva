def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        words = text.lower().split()
        score = sum(1 for w in words if w in ['great', 'good', 'excellent']) - sum(1 for w in words if w in ['bad', 'poor', 'terrible'])
        sentiment_scores.append(score)
    return sentiment_scores

# Simulate customer feedback processing
customer_feedback = [
    "This product is excellent and great!",
    "Poor quality and bad experience",
    "It's good but could be better",
    "Absolutely terrible and wasteful"
]

sentiments = analyze_sentiment(customer_feedback)

# Irrelevant distraction: word length analysis
word_lengths = [len(word) for feedback in customer_feedback for word in feedback.split()]
median_length = sorted(word_lengths)[len(word_lengths)//2] if word_lengths else 0

# Base rating from survey data
survey_ratings = [4.2, 3.8, 4.5, 4.0, 4.3]
base_rating = sum(survey_ratings) / len(survey_ratings)

# Feedback list with adjusted weights
feedback_list = []
for i, s in enumerate(sentiments):
    weight = 0.8 if s >= 0 else 0.5
    adjusted = (base_rating + s * 0.3) * weight
    feedback_list.append(round(adjusted, 2))

# Distractor: unused function
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean)**2 for x in data) / len(data)

# Distractor variables
temp_result = [x * 1.1 for x in feedback_list if x > 4.0]
placeholder_sum = sum(temp_result) if temp_result else 0.0

# Key logic chain using lambda and slicing
recent_three = feedback_list[-3:]
boost_factor = list(map(lambda x: x * 1.2 if x > 3.5 else x * 1.05, recent_three))

# Final performance evaluation
def evaluate_performance(feedbacks, base):
    total_impact = sum(boost_factor)
    penalty = 0
    for fb in feedbacks:
        if fb < 3.7:
            penalty += 0.4
    # Complex but deterministic computation
    raw_score = base * 10 + total_impact - penalty * 2
    return int(round(raw_score * 0.9))

final_score = evaluate_performance(feedback_list, base_rating)
print(f"Result: {final_score}")