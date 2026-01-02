from collections import defaultdict

# Simulate system performance evaluation with multiple metrics
def analyze_response_times(responses):
    stats = defaultdict(int)
    total = 0
    count = 0
    outliers = 0

    for r in responses:
        total += r
        count += 1
        if r > 500:
            outliers += 1
        if r < 100:
            stats['fast'] += 1
        elif r < 300:
            stats['medium'] += 1
        else:
            stats['slow'] += 1

    avg = total / count if count else 0
    stats['average'] = round(avg, 2)
    stats['outliers'] = outliers
    return stats

def calculate_efficiency_ratio(ops, errors, memory_usage):
    # Irrelevant efficiency calculation (distractor)
    base = ops / (errors + 1)
    penalty = memory_usage * 0.01
    return round(base / (1 + penalty), 3)

def evaluate_stability(load_pattern):
    # Distractor function with dead-end logic
    stable_periods = 0
    max_load = 0
    for i, load in enumerate(load_pattern):
        if load < 80:
            stable_periods += 1
        if load > max_load:
            max_load = load
    stability_score = stable_periods * 10 + (100 - max_load)
    return stability_score

def evaluate_performance(metrics, config):
    score = 0
    debug_flags = []

    # Core logic: score based on average response time and error rate
    avg_time = metrics['average']
    error_rate = metrics['errors']

    if avg_time < config['response_time_threshold']:
        score += 40
    else:
        score -= 10

    if error_rate < config['error_tolerance']:
        score += 30
    else:
        score -= 15

    # Minor bonus for low slow-response count (semi-relevant)
    if metrics['slow'] < 5:
        score += 5

    # Distractor: unused computation
    temp_weight = metrics['fast'] * 0.1 + metrics['medium'] * 0.05
    debug_flags.append(f'Weight component: {temp_weight}')

    # Hidden adjustment: only one of these branches affects final outcome
    if metrics['outliers'] == 0:
        score += 10
    elif metrics['outliers'] < 3:
        score += 5
    else:
        score -= 5

    # Dead code path (never executed due to data constraints) – red herring
    if score > 100:
        score = 100
        debug_flags.append('Capped at maximum')

    return score

# Main execution
if __name__ == '__main__':
    # Input data
    response_times = [120, 95, 310, 88, 256, 412, 99, 110, 290, 305]
    error_count = 2
    memory_kb = 45000
    load_fluctuations = [75, 60, 88, 45, 70, 50, 90, 65]

    # Process core metric
    performance_stats = analyze_response_times(response_times)
    performance_stats['errors'] = error_count

    # Unused intermediate calculations (distractors)
    efficiency = calculate_efficiency_ratio(len(response_times), error_count, memory_kb)
    stability = evaluate_stability(load_fluctuations)
    predicted_latency = sum(response_times) / len(response_times) + 5.5

    # Threshold configuration
    threshold_config = {
        'response_time_threshold': 250,
        'error_tolerance': 3
    }

    # Critical statement
    final_score = evaluate_performance(performance_stats, threshold_config)

    # Additional irrelevant tracking
    audit_log = []
    for key, val in performance_stats.items():
        if isinstance(val, int):
            audit_log.append(f'{key}:{val}')

    print(f"Result: {final_score}")