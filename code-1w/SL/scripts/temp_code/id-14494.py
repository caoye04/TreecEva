from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 135, 140, 128, 155, 160, 148, 130]
    timestamps = list(range(1001, 1009))
    
    # Misleading transformation: normalized but unused later
    normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data)) for x in raw_data]
    
    metrics = defaultdict(float)
    for i, val in enumerate(raw_data):
        metrics[f'step_{i+1}'] = val * 0.9 if i % 2 == 0 else val * 0.95
    
    # Dead code path: never used
    if len(timestamps) > 10:
        metrics['extra'] = 0
    else:
        temp_offset = sum(timestamps) % 7
        metrics['offset'] = temp_offset  # Semi-relevant red herring

    return dict(metrics)

def analyze_trend(data_dict):
    values = list(data_dict.values())
    trend_scores = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_scores.append(1)
        elif values[i] < values[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    
    # Distractor computation
    avg_change = sum(abs(values[i] - values[i-1]) for i in range(1, len(values))) / (len(values) - 1)
    volatility = avg_change * 0.75  # Not used in final logic
    
    return sum(trend_scores)  # Net directional trend

def filter_outliers(data_dict, threshold=135):
    filtered = {k: v for k, v in data_dict.items() if v >= threshold}
    excess_vals = [v for v in data_dict.values() if v > threshold + 10]
    adjustment_factor = len(excess_vals) * 0.1  # Unused distraction
    return filtered

def calculate_efficiency(data_dict):
    base_vals = [v for v in data_dict.values() if 'step_' in k for k in [k for k in data_dict.keys()]]
    total = sum(base_vals)
    count = len(base_vals)
    efficiency_ratio = (total / count) / 100
    return round(efficiency_ratio, 4)

def evaluate_performance(metrics, baseline):
    # Step 1: Filter significant steps
    relevant = filter_outliers(metrics, threshold=132)
    
    # Step 2: Compute trend signal
    trend_signal = analyze_trend(relevant)
    
    # Step 3: Efficiency score
    efficiency = calculate_efficiency(metrics)
    
    # Step 4: Baseline adjustment with slicing distraction
    keys = list(metrics.keys())[1::2]  # Every other key – not used
    slice_offset = len(keys) * 0.05  # Irrelevant
    
    # Step 5: Main scoring logic
    base_score = sum(relevant.values())
    adjustment = baseline * 0.8
    raw_final = base_score - adjustment
    
    # Step 6: Apply efficiency multiplier
    final_score = raw_final * efficiency
    
    # Step 7: Final flooring (deterministic)
    final_score = int(final_score)
    
    # Extra dead-end calculation
    if final_score > 1000:
        scaling_curve = [final_score / (i+1) for i in range(5)]
        final_score -= int(scaling_curve[3])

    return final_score

# Main execution flow
if __name__ == '__main__':
    collected = collect_metrics()
    baseline_ref = 125
    final_score = evaluate_performance(collected, baseline_ref)
    print(f"Result: {final_score}")