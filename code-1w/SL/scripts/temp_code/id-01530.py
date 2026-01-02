def calculate_adjusted_score(scores, thresholds):
    adjusted = []
    for i, (score, threshold) in enumerate(zip(scores, thresholds)):
        if score >= threshold:
            adjusted.append(score * (i + 1))
    return adjusted

# Raw data from user attempts
scores = [85, 72, 90, 60, 77]
thresholds = [70, 65, 88, 62, 75]

# Apply adjustment logic based on performance tier
adjusted_scores = calculate_adjusted_score(scores, thresholds)

# Filter only top-performing adjusted entries
valid_scores = [s for i, s in enumerate(adjusted_scores) if s > 80 or i % 2 == 0]

# Final aggregation step
result = sum(valid_scores)

# Irrelevant auxiliary variable (minimal distraction)
temp_debug = len(scores) - len(thresholds)

print(f"Result: {result}")