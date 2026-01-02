def analyze_workload(inputs):
    base_load = sum([x ** 0.5 for x in inputs if x > 0])
    peak_load = max(inputs) if inputs else 0
    avg_load = sum(inputs) / len(inputs) if inputs else 0
    
    # Distractor: irrelevant statistical measures
    variance_proxy = sum([(x - avg_load) ** 2 for x in inputs]) / len(inputs) if inputs else 0
    entropy_approx = -sum([x/sum(inputs) * (x/sum(inputs)) for x in inputs if x > 0]) if sum(inputs) > 0 else 0

    # Conditional expression used meaningfully
    load_category = 'high' if peak_load > 50 else 'moderate' if peak_load > 20 else 'low'
    
    # Semi-relevant transformation (only base_load and avg_load matter)
    normalized_load = base_load * 0.7 + avg_load * 0.3
    
    return normalized_load, load_category


def evaluate_efficiency(metrics, threshold=35.0):
    normalized_load, category = metrics
    
    # More distractions: simulated efficiency bands
    efficiency_bands = {'low': 0.5, 'moderate': 0.75, 'high': 0.9}
    band_multiplier = efficiency_bands.get(category, 0.6)
    
    raw_efficiency = normalized_load * band_multiplier
    
    # Dead computation path (never used)
    if raw_efficiency < 10:
        stability_flag = 'UNSTABLE'
    elif raw_efficiency > 50:
        stability_flag = 'OVERLOADED'
    else:
        stability_flag = 'STABLE'
    
    adjusted_efficiency = raw_efficiency * 1.1 if category == 'high' else raw_efficiency * 0.95
    
    return adjusted_efficiency

# Simulated system telemetry data
sensor_readings = [16, 25, 36, 49, 64, 81]

# Intermediate processing with meaningful and irrelevant variables
processed_metrics = analyze_workload(sensor_readings)
efficiency_score = evaluate_efficiency(processed_metrics)

# Auxiliary distraction: unrelated diagnostic check
consistency_check = all(r % 4 == 0 for r in sensor_readings)
diagnostic_log = f"Consistency verified: {consistency_check}"

# Core calculation chain continues...
baseline_reference = sum([r // 4 for r in sensor_readings])
penalty_factor = 0.98 if len(sensor_readings) > 5 else 1.0

# Final performance metric incorporating conditional logic
interim_value = efficiency_score + baseline_reference * 0.2
scaling_factor = 1.05 if interim_value > 40 else 1.0
final_score = interim_value * scaling_factor

Result: final_score