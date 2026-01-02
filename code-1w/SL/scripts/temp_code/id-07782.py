def process_feedback(reviews, weights):
    adjusted_totals = []
    scaling_factor = 1.2
    base_offset = 5
    temp_sum = 0
    noise_correction = 0.01

    for review in reviews:
        raw_value = len(review.strip())
        normalized = raw_value * 0.1
        
        # Irrelevant string processing (distractor)
        uppercase_chars = sum(1 for c in review if c.isupper())
        exclamation_count = review.count('!')
        padded_length = len(review) + uppercase_chars  # Unused

        if 'excellent' in review.lower():
            temp_sum += 10
        elif 'poor' in review.lower():
            temp_sum -= 5
        else:
            temp_sum += 3

        adjusted_totals.append(normalized)

    # Secondary logic path with partial relevance
    total_adjusted = sum(adjusted_totals)
    weighted_temp = 0
    for i, w in enumerate(weights):
        weighted_temp += w * (i + 1)  # Simulates positional weighting, semi-relevant

    # Core logic obscured by distractions
    final_score = int((temp_sum * scaling_factor) + base_offset - weighted_temp)
    
    # Dead code branch (distractor)
    if noise_correction > 1:
        final_score = int(final_score / noise_correction)

    return final_score

# Input data
reviews = [
    "Excellent service and great staff!",
    "Poor quality for the price.",
    "Average experience, nothing special",
    "excellent overall - very satisfied"
]
weights = [0.5, 0.3, 0.7, 0.4]

# Execution point
final_score = process_feedback(reviews, weights)
print(f"Result: {final_score}")