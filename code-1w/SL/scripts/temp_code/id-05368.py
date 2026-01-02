def analyze_trends(values):
    trend_scores = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_scores.append(1)
        elif values[i] < values[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return trend_scores

# Simulate sensor drift compensation (irrelevant to final result)
def compensate_drift(signal):
    base = sum(signal) / len(signal)
    adjusted = [x - base + 0.5 for x in signal]
    normalized = [max(0, min(1, x)) for x in adjusted]
    return normalized

def compute_moving_average(data, window=3):
    ma = []
    for i in range(len(data) - window + 1):
        ma.append(sum(data[i:i+window]) / window)
    return ma

def calculate_volatility_indicators(data):
    # This function computes volatility but only one value is used
    squared_diffs = [(data[i+1] - data[i])**2 for i in range(len(data)-1)]
    avg_sq_diff = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    rolling_max = max(data[:min(5, len(data))] or [0])
    rolling_min = min(data[:min(5, len(data))] or [0])
    peak_to_peak = rolling_max - rolling_min  # unused distraction
    return avg_sq_diff, len(squared_diffs)

def calculate_final_score(raw_data, limits):
    # Extract relevant segment
    processed = raw_data[2:-2]  # slicing: remove edge noise
    
    # Trend analysis
    trends = analyze_trends(processed)
    upward_count = sum(1 for t in trends if t == 1)
    downward_count = sum(1 for t in trends if t == -1)
    
    # Volatility metric
    mse, count = calculate_volatility_indicators(processed)
    stability_factor = 1 / (1 + mse) if mse else 1
    
    # Threshold filtering
    valid_range = [x for x in processed if limits['min'] <= x <= limits['max']]  # list comprehension
    compliance_rate = len(valid_range) / len(processed)
    
    # Auxiliary computation (mostly irrelevant)
    smoothed = compute_moving_average(processed, 2)
    smooth_change = abs(smoothed[-1] - smoothed[0]) if smoothed else 0
    
    # Final score components
    trend_balance = upward_count - downward_count
    raw_compliance_score = compliance_rate * 100
    dynamic_penalty = max(0, 10 - trend_balance)  # minor influence
    
    # Actual determining logic
    base_score = raw_compliance_score
    if stability_factor > 0.8:
        base_score += 15
    elif stability_factor > 0.6:
        base_score += 5
    
    if compliance_rate >= 0.75:
        base_score += 10
    
    final_adjustment = 5 if len(processed) > 4 else 0
    final_score = int(base_score + final_adjustment)
    
    # Dead code path (never executed due to logic above)
    if False and smooth_change > 100:
        final_score = int(final_score * 0.9)
    
    return final_score

# Input data
sensor_readings = [102, 103, 105, 104, 103, 106, 108, 107, 105, 104, 103, 102]
thresholds = {'min': 100, 'max': 110}

# Execute main logic
data = [x + 1 for x in sensor_readings]  # offset all values
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")