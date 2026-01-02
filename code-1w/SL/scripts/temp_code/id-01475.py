import math

# Simulated system performance metrics (irrelevant in part)
def generate_diagnostic_trace():
    return {k: (3 * k**2 + 7) % 101 for k in range(15)}

def analyze_hardware_stress():
    stress_levels = [((i * 17) % 97) / 10.0 for i in range(10)]
    avg_stress = sum(stress_levels) / len(stress_levels)
    return avg_stress  # Unused but plausible red herring

def compute_fallback_threshold(data_points):
    if len(data_points) == 0:
        return 0
    sorted_vals = sorted(data_points)
    mid = len(sorted_vals) // 2
    return sorted_vals[mid] if len(sorted_vals) % 2 == 1 else (sorted_vals[mid-1] + sorted_vals[mid]) / 2

# Core logic with embedded distractions
def preprocess_metrics(raw):
    processed = {}
    for key, val in raw.items():
        if key % 3 == 0 and val > 10:
            processed[f'filtered_{key}'] = val * 1.1
        elif key % 5 == 0:
            processed[f'debug_{key}'] = val * 0.9
    return processed

def validate_structure(obj):
    if not isinstance(obj, dict) or len(obj) < 5:
        return False
    keys = list(obj.keys())
    return all(isinstance(k, str) and k.startswith(('filtered', 'debug')) for k in keys)

def calculate_weighted_adjustment(config):
    base_factor = config.get('scaling', 1.0)
    boost = config.get('turbo_mode', False)
    multiplier = 1.5 if boost else 1.0
    penalty = 0.8 if config.get('legacy_mode', False) else 1.0
    return base_factor * multiplier * penalty

def evaluate_component_health(status_log):
    health_scores = []
    for entry in status_log:
        score = 0
        if entry['cpu'] < 80:
            score += 20
        if entry['mem'] < 70:
            score += 20
        if entry['disk_io'] < 50:
            score += 15
        if entry['network'] < 60:
            score += 25
        if entry.get('gpu_temp', 100) < 90:
            score += 20
        health_scores.append(score)
    return sum(health_scores) / len(health_scores) if health_scores else 0

def evaluate_performance(metrics_log, baseline_config):
    # Irrelevant preprocessing (distractor path)
    temp_trace = generate_diagnostic_trace()
    preprocessed = preprocess_metrics(metrics_log)
    
    # Another distraction: hardware analysis (not used later)
    _ = analyze_hardware_stress()
    
    # Real computation begins
    raw_values = list(metrics_log.values())
    median_val = compute_fallback_threshold(raw_values)
    adjustment = calculate_weighted_adjustment(baseline_config)
    
    # Conditional expression used
    base_score = sum(x for x in raw_values if x > 20) if median_val > 30 else sum(raw_values)
    
    # Simulate component health input (fixed for determinism)
    dummy_status = [
        {'cpu': 75, 'mem': 65, 'disk_io': 45, 'network': 55},
        {'cpu': 85, 'mem': 75, 'disk_io': 55, 'network': 65, 'gpu_temp': 95},
        {'cpu': 65, 'mem': 55, 'disk_io': 35, 'network': 45, 'gpu_temp': 80}
    ]
    health_bonus = evaluate_component_health(dummy_status)
    
    # Misleading dead branch
    if len(preprocessed) > 100:
        fallback = compute_fallback_threshold([])
        base_score = fallback * 2
    
    # Critical execution point
    final_score = (base_score * adjustment) + (health_bonus / 2)
    
    # Validate structure (dead check - doesn't affect flow)
    _ = validate_structure(preprocessed)
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics_log = {i: (i * 4 + 9) % 88 for i in range(1, 12)}  # values from seed logic
    baseline_config = {
        'scaling': 1.2,
        'turbo_mode': True,
        'legacy_mode': False,
        'version': '3.7.1',
        'timeout': 30
    }
    
    # Key statement
    final_score = evaluate_performance(metrics_log, baseline_config)
    
    print(f"Result: {final_score}")