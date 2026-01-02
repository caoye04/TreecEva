from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    readings = [23.4, 24.1, 19.5, 22.8, 25.6, 20.2, 21.7, 23.9, 24.4, 18.9]
    offset = 0.5
    adjusted = [r + offset for r in readings]
    return adjusted

def analyze_trends(data):
    moving_avg = []
    for i in range(2, len(data)):
        avg = (data[i-2] + data[i-1] + data[i]) / 3
        moving_avg.append(round(avg, 2))
    return moving_avg

def filter_outliers(values, threshold=2.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    filtered = [v for v in values if abs(v - mean_val) <= threshold * std_dev]
    return filtered

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_report_metadata():
    # Irrelevant metadata generation (distraction)
    meta = defaultdict(str)
    meta['version'] = '2.1.0'
    meta['author'] = 'sysadmin'
    meta['timestamp'] = '2023-11-05'
    meta['location'] = 'Zone B'
    return dict(meta)

def calculate_baseline_metrics(data):
    # Partially relevant but ultimately unused function (red herring)
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    normalized = [(x - min_val) / range_val for x in data]
    return {
        'peak': max_val,
        'floor': min_val,
        'dynamic_range': range_val,
        'efficiency_ratio': sum(normalized) / len(normalized)
    }

def derive_composite_index(readings):
    # Complex transformation with intermediate distractors
    temp_buckets = defaultdict(int)
    for val in readings:
        bucket = int(val // 1)
        temp_buckets[bucket] += 1
    
    index = 0
    weights = {20: 0.5, 21: 0.8, 22: 1.0, 23: 1.2, 24: 1.5}
    for k, v in temp_buckets.items():
        if k in weights:
            index += weights[k] * v
    
    # Decoy calculation
    dummy_index = sum(temp_buckets.values()) * 0.75
    
    return index  # Only this matters

def evaluate_performance(metrics, base):
    score = 0
    # Misleading weight adjustments
    if metrics['stability'] > base:
        score += 15
    if metrics['consistency'] >= base - 5:
        score += 10
    if metrics['entropy'] < 3.0:
        score += 20
    
    # Critical scoring branch
    if metrics['composite'] > 30.0:
        bonus = int((metrics['composite'] - 30.0) * 2)
        score += bonus
    else:
        score -= 5
    
    # Dead code path (never reached due to logic above)
    if metrics['composite'] < 0:
        score = 0  # This will not execute
    
    return score

# Main execution flow
if __name__ == '__main__':
    raw_data = collect_readings()
    trends = analyze_trends(raw_data)
    cleaned = filter_outliers(trends, threshold=1.8)
    
    # Generate irrelevant side data
    metadata = generate_report_metadata()
    unused_metrics = calculate_baseline_metrics(raw_data)  # Computed but unused
    
    stability_measure = sum(abs(cleaned[i] - cleaned[i-1]) for i in range(1, len(cleaned)))
    consistency_score = len(cleaned) * 2.5
    
    # Key metric computation
    entropy_value = compute_entropy([round(x) for x in cleaned])
    composite_index = derive_composite_index(raw_data)
    
    # Build metric dictionary
    metric_data = {
        'stability': round(stability_measure, 2),
        'consistency': int(consistency_score),
        'entropy': entropy_value,
        'composite': composite_index
    }
    
    base_threshold = 12
    adjustment_factor = 0.85  # Unused parameter (distractor)
    scaling_vector = [0.1, 0.3, 0.6]  # Dead data structure
    
    final_score = evaluate_performance(metric_data, base_threshold)
    print(f"Result: {final_score}")