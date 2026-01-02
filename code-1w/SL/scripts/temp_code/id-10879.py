from collections import defaultdict
import math

def analyze_component(x, threshold=5.0):
    if x < threshold:
        return x * 1.5
    else:
        return x - 2.0

def validate_readings(readings):
    valid_count = 0
    for r in readings:
        if r > 0 and r != float('inf'):
            valid_count += 1
    return valid_count > len(readings) * 0.7

def calculate_performance(data):
    temp_results = []
    scaling_factor = 1.2
    offset = 0.8
    
    # Irrelevant preprocessing: counts per category (not used in final logic)
    category_counts = defaultdict(int)
    for item in data:
        category_counts[item['type']] += 1
    
    # Core computation with distractions
    total_weight = 0.0
    raw_sum = 0.0
    penalty = 0.0
    
    for entry in data:
        value = entry['value']
        weight = entry['weight']
        
        adjusted = analyze_component(value)
        
        # Distractor: complex but unused transformation
        transformed = math.log(1 + abs(adjusted)) ** 0.5 if adjusted != 0 else 0
        
        raw_sum += adjusted * weight
        total_weight += weight
        
        if adjusted < 4.0:
            penalty += 1.5
    
    if total_weight == 0:
        normalized = 0.0
    else:
        normalized = raw_sum / total_weight
    
    # Additional distraction: simulate validation on a subset
    sample_values = [d['value'] for d in data[::2]]
    is_stable = validate_readings(sample_values)
    
    # Final score calculation — only this matters
    base_score = normalized * scaling_factor + offset
    if is_stable:
        base_score += 2.0  # bonus
    
    final_score = int(base_score - penalty)  # integer result
    
    # Dead code path (never reached in this input)
    if False and len(data) > 100:
        fallback = sum(d['value'] for d in data)
        final_score = int(fallback % 50)
    
    return final_score

# Simulated benchmark data
benchmark_data = [
    {'value': 3.0, 'weight': 2, 'type': 'A'},
    {'value': 7.5, 'weight': 3, 'type': 'B'},
    {'value': 2.0, 'weight': 1, 'type': 'A'},
    {'value': 6.0, 'weight': 4, 'type': 'C'},
    {'value': 4.5, 'weight': 2, 'type': 'B'}
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")