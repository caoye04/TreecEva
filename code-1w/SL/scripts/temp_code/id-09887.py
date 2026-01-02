from itertools import compress, cycle

def analyze_trends(data, threshold):
    trend_flags = []
    cumulative = 0
    for i, value in enumerate(data):
        if value > threshold:
            trend_flags.append(True)
            cumulative += value * 0.1
        else:
            trend_flags.append(False)
            cumulative -= 0.05
    return trend_flags, round(cumulative, 4)

def normalize(values):
    total = sum(values)
    return [v / total for v in values] if total != 0 else [0] * len(values)

def filter_outliers(seq, factor=1.5):
    if len(seq) == 0:
        return []
    q1 = sorted(seq)[len(seq)//4]
    q3 = sorted(seq)[3*len(seq)//4]
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    return [x for x in seq if low <= x <= high]

def calculate_stability_index(readings):
    if len(readings) < 2:
        return 0.0
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    avg_diff = sum(diffs) / len(diffs)
    stability = 1 / (1 + avg_diff)
    return round(stability, 4)

def evaluate_performance(metrics, weights):
    # Misleading: several metrics are normalized but not all used
    normalized_metrics = normalize([metrics['accuracy'], metrics['precision'], metrics['recall']])
    temp_result = sum(m * w for m, w in zip(normalized_metrics, weights[:3]))
    
    # Dummy computation that looks important but doesn't affect final result
    auxiliary_score = 0
    for k in range(3):
        auxiliary_score += temp_result * (k + 0.5) % 2
    auxiliary_score = round(auxiliary_score, 3)
    
    # Actual key calculation hidden among distractions
    base = metrics['accuracy'] * weights[0]
    adjustment = (metrics['stability'] - 0.5) * 0.2
    final_score = base + adjustment
    
    # Red herring: unused variable that looks critical
    comprehensive_score = (base + metrics['precision'] * weights[1] + metrics['recall'] * weights[2]) / 3
    
    return round(final_score, 4)

# Main execution block
if __name__ == '__main__':
    raw_data = [88, 92, 76, 95, 85, 67, 90, 93, 84, 78]
    
    # Simulate preprocessing with irrelevant filtering
    filtered_data = filter_outliers(raw_data, factor=2.0)
    trend_mask, cum_value = analyze_trends(filtered_data, threshold=80)
    
    # Construct metrics dictionary — only some fields are actually used
    metrics = {
        'accuracy': 0.87,
        'precision': 0.76,
        'recall': 0.72,
        'latency_ms': 45,
        'stability': calculate_stability_index([0.85, 0.87, 0.86, 0.88, 0.87]),
        'timestamp': 1712345678
    }
    
    # Weights — only first and fourth are truly relevant
    weights = [0.6, 0.2, 0.2, 0.0]  # Last weight unused but looks like it might be
    
    # Intermediate distraction: dummy use of itertools
    repeated_weights = list(compress(weights, [True, False, True, False]))
    cyclic_iter = cycle(repeated_weights)
    next(cyclic_iter); next(cyclic_iter)  # Advance iterator for no reason
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    print(f"Result: {final_score}")