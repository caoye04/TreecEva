from collections import defaultdict, Counter
from itertools import cycle

# Simulated system performance monitoring with multiple metrics
def collect_metrics():
    raw_data = [150, 200, 175, 180, 250, 160, 195]
    adjustments = [0.9, 1.1, 1.0, 0.95, 1.2, 0.85, 1.05]
    derived = [raw_data[i] * adjustments[i] for i in range(len(raw_data))]
    
    # Irrelevant transformation (distractor)
    inverted_map = {i: 1/v for i, v in enumerate(raw_data) if v != 0}
    temp_analysis = sum(v ** 0.5 for v in derived if v > 180)

    # Relevant data aggregation
    metric_data = defaultdict(float)
    for i, val in enumerate(derived):
        key = 'high' if val >= 190 else 'low'
        metric_data[key] += val * 0.1
    
    return metric_data

# Legacy function - never called (dead code path)
def deprecated_normalization(data):
    total = sum(data.values())
    return {k: v/total for k, v in data.items()} if total else data

# Auxiliary statistical tool (partial red herring)
def calculate_entropy(counts):
    from math import log
    total = sum(counts)
    entropy = 0
    for c in counts:
        p = c / total
        entropy -= p * log(p) if p > 0 else 0
    return round(entropy, 4)

# Core evaluation logic with embedded distractions
def evaluate_performance(metrics, bonus):
    base = metrics['high'] * 1.5 + metrics['low'] * 0.7
    
    # Decoy calculation using irrelevant variables
    shadow_value = 0
    history_log = [{'temp': base * 0.1}, {'temp': base * 0.2}]
    for entry in history_log:
        shadow_value += entry['temp'] ** 0.5
    
    # Real adjustment chain
    adjustment_chain = cycle([0.95, 1.05])
    refined = base
    for _ in range(4):
        refined *= next(adjustment_chain)
    
    # Secondary correction based on conditional logic
    if refined > 50:
        refined *= 0.85
    elif refined < 30:
        refined *= 1.2
    else:
        refined *= 1.0
    
    # Bonus integration (critical path)
    final_score = int(refined + bonus * 2.5)
    
    # Unused intermediate (misleading)
    diagnostic_flag = final_score & 1
    buffer_array = [final_score ^ i for i in range(3)]
    
    return final_score

# Spurious data generation (distractor)
def generate_noise(n):
    result = []
    for i in range(n):
        acc = 0
        for j in range(i % 5):
            acc += (j + 1) ** 2
        result.append(acc)
    return result

# Main execution flow
if __name__ == '__main__':
    # Collect performance metrics
    data = collect_metrics()
    
    # Simulated bonus factor from external config (relevant)
    config_flags = [True, False, True]
    bonus_factor = sum(1 for x in config_flags if x) * 3.2
    
    # Noise generation (irrelevant but plausible)
    noise = generate_noise(5)
    noise_entropy = calculate_entropy(noise) if noise else 0
    
    # Critical statement
    final_score = evaluate_performance(data, bonus_factor)
    
    # Track unused diagnostics (red herring)
    debug_trace = {"noise_level": noise_entropy, "shadow": 0}
    debug_trace["shadow"] = final_score % 7
    
    # Output target result
    print(f"Result: {final_score}")