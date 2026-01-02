import itertools

def evaluate_performance(metrics):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    return weighted_sum

def analyze_trends(data_stream):
    trend_values = []
    for x, y in zip(data_stream, data_stream[1:]):
        if y > x:
            trend_values.append(1)
        elif y < x:
            trend_values.append(-1)
        else:
            trend_values.append(0)
    net_trend = sum(trend_values)
    dummy_calc = (net_trend ** 2 + 5) // 3  # Distractor computation
    return net_trend

def calculate_final_score(ranks, points):
    adjusted_points = [p * (10 - r) for r, p in zip(ranks, points)]
    bonus_eligible = sum(1 for ap in adjusted_points if ap > 50)
    
    # Simulate conditional bonus using conditional expression
    bonus = 10 if bonus_eligible >= 2 else (5 if bonus_eligible == 1 else 0)
    
    total_base = sum(adjusted_points)
    
    # Irrelevant set operation (distractor)
    unique_adjusted = set(adjusted_points)
    outlier_count = len([x for x in adjusted_points if x > 80])
    adjustment_factor = 1.0
    if outlier_count > 0:
        adjustment_factor = 0.95
    
    # Another distractor: unused itertools usage
    permutations = list(itertools.permutations([1, 2, 3], 2))
    permutation_sum = sum(a + b for a, b in permutations)  # Not used later
    
    final_score = int(total_base * adjustment_factor) + bonus
    return final_score

# Main execution
base_metrics = [85, 78, 90, 88]
score_weights = [0.25, 0.25, 0.25, 0.25]
raw_performance = evaluate_performance(base_metrics)

data_flow = [10, 12, 11, 15, 14]
trend_analysis = analyze_trends(data_flow)

rankings = [1, 3, 2, 4]
base_points = [20, 25, 30, 35]

# Key statement
final_score = calculate_final_score(rankings, base_points)

# Output result
print(f"Result: {final_score}")