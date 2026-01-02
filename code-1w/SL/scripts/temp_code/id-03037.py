from collections import defaultdict
import math

def analyze_trend(data):
    trend_changes = 0
    for i in range(1, len(data)):
        if (data[i] > data[i-1]) != (data[i-1] > data[i-2] if i >= 2 else False):
            trend_changes += 1
    return trend_changes

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def calculate_performance(base, inputs):
    history = defaultdict(int)
    adjusted_values = []
    
    # Irrelevant smoothing (distractor)
    filtered = smooth_signal(inputs)
    
    temp_sum = 0
    for val in inputs:
        deviation = abs(val - base)
        penalty = math.log(deviation + 1)
        adjusted = val - penalty
n        adjusted_values.append(adjusted)
        temp_sum += adjusted
        
    # Misleading trend analysis (semi-relevant)
    trend_noise = analyze_trend(inputs)
    adjustment_factor = 1.0
    if trend_noise > 3:
        adjustment_factor = 0.95
    
    # Core logic: average of adjusted values with factor
    avg_adjusted = temp_sum / len(adjusted_values) if adjusted_values else 0
    score = avg_adjusted * adjustment_factor
    
    # Dead code path (irrelevant)
    if False:
        backup = sum(history.values())
        score = max(score, backup)
    
    return int(score)

# Main execution
baseline = 50
readings = [45, 55, 40, 60, 35, 65, 30, 70]

# Auxiliary computation (distractor)
data_stats = {
    'mean': sum(readings) / len(readings),
    'variance': sum((x - baseline) ** 2 for x in readings) / len(readings)
}

# Key computation
final_score = calculate_performance(baseline, readings)

# Output result
print(f"Result: {final_score}")