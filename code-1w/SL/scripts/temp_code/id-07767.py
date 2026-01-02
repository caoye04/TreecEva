from itertools import compress, cycle

def analyze_trends(data, threshold):
    trend_flags = []
    for i, value in enumerate(data):
        if value > threshold:
            trend_flags.append(1)
        elif value < -threshold:
            trend_flags.append(-1)
        else:
            trend_flags.append(0)
    return trend_flags

def compute_volatility(seq):
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs) if diffs else 0.0

def filter_outliers(values, factor=1.5):
    if len(values) == 0:
        return [], []
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [v for v in values if lower_bound <= v <= upper_bound]
    outlier_mask = [not (lower_bound <= v <= upper_bound) for v in values]
    return filtered, outlier_mask

def recursive_transform(arr, depth=0):
    if depth >= 3 or len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = recursive_transform([x * 0.9 for x in arr[:mid]], depth + 1)
    right = recursive_transform([x * 1.1 for x in arr[mid:]], depth + 1)
    return left + right

def evaluate_performance(metrics, weights):
    # Irrelevant preprocessing
    temp_data = [x * 2 for x in metrics]
    temp_data = [x for x in temp_data if x > 0]
    
    # Decoy function call with no effect
    _ = compute_volatility(temp_data)
    
    # Actual weighted computation
    base_score = sum(m * w for m, w in zip(metrics, weights))
    
    # Misleading normalization step (not used)
    max_metric = max(metrics) if metrics else 1
n    normalized = [m / max_metric for m in metrics]
    
    # Conditional adjustment based on pattern
    trend = analyze_trends(metrics, threshold=5)
    bonus = 0
    for t in trend:
        if t == 1:
            bonus += 2
        elif t == -1:
            bonus -= 3
    
    adjusted_score = base_score + bonus
    
    # Red herring: complex transformation that isn't used
    transformed_metrics = recursive_transform(metrics, 0)
    _ = list(compress(transformed_metrics, cycle([1, 0])))
    
    # Final irrelevant filtering
    clean_metrics, _ = filter_outliers(metrics, 2.0)
    
    # The real answer contribution
    final_adjustment = len([x for x in metrics if x > 10])
    final_score = adjusted_score + final_adjustment
    
    return int(final_score)

# Simulated input data
metrics = [12, 8, 15, 3, 20, 7, 5]
weights = [0.1, 0.2, 0.15, 0.05, 0.3, 0.1, 0.1]

# Unused variables - red herrings
baseline_metrics = [10, 10, 10, 10, 10, 10, 10]
drift_analysis = analyze_trends([x - 10 for x in metrics], threshold=0)
volatility_index = compute_volatility(metrics)

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")