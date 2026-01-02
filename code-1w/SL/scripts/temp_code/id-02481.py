import itertools

def analyze_trends(data, threshold):
    trends = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trends.append('up')
        elif data[i-1] - data[i] > threshold:
            trends.append('down')
        else:
            trends.append('stable')
    return trends

def generate_combinations(elements):
    # Distractor: unused function
    return list(itertools.combinations(elements, 3))

def filter_outliers(seq, factor=1.5):
    # Heavily obfuscated but ultimately unused logic
    if len(seq) == 0:
        return seq
    q1, q3 = sorted(seq)[len(seq)//4], sorted(seq)[-len(seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    filtered = [x for x in seq if lower <= x <= upper]
    return filtered if len(filtered) > 2 else seq

def compute_weighted_average(values, weights=None):
    if not weights:
        weights = [1] * len(values)
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight if total_weight else 0.0

def evaluate_performance(metrics, base):
    adjusted = []
    for k, v in metrics.items():
        if k.endswith('_score'):
            adjustment_factor = 1.1 if v > base else 0.9
            adjusted.append(v * adjustment_factor)
        elif k.startswith('error'):
            adjustment_factor = 0.85 if v < base else 1.15
            adjusted.append(max(0, base - v * adjustment_factor))
        else:
            adjusted.append(v * 0.5)
    temp_result = compute_weighted_average(adjusted)
    
    # Core red herring: complex transformation that doesn't affect final output
    shadow_copy = adjusted[:]
    for _ in range(2):
        shadow_copy = [x * 0.95 for x in shadow_copy]
        shadow_copy = [x for x in shadow_copy if x > 10]
    
    # Real computation path
    raw_avg = sum(adjusted) / len(adjusted)
    stability = sum(1 for x in adjusted if abs(x - raw_avg) < 5) / len(adjusted)
    bonus = 15 if stability > 0.6 else 5
    penalty = 10 if len([x for x in adjusted if x < 20]) > 2 else 0
    
    # Critical line
    final_score = int(raw_avg + bonus - penalty)
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = filter_outliers(adjusted)
        fallback_avg = sum(fallback) / len(fallback)
        final_score = int(fallback_avg * 1.1)
    
    return final_score

# Irrelevant setup data
market_data = [100, 103, 107, 105, 110, 120, 118, 116]
trend_analysis = analyze_trends(market_data, 4)
all_combinations = generate_combinations([1, 2, 3, 4, 5])

# Core input variables
base_metric = 45
metrics_dict = {
    'accuracy_score': 52,
    'precision_score': 48,
    'recall_score': 44,
    'f1_score': 50,
    'error_rate': 8,
    'latency_ms': 120,
    'throughput_ops': 850
}

# Noise variables
placeholder_data = [(i, j) for i, j in itertools.product(range(3), range(3))]
dummy_set = set([x * 2 for x in range(50) if x % 7 == 0])
shadow_metrics = metrics_dict.copy()
for k in shadow_metrics:
    if 'score' in k:
        shadow_metrics[k] *= 1.05

# Key execution point
final_score = evaluate_performance(metrics_dict, base_metric)
print(f"Result: {final_score}")