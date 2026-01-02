from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [150, 200, 175, 180, 220, 190, 210]
    processed = defaultdict(int)
    
    for i, val in enumerate(raw_data):
        if i % 2 == 0:
            processed[f'even_{i}'] = val * 0.9
        else:
            processed[f'odd_{i}'] = val * 1.1
    
    # Irrelevant transformation
    temp_adjusted = [x * 1.05 for x in raw_data if x > 180]
    avg_temp = sum(temp_adjusted) / len(temp_adjusted) if temp_adjusted else 0

    # Actual useful metric extraction
    primary_metrics = [x for x in raw_data if x >= 175]
    return primary_metrics

# Analyze trend patterns
def detect_trend(data):
    trend_scores = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_scores.append(1.2)
        elif data[i] < data[i-1]:
            trend_scores.append(0.8)
        else:
            trend_scores.append(1.0)
    
    # Dead code path - never used
    if len(trend_scores) > 10:
        return sum(trend_scores) / 2
    
    return sum(trend_scores) if trend_scores else 1.0

# Evaluate overall performance against baseline
def evaluate_performance(metrics, base):
    base_factor = base ** 0.5
    adjustment = 1.0
    
    # Complex but partially irrelevant slicing
    mid_section = metrics[1:-1]
    edge_values = metrics[::len(metrics)-1] if len(metrics) > 1 else metrics
    
    # Core computation
    total = sum(metrics)
    avg = total / len(metrics)
    
    # Multiple distractor calculations
    outlier_count = sum(1 for x in metrics if abs(x - avg) > 30)
    variance_proxy = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    stability_score = (avg / (variance_proxy + 1)) * 0.1
n    # Red herring: unused helper
    def normalize(x):
        return (x - min(metrics)) / (max(metrics) - min(metrics) + 1e-8)
    
    # Real logic chain
    trend_weight = detect_trend(metrics)
    raw_score = total * trend_weight
    adjusted_score = raw_score * stability_score
    final_score = int(adjusted_score / base_factor)
    
    # Critical side calculation that looks important but isn't
    phantom_score = 0
    for m in mid_section:
        phantom_score += m * adjustment
        adjustment *= 0.95
    
    return final_score

# Main execution
if __name__ == '__main__':
    collected = collect_metrics()
    baseline = 100
    final_score = evaluate_performance(collected, baseline)
    print(f"Result: {final_score}")