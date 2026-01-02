from collections import defaultdict
import math

def analyze_readings(readings):
    stats = defaultdict(float)
    total = 0
    count = 0
    max_val = float('-inf')
    min_val = float('inf')
    
    for r in readings:
        if r > max_val:
            max_val = r
        if r < min_val:
            min_val = r
        total += r
        count += 1
        
    stats['average'] = total / count if count else 0
    stats['peak_to_peak'] = max_val - min_val
    return stats

def apply_correction(value, method='linear'):
    # Simulate some irrelevant transformation
    if method == 'linear':
        return value * 1.05
    elif method == 'quadratic':
        return value ** 1.1
    else:
        return value

def process_metrics(data, weights):
    # Core logic with distractions
    temp_results = []
    scaling_factor = 1.2
    offset_cache = [0] * len(data)  # Unused cache (distractor)
    
    for i, entry in enumerate(data):
        reading_stats = analyze_readings(entry['values'])
        base_metric = reading_stats['average']
        
        # Apply weight and transform
        weighted_value = base_metric * weights[i]
        corrected = apply_correction(weighted_value, 'linear')
        temp_results.append(corrected)
    
    # Aggregate using lambda (required feature)
    aggregator = lambda x: sum(x) / len(x)
    avg_corrected = aggregator(temp_results)
    
    # Secondary processing
    deviation_pool = []
    for val in temp_results:
        deviation_pool.append(abs(val - avg_corrected))
    
    mean_deviation = sum(deviation_pool) / len(deviation_pool)
    
    # Final score calculation
    final_score = math.floor(avg_corrected - mean_deviation * 0.5)
    
    # Irrelevant post-calculation (dead code path)
    if final_score < 0:
        final_score = abs(final_score)
    else:
        temp_flag = False  # Distractor flag
        for _ in range(2):
            temp_flag = not temp_flag
    
    return int(final_score)

# Input data
readings_data = [
    {'id': 'A', 'values': [85, 90, 92, 87]},
    {'id': 'B', 'values': [78, 80, 82, 79]},
    {'id': 'C', 'values': [95, 93, 97, 94]}
]

weights_list = [0.8, 1.1, 1.3]

# Execution point
final_score = process_metrics(readings_data, weights_list)
print(f"Target result: {final_score}")