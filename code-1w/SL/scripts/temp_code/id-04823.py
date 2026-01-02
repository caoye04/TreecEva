def analyze_performance(scores, threshold=60):
    # Irrelevant transformation: convert to percentages (already in %)
    adjusted_scores = [min(s * 1.1, 100) for s in scores]
    
    # Distractor: unused statistical measures
    mean_score = sum(scores) / len(scores)
    variance_proxy = sum((s - mean_score) ** 2 for s in scores)
    stdev_estimate = variance_proxy ** 0.5

    # Track passing status with list comprehension
    passed = [score >= threshold for score in scores]
    pass_rate = sum(passed) / len(passed)

    # Compute weighted contribution of high performers
    bonus_weights = [1.2 if s >= 85 else 1.0 for s in scores]
    weighted_total = sum(score * weight for score, weight in zip(scores, bonus_weights))

    # Secondary metric: efficiency ratio (not used in final score)
    efficiency_ratio = (weighted_total / sum(scores)) if sum(scores) > 0 else 0

    # Apply non-linear scaling based on pass rate
    scaling_factor = 1.0
    if pass_rate >= 0.7:
        scaling_factor += 0.1
    elif pass_rate >= 0.5:
        scaling_factor += 0.05

    # Final adjustment using only original scores and pass logic
    base_score = sum(scores) / len(scores)
    extra_credit = 5 if all(p == True for p in passed[-3:]) else 0  # last three passed?
    final_score = int(base_score * scaling_factor + extra_credit)

    # Red herring: unused complex calculation
    phantom_metric = max(adjusted_scores) - min(adjusted_scores) if len(scores) > 1 else 0
    decay_correction = sum(s * (0.95 ** i) for i, s in enumerate(reversed(scores)))

    return final_score

# Simulate student test results
exam_results = [78, 82, 65, 91, 88, 73, 90, 85, 87, 89]

# Unused preprocessing: normalize scores to z-scores
mean_exam = sum(exam_results) / len(exam_results)
z_scores = [(x - mean_exam) / 8.5 for x in exam_results]  # arbitrary std dev

# Noise variable: historical average drift
historical_trend = sum(exam_results[i] - exam_results[i-1] for i in range(1, len(exam_results)))

# Key execution point
final_score = analyze_performance(exam_results)

# Output result
print(f"Result: {final_score}")