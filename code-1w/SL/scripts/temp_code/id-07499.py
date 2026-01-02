from itertools import compress, count

def analyze_metrics(raw_values, thresholds):
    filtered = []
    cumulative = 0
    temp_offset = 1.5
    for i, val in enumerate(raw_values):
        if val > thresholds[i % len(thresholds)]:
            cumulative += val * (i + 1)
            filtered.append(val)
    
    adjustment_factor = 0.9 if len(filtered) > 3 else 1.1
    adjusted_cumulative = cumulative * adjustment_factor
    
    # Irrelevant computation (distractor)
    squared_chain = [x**2 for x in range(len(filtered))]
    sum_squares = sum(squared_chain)
    
    return adjusted_cumulative

def calculate_performance(data_stream):
    base_weights = [0.8, 1.2, 0.9, 1.1]
    trend_peaks = []
    noise_floor = 0.05
    total_energy = 0.0
    
    for idx, segment in enumerate(data_stream):
        segment_sum = sum(segment)
        weighted_sum = segment_sum * base_weights[idx % len(base_weights)]
        
        if weighted_sum > 15:
            trend_peaks.append(weighted_sum)
        
        # Dead code path (misleading)
        if noise_floor > 1.0:
            total_energy += segment_sum ** 0.5
    
    # Slicing and conditional expression
    recent_trends = trend_peaks[-3:] if len(trend_peaks) > 3 else trend_peaks
    performance_base = sum(recent_trends) if recent_trends else 10.0
    
    # Unnecessary transformation
    expanded = list(compress(count(start=1), (x > 12 for x in recent_trends)))
    expansion_penalty = len(expanded) * 0.2
    
    final_metric = performance_base - expansion_penalty
    return int(round(final_metric))

# Main execution block
raw_input = [4, 6, 8, 7, 9]
threshold_config = [5, 6, 4]

interim_result = analyze_metrics(raw_input, threshold_config)

# Simulated benchmark data segments
segment_1 = [3, 4, 6]
segment_2 = [5, 7, 8]
segment_3 = [6, 5, 9]
segment_4 = [4, 8, 7]
benchmark_data = [segment_1, segment_2, segment_3, segment_4]

# Key statement
final_score = calculate_performance(benchmark_data)

# Print result
print(f"Result: {final_score}")