from collections import defaultdict
import math

def analyze_metrics(data, threshold=0.75):
    stats = defaultdict(int)
    temp_buffer = []
    for item in data:
        raw_value = item['value']
        normalized = raw_value / (max(1, item['baseline']))
        
        # Irrelevant transformation (distractor)
        squared_deviation = (normalized - 0.5) ** 2
        temp_buffer.append(squared_deviation)
        
        if normalized > threshold:
            stats['high'] += 1
        elif normalized > 0.5:
            stats['medium'] += 1
        else:
            stats['low'] += 1
    
    # Dead code path - never used later (distractor)
    if len(temp_buffer) > 10:
        moving_avg = sum(temp_buffer[-5:]) / 5
    else:
        moving_avg = 0
    
    return stats

def calculate_performance(dataset):
    totals = {'a': 0, 'b': 0, 'c': 0}
    count_tracker = defaultdict(int)
    
    for entry in dataset:
        category = entry['category']
        value = entry['value']
        baseline = entry['baseline']
        
        # Real computation branch
        adjusted = value * math.log2(max(1, baseline))
        if category == 'A':
            totals['a'] += adjusted
        elif category == 'B':
            totals['b'] += adjusted
        else:
            totals['c'] += adjusted
        
        # Misleading counter update (semi-relevant but unused)
        count_tracker[category] += 1
    
    # Composite score calculation (uses only totals)
    aggregate = sum(totals.values())
    penalty = abs(totals['a'] - totals['c']) * 0.1  # Small penalty factor
    raw_score = aggregate - penalty
    
    # Additional noise: irrelevant normalization
    max_total = max(totals.values())
    if max_total > 0:
        normalized_score = raw_score / max_total
    else:
        normalized_score = raw_score
    
    # Final transformation
    final_score = int(round(normalized_score * 1.25))
    
    # This print is required to show result
    print(f"Result: {final_score}")
    return final_score

# Simulated benchmark data
benchmark_data = [
    {'category': 'A', 'value': 12, 'baseline': 8},
    {'category': 'B', 'value': 9, 'baseline': 4},
    {'category': 'A', 'value': 15, 'baseline': 6},
    {'category': 'C', 'value': 7, 'baseline': 16},
    {'category': 'B', 'value': 11, 'baseline': 5},
    {'category': 'C', 'value': 6, 'baseline': 32},
    {'category': 'A', 'value': 10, 'baseline': 4}
]

# Secondary distractor analysis (never called)
def debug_consistency(data):
    errors = 0
    for d in data:
        if d['value'] < 0:
            errors += 1
    return errors

# Actual execution flow
metrics = analyze_metrics(benchmark_data, threshold=0.6)
final_score = calculate_performance(benchmark_data)