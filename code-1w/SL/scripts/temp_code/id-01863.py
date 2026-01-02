import itertools

# Simulated system health metrics from distributed nodes
def collect_metrics():
    raw_data = [15, 23, 42, 19, 8, 31, 27]
    offset = 0
    processed = []
    for val in raw_data:
        temp = (val + offset) * 1.5
        if temp > 30:
            processed.append(int(temp) // 2)
        else:
            processed.append(int(temp) + 5)
        offset += 2
    return {f'node_{i}': v for i, v in enumerate(processed)}

def analyze_stability(metric_dict):
    values = list(metric_dict.values())
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    # Irrelevant transformation
    transformed = [x * 0.9 + 3 for x in values if x % 2 == 0]
    adjustment_factor = 1.0
    if len(transformed) > 3:
        adjustment_factor = 0.95
    # Dead code path - never used
    def deprecated_normalize(data):
        m = max(data)
        return [d / m for d in data]
    return avg, variance, adjustment_factor

def compute_fragments(data):
    # Unrelated fragment: generates combinations but doesn't affect output
    keys = list(data.keys())
    combinations = list(itertools.combinations(keys, 2))
    pair_scores = {}
    for pair in combinations:
        k1, k2 = pair
        score = abs(int(k1.split('_')[1]) - int(k2.split('_')[1])) * 0.5
        pair_scores[f'{k1}-{k2}'] = round(score, 2)
    # This function appears important but is not used in final calculation
    return pair_scores

def filter_outliers(data_dict, threshold=25):
    filtered = {}
    total = 0
    count = 0
    for k, v in data_dict.items():
        if v < threshold:
            filtered[k] = v
            total += v
            count += 1
    # Misleading average
    fake_avg = total / (count + 1) if count < 5 else 0
    return filtered

# Core evaluation logic
def evaluate_reliability(seq):
    acc = 0
    for i, x in enumerate(seq):
        if i % 3 == 0:
            acc += x * 2
        elif i % 3 == 1:
            acc -= x
        else:
            acc += x // 2
    return acc

def evaluate_performance(metrics, benchmark):
    # Key variable initialization
    base_score = 0
    for key, value in metrics.items():
        if 'node_2' in key or 'node_5' in key:
            base_score += value * 1.1
        elif 'node_' in key:
            base_score += value * 0.9
    
    # Red herring: complex structure that isn't used
    history_log = [
        {'epoch': e, 'value': (e * 1.8) % 40, 'flag': False} 
        for e in range(10)
    ]
    recent = history_log[-1]['value'] if history_log else 0
    
    # Real computation branch
    valid_metrics = filter_outliers(metrics, threshold=22)
    sequence = list(valid_metrics.values())
    reliability_bonus = evaluate_reliability(sequence)
    
    # Decoy dictionary operations
    decoy_map = {i: chr(97 + (i * 7) % 26) for i in range(15)}
    mapped = ''.join([decoy_map.get(s % 15, '?') for s in sequence])
    
    # Actual accumulation
    final_score = int(base_score + reliability_bonus)
    
    # Unused branching logic to mislead
    if len(mapped) > 5 and recent > 20:
        final_score = int(final_score * 0.85)
    elif recent == 0:
        final_score += 10
    
    return final_score

# Execution flow
if __name__ == '__main__':
    # Collect primary metrics
    metrics = collect_metrics()
    
    # Generate unused benchmark structure
    benchmark_data = {
        'version': '2.1',
        'targets': [f'node_{i}' for i in range(8)],
        'weights': [0.1, 0.3, 0.6, 0.8, 1.0, 0.7, 0.4, 0.2],
        'baseline': 20.5
    }
    
    # Call irrelevant combinatorial analysis
    pair_analysis = compute_fragments(metrics)
    
    # Analyze stability (values unpacked but only one used indirectly)
    mean_val, var_val, factor = analyze_stability(metrics)
    
    # Critical execution point
    final_score = evaluate_performance(metrics, benchmark_data)
    
    # Print result as required
    print(f"Target result: {final_score}")