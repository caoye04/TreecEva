def analyze_trends(data, threshold=0.5):
    trend_scores = []
    temp_buffer = []

    for i, value in enumerate(data):
        if value > threshold:
            temp_buffer.append(value * (i + 1))
        else:
            temp_buffer.append(value / (i + 1) if i > 0 else 0)
    
    # Irrelevant normalization (distractor)
    normalized = [x / max(temp_buffer) for x in temp_buffer if max(temp_buffer) > 0]
    smoothed = list(map(lambda x: round(x, 3), normalized))

    # Actual relevant logic hidden among distractions
    raw_sum = sum(temp_buffer)
    penalty = len([x for x in data if x < 0.3])
    adjustment = raw_sum * 0.1 if penalty > 2 else 0
    trend_scores.append(raw_sum - adjustment)

    return trend_scores[0] if trend_scores else 0


def evaluate_performance(metrics, weights):
    weighted_sum = 0
    extra_tracking = []

    # Use of zip and enumerate together (required Python features)
    for idx, (m, w) in enumerate(zip(metrics, weights)):
        boosted = m + (idx * 0.05)
        contribution = boosted * w
        weighted_sum += contribution
        
        # Dead code path - misleading tracking
        if idx % 5 == 0:
            extra_tracking.append(contribution ** 0.5)

    # Secondary calculation with partial relevance
    base_total = sum(metrics) * sum(weights)
    inflation_factor = 1.05
    
    # Final score influenced only by weighted_sum and one conditional
    if base_total > 2.0:
        final = weighted_sum * inflation_factor
    else:
        final = weighted_sum

    # Red herring: complex but unused computation
    shadow_score = sum([w * (m ** 2) for m, w in zip(metrics, weights)])
    shadow_score = round(shadow_score, 4)

    return int(round(final * 100))  # Convert to integer scale

# Main execution
raw_data = [0.65, 0.72, 0.58, 0.83, 0.41]
weights_list = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distractor function call with unused result
_ = analyze_trends(raw_data, threshold=0.4)

# Key statement
final_score = evaluate_performance(raw_data, weights_list)

print(f"Result: {final_score}")