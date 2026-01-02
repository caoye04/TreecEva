def analyze_trends(data, threshold=5.0):
    trends = []
    for i, value in enumerate(data):
        if i == 0:
            continue
        change = data[i] - data[i-1]
        trend = 'up' if change > threshold else 'down' if change < -threshold else 'stable'
        trends.append(trend)
    return trends


def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]


def calculate_performance(raw_data):
    # Preprocess: remove outliers
    cleaned_data = filter_outliers(raw_data)
    
    # Secondary analysis (distraction): reverse slicing
    reversed_slice = cleaned_data[::-1][:len(cleaned_data)//2]
    avg_reversed = sum(reversed_slice) / len(reversed_slice) if reversed_slice else 0
    
    # Real computation begins
    base_metric = sum(cleaned_data) / len(cleaned_data)
    variance = sum((x - base_metric) ** 2 for x in cleaned_data) / len(cleaned_data)
    std_dev = variance ** 0.5
    
    # Misleading transformation (not used later but looks important)
    normalized = [(x - base_metric) / std_dev for x in cleaned_data]
    z_score_peak = max(normalized) - min(normalized)
    
    # Trend analysis on binned data
    binned = [cleaned_data[i:i+3] for i in range(0, len(cleaned_data), 3)]
    sizes = [len(bin_) for bin_ in binned]
    avg_size = sum(sizes) / len(sizes)
    
    # Distractor loop: calculates something unused
    cumulative_shift = 0
    for idx, s in enumerate(sizes):
        if s > avg_size:
            cumulative_shift += idx * 0.1
    
    # Core logic: stability index and efficiency boost
    trend_data = [sum(bin_) / len(bin_) for bin_ in binned if len(bin_) > 0]
    stability = sum(abs(trend_data[i+1] - trend_data[i]) for i in range(len(trend_data)-1))
    efficiency_boost = 1.0 if stability < 10 else 0.85
    
    # Conditional expression with slicing distraction
    adjustment_factor = 1.2 if len(cleaned_data) > 5 else 0.9
    secondary_criterion = avg_reversed > 20 and z_score_peak < 5
    
    # Final score computation
    raw_score = base_metric * efficiency_boost
    final_score = raw_score * adjustment_factor
    
    # Print result as required
    print(f"Result: {final_score}")
    
    return final_score

# Simulated benchmark dataset
benchmark_data = [12.5, 14.2, 11.8, 42.1, 13.0, 15.3, 10.7, 16.8, 12.9, 14.4, 13.2]

# Additional irrelevant tracking variables (dead code path)
data_snapshot = benchmark_data.copy()
processed_flags = [False] * len(benchmark_data)
for i in range(len(data_snapshot)):
    if data_snapshot[i] > 40:
        processed_flags[i] = True

# Trigger the main computation
final_score = calculate_performance(benchmark_data)