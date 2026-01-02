import math

# Simulated sensor readings and system telemetry
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8]
pressure_levels = [1013, 1009, 1015, 1020, 1018, 1012]
humidity_data = [45, 47, 50, 44, 46, 48]

# Irrelevant cached values (distractor)
cached_checksums = {i: (i ** 3 + 7) % 997 for i in range(15)}
recent_queries = [hash(str(x)) % 100 for x in range(8)]

# System health computation (core logic)
def compute_stability_index(temp, press):
    normalized_temp = sum(temp) / len(temp)
    variance = sum((t - normalized_temp) ** 2 for t in temp) / len(temp)
    trend = temp[-1] - temp[0]
    return (normalized_temp * 1.5 + (1 / (variance + 1)) * 10 - abs(trend))

# Misleading auxiliary function (dead path)
def predict_failure_risk(metrics):
    score = 0
    for val in metrics:
        if val > 25:
            score += 3
        elif val > 20:
            score += 1
    return score * 1.7  # Not used in final result

# Core diagnostic engine
def evaluate_health_status(metrics, load_profile):
    base_score = compute_stability_index(metrics, [1, 2, 3])
    
    # Distractor: complex but unused transformation
    transformed = [math.sin(x / 10) * math.cos(x / 20) for x in load_profile]
    entropy_proxy = -sum(t * math.log(abs(t) + 1e-8) for t in transformed)

    # Actual relevant logic
    peak_load = max(load_profile) if load_profile else 0
    avg_metric = sum(metrics) / len(metrics)
    deviation = sum(abs(m - avg_metric) for m in metrics)

    # Conditional expression with lambda filter
    significant_devs = list(filter(lambda x: x > (avg_metric * 1.1), metrics))
    adjustment_factor = 0.9 if len(significant_devs) > 2 else 1.05
    
    intermediate = base_score * adjustment_factor
    
    # Simulated calibration offset (irrelevant but plausible)
    calibration_map = {i: (i * 0.987 + 2.3) for i in range(1, 20)}
    calibrated = intermediate * calibration_map.get(round(intermediate) % 19 + 1, 1.0)
    
    return calibrated

# Data fusion layer
def fuse_sensors(temp, humid, press):
    # Complex formula that ultimately only uses temperature
    thermal_weight = sum(temp) * 0.6
    humidity_influence = (sum(humid) / len(humid)) * 0.05
    pressure_trend = (press[-1] - press[0]) * 0.1
    
    # This entire function distracts but only returns temp-derived value
    return thermal_weight  # Other terms computed but ignored

# Main analysis pipeline
def analyze_system_state(sensor_data, load):
    # Tuple unpacking distraction
    (a, b, c) = (len(sensor_data), sum(sensor_data), max(sensor_data))
    redundant_stats = {
        'count': a,
        'total': b,
        'peak': c,
        'range': c - min(sensor_data)
    }
    
    # Set operations (distractor)
    unique_values = set(round(x) for x in sensor_data)
    outliers = {x for x in unique_values if x > 25}
    
    # Real computation chain
    raw_index = evaluate_health_status(sensor_data, load)
    
    # Multiple layers of conditional logic
    if raw_index > 30:
        if any(x > 25 for x in sensor_data):
            category = 'STABLE_HIGH'
        else:
            category = 'STABLE_NORMAL'
    elif raw_index > 20:
        if len([x for x in sensor_data if x > 25]) >= 3:
            category = 'MONITORING'
        else:
            category = 'OPTIMAL'
    else:
        category = 'WARNING'
    
    # Final transformation
    scaling_factor = {'OPTIMAL': 1.2, 'STABLE_NORMAL': 1.1, 'STABLE_HIGH': 1.05}.get(category, 0.8)
    final_score = raw_index * scaling_factor
    
    # Decoy assignment
    diagnostic_report = f"System status: {category}, Score: {final_score:.2f}"
    
    # Key output variable
    final_diagnostic = int(round(final_score * 1.76))  # Final answer derivation
    
    return final_diagnostic

# Simulated operational data
health_metrics = [x + 0.5 for x in temperature_readings]  # Slight shift
system_load = [10, 20, 35, 50, 45, 40, 30, 25]

# Dead code path invocation (misleads traceability)
_ = predict_failure_risk(humidity_data)
_ = fuse_sensors(temperature_readings, humidity_data, pressure_levels)

# Critical execution point
final_diagnostic = analyze_system_state(health_metrics, system_load)

print(f"Result: {final_diagnostic}")