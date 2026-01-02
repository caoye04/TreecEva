def analyze_trends(data, threshold=0.5):
    trends = []
    for i, value in enumerate(data):
        if value > threshold:
            trends.append((i, value * 1.2))
        else:
            trends.append((i, value * 0.8))
    return trends

# Irrelevant helper function (decoy)
def compute_entropy(values):
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Unused but misleading data structure
decoys = {
    'outlier_filter': lambda x: x > 0.3,
    'normalizer': lambda x: x / 2.0 if x > 1 else x,
    'flagged': [False, True, False],
    'cache': {}
}

# Simulated sensor readings (distraction)
sensor_log = [
    [0.6, 0.4, 0.7],
    [0.3, 0.8, 0.2],
    [0.9, 0.1, 0.6]
]

# Fake aggregation with no downstream use
aggregated_noise = []
for seq in sensor_log:
    smoothed = [sum(seq[i:i+2]) / 2 for i in range(len(seq)-1)]
    aggregated_noise.append(smoothed)

# Real computation begins here
baseline = [0.5, 0.6, 0.4, 0.7, 0.3]
def evaluate_performance(metrics, base):
    adjusted = []
    for idx, (m, b) in enumerate(zip(metrics, base)):
        diff = m - b
        # Conditional expression used
        penalty = 0.1 if diff < -0.1 else (0.05 if diff < 0 else 0)
        adjusted.append(max(m - penalty, 0))
    
    # Complex transformation chain
    raw_total = sum(adjusted)
    count_above = len([x for x in adjusted if x > 0.5])
    bonus = 0.2 if count_above >= 3 else 0.05
    
    # Introduce bit manipulation red herring
    magic_offset = (len(adjusted) << 2) ^ 5  # distraction
    decoy_value = (raw_total * 100) & 0xFF   # unused bitwise
    
    # Actual logic path
    if raw_total > 2.0:
        raw_total *= 1.1
    elif raw_total > 1.5:
        raw_total *= 1.05
    else:
        raw_total *= 0.95
    
    final_raw = raw_total + bonus
    
    # More misdirection: unused early exit pattern
    for x in adjusted:
        if x < 0.1:
            break  # dead code due to max() above

    # Key assignment
    final_score = int(round(final_raw * 100))
    return final_score

# Primary metric input
metrics = [0.8, 0.4, 0.9, 0.6, 0.2]

# Call to key function
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")