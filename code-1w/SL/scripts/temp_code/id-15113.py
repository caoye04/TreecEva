from itertools import combinations

def analyze_trends(data, threshold):
    trend_count = 0
    magnitude_sum = 0.0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if abs(diff) > threshold:
            trend_count += 1
            magnitude_sum += abs(diff)
    avg_magnitude = magnitude_sum / trend_count if trend_count > 0 else 0
    return trend_count, avg_magnitude

def calculate_stability(ratios):
    variance = sum((x - sum(ratios)/len(ratios))**2 for x in ratios) / len(ratios)
    return 1 / (1 + variance)

def evaluate_performance(metrics, base):
    adjusted_metrics = [m * 1.1 for m in metrics if m > base]
    temp_sum = sum(adjusted_metrics)
    
    # Distractor: irrelevant stability calculation on subset
    subset = [metrics[i] for i in range(0, len(metrics), 2)]
    stability = calculate_stability(subset) if subset else 1.0
    
    # Real logic: count significant pairwise deviations above base
    pairs = list(combinations(adjusted_metrics, 2))
    dev_count = 0
    for a, b in pairs:
        if abs(a - b) > base * 0.5:
            dev_count += 1
    
    # Secondary distractor: unused nested loop over dummy states
    states = ['idle', 'active', 'pending']
    state_counter = 0
    for s in states:
        for _ in range(len(metrics)):
            state_counter += 1
    
    # Final score depends only on dev_count and temp_sum
    final_score = dev_count * 2 + int(temp_sum)
    return final_score

# Main execution
raw_data = [12, 15, 14, 18, 22, 25]
baseline = 16

# Extract growth rates as metrics
metrics = []
for i in range(1, len(raw_data)):
    growth = (raw_data[i] - raw_data[i-1]) / raw_data[i-1] * 100
    metrics.append(growth)

# Call the key function
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")