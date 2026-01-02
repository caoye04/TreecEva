def process_results(data, limits):
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    adjusted = [val * 1.1 if val < 50 else val * 0.9 for val in normalized]  # Semi-relevant adjustment

    # Key slicing operation
    segment = adjusted[1:-1]  # Exclude first and last elements

    # Red herring: unused statistical calculation
    mean_val = sum(adjusted) / len(adjusted)
    variance_proxy = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted)

    # Lambda function to classify performance
    classify = lambda x: 1 if x >= limits[0] else (-1 if x < limits[1] else 0)
    classifications = [classify(val) for val in segment]

    # Actual logic: count positive trends in adjacent pairs
    trend_count = 0
    for i in range(len(segment) - 1):
        if segment[i+1] > segment[i]:
            trend_count += 1

    # Secondary logic: apply weight based on classification balance
    pos_class = sum(1 for c in classifications if c == 1)
    neg_class = sum(1 for c in classifications if c == -1)
    balance_factor = (pos_class - neg_class) * 0.5

    # Final computation chain
    base_score = sum(segment) // len(segment)
    adjustment = int(trend_count * balance_factor)
    final_score = base_score + adjustment

    # Dead code path (never executed but looks relevant)
    if False:
        final_score = max(normalized) - min(normalized)

    return final_score

# Main execution
raw_scores = [88, 72, 91, 45, 60, 77, 54, 83]
config_thresholds = [75, 50]

# Unused preprocessing steps (distractors)
deciles = sorted(raw_scores)[::2]
reversed_scores = raw_scores[::-1]

# Key data used in computation
assessment_data = [x - 5 if x % 2 == 0 else x + 3 for x in raw_scores]
thresholds = config_thresholds

# Critical statement
final_score = process_results(assessment_data, thresholds)

print(f"Result: {final_score}")