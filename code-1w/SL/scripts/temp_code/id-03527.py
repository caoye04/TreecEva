from itertools import combinations
from math import log

# System performance evaluation with multiple metrics
def analyze_response_time(times):
    avg = sum(times) / len(times)
    variance = sum((t - avg) ** 2 for t in times) / len(times)
    return avg, variance

def compute_efficiency_ratio(ops, energy):
    if energy == 0:
        return float('inf')
    return ops / energy

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) / mean_val < threshold]
    return filtered

def generate_metric_pairs(metrics):
    return list(combinations(metrics, 2))

def evaluate_performance(raw_metrics):
    # Preprocess: remove outliers from response times
    cleaned_times = filter_outliers([m['response_time'] for m in raw_metrics])
    
    # Compute base efficiency ratios
    efficiencies = [compute_efficiency_ratio(m['ops'], m['energy']) for m in raw_metrics]
    
    # Analyze time characteristics
    time_analysis = analyze_response_time(cleaned_times)
    time_avg, time_var = time_analysis
    
    # Generate auxiliary metric pairs (not directly used but adds complexity)
    metric_names = [f"metric_{i}" for i in range(len(raw_metrics))]
    pairs = generate_metric_pairs(metric_names)
    pair_count = len(pairs)
    
    # Simulate system load impact (distractor computation)
    load_sim = 0
    for i in range(len(efficiencies)):
        for j in range(i + 1, len(efficiencies)):
            if efficiencies[i] > efficiencies[j]:
                load_sim += log(efficiencies[i] + 1) - log(efficiencies[j] + 1)
    
    # Weighted aggregation of key indicators
    response_weight = 0.4
    efficiency_weight = 0.6
    
    # Normalize time score (lower time = better)
    time_score = 100 / (time_avg + 1) if time_avg > 0 else 100
    
    # Efficiency contribution
    avg_efficiency = sum(efficiencies) / len(efficiencies)
    efficiency_score = min(avg_efficiency * 10, 90)  # Cap at 90
    
    # Final composite score
    final_score = (time_score * response_weight) + (efficiency_score * efficiency_weight)
    
    # Irrelevant transformation on unused variable
    temp_set = {int(eff) for eff in efficiencies}
    derived_pairs = set(combinations(temp_set, 2))
    complexity_factor = len(derived_pairs) * 0.01 if derived_pairs else 0
    
    # Unused conditional branch (dead code path)
    if complexity_factor > 10:
        final_score *= 0.95
    
    return final_score

# Input data setup
metrics_data = [
    {'response_time': 120, 'ops': 450, 'energy': 15},
    {'response_time': 110, 'ops': 480, 'energy': 16},
    {'response_time': 130, 'ops': 430, 'energy': 14},
    {'response_time': 115, 'ops': 460, 'energy': 15},
    {'response_time': 300, 'ops': 200, 'energy': 20},  # outlier
]

# Execute main logic
final_score = evaluate_performance(metrics_data)
print(f"Result: {final_score}")