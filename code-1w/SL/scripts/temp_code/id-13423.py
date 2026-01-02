from collections import defaultdict
import math

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 85, 92, 67, 88, 95, 82, 73, 90, 87]
    metrics = defaultdict(int)
    
    for val in raw_data:
        if val >= 90:
            metrics['excellent'] += 1
        elif val >= 80:
            metrics['good'] += 1
        else:
            metrics['needs_improvement'] += 1
    
    # Distractor: irrelevant transformation
    temp_processed = [math.sqrt(x * 1.5) for x in raw_data if x % 2 == 0]
    avg_temp = sum(temp_processed) / len(temp_processed) if temp_processed else 0
    
    # Another distractor: dead computation path
    outlier_count = 0
    for x in raw_data:
        deviation = abs(x - sum(raw_data) / len(raw_data))
        if deviation > 15:
            outlier_count += 1
    
    # Actual metric used later
    metrics['total_entries'] = len(raw_data)
    metrics['average'] = sum(raw_data) / len(raw_data)
    
    return metrics

# Evaluate performance against threshold
def evaluate_performance(data, threshold):
    base_score = 0
    
    if data['excellent'] > threshold:
        base_score += 25
    if data['good'] >= 3:
        base_score += 15
    
    # Use of slicing to analyze trend (last 5 entries)
    recent_trend = list(data.values())[-5:]  # semi-relevant, distracts from actual logic
    trend_boost = len([x for x in recent_trend if isinstance(x, int) and x > 2]) * 2
    
    # Bitwise manipulation for "encoding" score (actual relevant step)
    encoded_factor = (data['excellent'] ^ data['good']) & 7  # XOR and AND for obfuscation
    
    # Final calculation
    adjustment = round(math.log(data['average'] + 1), 2)
    base_score += encoded_factor * 3
    base_score += int(adjustment)
    
    # Irrelevant string operation (distractor)
    status_label = "PERFORMANCE_" + "_OK" if base_score > 50 else "_LOW"
    status_label = status_label.lower().replace('_', '.')
    
    return base_score

# Main execution
metrics = collect_metrics()
threshold = 2

# Key statement
final_score = evaluate_performance(metrics, threshold)

# Additional red herring variables
shadow_copy = {k: v * 1.1 for k, v in metrics.items() if isinstance(v, int)}
duplicate_calc = sum([v for v in shadow_copy.values() if v > 10])

print(f"Result: {final_score}")