from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 85, 92, 67, 88, 95, 76, 84]
    metric_data = defaultdict(list)
    for i, val in enumerate(raw_data):
        stage = 'initial' if i % 2 == 0 else 'optimized'
        metric_data[stage].append(val + (i % 3))
    return metric_data

def analyze_trends(data):
    # Irrelevant trend analysis (distractor)
    increases = 0
    flat = 0
    prev = data['initial'][0]
    for val in data['initial'] + data['optimized']:
        if val > prev:
            increases += 1
        elif val == prev:
            flat += 1
        prev = val
    return increases - flat  # Not used in final logic

def compute_stability(values):
    # Auxiliary function to compute variance-like measure
    mean_val = sum(values) / len(values)
    variance_proxy = sum((v - mean_val) ** 2 for v in values) / len(values)
    return round(100 / (1 + variance_proxy), 2)

def apply_correction(metrics):
    # Misleading transformation that isn't used
    corrected = {}
    for k, v in metrics.items():
        shifted = [(x * 0.95) + 3 for x in v]
        corrected[k + '_adj'] = [int(x) for x in shifted]
    return corrected

def evaluate_performance(metrics, thresholds):
    # Core logic: combine multiple reasoning types
    base_initial = sum(metrics['initial']) // len(metrics['initial'])
    base_optimized = sum(metrics['optimized']) // len(metrics['optimized'])
    
    # Compute stability scores (used in final answer)
    initial_stability = compute_stability(metrics['initial'])
    optimized_stability = compute_stability(metrics['optimized'])
    
    # Logical combination with conditional boosts
    performance_delta = base_optimized - base_initial
    stability_improvement = optimized_stability > initial_stability
    
    bonus = 0
    if performance_delta > 5 and stability_improvement:
        bonus = 15
    elif performance_delta > 3:
        bonus = 5
    
    # Decision based on threshold crossings
    above_threshold = sum(1 for v in metrics['optimized'] if v >= thresholds['critical'])
    if above_threshold >= 3:
        bonus += 10
    
    # Final score calculation
    base_score = base_optimized + bonus
    adjustment = 5 if len(metrics['optimized']) % 2 == 1 else 0
    final_score = base_score + adjustment
    
    # Dead code path - never executed due to fixed thresholds
    if thresholds.get('ultra') is not None and final_score > 200:
        final_score *= 0.8  # Would scale down, but condition never met
    
    return int(final_score)

# Main execution flow
if __name__ == "__main__":
    # Setup
    thresholds = {
        'warning': 75,
        'critical': 85,
        'experimental': 90
    }
    
    # Collect and process data
    data = collect_metrics()
    trend_metric = analyze_trends(data)  # Computed but not used
    adjusted_data = apply_correction(data)  # Creates irrelevant corrected data
    
    # Key evaluation step
    final_score = evaluate_performance(data, thresholds)
    
    # Output result
    print(f"Result: {final_score}")