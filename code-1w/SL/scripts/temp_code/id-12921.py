def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'great', 'outstanding']
    negative_words = ['poor', 'bad', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        cleaned = word.strip('.,!?:;')
        if cleaned in positive_words:
            score += 1
        elif cleaned in negative_words:
            score -= 1
    return score

# Simulate customer feedback processing
feedback_data = [
    "The service was excellent and great!",
    "Poor experience, very bad service.",
    "It was good but could be better",
    "Outstanding quality overall!"
]

sentiment_scores = []
for feedback in feedback_data:
    sentiment_scores.append(analyze_sentiment(feedback))

# Irrelevant statistical distraction
mean_sentiment = sum(sentiment_scores) / len(sentiment_scores)
deviations = [(s - mean_sentiment)**2 for s in sentiment_scores]
variance = sum(deviations) / len(deviations)  # Not used later

# Base performance metric
base_count = 0
for s in sentiment_scores:
    if s > 0:
        base_count += 1

# Weighted adjustment (distractor computation)
total_length = 0
for fb in feedback_data:
    total_length += len(fb.split())
average_length = total_length / len(feedback_data)
length_factor = 1.0 if average_length > 5 else 0.8  # Unused in final logic

# Core logic with string-based filtering
filtered_feedback = []
for fb in feedback_data:
    tokens = fb.lower().split()
    if 'excellent' in tokens or 'outstanding' in tokens:
        filtered_feedback.append(fb)

# Misleading normalization step
norm_const = max(sentiment_scores) if sentiment_scores else 1
normalized_scores = [s / norm_const for s in sentiment_scores]  # Partially used

# Key state tracking
feedback_status = {}
for i, fb in enumerate(feedback_data):
    status = 'flagged' if 'poor' in fb.lower() or 'bad' in fb.lower() else 'normal'
    feedback_status[i] = status

# Actual multiplier logic
base_multiplier = 10
if feedback_status[0] == 'normal':
    base_multiplier += 5

# Final evaluation function
def evaluate_performance(feedback_list, multiplier):
    count_high_impact = 0
    cumulative = 0
    for fb in feedback_list:
        if 'excellent' in fb.lower() or 'outstanding' in fb.lower():
            count_high_impact += 1
        # Secondary check using string method
        if fb.strip().endswith('!'):
            cumulative += 2
    result = multiplier * count_high_impact + cumulative
    
    # Dead code path - never executed under current data
    if False:
        fallback = sum([len(s.split()) for s in feedback_list])
        result = max(result, fallback)
        
    return result

# Execution point of interest
final_score = evaluate_performance(feedback_list=feedback_data, base_multiplier=base_multiplier)
print(f"Result: {final_score}")