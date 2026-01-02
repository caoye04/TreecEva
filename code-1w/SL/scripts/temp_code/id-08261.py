def analyze_trend(values):
    trend_scores = []
    for i, val in enumerate(values):
        if i == 0:
            trend_scores.append(0)
        else:
            diff = val - values[i-1]
            trend_scores.append(1 if diff > 0 else (-1 if diff < 0 else 0))
    return trend_scores

values = [15, 18, 16, 20, 22, 21]
trend_analysis = analyze_trend(values)

# Misleading intermediate computation (distractor)
cumulative_shift = 0
for shift in trend_analysis:
    cumulative_shift += shift * 2  # Not used in final result

baseline = sum(values) / len(values)
adjusted_values = [v - baseline for v in values]

# Simulate benchmark confidence levels (irrelevant to final score)
confidence_levels = []
for idx, adj in enumerate(adjusted_values):
    conf = 0.5 + (abs(adj) * 0.1)
    confidence_levels.append(round(conf, 2))

# Create paired index-value mapping (semi-relevant)
indexed_metrics = list(enumerate(adjusted_values))
pairwise_deltas = [indexed_metrics[i+1][1] - indexed_metrics[i][1] for i in range(len(indexed_metrics)-1)]

# Introduce red herring: unused transformation
transformed_deltas = []
scaling_factor = 1.5
for d in pairwise_deltas:
    transformed_deltas.append(d * scaling_factor if d > 0 else d * 0.5)

# Actual scoring logic
positive_momentum = sum(1 for d in pairwise_deltas if d > 0)
negative_momentum = sum(1 for d in pairwise_deltas if d < 0)
neutral_momentum = sum(1 for d in pairwise_deltas if d == 0)

momentum_ratio = (positive_momentum + 1) / (negative_momentum + 1)  # Avoid division by zero

# Secondary metric: consistency streak
max_streak = current_streak = 0
for t in trend_analysis:
    if t == 1:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

streak_bonus = max_streak * 2

# Benchmark data structure
benchmark_data = {
    'metrics': adjusted_values,
    'deltas': pairwise_deltas,
    'trends': trend_analysis,
    'baseline_deviation': sum(abs(x) for x in adjusted_values)
}

# Core calculation function
def calculate_performance(data):
    raw_performance = sum(data['metrics'])
    delta_contribution = sum(d for d in data['deltas'] if d > 0)
    trend_weight = sum(t for t in data['trends'] if t > 0)
    
    # Irrelevant filtering (distractor)
    filtered_trends = [t for t in data['trends'] if t != 0]
    noise_level = len(filtered_trends) - len(data['trends']) // 2  # Fake metric
    
    # Real formula
    score = raw_performance + delta_contribution + trend_weight
    return int(score)

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")