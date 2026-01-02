from collections import defaultdict, Counter

def analyze_metrics(entries):
    totals = defaultdict(float)
    counts = Counter()
    temp_buffer = []
    
    for idx, entry in enumerate(entries):
        category = entry['type']
        value = entry['value']
        
        if category == 'latency':
            totals['response_time'] += value * 0.8
        elif category == 'throughput':
            totals['volume'] += value
            counts['throughput'] += 1
        elif category == 'error_rate':
            totals['errors'] += max(value, 0.1)
        
        # Irrelevant computation (distractor)
        temp_buffer.append(idx * value % 3)
    
    # Dead code path - never executed due to logic above
    if len(temp_buffer) > 1000:
        totals['overflow'] = sum(temp_buffer) / 100

    return totals

def calculate_performance(logs):
    aggregated = analyze_metrics(logs)
    base_score = 100.0
    penalty = 0.0
    
    # Real scoring logic
    if 'response_time' in aggregated:
        penalty += aggregated['response_time'] / 10
    if 'volume' in aggregated and counts.get('throughput', 0) > 0:
        base_score += min(aggregated['volume'] / counts['throughput'], 20)
    if 'errors' in aggregated:
        penalty += aggregated['errors'] * 5
    
    # Misleading intermediate calculations
    debug_factor = len(logs) % 7
    adjustment = debug_factor * 0.3
    dummy_score = (base_score - penalty) * adjustment  # Not used
    
    final_score = int(base_score - penalty)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

counts = {}  # Global counter reused in logic
benchmark_data = [
    {'type': 'latency', 'value': 15},
    {'type': 'throughput', 'value': 120},
    {'type': 'latency', 'value': 25},
    {'type': 'throughput', 'value': 140},
    {'type': 'error_rate', 'value': 0.15},
    {'type': 'latency', 'value': 10},
    {'type': 'throughput', 'value': 130}
]

# Key execution point
final_score = calculate_performance(benchmark_data)