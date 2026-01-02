from collections import defaultdict

def calculate_performance(flags, metrics):
    score = 0
    adjustments = defaultdict(int)
    
    for key in metrics:
        if key == 'latency' and metrics[key] < 100:
            adjustments['speed_bonus'] += 15
        elif key == 'throughput' and metrics[key] > 500:
            adjustments['capacity_bonus'] += 10

    for flag in flags:
        if flag.startswith('CRITICAL_'):
            adjustments['priority_penalty'] -= 20
            break
        elif flag.startswith('OPT_'):
            adjustments['optimization_bonus'] += 5

    score = sum(metrics.values()) + sum(adjustments.values())
    return score

# Base performance metrics
base_metrics = {
    'latency': 80,
    'throughput': 600,
    'error_rate': 2
}

# Optimization flags
bonus_flags = ['OPT_CACHE', 'OPT_PREFETCH', 'CRITICAL_RECOVERY_MODE']

# Irrelevant tracking variable (minor distraction)
execution_trace = []

final_score = calculate_performance(bonus_flags, base_metrics)
print(f"Result: {final_score}")