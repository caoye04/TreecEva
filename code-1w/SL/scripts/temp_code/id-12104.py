def analyze_trend(data, threshold):
    trend_vector = [1 if data[i] > data[i-1] else -1 for i in range(1, len(data))]
    volatility = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    significant_moves = [x for x in data if abs(x - threshold) > threshold * 0.1]
    return trend_vector, len(significant_moves) > 3


def normalize(values):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.5 for _ in values]
    return [(v - min_val) / (max_val - min_val) for v in values]


def filter_outliers(series, factor=1.5):
    q1, q3 = sorted(series)[len(series)//4], sorted(series)[3*len(series)//4]
    iqr = q3 - q1
    lower_bound, upper_bound = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in series if lower_bound <= x <= upper_bound]


def evaluate_performance(metrics, baseline):
    # Irrelevant transformation
    adjusted_metrics = [m * 1.07 for m in metrics][:len(metrics)//2 + 1]
    
    # Real computation branch
    processed = [m ** 0.5 for m in metrics if m > 0]
    capped = [min(p, 10) for p in processed]
    
    # Distractor: complex slicing and set operations
    mid_section = capped[1:-1]
    unique_caps = list(set(mid_section))
    unique_caps.sort()
    
    # Semi-relevant: trend analysis on normalized data
    norm_metrics = normalize(metrics)
    _, strong_trend = analyze_trend(norm_metrics, 0.5)
    
    # Actual logic contributing to result
    filtered_vals = filter_outliers(capped)
    avg_filtered = sum(filtered_vals) / len(filtered_vals) if filtered_vals else 0
    
    bonus = 5 if len(metrics) > 6 else 0
    penalty = 2 if len([x for x in metrics if x < 0]) else 0
    
    # Key computational step
    base_score = avg_filtered * 8.5
    final_score = base_score + bonus - penalty
    
    # Dead code path (never executed under current inputs)
    if False and strong_trend:
        correction_factor = sum(unique_caps[-2:]) / 2 if len(unique_caps) >= 2 else 1
        final_score *= correction_factor
    
    return final_score

# Input data
baseline = [3.2, 4.1, 2.8, 5.0, 4.9, 4.7, 5.2]
metrics = [16, 25, 9, 36, 4, 49, 1, 64]

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")