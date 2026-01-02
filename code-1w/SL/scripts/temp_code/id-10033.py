def analyze_trend(data, threshold=0.5):
    trend = []
    for i, value in enumerate(data):
        if value > threshold:
            trend.append(1)
        elif value < -threshold:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Irrelevant helper function (dead path)
def compute_entropy(values):
    from math import log
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total if total != 0 else 1 / len(values)
        entropy -= prob * log(prob + 1e-9)
    return round(entropy, 4)

# Another decoy: unused transformation
def transform_scale(x, a=2.5, b=-1.3):
    return a * x ** 2 + b * x

# Misleading intermediate metric
def get_volatility(series):
    diffs = [abs(series[i] - series[i-1]) for i in range(1, len(series))]
    return sum(diffs) / len(diffs) if diffs else 0

# Core logic buried among distractions
def evaluate_performance(metrics, weights):
    adjusted = []
    for idx, (m, w) in enumerate(zip(metrics, weights)):
        if idx % 2 == 0:
            adjusted.append(m * w + 0.1)
        else:
            adjusted.append(m * w - 0.05)

    # Apply non-linear correction on specific positions
    for j, val in enumerate(adjusted):
        if j in [1, 3]:
            adjusted[j] = abs(val) ** 0.5 if val >= 0 else -abs(val) ** 0.5

    base_score = sum(adjusted)

    # Conditional boost based on pattern detection
    trend_pattern = [1 if x > 0 else -1 if x < 0 else 0 for x in metrics]
    positive_runs = 0
    current_run = 0
    for p in trend_pattern:
        if p == 1:
            current_run += 1
        else:
            if current_run >= 2:
                positive_runs += current_run
            current_run = 0
    if current_run >= 2:
        positive_runs += current_run

    bonus = 0.25 * positive_runs if positive_runs > 0 else 0

    # Final aggregation with integer weighting
    raw_total = int(base_score * 100) + int(bonus * 50)

    # Red herring: unused complex structure
    snapshot = {
        'momentum': [x for x in metrics if x > 0.4],
        'drag': [x for x in metrics if x < -0.3],
        'inertia': sum(1 for x in metrics if -0.1 <= x <= 0.1)
    }

    # Actual answer computation
    penalty = len([w for w in weights if w < 0.2]) * 7
    final_score = raw_total - penalty

    # Decoy print (never executed in logic flow)
    # print(f'Debug: snapshot={snapshot}, entropy={compute_entropy([1,2,3])}')

    return final_score

# Irrelevant data initialization
dummy_data = [0.1 * (i % 3) for i in range(12)]
trend_analysis = analyze_trend(dummy_data, threshold=0.15)
volatility = get_volatility(dummy_data)

# Main execution context
metrics = [0.85, -0.12, 0.93, 0.41, 0.67]
weights = [0.35, 0.52, 0.18, 0.74, 0.29]

# Unused slicing distraction
subset_a = metrics[1:4:1]
subset_b = weights[::-1]
pair_data = list(zip(subset_a, subset_b[:3]))

# Key statement
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")