import math

# Simulated system performance metrics (some are decoys)
def get_system_metrics():
    raw_data = [120, 45, 67, 90, 23]
    temp_fahrenheit = 98.6
    temp_celsius = (temp_fahrenheit - 32) * 5 / 9
    
    # Irrelevant sensor processing (distractor)
    def process_sensor_noise(data):
        return [x + 0.1 * x for x in data if x > 50]
    
    noise_filtered = process_sensor_noise(raw_data)
    
    # Real metrics used later
    response_times = [r * 1.1 for r in raw_data]
    error_rate = len([x for x in raw_data if x < 30]) / len(raw_data)
    throughput = sum(raw_data) / 10
    latency_spike = any(x > 100 for x in raw_data)
    uptime_ratio = 0.98 if not latency_spike else 0.92

    # Dummy transformations (red herring)
    normalized = list(map(lambda x: x / max(raw_data), raw_data))
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)

    # Return mix of relevant and irrelevant values
    return {
        'rt_avg': sum(response_times) / len(response_times),
        'err': error_rate,
        'thr': throughput,
        'up': uptime_ratio,
        'noise': noise_filtered,  # unused
        'entropy': entropy       # unused
    }

# Weighting strategy with conditional logic
weights = {
    'rt_avg': 0.3,
    'err': -0.4,  # negative weight: lower is better
    'thr': 0.2,
    'up': 0.1
}

# Complex evaluation function with branching logic
def evaluate_performance(metrics, w):
    base = 0
    adjustments = []
    
    # Conditional scaling based on thresholds (distractor logic)
    if metrics['rt_avg'] > 100:
        base += 10
        jitter_comp = metrics['rt_avg'] * 0.05
        adjustments.append(jitter_comp)
    elif metrics['rt_avg'] > 80:
        base += 5
    else:
        base += 0
    
    # Core scoring logic
    score_components = {}
    for key in w:
        if key == 'rt_avg':
            # Inverted because lower response time is better
            score_components[key] = (100 - metrics[key]) * w[key]
        elif key == 'err':
            score_components[key] = (1 - metrics[key]) * abs(w[key]) * 100
        else:
            score_components[key] = metrics[key] * w[key]
    
    # Additional misleading branch (dead path due to logic)
    if metrics['thr'] > 1000:
        bonus = 20
        adjustments.append(bonus)
    else:
        bonus = 0  # This runs but bonus isn't used
    
    # Aggregate main score
    aggregated = base + sum(score_components.values())
    
    # Final nonlinear transformation (key step)
    if aggregated > 70:
        final_adjustment = aggregated * 0.9 + 5
    else:
        final_adjustment = aggregated * 1.1
    
    # Decoy computation (looks important but unused)
    def calculate_reliability_index(m):
        return math.exp(-m['err']) * m['up'] * 100
    
    reliability = calculate_reliability_index(metrics)  # computed but ignored
    
    # Correct result
    return round(final_adjustment, 4)

# Unused helper (distractor)
def generate_report(data):
    return f"Performance Report: {data}\nGenerated at t=0"

# Main execution flow
metrics = get_system_metrics()

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")