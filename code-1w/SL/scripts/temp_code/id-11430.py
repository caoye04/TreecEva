def analyze_component_health(metrics, baseline):
    # Auxiliary calculation with partial relevance
    deviations = [abs(m - baseline[i % len(baseline)]) for i, m in enumerate(metrics)]
    avg_deviation = sum(deviations) / len(deviations)
    
    # Distractor: complex but unused health profile
    health_profile = {i: 'stable' if m >= baseline[i % len(baseline)] else 'degraded' for i, m in enumerate(metrics)}
    
    # Semi-relevant transformation
    normalized = [m / (baseline[i % len(baseline)] + 1e-5) for i, m in enumerate(metrics)]
    return sum(normalized) / len(normalized)


def calculate_performance(results, limits):
    # Key function with moderate nesting and interference
    aggregated = []
    temp_offsets = []
    
    for idx, entry in enumerate(results):
        component_data = entry['values']
        threshold_set = limits[idx % len(limits)]
        
        # Intermediate processing with distractor variables
        filtered = [v for v in component_data if v >= threshold_set['min']]
        excess = [v for v in component_data if v > threshold_set['max']]
        
        # Track excess count (not used later)
        temp_offsets.append(len(excess))
        
        # Core metric: average of filtered values
        if filtered:
            mean_val = sum(filtered) / len(filtered)
            aggregated.append(mean_val * 0.8)  # Weighted contribution
        else:
            aggregated.append(0.0)
    
    # Secondary logic path with dead computation
    outlier_summary = set()
    for a in aggregated:
        if a > 150:
            outlier_summary.add('high_tier')
        elif a > 100:
            outlier_summary.add('mid_tier')
    # ^ This block has no effect on output — intentional red herring
    
    # Final aggregation
    base_score = sum(aggregated)
    adjustment_factor = 1.2 if len(outlier_summary) > 0 else 1.0
    final_score = int(base_score * adjustment_factor)  # Deterministic integer result
    
    # Print required at end
    print(f"Target result: {final_score}")
    return final_score

# Simulated input data
benchmark_results = [
    {'component': 'A', 'values': [95, 102, 130, 88, 115]},
    {'component': 'B', 'values': [120, 155, 90, 100, 140]},
    {'component': 'C', 'values': [70, 110, 105, 95]}
]

thresholds = [
    {'min': 90, 'max': 120},
    {'min': 100, 'max': 130},
    {'min': 85, 'max': 115}
]

# Health analysis (distractor call — not affecting final_score)
dummy_health = analyze_component_health([100, 95, 110], [98, 97, 105])

# Critical execution point
final_score = calculate_performance(benchmark_results, thresholds)