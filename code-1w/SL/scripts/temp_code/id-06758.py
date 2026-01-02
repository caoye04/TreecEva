def analyze_trends(data, threshold=0.5):
    """Irrelevant trend analysis function (dead code path)."""
    moving_avg = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)]
    anomalies = [i for i, v in enumerate(moving_avg) if abs(v) > threshold]
    return anomalies


def preprocess_signal(signal):
    """Noise filtering that isn't used in main logic."""
    filtered = [s * 0.9 for s in signal if s > 0]
    normalized = [f / max(filtered) for f in filtered]
    return normalized

# Unused complex data structure
historical_logs = {
    'Q1': {'errors': 12, 'retries': 3},
    'Q2': {'errors': 8, 'retries': 2},
    'Q3': {'errors': 15, 'retries': 5},
    'Q4': {'errors': 6, 'retries': 1}
}

# Misleading intermediate metrics
raw_metrics = [0.4, 0.7, 0.3, 0.9, 0.6]
decoy_weights = [1, -1, 2, -2, 3]
shadow_score = sum([a * b for a, b in zip(raw_metrics, decoy_weights)])

baseline = {'alpha': 0.5, 'beta': 0.7, 'gamma': 0.4}

# Real input data
metrics = {
    'accuracy': 0.85,
    'latency': 0.65,
    'throughput': 0.92,
    'consistency': 0.78
}

# Decoy calculation with bitwise red herring
obfuscation_key = 0b10101
scrambled = sum([ord(ch) ^ obfuscation_key for ch in 'placeholder']) % 100

# Conditional expression mix with list comprehension
penalty_mask = [1 if x < 0.7 else 0.95 for x in metrics.values()]
correction_factor = 1.05 if sum(penalty_mask) < 3 else 0.98

# Simulated recursive validation (unused)
def validate_hierarchy(level=3):
    if level == 0:
        return [0]
    return [level] + validate_hierarchy(level - 1)

# Fake aggregation path
temp_aggregate = [metrics[k] * (0.8 if 'lat' in k else 1.0) for k in metrics]

# Core logic buried within distractions
def calculate_stability(vals):
    diffs = [abs(a - b) for a, b in zip(vals[:-1], vals[1:])]
    return 1 - (sum(diffs) / len(diffs)) if diffs else 1

stability = calculate_stability(list(metrics.values()))

# Main evaluation function
def evaluate_performance(met, base):
    # Extract relevant thresholds
    acc_dev = abs(met['accuracy'] - base['alpha'])
    delay_penalty = met['latency'] < base['beta']
    tp_bonus = met['throughput'] > base['gamma']
    
    # Multi-step scoring logic
    score = 100
    score -= int(acc_dev * 20)
    score -= 10 if delay_penalty else 0
    score += 15 if tp_bonus else 0
    score *= correction_factor
    score += int(stability * 10)
    
    # Final adjustment using conditional expression
    adjustment = -5 if shadow_score > 10 else 5
    score += adjustment
    
    # Destructuring irrelevant tuple
    _, _, meta_adjust = (0.1, 0.2, 3)
    score += meta_adjust
    
    return int(score)

# Key execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")