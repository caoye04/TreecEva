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

def calculate_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

def filter_outliers(data, threshold=1.5):
    volatility = calculate_volatility(data)
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) <= threshold * volatility]
    return filtered if len(filtered) > 0 else data

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified info content
    return entropy

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    for m, w in zip(metrics, weights):
        weighted_sum += m * w
    
    adjustment_factor = 1.0
    if len(metrics) > 3:
        adjustment_factor *= 1.1
    if sum(metrics) > 50:
        adjustment_factor *= 1.05
    
    temp_debug = [x * adjustment_factor for x in metrics]  # Irrelevant intermediate
    debug_log = ''.join(map(str, map(int, temp_debug[:3])))  # Dead computation
    
    final_raw = weighted_sum * adjustment_factor
    
    # Dummy bitwise manipulation (distraction)
    magic_offset = 0
    for x in temp_debug[:4]:
        magic_offset ^= int(x) & 7
    
    final_raw += magic_offset

    scaling_factor = calculate_volatility(metrics) / 10
    final_score = int(final_raw - scaling_factor * 10)
    
    return final_score

# Main execution
raw_data = [85, 90, 78, 92, 88, 76, 95, 87, 83]
smoothed_data = filter_outliers(raw_data, threshold=1.2)
trend_metric = analyze_trend(smoothed_data)
volt_metric = calculate_volatility(smoothed_data)
entropy_metric = compute_entropy(smoothed_data)
size_metric = len(smoothed_data) * 2

dummy_pairs = list(itertools.combinations([1, 2, 3], 2))
dummy_sum = sum(a + b for a, b in dummy_pairs)  # Distractor using itertools

metrics = [trend_metric, volt_metric * 10, entropy_metric * 5, size_metric]
weights = [0.3, 0.2, 0.25, 0.25]

intermediate_result = sum(metrics) / len(metrics)
baseline_check = (min(metrics) + max(metrics)) / 2

final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")