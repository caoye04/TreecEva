import math

def analyze_trend(data, threshold=0.5):
    trend = 0
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trend += 1
        elif data[i-1] - data[i] > threshold:
            trend -= 1
    return trend

# Irrelevant helper function (dead code path)
def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total

def normalize_vector(vec):
    norm = sum(x**2 for x in vec) ** 0.5
    return [x / norm for x in vec] if norm else vec

def validate_inputs(raw_metrics):
    if not raw_metrics or len(raw_metrics) == 0:
        return False
    for k, v in raw_metrics.items():
        if v < 0 or v > 1:
            return False
    return True

def filter_outliers(seq, factor=1.5):
    if len(seq) < 2:
        return seq
    q1, q3 = sorted(seq)[len(seq)//4], sorted(seq)[-len(seq)//4]
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if low <= x <= high]

# Misleading aggregation function that isn't used in final calculation
def get_summary_stats(logs):
    flat = []
    for entry in logs:
        flat.extend(entry.values())
    clean_data = filter_outliers(flat)
    return {
        'mean': sum(clean_data) / len(clean_data),
        'peak': max(clean_data),
        'volatility': analyze_trend(clean_data)
    }

# Core logic disguised among distractors
def evaluate_performance(log, weight_map):
    base = 0
    multipliers = []
    
    # Real but obscured computation
    for entry in log:
        temp_val = 0
        for key, val in entry.items():
            if key in weight_map:
                temp_val += val * weight_map[key]
        multipliers.append(temp_val * 100)
    
    # Actual answer derivation hidden here
    adjusted = [m for m in multipliers if m > 50]  # Filter step
    if len(adjusted) == 0:
        adjusted = [0]
    
    # Critical distraction: complex-looking but unused transformation
    transformed = [math.sin(x / 10) * math.cos(x / 20) for x in multipliers]
    entropy_like = sum(-t * math.log(abs(t)+1e-9) for t in transformed)  # Red herring
    
    # Final result relies only on filtered average and count
    avg_performance = sum(adjusted) / len(adjusted)
    count_bonus = len(adjusted) * 5
    
    # Final score built from non-obvious components
    result = int(avg_performance + count_bonus)
    return result

# Simulated input data
weights = {
    'accuracy': 0.3,
    'latency': -0.1,
    'throughput': 0.25,
    'stability': 0.15,
    'reliability': 0.2
}

metrics_log = [
    {'accuracy': 0.92, 'latency': 0.45, 'throughput': 0.88, 'stability': 0.75, 'reliability': 0.90},
    {'accuracy': 0.85, 'latency': 0.60, 'throughput': 0.70, 'stability': 0.60, 'reliability': 0.80},
    {'accuracy': 0.95, 'latency': 0.30, 'throughput': 0.92, 'stability': 0.85, 'reliability': 0.93},
    {'accuracy': 0.70, 'latency': 0.80, 'throughput': 0.50, 'stability': 0.40, 'reliability': 0.65},
    {'accuracy': 0.88, 'latency': 0.50, 'throughput': 0.80, 'stability': 0.70, 'reliability': 0.85}
]

# Unused but plausible intermediate variables
summary = get_summary_stats(metrics_log)
trend_analysis = analyze_trend([sum(e.values()) for e in metrics_log])
normalized_weights = normalize_vector(list(weights.values()))

# Key execution point
final_score = evaluate_performance(metrics_log, weights)

# Print result as required
print(f"Target result: {final_score}")