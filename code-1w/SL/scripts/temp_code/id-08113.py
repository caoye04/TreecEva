from collections import defaultdict
import math

def analyze_trend(data):
    trend_changes = 0
    for i in range(1, len(data)):
        if (data[i] > data[i-1]) != (data[i-1] > data[i-2] if i >= 2 else False):
            trend_changes += 1
    return trend_changes

def calculate_performance(base, values):
    adjusted = [v - base + 10 for v in values]
    
    # Irrelevant transformation (distractor)
    squared_offsets = [math.pow(x, 2) for x in adjusted if x < 0]
    temp_sum = sum(squared_offsets) if squared_offsets else 0
    
    # Core logic disguised among noise
    magnitude_factor = sum(abs(x) for x in adjusted)
    sign_flips = sum(1 for x in range(1, len(adjusted)) if adjusted[x] * adjusted[x-1] < 0)
    
    # Dead computation path (distractor)
    helper_map = defaultdict(int)
    for val in adjusted:
        if val % 4 == 0:
            helper_map['even_quarter'] += 1
        elif val % 3 == 0:
            helper_map['triple'] += 1
    
    # Actual answer derivation
    stability_penalty = sign_flips * 2.5
    raw_performance = magnitude_factor - stability_penalty
    
    # Conditional expression used idiomatically
    final_score = raw_performance if raw_performance > 0 else max(raw_performance, -50)
    
    return final_score

# Simulated sensor readings
baseline = 78
readings = [85, 70, 72, 60, 65, 55, 58]

# Auxiliary variables (misleading state tracking)
total_drift = sum(abs(readings[i] - readings[i-1]) for i in range(1, len(readings)))
fluctuation_rate = total_drift / len(readings)

# Key call point
trend_complexity = analyze_trend(readings)
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")