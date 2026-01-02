from collections import Counter, defaultdict
import math

def analyze_trend(data):
    trend_changes = 0
    for i in range(1, len(data)):
        if (data[i] > data[i-1]) != (data[i-1] > data[i-2] if i >= 2 else False):
            trend_changes += 1
    return trend_changes

def calculate_performance(base, inputs):
    # Normalize inputs relative to base with some irrelevant transformations
    normalized = [(x - base) / (base + 1e-5) for x in inputs]
    squared_errors = [((x - base) ** 2) for x in inputs]
    
    # Distractor: string-based tagging of values (not used in final result)
    labels = []
    for val in inputs:
        if val > base * 1.1:
            labels.append('high')
        elif val < base * 0.9:
            labels.append('low')
        else:
            labels.append('stable')
    label_counts = Counter(labels)
    
    # Actual logic path
    above_base = sum(1 for x in inputs if x > base)
    below_base = sum(1 for x in inputs if x < base)
    matches = sum(1 for x in inputs if abs(x - base) < 1e-3)
    
    # Simulate performance score with weighted factors
    stability_factor = len(inputs) - analyze_trend(inputs)
    raw_score = above_base * 1.5 + below_base * (-1.2) + stability_factor * 0.8
    
    # Dead code path — never affects result but adds cognitive load
    debug_info = defaultdict(list)
    for i, x in enumerate(inputs):
        debug_info['indices'].append(i)
        if x % 2 == 0:
            debug_info['evens'].append(x)
    
    # Final computation
    adjustment = math.log(abs(raw_score) + 1)
    final_score = int(raw_score + adjustment)
    
    # Irrelevant slicing and string operations
    seq_str = ''.join([str(int(x))[-1] for x in inputs if x > 0])
    mid_segment = seq_str[1:-1] if len(seq_str) > 2 else ''
    digit_freq = {d: mid_segment.count(d) for d in set(mid_segment)}
    
    return final_score

# Main execution block
baseline = 42
readings = [38, 45, 47, 39, 40, 48, 50, 37, 41, 43]
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")