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
    volatility = compute_volatility(values)
    mean_val = sum(values) / len(values)
    filtered = [v for v in values if abs(v - mean_val) <= threshold * volatility]
    return filtered

def evaluate_performance(metrics, weights):
    normalized = []
    for val in metrics:
        if val > 0:
            norm_val = (val + 1) / (max(metrics) + 1)
        else:
            norm_val = val / (abs(min(metrics)) + 1) if min(metrics) != 0 else 0
        normalized.append(norm_val)
    
    weighted_sum = 0
    for n, w in zip(normalized, weights):
        weighted_sum += n * w
    
    adjustment_factor = 1.0
    if len(metrics) % 2 == 0:
        adjustment_factor *= 1.1
    if sum(metrics) > 50:
        adjustment_factor *= 1.05

    temp_result = 0
    for a, b in itertools.pairwise(metrics):
        temp_result += (a ^ b) & 1  # XOR and check least significant bit

    diagnostic_flag = temp_result > 3
    debug_value = sum(1 for x in metrics if x % 2 == 0)

    final_score = int(weighted_sum * adjustment_factor * 100)
    
    return final_score

# Main execution
raw_data = [12, 15, 10, 23, 18, 25, 30, 14, 40, 22]
processed_data = filter_outliers(raw_data)
trend_metric = analyze_trend(processed_data)
risk_factor = compute_volatility(raw_data[:5])
metrics = [
    trend_metric * 2,
    len(processed_data) * 3,
    int(risk_factor),
    sum(x for x in processed_data if x > 20),
    raw_data[0] + raw_data[-1]
]
weights = [0.2, 0.25, 0.15, 0.3, 0.1]

interim_diagnostic = [x * 0.1 for x in metrics if x > 10]
dropped_count = len(raw_data) - len(processed_data)

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")