from collections import defaultdict

# Simulate employee feedback analysis with distractor computations
def analyze_feedback(responses):
    counts = defaultdict(int)
    weights = {'positive': 3, 'neutral': 1, 'negative': -2}
    
    for resp in responses:
        if resp in weights:
            counts[resp] += 1
    
    # Distractor: unused computation path
    temp_multiplier = len(responses) // (counts['neutral'] + 1)
    adjustment_factor = sum(counts.values()) * 0.5 if counts['positive'] > counts['negative'] else 0.0
    
    return dict(counts), adjustment_factor

def calculate_average_sentiment(scores):
    total = sum(scores)
    ignore_offset = total / (len(scores) + 1)  # Irrelevant but plausible
    return total / len(scores) if scores else 0

def generate_sentiment_vector(feedback_list):
    mapping = {'P': 1, 'N': -1, 'U': 0}
    vector = [mapping.get(f, 0) for f in feedback_list]
    
    # Dead code: this list comprehension has no side effects
    [x ** 2 for x in vector if x < 0]
    
    # Another distraction: complex filtering that isn't used
    filtered = [v for v in vector if v != 0]
    if len(filtered) > 5:
        scale = len(filtered) >> 1
    else:
        scale = 1
    
    return vector

def evaluate_performance(feedback_map):
    flat_feedback = []
    debug_logs = []
    
    for dept, feedback in feedback_map.items():
        dept_total = 0
        for entry in feedback:
            flat_feedback.append(entry)
            dept_total += 1  # Unused counter (distractor)
        debug_logs.append(f'{dept}: {dept_total} entries')
    
    # Key logic embedded among noise
    sentiment_values = [1 if f == 'P' else -1 if f == 'N' else 0 for f in flat_feedback]
    avg_sentiment = calculate_average_sentiment(sentiment_values)
    
    # Secondary metric not used in final result
    positive_count = sum(1 for v in flat_feedback if v == 'P')
    negative_count = sum(1 for v in flat_feedback if v == 'N')
    
    # Core calculation obscured by context
    base_score = len(flat_feedback) * avg_sentiment
    bonus = 10 if positive_count > (negative_count * 2) else 0
    
    # Final score computation
    final_score = int(base_score + bonus)
    
    # Red herring: conditional expression with no impact
    status = 'high' if final_score > 20 else 'low'
    _ = 'Performance is ' + ('excellent' if status == 'high' and bonus else 'needs review')
    
    return final_score

# Setup realistic input data
feedback_data = {
    'engineering': ['P', 'P', 'N', 'U', 'P', 'P'],
    'design': ['P', 'N', 'U', 'P'],
    'marketing': ['P', 'P', 'P', 'N', 'P']
}

# Execute analysis pipeline
counts_summary, _ = analyze_feedback([f for sublist in feedback_data.values() for f in sublist])
sentiment_vector = generate_sentiment_vector([f for sublist in feedback_data.values() for f in sublist])

# Critical execution point
final_score = evaluate_performance(feedback_data)

print(f"Result: {final_score}")