from collections import defaultdict

# Simulate system performance evaluation with noise and filtering
def collect_telemetry():
    raw_data = [120, 85, 90, 130, 75, 145, 60]
    timestamps = list(range(len(raw_data)))
    return list(zip(timestamps, raw_data))

def filter_outliers(data, threshold=100):
    filtered = []
    anomalies = []
    for ts, val in data:
        if val < threshold:
            anomalies.append((ts, val))
        else:
            filtered.append(val)
    return filtered, anomalies

def compute_trend(values):
    if len(values) < 2:
        return 0
    diffs = [values[i] - values[i-1] for i in range(1, len(values))]
    return sum(diffs) / len(diffs)

def normalize_scores(raw):
    total = sum(raw)
    return [round(x / total * 100, 2) for x in raw]

def evaluate_performance(metrics, base):
    trend = compute_trend(metrics)
    normalized = normalize_scores(metrics)
    
    # Distractor: unused complex calculation
    entropy = 0.0
    for x in normalized:
        if x > 0:
            import math
            entropy -= (x/100) * math.log(x/100)
    
    # Irrelevant state tracking
    status_log = defaultdict(int)
    for val in metrics:
        if val > base * 1.1:
            status_log['high'] += 1
        elif val < base * 0.9:
            status_log['low'] += 1
        else:
            status_log['normal'] += 1
    
    # Core logic disguised among distractions
    above_base = sum(1 for m in metrics if m > base)
    stability_factor = abs(trend)
    
    # Actual computation path
    if above_base >= 3:
        bonus = 15
    else:
        bonus = 5
    
    base_score = sum(normalized[:3])  # Only first three matter
    penalty = len([m for m in metrics if m < 70]) * 2
    
    final_score = base_score + bonus - penalty - int(stability_factor)
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = sorted(normalized, reverse=True)
        final_score = sum(fallback[:2])
    
    return int(final_score)

# Main execution flow
data_stream = collect_telemetry()
clean_metrics, outliers = filter_outliers(data_stream)
baseline_ref = 88

# Key statement
final_score = evaluate_performance(clean_metrics, baseline_ref)

print(f"Result: {final_score}")