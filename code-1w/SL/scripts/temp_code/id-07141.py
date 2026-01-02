from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 92, 85, 76, 88, 95, 82, 91, 87, 83]
    metrics = defaultdict(int)
    
    for i, val in enumerate(raw_data):
        if val > 85:
            metrics['high_count'] += 1
            metrics['sum_high'] += val
        else:
            metrics['low_count'] += 1
            metrics['sum_low'] += val

    metrics['total'] = sum(raw_data)
    metrics['average'] = metrics['total'] / len(raw_data)
    
    # Distractor: irrelevant tracking
    temp_buffer = [x ** 0.5 for x in raw_data if x % 2 == 0]
    buffer_sum = sum(temp_buffer)
    
    return metrics

# Analyze trend stability (irrelevant to final score but adds cognitive load)
def analyze_trend(data_dict):
    sequence = []
    for key in ['high_count', 'low_count', 'sum_high', 'sum_low']:
        if key in data_dict:
            sequence.append(data_dict[key] % 10)
    
    stability = 0
    for i in range(1, len(sequence)):
        stability += abs(sequence[i] - sequence[i-1])
    
    # Dead computation - not used later
    if stability > 10:
        adjustment_factor = -1
    else:
        adjustment_factor = 1
    
    return stability  # Unused in main logic

# Core evaluation logic
def evaluate_performance(metrics, threshold):
    base_score = 0
    
    if metrics['average'] >= threshold:
        base_score += 25
    
    if metrics['high_count'] >= 4:
        base_score += 15
    
    # Bonus for balanced distribution
    imbalance = abs(metrics['high_count'] - metrics['low_count'])
    if imbalance <= 2:
        base_score += 10
    
    # Arbitrary penalty for low total (distractor logic)
    dummy_penalty = 0
    if metrics['total'] < 800:
        dummy_penalty = 5  # Never applied due to actual data
    
    # Final nonlinear adjustment
    final_score = (base_score ** 1.1) + (metrics['sum_high'] // 10)
    
    # Irrelevant logging
    log_entry = f"Score computed: {final_score:.2f}"
    
    return int(final_score)

# Main execution
if __name__ == "__main__":
    collected = collect_metrics()
    _ = analyze_trend(collected)  # Call with no effect
    threshold = 85.0
    final_score = evaluate_performance(collected, threshold)
    print(f"Result: {final_score}")