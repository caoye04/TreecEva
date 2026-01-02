def analyze_trends(data, window_size):
    trends = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i + window_size]
        avg = sum(segment) / len(segment)
        trend = 'up' if segment[-1] > segment[0] else 'down'
        trends.append((avg, trend))
    return trends

# Irrelevant helper function (distractor)
def normalize_values(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

def calculate_volatility(series):
    if len(series) < 2:
        return 0.0
    diffs = [abs(series[i] - series[i-1]) for i in range(1, len(series))]
    return sum(diffs) / len(diffs)

def evaluate_performance(metrics, base):
    adjusted = {}
    for k, v in metrics.items():
        if k == 'latency':
            adjusted[k] = base['latency'] / v  # efficiency ratio
        elif k == 'throughput':
            adjusted[k] = v / base['throughput']
        elif k == 'error_rate':
            adjusted[k] = 1 - (v / base['error_rate']) if base['error_rate'] > 0 else 0
    
    # Semi-relevant computation (only one value used later)
    stability = calculate_volatility(list(metrics.values()))
    temp_flag = True if stability < 0.5 else False
    
    composite = 0
    for val in adjusted.values():
        composite += val * 100  # scale up for percentage-like score

    # Distractor variables
    temp_offset = 17
    dummy_list = [1, 2, 3, 4]
    unused_calc = sum(dummy_list) * temp_offset
    
    final_score = int(composite)
    return final_score

# Main execution
raw_data = [120, 135, 130, 145, 160, 158, 170]
window = 3
results = analyze_trends(raw_data, window)

# Extract key metric components
metric_snapshot = {
    'latency': 45,
    'throughput': 880,
    'error_rate': 0.023
}
baseline_config = {
    'latency': 50,
    'throughput': 800,
    'error_rate': 0.025
}

# Key statement
final_score = evaluate_performance(metric_snapshot, baseline_config)
print(f"Target result: {final_score}")