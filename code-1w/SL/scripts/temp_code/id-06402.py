from collections import defaultdict
import math

# Simulate system performance metrics over time
raw_data = [120, 85, 90, 100, 75, 95, 80]
timestamps = [1, 2, 3, 4, 5, 6, 7]

def smooth_signal(data, factor=0.2):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(factor * data[i] + (1 - factor) * smoothed[-1])
    return smoothed

# Apply smoothing to raw data
filtered = smooth_signal(raw_data)

# Misleading transformation - not used in final result
transformed = list(map(lambda x: round(math.log(x + 1) ** 2), raw_data))
offset = sum(transformed) // len(transformed)  # Irrelevant aggregation

# Extract key performance indicators
kpi_map = defaultdict(int)
for i, val in enumerate(filtered):
    if val >= 85:
        kpi_map['high'] += 1
    elif val >= 75:
        kpi_map['medium'] += 1
    else:
        kpi_map['low'] += 1

# Compute rolling averages (partially relevant)
window_size = 3
rolling_averages = [sum(filtered[i:i+window_size]) / window_size 
                        for i in range(len(filtered) - window_size + 1)]

# Distractor: unused statistical measures
variance_proxy = sum((x - sum(filtered)/len(filtered))**2 for x in filtered) / len(filtered)
peak_deviation = max(filtered) - min(filtered)

# Core evaluation logic
baseline = sum(filtered[:3]) / 3
recent_trend = sum(filtered[-3:]) / 3
improvement = recent_trend - baseline

# Weighted metric computation
metrics = {
    'stability': len(rolling_averages),
    'consistency': kpi_map['high'],
    'trend': improvement,
    'volume': sum(raw_data)
}

weights = {
    'stability': 0.2,
    'consistency': 0.3,
    'trend': 0.4,
    'volume': 0.1
}

# Dead code path - never executed but looks important
def deprecated_scoring(m):
    return sum(v**0.5 for v in m.values())

# Actual scoring function
def evaluate_performance(m, w):
    score = 0.0
    for key in m:
        if key == 'trend':
            # Special non-linear boost for positive trend
            adjusted = max(0, m[key]) * 1.5
        else:
            adjusted = m[key]
        score += adjusted * w[key]
    
    # Additional adjustment based on high-performance streaks
    streak = 0
    max_streak = 0
    for val in filtered:
        if val >= 85:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    
    if max_streak >= 3:
        score *= 1.1  # Bonus for sustained performance
        
    return round(score, 4)

# Final computation
final_score = evaluate_performance(metrics, weights)

# Debug print that could mislead about importance
print(f"Signal variance: {variance_proxy:.2f}")
print(f"Peak deviation: {peak_deviation}")

Result: {final_score}