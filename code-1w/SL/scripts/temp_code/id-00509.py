from collections import Counter, defaultdict

def analyze_trend(data):
    trend_counter = Counter()
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_counter['up'] += 1
        elif data[i] < data[i-1]:
            trend_counter['down'] += 1
        else:
            trend_counter['flat'] += 1
    return trend_counter

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def calculate_outlier_threshold(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return mean_val + (variance ** 0.5) * 1.5

def calculate_performance(base, logs):
    # Misleading preprocessing
    temp_data = [x * 1.05 for x in logs if x > 0]
    filtered_logs = [x for x in temp_data if x < calculate_outlier_threshold(temp_data)]
    
    # Actual logic begins
    if not filtered_logs:
        return 0
    
    # Simulate performance drift
    drift_metrics = defaultdict(float)
    for val in filtered_logs:
        if val > base * 1.1:
            drift_metrics['positive_drift'] += 1
        elif val < base * 0.9:
            drift_metrics['negative_drift'] += 1
    
    # Red herring: unused complex string analysis
    status_log = "System operational. All modules nominal."
    flag_count = len([c for c in status_log if c.isupper()])
    dummy_shift = status_log[::-1].replace(" ", "_").split('_')
    
    # Key slicing operation
    recent_logs = filtered_logs[-5:]  # Focus on latest 5
    
    # Compute stability score using modular arithmetic
    stability_score = 0
    for idx, reading in enumerate(recent_logs):
        contribution = (reading % 7) * (idx + 1)
        stability_score += contribution
    
    # Final performance formula
    positive = drift_metrics['positive_drift']
    negative = drift_metrics['negative_drift']
    net_bias = positive - negative
    
    # Final computation
    final_raw = stability_score + (net_bias * 3.5)
    
    # Normalize with redundant length check
    n = len(recent_logs)
    normalized = final_raw / n if n > 0 else 0
    
    # Distractor: unused helper call
    _ = analyze_trend(filtered_logs)
    
    return int(round(normalized))

# Main execution
baseline = 42
readings = [40, 45, 43, 38, 47, 46, 39, 41, 44, 48]

# Unused dead code path (distractor)
def deprecated_analysis():
    return sum(readings[i] * (i % 3) for i in range(len(readings)))

# Smooth but don't use
_ = smooth_signal(readings)

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")