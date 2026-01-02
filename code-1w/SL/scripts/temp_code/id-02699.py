def evaluate_performance(metrics, baseline):
    # Irrelevant transformation (distractor)
    adjusted_metrics = [x * 1.05 for x in metrics if x > 70]
    
    # Semi-relevant filtering
    above_baseline = [m for m in metrics if m >= baseline]
    below_baseline = [m for m in metrics if m < baseline]
    
    # Dummy statistical computation (not used in final logic)
    avg_deviation = sum(abs(m - baseline) for m in metrics) / len(metrics) if metrics else 0
    
    # Key logic begins: count how many times consecutive metrics improve
    improvement_streaks = 0
    for i in range(1, len(metrics)):
        if metrics[i] > metrics[i-1]:
            improvement_streaks += 1

    # Use of set operations to identify unique performance bands (semi-relevant)
    performance_bands = set()
    for m in metrics:
        if m >= 90:
            performance_bands.add('excellent')
        elif m >= 80:
            performance_bands.add('good')
        elif m >= 70:
            performance_bands.add('fair')
        else:
            performance_bands.add('poor')
    
    # Conditional expression with slicing: determines weight based on trend
    recent_trend = metrics[-3:] if len(metrics) >= 3 else metrics
    trend_factor = 1.2 if sum(recent_trend) / len(recent_trend) > baseline else 0.9
    
    # Early return red herring: looks important but not triggered
    if len(performance_bands) == 1 and 'excellent' in performance_bands:
        return int(sum(metrics) * 1.5)  # Not actually reached in this case

    # Core calculation: combines streaks, baseline comparison, and trend
    base_score = len(above_baseline) * 10
    bonus = improvement_streaks * 5 if improvement_streaks > 4 else improvement_streaks * 2
    penalty = len(below_baseline) * 3
    
    # Final score computation
    final_score = base_score + bonus - penalty
    final_score = int(final_score * trend_factor)  # Apply trend adjustment
    
    return final_score

# Main execution
metrics_data = [75, 82, 68, 90, 88, 73, 85]
baseline_value = 80

# Spurious data transformations (distractors)
data_copy = metrics_data[:]
data_copy.sort(reverse=True)
duplicate_filtered = list(set(data_copy))

# Unused helper that computes irrelevant statistic
def calc_entropy(vals):
    from math import log
    freq = {}
    for v in vals:
        freq[v] = freq.get(v, 0) + 1
    total = len(vals)
    return -sum((count/total) * log(count/total) for count in freq.values())

entropy_val = calc_entropy(metrics_data)  # Dead code path (value not used)

# Key execution point
final_score = evaluate_performance(metrics_data, baseline_value)
print(f"Result: {final_score}")