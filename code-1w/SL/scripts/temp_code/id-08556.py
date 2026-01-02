import math

# Simulated sensor data processing system
def analyze_readings(raw_samples):
    filtered = [x for x in raw_samples if 0.1 < abs(x) < 100.0]
    baseline = sum(filtered) / len(filtered) if filtered else 0.0
    
    # Irrelevant transformation (distractor)
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered] if filtered else []
    noise_floor = sum([abs(x - baseline) for x in filtered]) / len(filtered) if filtered else 0.0
    
    return {'baseline': baseline, 'noise': noise_floor, 'count': len(filtered)}

# Unused helper (dead code path)
def deprecated_calibrate(signal):
    return [math.sin(x) * 0.5 + 1 for x in signal]

# Core evaluation logic
def compute_metric_a(data, weights):
    weighted_sum = sum(d * w for d, w in zip(data, weights))
    penalty = 0.1 * len([x for x in data if x < 0])
    return max(weighted_sum - penalty, 0.0)

def compute_metric_b(values):
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val)**2 for x in values) / len(values)
    return math.sqrt(variance) if variance > 0.1 else 0.1

# Complex conditional aggregator
def aggregate_metrics(metrics, mode='strict'):
    if mode == 'strict':
        threshold_op = lambda x: x >= 0.7
    else:
        threshold_op = lambda x: x >= 0.5

    valid_count = sum(1 for m in metrics if threshold_op(m['score']))
    total_impact = sum(m['weight'] * m['score'] for m in metrics)
    
    # Distractor computation with unused result
    hypothetical = [m['score'] * 1.2 for m in metrics if m['weight'] > 0.3]
    stability_factor = len(hypothetical) / len(metrics) if metrics else 0
    
    return {'valid': valid_count, 'impact': total_impact, 'stability': stability_factor}

# Misleading auxiliary function (never called in execution path)
def adjust_for_drift(readings, factor=0.98):
    return [r * factor ** i for i, r in enumerate(readings)]

# Primary evaluation engine
def evaluate_performance(criteria, context):
    results = []n    temp_buffer = []
    
    for i, item in enumerate(criteria):
        raw_data = context.get(f'data_{i}', [])
        analysis = analyze_readings(raw_data)
        
        # Compute two different metrics per criterion
        metric_a = compute_metric_a(raw_data, context.get('weights', [1.0]))
        metric_b = compute_metric_b(raw_data)
        
        # Normalize and combine
        combined_score = (metric_a * 0.6 + metric_b * 0.4) / (10.0 + analysis['noise'])
        weight = context.get('importance', [1.0]*len(criteria))[i]
        
        # Add to results
        results.append({'score': combined_score, 'weight': weight})
        
        # Red herring: build buffer that's never used
        temp_buffer.append({
            'idx': i,
            'raw_len': len(raw_data),
            'base': analysis['baseline'],
            'calib': math.log(analysis['noise'] + 1)
        })
    
    # Aggregate final assessment
    summary = aggregate_metrics(results, mode='strict')
    
    # Final scoring with distraction variables
    base_score = summary['impact']
    bonus = 5.0 if summary['valid'] >= 2 else 0.0
    decay = 0.95 ** len(temp_buffer)  # Uses unused buffer (misleading)
    
    # Key assignment - this is the answer point
    final_score = int(round(base_score * 100 * decay + bonus))
    
    # Unrelated cleanup
    temp_buffer.clear()
    
    return final_score

# Execution setup
if __name__ == '__main__':
    # Simulation parameters
    metric_set = [
        {'type': 'pressure', 'threshold': 0.5},
        {'type': 'temperature', 'threshold': 0.6},
        {'type': 'flow', 'threshold': 0.4}
    ]
    
    calibration_data = {
        'data_0': [12.5, 13.1, 11.8, -2.3, 14.0, 13.5],
        'data_1': [8.7, 9.2, -1.5, 8.9],
        'data_2': [25.3, 24.8, 26.1, -3.2, 25.7],
        'weights': [0.8, 0.9, 1.1, 0.7],
        'importance': [0.9, 1.2, 1.0]
    }
    
    # These variables are distractions
    system_status = 'ACTIVE'
    last_update = '2023-11-05'
    debug_trace = []
    
    # Critical execution point
    final_score = evaluate_performance(metric_set, calibration_data)
    
    # Output result
    print(f"Result: {final_score}")