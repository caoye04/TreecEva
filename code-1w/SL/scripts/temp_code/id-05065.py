from itertools import combinations

# Simulate system health evaluation across multiple subsystems
def analyze_subsystem_load(loads):
    baseline = sum(loads) / len(loads)
    adjusted = [x * 1.1 if x > baseline else x * 0.9 for x in loads]
    return sum(adjusted)

def generate_diagnostic_flags(health_values):
    flags = []
    for val in health_values:
        if val < 30:
            flags.append('CRITICAL')
        elif val < 60:
            flags.append('WARNING')
        else:
            flags.append('OK')
    return flags

def calculate_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0.0

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    
    # Irrelevant combination analysis (distractor)
    combo_count = 0
    for r in range(2, 4):
        for _ in combinations(metrics, r):
            combo_count += 1
    
    # Dummy adjustment based on parity (misleading computation)
    temp_adjust = 0
    for m in metrics:
        temp_adjust ^= int(m)  # Bitwise distraction
    
    # Actual logic: apply non-linear bonus if stability is high
    stability_metric = metrics[2]
    bonus = 1.0
    if stability_metric > 75:
        bonus = 1.2
    elif stability_metric > 60:
        bonus = 1.1
    
    final = weighted_sum * bonus
    
    # Dead code path - never reached due to structure (irrelevant control flow)
    if False:
        fallback = 0
        for w in weights:
            fallback += w ** 2
        final = max(final, fallback)
    
    return int(final)

# Main execution
if __name__ == "__main__":
    # Input data from monitoring system
    cpu_loads = [45, 67, 58, 72, 61]
    memory_health = [88, 76, 92, 81, 74]
    response_times = [120, 95, 110, 100, 90]
    
    # Derived metrics
    avg_cpu = analyze_subsystem_load(cpu_loads)
    stability = calculate_stability_index(response_times)
    
    # Generate unused diagnostic info (distractor)
    health_flags = generate_diagnostic_flags(memory_health)
    critical_count = health_flags.count('CRITICAL')
    
    # Prepare evaluation vector
    metrics = [
        avg_cpu / 10,           # normalized CPU
        sum(memory_health) / 5,   # average memory health
        100 - stability,          # inverse stability as metric
        len([x for x in response_times if x < 100]) * 5  # fast response bonus
    ]
    
    weights = [0.3, 0.2, 0.4, 0.1]
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    print(f"Result: {final_score}")