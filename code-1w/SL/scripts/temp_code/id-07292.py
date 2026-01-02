def analyze_trends(data, threshold=0.5):
    trends = []
    for i, value in enumerate(data):
        if value > threshold:
            trend = (i, value * 1.2)
            trends.append(trend)
    return trends


def normalize_values(arr):
    total = sum(arr)
    return [x / total for x in arr] if total != 0 else arr

# Irrelevant utility function (dead code path)
def deprecated_scale(x):
    return x * 0.9

# Misleading intermediate computation
temp_offset = 42
scaling_factor = 1.8
adjustment_log = []
for i in range(5):
    adjustment_log.append(temp_offset * (i + 1))

# Core data
raw_metrics = [0.6, 0.4, 0.75, 0.3, 0.9]

# Distractor: complex-looking but unused transformation
processed = [
    (idx, val ** 2) for idx, val in enumerate(raw_metrics) if val < 0.8
]

# Another red herring: bit manipulation with no impact
eval_mask = 0b101010
masked_results = []
for x in raw_metrics:
    shifted = int(x * 100)
    masked = shifted ^ eval_mask
    masked_results.append(masked >> 2)

# Actual relevant logic begins here
baseline = {
    'low': 0.35,
    'high': 0.75
}

weights = {
    'growth': 1.5,
    'stability': 0.8,
    'risk': -0.5
}

metrics = {}
for i, val in enumerate(raw_metrics):
    key = f'metric_{i}'
    metrics[key] = {
        'value': val,
        'above_baseline': val > baseline['high'],
        'penalty': 1 if val < baseline['low'] else 0
    }

# Conditional branching with distractors
status_flags = []
for k, v in metrics.items():
    if v['above_baseline']:
        status_flags.append(1)
    elif v['penalty']:
        status_flags.append(-1)
    else:
        status_flags.append(0)

# Unused zip operation (distractor)
pairs = list(zip(raw_metrics, status_flags))

# Real scoring logic
contribution = 0.0
for i, (k, m) in enumerate(metrics.items()):
    base_contrib = m['value'] * weights['growth'] if m['above_baseline'] else m['value'] * weights['stability']
    penalty_adjust = 0.2 * m['penalty']
    contribution += base_contrib - penalty_adjust

# Final evaluation with key statement
final_score = 0

def evaluate_performance(mets, base):
    global final_score
    score = 100.0
    count_high = 0
    total_penalty = 0
    
    # Nested conditionals and counting
    for key, entry in mets.items():
        if entry['above_baseline']:
            count_high += 1
            score += 12.5
        if entry['penalty']:
            total_penalty += 1
    
    # Additional adjustments
    if count_high >= 3:
        score *= 1.1
    
    if total_penalty == 0:
        score += 10
    
    # Decoy calculation
    fake_boost = count_high * 7.7
    dummy = fake_boost / (total_penalty + 1)
    
    # Actual assignment
    score -= total_penalty * 5.0
    return int(round(score))

# Execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")