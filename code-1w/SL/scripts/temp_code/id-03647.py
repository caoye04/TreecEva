from collections import defaultdict

# Simulate employee review analysis with adjustment logic
def analyze_feedback(reviews):
    sentiment_count = defaultdict(int)
    total_entries = 0
    
    for review in reviews:
        words = review.lower().split()
        for word in words:
            if word in ['excellent', 'good', 'adequate']:
                sentiment_count['positive'] += 1
            elif word in ['poor', 'bad', 'terrible']:
                sentiment_count['negative'] += 1
            elif word in ['okay', 'average', 'acceptable']:
                sentiment_count['neutral'] += 1
        total_entries += 1
    
    # Irrelevant intermediate calculation (distractor)
    avg_length = sum(len(r.split()) for r in reviews) / len(reviews) if reviews else 0
    size_metric = len(reviews) * 1.5
    
    return sentiment_count, total_entries

# Adjustment heuristics based on team size
def adjust_for_bias(team_size, base_scores):
    adjusted = {}
    bias_factor = 0.9 if team_size < 5 else 1.1 if team_size > 10 else 1.0
    
    for k, v in base_scores.items():
        adjusted[k] = v * bias_factor
    
    # Dead code path - never used (distractor)
    if team_size == 7:
        temp_debug = [x * 2 for x in range(5)]
    
    return adjusted

# Core evaluation function
evaluate_performance = lambda scores, factor: int(
    (scores.get('positive', 0) * 10 
     - scores.get('negative', 0) * 5 
     + scores.get('neutral', 0) * 2) * factor
)

# Input data
feedback_texts = [
    "good performance overall",
    "excellent teamwork and excellent initiative",
    "poor attendance but adequate output",
    "average discipline",
    "bad attitude despite good technical skills"
]

team_member_count = 8
adjustment_factor = 1.05

# Step 1: Analyze raw feedback
sentiment_distribution, entry_count = analyze_feedback(feedback_texts)

# Step 2: Apply team-based adjustment
adjusted_sentiments = adjust_for_bias(team_member_count, sentiment_distribution)

# Step 3: Compute final performance score
final_score = evaluate_performance(adjusted_sentiments, adjustment_factor)

# Print result for extraction
case_normalizer = lambda s: s.upper() if len(s) % 2 == 0 else s.lower()
size_proxy = entry_count * 3.14

Result: {final_score}