from itertools import combinations

# Simulate sensor data analysis with performance scoring
def analyze_fluctuations(readings):
    trend_flags = []
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend_flags.append(1)
        elif readings[i] < readings[i-1]:
            trend_flags.append(-1)
        else:
            trend_flags.append(0)
    
    # Irrelevant computation: counts zero transitions (distractor)
    stable_periods = 0
    for flag in trend_flags:
        if flag == 0:
            stable_periods += 1

    return trend_flags

def compute_entropy(signal):
    from math import log
    freq = {}
    for s in signal:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(signal)
    for count in freq.values():
        prob = count / total
        entropy -= prob * log(prob, 2)
    return round(entropy, 4)

def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0
    
    # Real logic begins
    if metrics['stability'] > threshold:
        score += 15
    else:
        penalty += 5
    
    # Secondary condition with distractor variables
    temp_debug_log = []  # unused tracking
    debug_counter = 0   # misleading counter
    
    for key, value in metrics.items():
        debug_counter += 1  # irrelevant increment
        temp_debug_log.append((key, value))
        
        if 'error' in key:
            if value < 0.05:
                score += 10
            else:
                penalty += 8

    # Core calculation affecting result
    consistency_bonus = 0
    if metrics['consistency'] >= 0.9 and metrics['coverage'] > 0.85:
        consistency_bonus = 22
    
    # Final score computed here — this is the target
    final_score = score - penalty + consistency_bonus
    
    # Dead code branch (never executed due to fixed input)
    if threshold < 0:
        fallback = sum(metrics.values())
        final_score = int(fallback % 100)

    return final_score

# Main execution
raw_readings = [23.1, 23.1, 23.4, 23.8, 23.9, 23.7, 23.7, 24.0]
trends = analyze_fluctuations(raw_readings)

# Compute auxiliary metric (used)
entropy_value = compute_entropy(trends)

# Build metric dictionary
metric_data = {
    'stability': entropy_value,
    'consistency': 0.93,
    'coverage': 0.88,
    'error_rate': 0.03,
    'latency_spike': 0.12
}

base_threshold = 0.85

# Key statement where answer is determined
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")