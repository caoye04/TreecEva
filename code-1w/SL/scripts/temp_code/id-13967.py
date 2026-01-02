from itertools import compress, cycle

def evaluate_performance(metrics, baseline):
    # Normalize metrics using z-score like transformation (only some are relevant)
    mean_val = sum(metrics) / len(metrics)
    std_dev = (sum((x - mean_val) ** 2 for x in metrics) / len(metrics)) ** 0.5
    normalized = [(x - mean_val) / std_dev for x in metrics] if std_dev != 0 else metrics

    # Irrelevant: Simulate time-series smoothing (not used in final logic)
    smoothed = []
    for i, val in enumerate(normalized):
        window = normalized[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))

    # Distractor: complex flag logic with dead end
    critical_flags = [False] * len(normalized)
    for i in range(len(normalized)):
        if normalized[i] > 0.5:
            critical_flags[i] = True
        elif normalized[i] < -0.5:
            critical_flags[i] = False  # Redundant assignment

    # Only the first 4 metrics are actually used
    relevant_metrics = normalized[:4]

    # Baseline comparison with vectorized thresholding (semi-relevant computation)
    above_baseline = [nm > bl for nm, bl in zip(relevant_metrics, baseline)]

    # Weighted scoring: only odd-indexed weights matter due to masking
    weights = [0.8, 1.2, 0.9, 1.1]
    mask = [i % 2 == 1 for i in range(len(weights))]  # Only indices 1 and 3 count
    masked_weights = list(compress(weights, mask))
    masked_scores = list(compress(relevant_metrics, mask))

    # Actual score computation (key path)
    raw_score = sum(ms * mw for ms, mw in zip(masked_scores, masked_weights))

    # Irrelevant: attempt to fit trendline (dead code path)
    trend = 0.0
    for x, y in zip(cycle([1, 2]), enumerate(relevant_metrics)):
        if x > y[0]:
            trend += x * y[1]

    # Final adjustment based on logical conditions (short-circuit evaluation)
    bonus = 10 if all(above_baseline) and len(relevant_metrics) >= 4 else 0
    penalty = 5 if not any(critical_flags) or std_dev == 0 else 0

    # Core answer calculation
    final_score = raw_score * 100 + bonus - penalty

    return final_score

# Setup inputs
metrics = [85, 92, 78, 96, 88, 73, 91, 80]
baseline = [0.5, 0.7, 0.6, 0.8]

# Execute key statement
target_result = evaluate_performance(metrics, baseline)
print(f"Target result: {target_result}")