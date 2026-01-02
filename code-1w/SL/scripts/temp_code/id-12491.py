from itertools import combinations

# Simulate sensor array readings with noise filtering
def process_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    baseline = sum(filtered) / len(filtered)
    deviation = [abs(x - baseline) for x in filtered]
    return baseline, deviation

# Analyze pattern consistency across time windows
def analyze_patterns(data_sequence):
    pattern_scores = []
    for i in range(len(data_sequence) - 3):
        window = data_sequence[i:i+4]
        if len(set(window)) == 4:  # all distinct
            score = (window[3] - window[0]) / 3
            pattern_scores.append(score)
    return pattern_scores

# Main performance calculator combining multiple metrics
def calculate_performance(dataset):
    temp_results = []
    noise_floor = 0.05
    aggregate_offset = 0

    for segment in dataset:
        base, dev = process_readings(segment)
        
        # Irrelevant transformation (distractor)
        squared_dev = [d**2 for d in dev if d > noise_floor]
        smoothing_factor = len(squared_dev) / (len(dev) + 1)
        
        # Key metric computation
        trend = analyze_patterns(segment)
        if trend:
            avg_trend = sum(trend) / len(trend)
        else:
            avg_trend = 0
        
        # Secondary distractor: unused complex calculation
        cross_pairs = list(combinations(segment[:5], 2))
        spread_metric = sum(abs(a - b) for a, b in cross_pairs) / len(cross_pairs) if cross_pairs else 0
        
        # Weighted combination
        reliability = len(dev) / len(segment)
        segment_score = base * 0.4 + avg_trend * 10 + reliability * 5
        temp_results.append(segment_score)
    
    # Final aggregation
    final_score = sum(temp_results) / len(temp_results)
    
    # Dead code branch (misleading)
    if False:
        correction = lambda x: x * 1.1 if x < 50 else x * 0.95
        final_score = correction(final_score)
    
    return final_score

# Input data - sensor readings over 3 time intervals
benchmark_data = [
    [12, 15, 98, 45, 67, 23, 89],
    [11, 14, 99, 44, 68, 22, 90],
    [13, 16, 97, 46, 66, 24, 88]
]

# Execute main logic
temp_var_x = [min(row) for row in benchmark_data]  # Distractor variable
temp_var_y = sum(temp_var_x) * 0.1                     # Another distractor

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")