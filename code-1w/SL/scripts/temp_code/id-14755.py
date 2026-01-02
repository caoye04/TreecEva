import math

# Simulated system diagnostics (irrelevant to final result)
def analyze_health(logs):
    if not logs:
        return 0
    total = sum([log['value'] for log in logs])
    avg = total / len(logs)
    return avg * 0.75

# Unused transformation function (dead code path)
def transform_data(x):
    return [i ** 2 for i in x if i % 2 == 0]

# Misleading normalization process (distractor)
def normalize(values):
    min_val = min(values)
    max_val = max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Auxiliary calculation with decoy output (irrelevant)
def compute_entropy(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    probabilities = [f / len(data) for f in freq_map.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

# Core logic: performance evaluation based on weighted criteria
def evaluate_criterion(value, threshold, weight):
    return weight * (1 + math.exp(-0.1 * abs(value - threshold)))

# Main evaluation function combining multiple concepts
def evaluate_performance(metrics, base):
    # Extract relevant slices from input list
    recent_metrics = metrics[-5:]  # slicing operation
    
    # Conditional expression used in scoring
    adjustment = 1.2 if sum(recent_metrics) > 3 * base else 0.85
    
    # Bit manipulation as part of obfuscation (only some bits matter)
    magic_offset = (base ^ 0b1010) & 0xFF
    
    # Dictionary-based weight mapping (dictionary operation)
    weights = {
        'critical': 3.0,
        'high': 2.0,
        'medium': 1.2,
        'low': 0.5
    }
    
    # Simulated multi-step reasoning chain
    score = 0.0
    for i, val in enumerate(recent_metrics):
        # Nested conditionals with short-circuiting
        if val > base - 5 and base != 0:
            tier = 'high' if val > base + 3 else ('medium' if val > base else 'low')
        else:
            tier = 'critical'
        
        raw_contribution = evaluate_criterion(val, base, weights[tier])
        score += raw_contribution * (0.9 ** i)  # exponential decay factor
    
    # Final adjustment using conditional expression
    score *= adjustment
    
    # Red herring: unused transformed array
    temp_array = [math.sqrt(x) for x in recent_metrics if x > 0]
    temp_sum = sum(temp_array) / len(temp_array) if temp_array else 0
    _ = temp_sum * 2.5  # irrelevant computation
    
    # Key assignment point
    final_score = int(round(score + magic_offset))
    return final_score

# Irrelevant diagnostic data (distractor)
system_logs = [
    {'timestamp': 1, 'value': 42},
    {'timestamp': 2, 'value': 38},
    {'timestamp': 3, 'value': 45}
]

# Unused dataset (red herring)
dummy_dataset = [12, 15, 22, 18, 17, 20, 25, 30]
transformed = transform_data(dummy_dataset)

# Decoy entropy calculation (misleading intermediate)
entropy = compute_entropy([1, 1, 2, 2, 3])

# Baseline configuration (appears important but only partially used)
baseline_config = {
    'initial': 10,
    'threshold': 15,
    'window': 5
}

# Input data for actual computation
metric_data = [8, 12, 16, 9, 14, 18, 11, 13]
baseline = 12

# Execute main logic
final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")