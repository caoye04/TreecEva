import itertools

def analyze_trend(data):
    trend_scores = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_scores.append(1)
        elif data[i] < data[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return sum(trend_scores)

def compute_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

def filter_outliers(values, threshold=1.5):
    median_val = sorted(values)[len(values)//2]
    filtered = [v for v in values if abs(v - median_val) / (median_val + 1e-5) < threshold]
    return filtered if len(filtered) > 0 else values

def calculate_efficiency(raw_metrics):
    total_ops = sum(raw_metrics)
    peak_load = max(raw_metrics)
    efficiency = total_ops / (peak_load * len(raw_metrics))
    temp_debug = [x * 0.9 for x in raw_metrics]  # irrelevant computation
    return efficiency * 100

def evaluate_performance(metrics, weights):
    normalized = [m / (sum(metrics) + 1e-8) for m in metrics]
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    
    # Distractor: complex but unused structure
    combinations = list(itertools.combinations(weights, 2))
    combo_product_sum = sum(a * b for a, b in combinations)
    dummy_accum = 0
    for c in combinations:
        if c[0] > 0.2:
            dummy_accum += c[1] * 0.1
    
    # Real logic continues
    adjustment_factor = 1.0
    if len(metrics) > 3:
        trend = analyze_trend(metrics)
        vol = compute_volatility(metrics)
        if vol > 5:
            adjustment_factor = 0.9
        if trend > 0:
            adjustment_factor *= 1.1
    
    base_score = weighted_sum * 1000
    final_score = base_score * adjustment_factor
    
    # Irrelevant filtering
    cleaned_metrics = filter_outliers(metrics)
    _ = calculate_efficiency(cleaned_metrics)
    
    return int(final_score)

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.25, 0.15, 0.3, 0.1]

intermediate_result = compute_volatility(metrics)
dummy_list = [i ** 2 for i in range(len(weights))]  # dead code path
temp_value = sum(w * 100 for w in weights)  # misleading computation

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")