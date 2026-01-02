from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and trend analysis
def process_readings(raw_data):
    filtered = [x for x in raw_data if 10 <= x <= 100]
    shifts = []
    for i in range(1, len(filtered)):
        diff = filtered[i] - filtered[i-1]
        shifts.append(diff)
    avg_shift = sum(shifts) / len(shifts) if shifts else 0
    return filtered, avg_shift

def analyze_trends(values):
    trends = defaultdict(int)
    for i in range(len(values) - 1):
        if values[i+1] > values[i]:
            trends['up'] += 1
        elif values[i+1] < values[i]:
            trends['down'] += 1
    return dict(trends)

def calculate_stability(metric_log):
    if not metric_log:
        return 0.0
    mean_val = sum(metric_log) / len(metric_log)
    variance = sum((x - mean_val) ** 2 for x in metric_log) / len(metric_log)
    stability = 1 / (1 + variance)  # higher variance → lower stability
    return round(stability, 4)

def calculate_performance(base, inputs):
    # Core logic path
    processed, delta = process_readings(inputs)
    trend_map = analyze_trends(processed)
    up_count = trend_map.get('up', 0)
    down_count = trend_map.get('down', 0)
    net_trend = up_count - down_count

    # Irrelevant computation block (distractor)
    temp_analysis = [x * 1.05 for x in inputs if x % 2 == 0]
    temp_sum = sum(temp_analysis)
    normalized_total = temp_sum / (len(temp_analysis) if temp_analysis else 1)

    # More distractions: unused intermediate calculations
    stats_summary = Counter(inputs)
    peak_frequency = max(stats_summary.values())
    entropy_proxy = len(set(inputs)) / (len(inputs) + 1e-5)

    # Actual contribution to result
    base_adjustment = base * 0.8
    trend_influence = net_trend * 1.5
    stability_metric = calculate_stability(processed)

    # Final score computation (only some components are relevant)
    raw_score = base_adjustment + trend_influence
    penalty = 5 if stability_metric < 0.2 else 0
    final_score = int(raw_score - penalty)

    # Dead code branch (never executed but looks plausible)
    if False:
        fallback = sum(processed) // len(processed)
        final_score = fallback

    return final_score

# Main execution
baseline = 50
readings = [12, 15, 14, 18, 20, 19, 25, 22, 30, 28, 11, 105, 9]
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")