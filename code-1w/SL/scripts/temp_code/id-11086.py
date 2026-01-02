from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 135, 140, 128, 150, 160, 155, 170, 180, 175]
    metrics = defaultdict(int)
    
    for i, value in enumerate(data):
        if value > 130:
            metrics['high_count'] += 1
            metrics['cumulative_high'] += value
        if i % 2 == 0:
            metrics['even_index_sum'] += value  # Irrelevant distractor

    metrics['overall_avg'] = sum(data) / len(data)
    return metrics

# Baseline comparator
def establish_baseline():
    base = {}
    base['threshold'] = 135
    base['grace_period'] = 5  # Unused field
    base['min_duration'] = 3
    return base

# Secondary helper - computes trend (not used directly in final logic)
def compute_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return abs(trend)  # Distractor computation

# Main evaluation logic
def evaluate_performance(metrics, baseline):
    score = 0
    adjustments = []
    
    # Core scoring logic
    if metrics['high_count'] >= 6:
        score += 25
    
    if metrics['cumulative_high'] > 1000:
        score += 35
    
    temp_var = metrics['even_index_sum'] * 0.1  # Computation with no impact
    adjustments.append(temp_var)
    
    # Simulated correction factor
    correction = 1.0
    if metrics['overall_avg'] > 150:
        correction = 0.9
    
    intermediate = score * correction
    
    # Additional check
    if intermediate >= 30:
        intermediate += 10
    
    # Final adjustment based on arbitrary rule
    final_score = int(intermediate + 5)
    
    # Dead code branch - never executed due to logic above
    if correction < 0.8:
        final_score = int(final_score * 0.8)
    
    return final_score

# Execution flow
def main():
    raw_data = [120, 135, 140, 128, 150, 160, 155, 170, 180, 175]
    trend_value = compute_trend(raw_data)  # Call with no downstream effect
    
    metrics = collect_metrics()
    baseline = establish_baseline()
    final_score = evaluate_performance(metrics, baseline)
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()