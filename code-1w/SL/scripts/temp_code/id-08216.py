from itertools import combinations

def analyze_trends(data_points):
    trends = []
    for i in range(1, len(data_points)):
        if data_points[i] > data_points[i-1]:
            trends.append(1)
        elif data_points[i] < data_points[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def calculate_volatility(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0

def filter_anomalies(values, threshold=2):
    mean_val = sum(values) / len(values)
    devs = [(v - mean_val) ** 2 for v in values]
    std_dev = (sum(devs) / len(devs)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def evaluate_performance(weights, outcomes):
    # Normalize weights
    total_weight = sum(weights)
    normalized = [w / total_weight for w in weights]
    
    # Apply transformation to outcomes
    adjusted = []
    for x in outcomes:
        if x > 75:
            adjusted.append(x * 1.1)
        elif x < 25:
            adjusted.append(x * 0.9)
        else:
            adjusted.append(x)
    
    # Simulate sensitivity analysis (distraction)
    sensitivity_check = 0
    for pair in combinations(adjusted, 2):
        sensitivity_check += abs(pair[0] - pair[1])
    sensitivity_check /= len(adjusted)**2 if adjusted else 1
    
    # Irrelevant trend analysis
    trend_sequence = analyze_trends(adjusted)
    positive_trends = sum(1 for t in trend_sequence if t == 1)
    negative_trends = sum(1 for t in trend_sequence if t == -1)
    
    # Real scoring logic
    raw_score = sum(n * a for n, a in zip(normalized, adjusted))
    volatility_penalty = calculate_volatility(adjusted) * 0.5
    
    # Final computation
    final_score = raw_score - volatility_penalty
    
    # Dead code - never used
    if final_score < 0:
        final_score = 0
    
    return final_score

# Main execution
metric_weights = [3, 7, 5, 8]
raw_outcomes = [68, 72, 76, 81]

# Preprocessing distraction
filtered_data = filter_anomalies(raw_outcomes)
duplicate_check = set(raw_outcomes) != set(filtered_data)

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")