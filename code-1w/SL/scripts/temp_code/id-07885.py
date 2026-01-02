from collections import defaultdict
import math

def analyze_metrics(entries):
    totals = defaultdict(float)
    counts = defaultdict(int)
    
    # Process each entry with multiple irrelevant transformations
    temp_offsets = [math.sin(i * 0.1) for i in range(len(entries))]
    base_adjustment = sum(temp_offsets) / len(temp_offsets) if temp_offsets else 0
    
    for idx, entry in enumerate(entries):
        category = entry['type']
        raw_value = entry['value']
        
        # Real computation path
        adjusted = raw_value * (1 + math.cos(idx)) ** 2
        totals[category] += adjusted
        counts[category] += 1
        
        # Distractor: tracking unused intermediate stats
        noise_factor = abs(math.tanh(raw_value - base_adjustment))
        _ = noise_factor * 0.01  # Dead computation
    
    return totals, counts

def normalize_results(totals, counts):
    averages = {}
    for k in totals:
        averages[k] = totals[k] / counts[k] if counts[k] else 0
    
    # Extra logic that doesn't impact final result
    outlier_threshold = sum(averages.values()) / len(averages) * 1.5 if averages else 0
    filtered = {k: v for k, v in averages.items() if v <= outlier_threshold}
    
    # Return full averages anyway (distractor)
    return averages

def calculate_performance(data):
    # Secondary distraction: pre-scan for rare types
    rare_types = [d['type'] for d in data if d['value'] < 10]
    rare_freq = defaultdict(int)
    for t in rare_types:
        rare_freq[t] += 1
    
    # Real pipeline begins
    totals, counts = analyze_metrics(data)
    norms = normalize_results(totals, counts)
    
    # Core calculation disguised among distractions
    primary_weight = 0.7
    secondary_weight = 0.3
    
    main_contrib = sum(v for k, v in norms.items() if 'A' in k)
    aux_contrib = sum(v for k, v in norms.items() if 'B' in k)
    
    # Actual answer derived here
    final_score = (main_contrib * primary_weight + aux_contrib * secondary_weight) // 1
    
    # More red herrings
    _ = [math.log(1 + x) for x in [main_contrib, aux_contrib]]
    _ = ''.join([chr(65 + (i % 26)) for i in range(10)])  # Irrelevant string gen
    
    return final_score

# Simulated benchmark dataset
benchmark_data = [
    {'type': 'AX7', 'value': 25},
    {'type': 'BX2', 'value': 18},
    {'type': 'AX1', 'value': 33},
    {'type': 'CX9', 'value': 8},
    {'type': 'BX2', 'value': 21},
    {'type': 'AX5', 'value': 15},
    {'type': 'DX4', 'value': 12}
]

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")