from itertools import combinations

def analyze_trends(data_points):
    trends = []
    for i in range(1, len(data_points)):
        if data_points[i] > data_points[i-1]:
            trends.append('up')
        elif data_points[i] < data_points[i-1]:
            trends.append('down')
        else:
            trends.append('flat')
    return trends

# Simulate system health metrics over time
timestamps = list(range(10))
data_stream = [23, 45, 45, 67, 66, 89, 95, 95, 101, 102]

# Extract trend behavior
trend_sequence = analyze_trends(data_stream)

# Misleading auxiliary computation (distractor)
streak_count = 0
max_streak = 0
for trend in trend_sequence:
    if trend == 'up':
        streak_count += 1
        max_streak = max(max_streak, streak_count)
    else:
        streak_count = 0

# Core metric processing
baseline = sum(data_stream) / len(data_stream)
variance = sum((x - baseline) ** 2 for x in data_stream) / len(data_stream)
std_deviation = variance ** 0.5

# Normalize values into performance metrics
metrics = {
    'stability': round(100 - (std_deviation / baseline * 50), 2),
    'growth': sum(1 for t in trend_sequence if t == 'up'),
    'consistency': len(set(data_stream[i:i+2]) for i in range(len(data_stream)-1)),  # dummy complexity
    'peaks': len([i for i in range(1, len(data_stream)-1) if data_stream[i-1] < data_stream[i] > data_stream[i+1]])
}

# Real consistency measure overwritten due to distractor above
metrics['consistency'] = len([i for i in range(len(trend_sequence)) if trend_sequence[i] == 'up'])

thresholds = {
    'min_growth': 4,
    'min_stability': 70.0,
    'max_peaks': 3
}

# Evaluate performance with conditional logic and set operations
def evaluate_performance(metrics, thresholds):
    score = 50
    adjustments = set()
    
    # Logical checks with bit manipulation red herring
    growth_met = metrics['growth'] >= thresholds['min_growth']
    stability_met = metrics['stability'] >= thresholds['min_stability']
    peaks_met = metrics['peaks'] <= thresholds['max_peaks']
    
    # Irrelevant bitwise operation chain (distractor)
    flag = 1
    flag = flag << 2 | 1
    flag ^= 3
    
    # Actual scoring logic
    if growth_met:
        score += 15
        adjustments.add('growth_bonus')
    if stability_met:
        score += 20
        adjustments.add('stability_bonus')
    if peaks_met:
        score += 10
        adjustments.add('peak_penalty_avoided')
    
    # Bonus for perfect flat sequences (not triggered)
    flat_segments = [i for i, t in enumerate(trend_sequence) if t == 'flat']
    flat_pairs = list(combinations(flat_segments, 2))
    if len(flat_pairs) > 5:
        score += 5  # dead code path
    
    # Final correction based on initial data properties
    first_val, last_val = data_stream[0], data_stream[-1]
    improvement_ratio = (last_val - first_val) / first_val
    if improvement_ratio > 0.2:
        score += 5
    
    return int(score)

# Critical execution point
final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")