def analyze_system_load(usage_data):
    # Irrelevant preprocessing (distractor)
    normalized = [u / max(usage_data) for u in usage_data]
    thresholds = [0.5, 0.75, 0.9]
    alerts = []
    for val in normalized:
        if val > thresholds[2]:
            alerts.append('CRITICAL')
        elif val > thresholds[1]:
            alerts.append('WARNING')
        else:
            alerts.append('OK')
    return alerts

# Simulated sensor metrics (red herring - not used in final answer)
sensor_readings = [23.4, 25.1, 22.8, 26.0, 24.5]
system_alerts = analyze_system_load([80, 120, 95, 150, 130])

# Core logic disguised among distractions
def transform_value(x):
    return (x ** 2 + 3 * x + 1) % 100

def bitwise_magic(a, b):
    # Complex-looking but unused function (dead code path)
    temp = (a << 2) ^ (b >> 1)
    return temp & 0xFF

def calculate_entropy(sequence):
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Real data processing chain
raw_metrics = [12, 18, 24, 30]
scaling_factors = [2, 1.5, 1, 0.5]

# Distractor: unused transformation pipeline
pipeline = [
    lambda x: x * 2,
    lambda x: x + 10 if x < 20 else x - 5,
    lambda x: abs(x - 15)
]

# Meaningful transformations mixed with noise
temp_results = []
for i, val in enumerate(raw_metrics):
    transformed = val
    if i % 2 == 0:
        transformed = (transformed * scaling_factors[i]) + 5
    else:
        transformed = (transformed / scaling_factors[i]) - 3
    temp_results.append(transformed)

# Decoy container (looks important)
summary_stats = {
    'min': min(temp_results),
    'max': max(temp_results),
    'range': max(temp_results) - min(temp_results),
    'median': sorted(temp_results)[len(temp_results)//2]
}

# Actual critical computation begins here
weights = [0.1, 0.3, 0.4, 0.2]

# Real evaluation function (obscured by context)
def evaluate_performance(data, w):
    # Apply non-linear transformation
    processed = list(map(lambda x: (x ** 1.5) // 1, data))
    
    # Weighted sum with normalization
    weighted_sum = sum(d * w[i] for i, d in enumerate(processed))
    norm_factor = sum(w)
    
    # Additional adjustment based on pattern recognition
    patterns = [(processed[i+1] - processed[i]) for i in range(len(processed)-1)]
    trend_adjustment = 0
    if all(p >= 0 for p in patterns):
        trend_adjustment = 10
    elif all(p <= 0 for p in patterns):
        trend_adjustment = -5
    else:
        trend_adjustment = 2
    
    # Final computation
    base_score = weighted_sum / norm_factor
    final = base_score + trend_adjustment
    
    # Dead code branch (misleading)
    if final > 100:
        final = final % 75 + 5
    
    return final

# Auxiliary irrelevant calculation
checksum = 0
for c in 'performance_eval':
    checksum += ord(c) % 11

# Critical execution point
metrics = [x * 1.1 for x in temp_results]  # Further obscure source
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")