from itertools import compress, cycle

def analyze_pattern(sequence):
    # Distractor: Analyzes frequency but not used in final result
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in freq.items() if v > 1}

def validate_stability(readings):
    # Distractor: Stability check that is never called
    threshold = 0.05
    return all(abs(a - b) < threshold for a, b in zip(readings, readings[1:]))

def filter_outliers(data, limit=3):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    # This function is called but filtered_data is partially ignored
    return [x for x in data if abs(x - mean_val) <= limit * std_dev]

def compute_efficiency(tasks, overhead):
    total_work = sum(t['cycles'] for t in tasks)
    base_time = sum(t['duration'] for t in tasks)
    if base_time == 0:
        return 0.0
    efficiency = (total_work / (base_time + overhead)) * 0.95
    return round(efficiency, 4)

def main():
    # Irrelevant sensor data
    sensor_logs = [23.1, 22.9, 24.0, 23.1, 23.5, 1000.0, -999.0, 23.3]
    processed_logs = filter_outliers(sensor_logs)
    
    # Red herring: unused transformation
    normalized = [(x - min(processed_logs)) / (max(processed_logs) - min(processed_logs)) for x in processed_logs]
    
    # Core input data (real signal amidst noise)
    metrics = [
        {'name': 'throughput', 'value': 850},
        {'name': 'latency', 'value': 120},
        {'name': 'accuracy', 'value': 0.98},
        {'name': 'bandwidth', 'value': 45.5}
    ]
    
    # Weight vector – some weights are decoys
    raw_weights = [0.4, 0.3, 0.2, 0.1]
    weight_cycle = cycle(raw_weights)
    weights = [next(weight_cycle) for _ in range(len(metrics))]
    
    # Fake subsystem: resource contention simulation (dead path)
    contention_levels = [0.1, 0.3, 0.2]
    impact_factor = 0
    for level in contention_levels:
        if level > 0.25:
            impact_factor += level * 1.5
    # impact_factor is computed but unused

    # Real logic buried here
    adjusted_metrics = []
    for i, m in enumerate(metrics):
        raw_val = m['value']
        w = weights[i]
        if m['name'] == 'latency':
            # Invert latency since lower is better
            transformed = (1 / raw_val) * 1000
        elif m['name'] == 'accuracy':
            transformed = raw_val * 100  # Convert to percentage
        else:
            transformed = raw_val
        adjusted_metrics.append(transformed * w)
    
    # Aggregate with distraction of lambda and zip
    multiplier = lambda x: x * 1.1 if x < 90 else x * 0.95
    boosted = [multiplier(val) for val in adjusted_metrics]
    
    # Key statement embedded in irrelevant pairing
    paired = list(zip(boosted, ['A', 'B', 'C', 'D']))  # 'B', 'C', 'D' are red herrings
    final_score = sum(p[0] for p in paired)  # Actual answer computation
    
    # Decoy print and unused variable
    temp_result = sum(b for b in boosted if b > 100)
    
    # Critical output
    print(f"Result: {final_score}")
    
    return final_score

if __name__ == "__main__":
    main()