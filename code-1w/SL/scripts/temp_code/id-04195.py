def analyze_trends(data_slice, threshold=0.5):
    trend_count = 0
    volatility = 0.0
    for i in range(1, len(data_slice)):
        change = data_slice[i] - data_slice[i-1]
        if abs(change) > threshold:
            trend_count += 1
        volatility += abs(change)
    normalized_volatility = volatility / len(data_slice)
    return trend_count, normalized_volatility


def filter_outliers(raw_series, factor=1.5):
    median_val = sorted(raw_series)[len(raw_series)//2]
    deviation = [abs(x - median_val) for x in raw_series]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    upper_bound = median_val + factor * mad
    lower_bound = median_val - factor * mad
    filtered = [x for x in raw_series if lower_bound <= x <= upper_bound]
    return filtered if len(filtered) > 0 else raw_series[:len(raw_series)//2 + 1]


def calculate_performance(metrics_log):
    # Preprocessing phase with slicing and filtering
    recent_segment = metrics_log[-7:]  # Last 7 entries
    base_reference = metrics_log[:len(metrics_log)//3]  # First third
    
    # Distraction: Irrelevant transformation
    amplified = [x * 1.1 for x in base_reference if x > 0.3]
    amplification_factor = sum(amplified) / len(amplified) if amplified else 1.0
n    # Real processing begins
    cleaned_data = filter_outliers(recent_segment, factor=1.2)
    trend_strength, stability = analyze_trends(cleaned_data, threshold=0.3)
    
    # Secondary distraction: unused intermediate calculation
    peak_density = sum(1 for x in cleaned_data if x > 0.7) / len(cleaned_data) if cleaned_data else 0
    baseline_avg = sum(base_reference) / len(base_reference)
    
    # Core logic with conditional expression and tuple unpacking
    adjustment = 1.5 if stability < 0.4 else 0.8
    score_component_1 = trend_strength * 10
    score_component_2 = int(baseline_avg * 50)
    
    # Final score computation
    final_score = score_component_1 + score_component_2
    temp_offset = (score_component_1 - score_component_2) // 5  # Unused but looks relevant
    
    return final_score

# Simulated benchmark input
benchmark_data = [0.45, 0.49, 0.32, 0.78, 0.81, 0.41, 0.52, 0.63, 0.58, 0.51, 0.47, 0.66, 0.69]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")