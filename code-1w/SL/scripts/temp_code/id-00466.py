def analyze_trends(data, threshold):
    trend_count = 0
    temp_buffer = []
    for val in data:
        if val > threshold:
            trend_count += 1
            temp_buffer.append(val * 0.1)
        elif val == threshold:
            temp_buffer.append(0)
    # Irrelevant aggregation
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return trend_count

# Decoy function with misleading logic
def calculate_robustness(x):
    if x < 0:
        return abs(x) ** 0.5
    result = 0
    for i in range(3):
        result += (x + i) * (i + 1)
    return result  # Never used but looks important

# Unused transformation chain
def transform_sequence(seq):
    transformed = [s << 2 for s in seq if s % 3 == 0]
    filtered = list(filter(lambda x: x > 10, transformed))
    return [x ^ 5 for x in filtered]

# Core logic buried among distractions
baseline = {"alpha": 12, "beta": 18, "gamma": 24}
def evaluate_performance(metrics, base_config):
    score = 0
    keys_matched = set()
    
    # Real computation starts here
    for k, v in metrics.items():
        if k in base_config:
            diff = abs(v - base_config[k])
            if diff <= 5:
                score += 10
                keys_matched.add(k)
            elif diff <= 10:
                score += 5
            else:
                score -= 3
    
    # Distractor: complex unused calculation
    outlier_ratio = len([v for v in metrics.values() if v > 100]) / len(metrics) if metrics else 0
    penalty_factor = 2 if outlier_ratio > 0.3 else 1
    
    # Another red herring
    backup_scores = []
    for i, (k, v) in enumerate(metrics.items()):
        backup_scores.append((i + v) % 7)
    shuffle_sum = sum(backup_scores[::2]) - sum(backup_scores[1::2])
    
    # Actual key update
    if 'gamma' in keys_matched and metrics.get('delta', 0) > 20:
        score += 7
    
    # Final adjustment based on set size
    modifier = len(keys_matched.intersection({'alpha', 'beta'}))
    score += modifier * 4
    
    return score

# Irrelevant data structures
historical_data = [15, 22, 9, 31, 44, 8]
unused_cache = {x: x**2 for x in range(10)}

# Simulated input with plausible noise
metrics_input = {
    "alpha": 14,      # within 5 → +10
    "beta": 21,       # diff=3 → +10
    "gamma": 23,      # diff=1 → +10
    "delta": 25,      # triggers bonus +7
    "epsilon": 50     # irrelevant
}

# Dead code path
if __name__ != '__main__':
    phantom_var = [i**3 for i in range(5)]
    for p in phantom_var:
        if p > 100:
            break

# Key execution point
final_score = evaluate_performance(metrics_input, baseline)
print(f"Result: {final_score}")