def analyze_sentiment(text):
    positive_words = ['great', 'excellent', 'good', 'amazing', 'wonderful', 'fantastic']
    negative_words = ['bad', 'terrible', 'awful', 'poor', 'horrible']
    words = text.lower().split()
    pos_count = sum(1 for word in words if word.strip('.,!') in positive_words)
    neg_count = sum(1 for word in words if word.strip('.,!') in negative_words)
    return (pos_count - neg_count) * 10

feedback_data = [
    "The service was excellent and wonderful!",
    "Poor quality, really bad experience.",
    "It was good, not great but acceptable.",
    "Absolutely fantastic and amazing!",
    "Terrible, just terrible."
]

# Preprocessing step: filter out very short reviews (less than 4 words)
cleaned_feedback = [review for review in feedback_data if len(review.split()) >= 4]

# Extract sentiment scores using list comprehension with conditional expression
raw_scores = [analyze_sentiment(review) if len(review) > 20 else 0 for review in cleaned_feedback]

# Compute rolling average over sliding window of size 2 (for stability analysis)
rolling_avg = []
for i in range(1, len(raw_scores)):
    rolling_avg.append((raw_scores[i-1] + raw_scores[i]) / 2)

# Calculate trend indicator based on score progression
trend_direction = 0
for i in range(1, len(raw_scores)):
    if raw_scores[i] > raw_scores[i-1]:
        trend_direction += 1
    elif raw_scores[i] < raw_scores[i-1]:
        trend_direction -= 1

# Auxiliary metric: longest review length (distraction)
max_review_length = max(len(review) for review in feedback_data)
median_score = sorted(raw_scores)[len(raw_scores)//2] if raw_scores else 0

# Simulate confidence interval adjustment (irrelevant to final logic)
confidence_adjustment = 0.95 if len(cleaned_feedback) >= 3 else 0.85
adjusted_scores = [score * confidence_adjustment for score in raw_scores]

# Aggregate performance using min, max, and median (core logic)
min_perf = min(raw_scores)
max_perf = max(raw_scores)

# Final scoring formula combines multiple metrics but only uses raw min/max/median
final_score = (min_perf + max_perf + median_score) / 3

# Distractor variables below (not used in final result)
overall_avg = sum(raw_scores) / len(raw_scores) if raw_scores else 0
penalty_factor = 1.0
if trend_direction < 0:
    penalty_factor = 0.9

# Misleading normalization step (never applied)
normalized_final = final_score / (max_perf - min_perf + 1) if max_perf != min_perf else 0

# This print statement ensures output visibility
print(f"Result: {final_score}")