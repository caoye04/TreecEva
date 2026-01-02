from collections import defaultdict
import itertools

# Simulate system performance metrics over time
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant historical data (distractor)
historical_data = defaultdict(list)
for year in range(2018, 2023):
    historical_data[year] = [x - (year - 2020) for x in metrics]

# Misleading normalization attempt (not used in final calculation)
normalized_metrics = [m / max(metrics) for m in metrics]
scaled_metrics = [m * 100 for m in normalized_metrics]  # Red herring

# Auxiliary function with early return (semi-relevant)
def is_above_threshold(values, threshold=80):
    for v in values:
        if v > threshold:
            return True
    return False

# Check performance trend (irrelevant to final score)
trend_increasing = all(metrics[i] <= metrics[i+1] for i in range(len(metrics)-1))

temp_result = 0
for i in range(len(metrics)):
    temp_result += metrics[i] * weights[i]  # Weighted sum computation

# Additional distraction: pairwise combinations (unused)
pairwise_sums = [a + b for a, b in itertools.combinations(metrics, 2)]

# Simulate conditional adjustment (never triggers due to logic)
adjustment_factor = 0.9 if sum(metrics) > 500 and not trend_increasing else 1.0

# Core evaluation logic
final_score = 0
def evaluate_performance(mets, wts):
    score = 0.0
    for i in range(len(mets)):
        score += mets[i] * wts[i]
    return score

final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")