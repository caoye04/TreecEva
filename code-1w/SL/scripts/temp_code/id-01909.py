from collections import defaultdict
import math

def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    return trend_score

def smooth_data(data, factor=0.1):
    # Irrelevant smoothing function (not used in final logic)
    smoothed = [data[0]]
    for x in data[1:]:
        smoothed.append(smoothed[-1] * (1 - factor) + x * factor)
    return smoothed

def calculate_entropy(counts):
    total = sum(counts)
    entropy = 0
    for c in counts:
        if c > 0:
            p = c / total
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def evaluate_performance(metrics, threshold):
    # Core logic starts here
    high_count = 0
    low_count = 0
    status_map = defaultdict(int)
    
    for k, v in metrics.items():
        if v > threshold:
            high_count += 1
            status_map['above'] += 1
        else:
            low_count += 1
            status_map['below'] += 1
    
    # Distractor: complex but unused calculation
    imbalance_ratio = (high_count + 1) / (low_count + 1) if low_count != 0 else float('inf')
    adjustment_factor = math.sqrt(abs(high_count - low_count)) if high_count != low_count else 1.0
    
    # Semi-relevant transformation
    normalized_diff = abs(high_count - low_count) // max(1, (high_count + low_count) // 3)
    
    # Key decision path
    if high_count >= low_count:
        base_bonus = 10
    else:
        base_bonus = 5
    
    # Additional distractor: unused entropy computation on artificial data
    dummy_counts = [len(metrics), high_count * 2, low_count + 3]
    _ = calculate_entropy(dummy_counts)
    
    # Final score computation
    raw_score = (high_count * 7) + (low_count * 2) + base_bonus
    penalty = normalized_diff * 3
    final_score = raw_score - penalty
    
    # Dead code branch (never executed due to logic above)
    if False and adjustment_factor > 5:
        final_score *= 0.8
    
    return int(final_score)

# Main execution
metric_data = {
    'throughput': 89,
    'latency': 45,
    'error_rate': 12,
    'availability': 98,
    'response_time': 67,
    'reliability': 88
}

base_threshold = 60

# Intermediate irrelevant variables
historical_trend = [55, 57, 60, 58, 62]
trend_value = analyze_trend(historical_trend)
data_snapshot = smooth_data([100, 98, 95, 97, 102])

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")