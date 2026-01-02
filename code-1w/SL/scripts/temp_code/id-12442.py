def evaluate_performance(feedback, criteria):
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0

    # Irrelevant string processing (distractor)
    processed_feedback = [f.strip().lower() for f in feedback if len(f.strip()) > 0]
    unique_chars = set(''.join(processed_feedback))
    char_count_map = {c: ''.join(processed_feedback).count(c) for c in unique_chars}

    # Misleading statistical computation (dead path)
    avg_length = sum(len(f) for f in processed_feedback) / len(processed_feedback) if processed_feedback else 0
    length_deviation = abs(avg_length - 5.0)

    # Actual logic begins: count positive vs negative keywords
    positive_terms = {'excellent', 'good', 'optimal', 'efficient'}
    negative_terms = {'poor', 'bad', 'inefficient', 'subpar', 'flawed'}

    pos_count = 0
    neg_count = 0
    for comment in feedback:
        words = comment.lower().split()
        pos_count += len(set(words) & positive_terms)
        neg_count += len(set(words) & negative_terms)

    # Apply modular arithmetic to simulate cyclical review weighting
    cycle_offset = (pos_count + neg_count) % 4
    if cycle_offset == 0:
        bonus_multiplier = 1.2
    elif cycle_offset == 2:
        penalty_adjustment = -1

    # Core scoring logic
    raw_score = (pos_count * 3) - (neg_count * 2)
    adjusted_score = raw_score + penalty_adjustment
    final_score = int(adjusted_score * bonus_multiplier)

    # Additional distraction: unused data structure manipulation
    summary_stats = {
        'total_comments': len(feedback),
        'sentiment_ratio': pos_count / (neg_count + 1),
        'net_tone': 'positive' if pos_count > neg_count else 'negative'
    }

    # Key execution point
    final_score = evaluate_performance(feedback_set, benchmark)

    # Print result as required
    print(f"Result: {final_score}")

# Setup inputs
feedback_set = [
    "The excellent model showed optimal efficiency",
    "Good performance but has inefficiencies",
    "Poor accuracy in some cases",
    "Flawed logic detected, needs improvement",
    "Efficient and excellent overall"
]
benchmark = 'default'

# Initialize before function call
final_score = 0