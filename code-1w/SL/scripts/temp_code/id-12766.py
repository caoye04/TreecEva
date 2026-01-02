def analyze_feedback(reviews):
    positive_keywords = {'excellent', 'great', 'good', 'amazing', 'outstanding'}
    negative_keywords = {'poor', 'bad', 'terrible', 'awful', 'disappointing'}
    score = 0
    feedback_set = set()
    
    for review in reviews:
        words = review.lower().split()
        matched = False
        
        # Analyze sentiment with keyword matching
        for word in words:
            cleaned = word.strip('.,!?"')
            if cleaned in positive_keywords:
                score += 2
                feedback_set.add(cleaned)
                matched = True
            elif cleaned in negative_keywords:
                score -= 3
                feedback_set.discard(cleaned)  # Irrelevant operation: discard non-existent
                matched = True
        
        if not matched:
            score -= 1  # Neutral reviews slightly penalized

    return score, feedback_set

# Baseline metrics from previous quarter
def compute_trend(current, previous):
    trend_vals = []
    for i in range(len(current)):
        if previous[i] == 0:
            trend_vals.append(100 if current[i] > 0 else 0)
        else:
            change = (current[i] - previous[i]) / previous[i] * 100
            trend_vals.append(round(change, 2))
    return trend_vals  # Unused in final logic

def evaluate_performance(feedback, base):
    raw_score = sum(ord(ch) for ch in feedback) % 100
    adjustment = len(base.get('metrics', [])) - len(base.get('flags', []))
    # Complex but irrelevant transformation
    temp_data = [raw_score + i for i in range(5) if i % 2 == 0]
    temp_sum = sum(temp_data) // 3 if temp_data else 0
    
    # Actual scoring uses only raw_score and fixed offset
    result = raw_score - 10  # Key computation
    return result

# Simulated input data
customer_reviews = [
    "The product was excellent and amazing!",
    "Terrible quality, very disappointing experience.",
    "It's okay, nothing special.",
    "Great value for money, good performance",
    "Poor design but fast delivery"
]

baseline_metrics = {
    'version': '2.1',
    'metrics': ['latency', 'uptime', 'response'],
    'flags': ['deprecated_api']
}

# Execution flow
aggregate_score, feedback_tokens = analyze_feedback(customer_reviews)

# Extraneous intermediate processing
token_count_map = {token: len(token) for token in feedback_tokens}
duplicate_check = set(token_count_map.keys()) & feedback_tokens  # Redundant

# Misleading normalization step
normalized_tokens = [t.upper() for t in feedback_tokens if t.startswith('g')]
placeholder_result = len(normalized_tokens) * 5  # Dead-end variable

final_score = evaluate_performance(feedback_tokens, baseline_metrics)

print(f"Result: {final_score}")