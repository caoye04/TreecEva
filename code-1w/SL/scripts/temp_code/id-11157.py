from collections import defaultdict, Counter

def analyze_trends(data, threshold=0.5):
    trends = defaultdict(int)
    for i, value in enumerate(data):
        if value > threshold:
            trends['above'] += 1
        elif value < -threshold:
            trends['below'] += 1
        else:
            trends['neutral'] += 1
    return dict(trends)

def compute_moving_average(series, window=3):
    if len(series) < window:
        return [0]
    averages = []
    for i in range(len(series) - window + 1):
        averages.append(sum(series[i:i+window]) / window)
    return averages

def detect_anomalies(values):
    count_freq = Counter(values)
    most_common_val, freq = count_freq.most_common(1)[0]
    anomalies = [i for i, v in enumerate(values) if v != most_common_val and abs(v - most_common_val) > 1]
    return anomalies if anomalies else [0]

def transform_coordinates(coords):
    # Irrelevant geometric transformation (distractor)
    transformed = []
    for x, y in coords:
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        transformed.append((rotated_x, rotated_y))
    return transformed

def filter_outliers(sequence, factor=1.5):
    # Dead code path — never used in final logic
    q1 = sorted(sequence)[len(sequence)//4]
    q3 = sorted(sequence)[3*len(sequence)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in sequence if lower_bound <= x <= upper_bound]

def recursive_weight_accumulate(arr, idx=0, acc=1.0):
    if idx >= len(arr):
        return acc
    acc *= (1 + arr[idx] / 100)
    return recursive_weight_accumulate(arr, idx + 1, acc)

def calculate_risk_profile(history):
    risk = 1.0
    for h in history:
        if h < 0:
            risk *= 1.1
        elif h == 0:
            risk *= 0.95
    return round(risk, 6)

def evaluate_performance(metrics, weights):
    # Core relevant logic starts here
    base_scores = []
    adjustments = []
    
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        raw_score = metric * weight
        if i % 2 == 0:
            raw_score += 0.1
        else:
            raw_score -= 0.05
        base_scores.append(raw_score)
    
    # Intermediate aggregation
    total_base = sum(base_scores)
    adjustment_factor = recursive_weight_accumulate([10, -5, 8])  # Uses recursion with fixed input
    volatility = calculate_risk_profile([1, 0, -1, 0, 1])
    
    temp_result = total_base * adjustment_factor
    adjustments.append(temp_result * 0.01)
    adjustments.append(volatility * 0.5)
    
    # Final computation chain
    interim = temp_result - adjustments[0] + adjustments[1]
    scaling = len(metrics) / len(weights) if weights else 1
    normalized = interim * scaling
    
    # Critical assignment
    final_score = int(round(normalized * 100))  # This is the key line
    
    # Below are decoy operations that do not affect final_score
    decoy_metrics = [(x**2 + 1) for x in metrics]
    _ = analyze_trends(decoy_metrics, threshold=0.7)
    _ = compute_moving_average(decoy_metrics)
    _ = detect_anomalies(decoy_metrics)
    _ = transform_coordinates([(1, 2), (3, 4), (5, 6)])
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = [0.85, 0.92, 0.78, 0.96]
    weights = [0.2, 0.3, 0.25, 0.25]
    
    # Misleading pre-computations
    _ = filter_outliers(metrics)
    _ = compute_moving_average([1, 2, 3, 4, 5])
    
    # Key function call
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Target result: {final_score}")