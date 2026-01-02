import itertools

# Simulated system performance metrics with noise and redundant data
def generate_diagnostics():
    return {
        'cpu_load': [0.78, 0.82, 0.91, 0.85, 0.76],
        'memory_usage_gb': [12.4, 13.1, 11.9, 14.2, 13.7],
        'disk_iops': [210, 198, 225, 215, 203],
        'network_latency_ms': [45, 52, 48, 55, 43],
        'thermal_throttling_events': [1, 0, 2, 1, 0]
    }

def analyze_trends(data):
    trends = {}
    for key, values in data.items():
        if len(values) < 2:
            trends[key] = 0.0
        else:
            # Compute average slope
            slopes = [(values[i] - values[i-1]) for i in range(1, len(values))]
            trends[key] = sum(slopes) / len(slopes)
    return trends

def filter_outliers(sequence, threshold=1.5):
    if not sequence:
        return []
    median_val = sorted(sequence)[len(sequence)//2]
    return [x for x in sequence if abs(x - median_val) <= threshold]

def calculate_stability_index(readings):
    filtered = filter_outliers(readings, threshold=1.2)
    if len(filtered) < 2:
        return 0.95  # Default high stability for low variance
    variance = sum((x - sum(filtered)/len(filtered))**2 for x in filtered) / len(filtered)
    return round(1 / (1 + variance), 4)

def synthetic_workload_simulation(size):
    # Irrelevant simulation - red herring function
    result = 0
    for i in range(size // 100):
        result += (i * i) % 97
    return result

def decode_configuration_flag(flag_str):
    # Decodes a fake configuration string - distractor logic
    decoded = 0
    for ch in flag_str:
        decoded ^= ord(ch)
    return decoded % 13

def assess_risk_level(value, threshold_low, threshold_high):
    if value < threshold_low:
        return 'LOW'
    elif value > threshold_high:
        return 'CRITICAL'
    else:
        return 'MODERATE'

# Core evaluation logic with meaningful computation buried in distractions
def evaluate_component_health(metric_name, raw_data, trend_data):
    base_score = 100.0
    
    # Real impact: adjust score based on trend
    trend_impact = abs(trend_data.get(metric_name, 0))
    base_score -= trend_impact * 15
    
    if metric_name == 'cpu_load':
        avg_load = sum(raw_data) / len(raw_data)
        if avg_load > 0.85:
            base_score -= 10
    elif metric_name == 'memory_usage_gb':
        growth_trend = trend_data.get('memory_usage_gb', 0)
        if growth_trend > 0.5:
            base_score -= 8
    elif metric_name == 'disk_iops':
        stability = calculate_stability_index(raw_data)
        base_score += stability * 5  # Better stability improves score
    
    return max(base_score, 0)

def evaluate_performance(metrics, benchmark_ref):
    
    # Irrelevant preprocessing - distractor
    _ = list(itertools.combinations([1, 2, 3], 2))
    _ = [x for x in range(50) if x % 7 == 0]
    
    trends = analyze_trends(metrics)
    
    # Fake calibration sequence - misleading code path
    calibration_offset = 0
    for i in range(3):
        calibration_offset += synthetic_workload_simulation(500)
    calibration_offset %= 17
    
    # Actual scoring begins here
    component_scores = {}
    
    for name, data in metrics.items():
        score = evaluate_component_health(name, data, trends)
        component_scores[name] = score
    
    # Aggregate score calculation - critical step
    raw_average = sum(component_scores.values()) / len(component_scores)
    
    # Bonus logic using conditional expression and slicing
    recent_cpu_trend = metrics['cpu_load'][-2:]  # Last two readings
    recent_avg = sum(recent_cpu_trend) / len(recent_cpu_trend)
    
    performance_bonus = 10 if recent_avg < 0.8 else (5 if recent_avg < 0.87 else 0)
    
    # Final adjustment using set intersection logic (distractor vs real)
    expected_keys = {'cpu_load', 'memory_usage_gb', 'disk_iops'}
    present_keys = set(metrics.keys())
    missing_penalty = 0
    if not expected_keys.issubset(present_keys):
        missing_penalty = 15
    
    # This early break is never reached due to condition — dead code path
    for val in benchmark_ref['baseline']:
        if val < 0:
            missing_penalty += 100
            break  # Unreachable
    
    # Real final score computation
    final_raw = raw_average + performance_bonus - missing_penalty
    
    # Additional red herring: unused transformation
    transformed = [round(x ** 0.5, 3) for x in component_scores.values()]
    _ = sum(transformed) / len(transformed)  # Not used
    
    # Key statement: final_score assignment
    final_score = round(final_raw, 4)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Generate real diagnostic data
    system_metrics = generate_diagnostics()
    
    # Benchmark reference data (contains decoy fields)
    benchmark_data = {
        'baseline': [0.8, 13.0, 210, 48, 1],
        'tolerances': {'load': 0.05, 'mem': 0.8},
        'version': '2.1.9-alpha',
        'calibration_needed': False
    }
    
    # Unused but misleading variable
    config_flag_value = decode_configuration_flag("X9K!mN2@qR")
    
    # Trigger the key statement
    final_score = evaluate_performance(system_metrics, benchmark_data)
