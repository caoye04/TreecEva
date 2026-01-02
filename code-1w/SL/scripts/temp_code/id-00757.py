from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 85, 90, 65, 72, 88, 93, 60, 77, 84]
    timestamps = list(range(10))
    
    # Irrelevant transformation (distractor)
    squared_offsets = [x**2 for x in range(5)]
    temp_correction = sum(squared_offsets) / len(squared_offsets)
    
    metric_dict = defaultdict(list)
    for t, val in zip(timestamps, raw_data):
        metric_dict['values'].append(val)
        metric_dict['status'].append('high' if val >= 80 else 'low')
    
    return metric_dict

def analyze_trend(data):
    trend_counter = defaultdict(int)
    prev = data['values'][0]
    
    # Track direction changes (up/down/stable)
    for val in data['values'][1:]:
        if val > prev:
            trend_counter['up'] += 1
        elif val < prev:
            trend_counter['down'] += 1
        else:
            trend_counter['stable'] += 1
        prev = val
    
    # Compute derived statistics (some irrelevant)
    total_change = sum(abs(data['values'][i+1] - data['values'][i]) for i in range(len(data['values'])-1))
    average_fluctuation = total_change / (len(data['values']) - 1)
    
    # Distractor computation with no impact
    phantom_score = 0
    for i in range(3):
        for j in range(3):
            phantom_score += i * j
    
    return trend_counter['up'] > trend_counter['down']

def apply_weighting(values, base_weight=0.1):
    weighted_sum = 0.0
    decay = 0.9
    for i, val in enumerate(reversed(values)):
        weight = base_weight * (decay ** i)
        weighted_sum += val * weight
    return weighted_sum

def evaluate_performance(metric_data, thresholds):
    values = metric_data['values']
    
    # Early filtering based on threshold
    filtered_vals = [v for v in values if v >= thresholds['min_acceptable']]
    
    if len(filtered_vals) == 0:
        return 0
    
    # Key logic: trend matters only if recent performance is good
    recent_trend_positive = analyze_trend(metric_data)
    recent_average = sum(values[-3:]) / 3
    
    # Secondary distractor variables
    peak_value = max(values)
    valley_count = 0
    for i in range(1, len(values)-1):
        if values[i-1] > values[i] < values[i+1]:
            valley_count += 1
    
    # Weighted score using decay
    base_score = apply_weighting(values)
    
    # Final decision logic
    if recent_trend_positive and recent_average >= thresholds['trend_bonus_min']:
        bonus_multiplier = 1.5
    else:
        bonus_multiplier = 1.0
    
    final_score = int(base_score * bonus_multiplier)
    
    # Dead code branch (never executed under current logic)
    if False and peak_value > 100:
        final_score = min(final_score, 95)
    
    return final_score

# Main execution
metric_data = collect_metrics()
thresholds = {
    'min_acceptable': 70,
    'trend_bonus_min': 75
}
final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")