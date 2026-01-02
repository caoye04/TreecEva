def analyze_trend(data, window):
    if len(data) < window:
        return [0]
    trends = []
    for i in range(len(data) - window + 1):
        segment = data[i:i + window]
        avg = sum(segment) / window
        trend = 1 if segment[-1] > avg else -1 if segment[-1] < avg else 0
        trends.append(trend)
    return trends

# Simulate system health metrics over time
raw_logs = [85, 90, 88, 92, 95, 87, 89, 94, 96, 93]
baseline = [90, 88, 86, 91, 89, 87, 92, 90, 88, 91]

# Misleading transformation (not used in final result)
transformed = [x ** 0.5 * 1.5 for x in raw_logs]
scaled_logs = [x + 5 for x in raw_logs]  # Distractor: looks important but unused

# Extract key performance windows
window_size = 3
smoothed = [sum(raw_logs[i:i+window_size]) / window_size for i in range(0, len(raw_logs), window_size)]

# Detect improvement patterns
improvement_flags = []
for i in range(1, len(smoothed)):
    if smoothed[i] > smoothed[i-1]:
        improvement_flags.append(1)
    else:
        improvement_flags.append(0)

# Auxiliary calculation with red herring variables
offset_correction = sum(baseline[:3]) - sum(raw_logs[:3])
dummy_state = {'status': 'active', 'count': offset_correction}  # Dead code path

# Core evaluation logic
def evaluate_performance(metrics, reference):
    base_metric = sum(metrics[:4]) / 4
    ref_avg = sum(reference[2:6]) / 4
    deviation = abs(base_metric - ref_avg)
    
    # Secondary adjustment using slice analysis
    recent_slice = metrics[-4:]
    growth_trend = 0
    for j in range(1, len(recent_slice)):
        if recent_slice[j] > recent_slice[j-1]:
            growth_trend += 1
    
    # Combine factors with weight
    score = base_metric - deviation
    if growth_trend >= 2:
        score += 5
    
    # Final adjustment based on trend consistency
    full_trends = analyze_trend(metrics, 2)
    consistent_up = full_trends.count(1)
    if consistent_up > 5:
        score += 3
    
    return int(score)

# Execute main logic
intermediate_result = analyze_trend(raw_logs, 2)
final_score = evaluate_performance(raw_logs, baseline)
print(f"Result: {final_score}")