def evaluate_performance(feedback, rating):
    # Normalize feedback string
    cleaned = feedback.strip().lower().replace('!', '').replace('.', '')
    words = cleaned.split()
    
    # Irrelevant metrics (distractor computations)
    word_count = len(words)
    avg_word_length = sum(len(w) for w in words) / word_count if word_count > 0 else 0
    sentiment_boost = 0.0
    
    if 'excellent' in words:
        sentiment_boost += 0.8
    elif 'good' in words:
        sentiment_boost += 0.4
    elif 'poor' in words:
        sentiment_boost -= 0.5
    elif 'unsatisfactory' in words:
        sentiment_boost -= 0.9

    # Secondary logic path with dead end (not used)
    temp_adjustment = 0
    for i in range(3):
        temp_adjustment += i * 2
    temp_adjustment = temp_adjustment ** 2  # Unused computation

    # Actual scoring logic
    modifier = 0
    if rating >= 8:
        if 'consistently' in words:
            modifier += 2
        if 'reliable' in words or 'dependable' in words:
            modifier += 1
    elif rating < 5:
        if 'improvement' in feedback:
            modifier += 1  # small positive if mentioned
        else:
            modifier -= 1

    # Nested condition with red herring variable
    performance_level = ""
    if rating + modifier > 9:
        performance_level = "outstanding"
    elif rating + modifier > 7:
        performance_level = "strong"
    else:
        performance_level = "needs_work"

    # Distractor: complex string formatting not affecting result
    report_line = f"Performance: {performance_level.upper()[:3]} | Score: {rating:.1f}"
    report_checksum = sum(ord(c) for c in report_line) % 100

    # Core calculation
    raw_score = rating + modifier + sentiment_boost
    
    # Final clamping and rounding
    final_score = max(1.0, min(10.0, round(raw_score, 2)))
    return final_score

# Simulated input data
feedback_str = "The employee performed excellently and was consistently reliable!"
base_rating = 8.5
audit_log = [len(feedback_str), feedback_str.count('e'), feedback_str.startswith('The')]

# Dead code block — misleading state tracking
status_tracker = {}
for idx, log in enumerate(audit_log):
    status_tracker[f'entry_{idx}'] = log * 17

# Key execution point
final_score = evaluate_performance(feedback_str, base_rating)

print(f"Result: {final_score}")