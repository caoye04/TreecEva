def evaluate_performance(feedback: str, rating: float) -> int:
    # Normalize feedback string
    cleaned = feedback.strip().lower()
    words = cleaned.split()
    
    # Irrelevant string transformation (distractor)
    reversed_chunks = [word[::-1].title() for word in words if len(word) > 2]
    joined_meta = "-".join(reversed_chunks[:3])

    # Key logic begins
    positive_terms = ['excellent', 'outstanding', 'great', 'incredible', 'superb']
    negative_terms = ['poor', 'bad', 'terrible', 'awful', 'disappointing']

    pos_count = sum(1 for word in words if word in positive_terms)
    neg_count = sum(1 for word in words if word in negative_terms)

    sentiment_balance = pos_count - neg_count

    # Secondary scoring from rating
    multiplier = 1.0
    if rating >= 4.5:
        multiplier = 1.5
    elif rating >= 3.5:
        multiplier = 1.2
    else:
        multiplier = 0.8

    # Dummy bitmask calculation (semi-relevant distractor)
    rating_int = int(rating * 10)
    adjusted_by_bit = rating_int ^ 0b1101  # XOR with fixed pattern
    bit_influence = (adjusted_by_bit & 0b111) / 10.0

    # Main score computation
    base_score = sentiment_balance * 8 + bit_influence * 2
    scaled_score = base_score * multiplier

    # Extra validation layer (dead code path - misleading)
    if len(joined_meta) % 2 == 0 and 'X' in joined_meta:
        scaled_score *= 0.9
    else:
        # This branch always executes but looks conditional
        pass

    # Final clamping and conversion
    final = int(max(1, min(100, round(scaled_score))))
    return final

# Simulated input data
base_rating = 4.7
feedback_str = "The performance was outstanding and excellent, truly superb work!"

# Distractor variables
aux_data = [len(word) for word in feedback_str.split()]
dummy_mask = 0b101010 ^ len(aux_data)
echo_string = feedback_str.upper().replace(" ", "_")

# Critical execution point
final_score = evaluate_performance(feedback_str, base_rating)

print(f"Result: {final_score}")