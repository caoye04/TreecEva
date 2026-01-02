def analyze_trends(data, threshold=0.5):
    trend_summary = {}
    for key, values in data.items():
        avg = sum(values) / len(values)
        trend_summary[key] = 'up' if avg > threshold else 'down'
    return trend_summary

# Irrelevant helper function (dead code path)
def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

# Misleading metric with decoy logic
def assess_stability(readings):
    baseline = readings[0]
    drift = sum(abs(readings[i] - readings[i-1]) for i in range(1, len(readings)))
    return drift < 5.0

# Core logic disguised among distractions
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal] if max_val != 0 else signal

# Heavily distracted main processing function
def evaluate_performance(metrics, config):
    # Real computation begins
    raw_scores = []
    adjustment_factor = 0.85
    
    # Distractor: unused intermediate
    temp_analysis = {'peaks': 0, 'valleys': 0}
    peak_count = 0  # Red herring counter
    
    for name, series in metrics.items():
        if name in config['active']:
            # Normalize and compute weighted mean
            norm_series = normalize_signal(series)
            weight = config['weights'].get(name, 1.0)
            score = sum(x * weight for x in norm_series) * adjustment_factor
            raw_scores.append(score)
            
            # Distractor: updating irrelevant tracking
            for i in range(1, len(series)-1):
                if series[i] > series[i-1] and series[i] > series[i+1]:
                    peak_count += 1  # Used nowhere

    # Critical calculation buried in noise
    base_result = sum(raw_scores)
    penalty = 0.0
    
    # Decoy conditional with plausible but unused logic
    if len(raw_scores) > 3:\n        bonus = 10 if all(s > 0.7 for s in raw_scores) else 0
    else:
        bonus = 0  # Unused in final result
    
    # Actual answer derivation
    multiplier = config['scaling']['final'] if base_result > 2.0 else 0.5
    preliminary = base_result * multiplier
    
    # Final adjustment using dictionary lookup
    adjustments = {"A": 1.1, "B": 0.95, "C": 1.0}
    category = config.get('category', 'C')
    adjusted_final = preliminary * adjustments.get(category, 1.0)
    
    # Answer variable
    final_score = int(round(adjusted_final * 100))  # Scale to integer
    
    # Dead code: looks important but does nothing
    validation_check = all(v > 0 for v in metrics.values()) if metrics else False
    
    return final_score

# Simulated input data
metric_data = {
    'throughput': [0.8, 0.9, 0.75, 0.85],
    'latency': [0.4, 0.3, 0.5, 0.45],
    'reliability': [0.95, 0.98, 0.97, 0.96],
    'bandwidth': [0.65, 0.7, 0.72, 0.68]
}

benchmarks = {
    'active': ['throughput', 'reliability', 'bandwidth'],
    'weights': {'throughput': 1.2, 'reliability': 1.5, 'bandwidth': 0.8},
    'scaling': {'final': 1.3},
    'category': 'A'
}

# Execution point of interest
final_score = evaluate_performance(metric_data, benchmarks)
print(f"Target result: {final_score}")