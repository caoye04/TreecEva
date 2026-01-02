def analyze_sequence(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Simulate sensor readings over time
timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sensor_data = [104, 102, 105, 103, 105, 106, 102, 104, 105, 107]

# Track frequency of each reading
freq_map = analyze_sequence(sensor_data)

# Misleading transformation - not used in final calculation
distorted_values = [x ** 2 % 97 for x in sensor_data]
sum_distorted = sum(distorted_values)

# Benchmark thresholds for performance levels
benchmark_levels = {
    'low': 103,
    'medium': 105,
    'high': 106
}

# Extract relevant metrics
above_medium = len([x for x in sensor_data if x > benchmark_levels['medium']])
below_low = len([x for x in sensor_data if x < benchmark_levels['low']])
equal_medium = len([x for x in sensor_data if x == benchmark_levels['medium']])

# Secondary distraction: character counting in labels (irrelevant)
label_chars = sum(len(key) for key in benchmark_levels.keys())
scaling_factor = label_chars / 10  # Distractor, not used later

# Build detailed metrics dictionary
metrics = {
    'peak_count': freq_map.get(105, 0),
    'stability_ratio': (sensor_data[-1] - sensor_data[0]) / len(sensor_data),
    'above_threshold': above_medium,
    'critical_events': below_low,
    'baseline_hits': equal_medium,
    'consistency_score': sum(1 for i in range(1, len(sensor_data)) if abs(sensor_data[i] - sensor_data[i-1]) <= 2)
}

# Red herring computation: sequence analysis with no impact
running_avg_deviation = 0.0
if len(sensor_data) > 1:
    avg_diffs = [abs(sensor_data[i] - sensor_data[i-1]) for i in range(1, len(sensor_data))]
    running_avg_deviation = sum(avg_diffs) / len(avg_diffs)

# Core logic hidden among distractions
def evaluate_performance(met, levels):
    score = 0
    peak = met['peak_count']
    stable = met['consistency_score']
    high_perf = met['above_threshold']
    
    # Multiple logic steps with interdependencies
    if peak > 2:
        score += 15
        if stable > 6:
            score += 10
            if high_perf >= 2:
                score += 25
            else:
                score += 5
        else:
            bonus = (levels['high'] - levels['medium']) * 2  # Computed but unused
            score += 5
    else:
        score -= 10
    
    # Additional branching based on baseline
    if met['baseline_hits'] == 1:
        score *= 1.1
    elif met['baseline_hits'] > 1:
        score *= 1.25
    else:
        score = int(score * 0.9)
    
    # Final adjustment using dictionary-derived metric
    stability = met['stability_ratio']
    if stability > 0:
        score += 5
    
    return int(score)

# Execute main evaluation
final_score = evaluate_performance(metrics, benchmark_levels)

# Print result as required
print(f"Result: {final_score}")