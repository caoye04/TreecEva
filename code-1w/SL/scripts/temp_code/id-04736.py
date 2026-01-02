from collections import Counter, defaultdict

# Simulate user feedback analysis for a training module
def analyze_feedback(responses):
    sentiment_count = Counter()
    total_entries = 0
    ignored_keywords = ['maybe', 'unsure', 'neutral']
    
    for response in responses:
        words = response.lower().split()
        if 'excellent' in words or 'great' in words:
            sentiment_count['positive'] += 1
        elif 'poor' in words or 'bad' in words:
            sentiment_count['negative'] += 1
        else:
            sentiment_count['neutral'] += 1
        total_entries += 1

    # Irrelevant aggregation
    stats = defaultdict(int)
    for word, count in sentiment_count.items():
        stats[f'total_{word}'] += count * 2  # Distractor computation

    return dict(sentiment_count)

# Process performance metrics
def calculate_baseline(metrics):
    base = 0
    penalty = 0
    for key, value in metrics.items():
        if 'accuracy' in key:
            base += value * 10
        elif 'latency' in key and value > 50:
            penalty += 5
    adjusted = base - penalty
    if adjusted < 0:
        adjusted = 0
    return adjusted

# Main evaluation logic
def evaluate_performance(counts, factor):
    pos = counts.get('positive', 0)
    neg = counts.get('negative', 0)
    net_sentiment = pos - neg
    
    # Secondary adjustment using distractor variable
    temp_buffer = [pos + 1, neg + 1]
    ratio = temp_buffer[0] / temp_buffer[1] if temp_buffer[1] > 0 else 1
    
    result = net_sentiment * factor * ratio
    final_value = int(result)  # Rounded down to integer
    
    # Dead code branch (never executed under current logic)
    if False:
        backup = pos * neg
        final_value += backup  # Never reached
    
    return final_value

# Input data
feedback_responses = [
    "great job on accuracy",
    "poor latency performance",
    "excellent results overall",
    "bad user experience",
    "great improvement in speed"
]

performance_metrics = {
    'accuracy_rate': 8.5,
    'latency_ms': 60,
    'throughput': 200
}

# Step 1: Analyze sentiment
raw_feedback = analyze_feedback(feedback_responses)

# Step 2: Compute baseline score (unused but computed)
baseline_score = calculate_baseline(performance_metrics)  # Distractor

# Step 3: Determine adjustment factor based on arbitrary rule
adjustment_factor = 3
if raw_feedback.get('neutral', 0) < 2:
    adjustment_factor *= 1.5

# Key execution point
final_score = evaluate_performance(raw_feedback, adjustment_factor)

print(f"Result: {final_score}")