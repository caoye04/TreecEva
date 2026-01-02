from itertools import combinations

# Simulate employee performance evaluation with distraction metrics
base_metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant weight normalization (distractor)
normalized_weights = [w / sum(weights) for w in weights]

# Compute weighted average (relevant)
weighted_avg = sum(base_metrics[i] * weights[i] for i in range(len(base_metrics)))

# Generate all possible metric pairs (partially relevant - used later)
metric_pairs = list(combinations(base_metrics, 2))

# Distraction: analyze pair differences that won't be fully used
distance_analysis = [abs(a - b) for a, b in metric_pairs if a > 80 and b > 80]
mean_pair_distance = sum(distance_analysis) / len(distance_analysis) if distance_analysis else 0

# Simulate productivity index with red herring calculation
raw_productivity = weighted_avg * 1.05
adjustment_factor = mean_pair_distance * 0.1  # Slight influence, mostly noise
productivity = int(raw_productivity - adjustment_factor)

# Risk factor computation with dead-end logic
risk_candidates = [x for x in base_metrics if x < 85]
risk_factor = 0
for val in risk_candidates:
    if val < 80:
        risk_factor += 5
    else:
        risk_factor += 2  # This path is taken but partially irrelevant

# Dead code branch (never executed - distractor)
temporary_buffer = []
if False:
    for _ in range(10):
        temporary_buffer.append(hash(str(_)))

# Core evaluation logic
penalty = 0
if productivity > 90:
    penalty += risk_factor * 0.8
elif productivity > 80:
    penalty += risk_factor * 0.4
else:
    penalty += risk_factor * 1.2

# Final non-linear transformation (key step)
def evaluate_performance(prod, risk):
    base = prod * 0.95
    adjustment = (risk ** 0.5) * 1.1
    return int(base - adjustment)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")