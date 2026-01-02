from itertools import compress, count

def analyze_sentiment(texts):
    scores = []
    for text in texts:
        upper_count = sum(1 for c in text if c.isupper())
        lower_count = sum(1 for c in text if c.islower())
        net_tone = upper_count - lower_count  # More uppercase = harsher tone
        sentiment_score = 1 if net_tone < 2 else 2
        scores.append(sentiment_score)
    return scores

def filter_valid_entries(logs, min_length=5):
    valid = []
    for log in logs:
        if len(log) >= min_length and 'ERROR' not in log:
            valid.append(True)
        else:
            valid.append(False)
    return valid

def evaluate_performance(feedback, threshold):
    # Step 1: Analyze emotional tone of feedback
    tone_levels = analyze_sentiment(feedback)
    
    # Step 2: Validate entries (some may be corrupted)
    is_valid = filter_valid_entries(feedback)
    
    # Step 3: Use itertools to align data
    filtered_tones = list(compress(tone_levels, is_valid))
    
    # Irrelevant distraction: counting characters (not used later)
    total_chars = 0
    for entry in feedback:
        for char in entry:
            total_chars += 1
    avg_chars = total_chars / len(feedback) if feedback else 0
    size_metric = avg_chars * 0.7  # Dead computation
    
    # Step 4: Apply dynamic weighting based on position using slicing
    recent_feedback = tone_levels[-3:]  # Focus on last three
    base_score = sum(recent_feedback)
    
    # Step 5: Adjust score based on threshold comparison
    adjustment = 0
    running = count(1)
    for i, tone in enumerate(tone_levels):
        if tone >= 2 and i % 2 == 0:
            adjustment += next(running)
        else:
            next(running)
    
    # Step 6: Final calculation
    raw_score = base_score + adjustment
    if raw_score > threshold:
        final_score = raw_score * 1.5
    else:
        final_score = raw_score * 0.8
    
    # Key assignment point
    final_score = int(final_score)
    return final_score

# Input data
feedback_responses = [
    "Great work!",
    "NOT satisfied with service.",
    "excellent as always",
    "FANTASTIC support team!",
    "Could be better."
]
threshold_limit = 10

# Execute main logic
tone_analysis = analyze_sentiment(feedback_responses)
valid_mask = filter_valid_entries(feedback_responses)
final_score = evaluate_performance(feedback_responses, threshold_limit)
print(f"Result: {final_score}")