def analyze_signal(data, threshold=5.0):
    filtered = [x for x in data if abs(x) > threshold]
    return [abs(x) ** 0.5 for x in filtered if x != 0]


def compute_risk(profile):
    base = sum(profile.get('history', []))
    adjustment = profile.get('volatility', 0) * 0.3
    return base - adjustment


def normalize(values):
    max_val = max(values) if values else 1
    return [v / max_val for v in values]


def evaluate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs) if diffs else 0.0


def extract_features(samples):
    features = {}
    even_idx = [v for i, v in enumerate(samples) if i % 2 == 0]
    odd_idx = [v for i, v in enumerate(samples) if i % 2 == 1]
    paired = [a * b for a, b in zip(even_idx, odd_idx[:len(even_idx)])]
    features['paired_product'] = sum(paired)
    features['length_ratio'] = len(even_idx) / (len(odd_idx) + 1)
    return features


def aggregate_performance(metrics, weights):
    # Irrelevant transformations
    temp_data = [m * 1.1 for m in metrics if m > 0]
    offset = sum(temp_data) * 0.05
    
    # Decoy logic with misleading intermediate
    candidate = 0
    for i, val in enumerate(temp_data):
        if i % 3 == 0:
            candidate += val * 0.1
    
    # Actual critical path
    adjusted = [m * w for m, w in zip(metrics, weights)]
    raw_score = sum(adjusted)
    
    # Fake branching that doesn't affect result
    if raw_score > 100:
        raw_score -= 10
    elif raw_score < 0:
        raw_score += 5

    # More distractions: unused calculations
    magnitude = sum(m**2 for m in metrics)**0.5
    normalized_metrics = normalize(metrics)
    noise_floor = evaluate_stability(metrics)

    # Final computation
    penalty = 0
    if noise_floor > 2.0:
        penalty = 8
    elif noise_floor > 1.0:
        penalty = 4

    final_score = int(raw_score - penalty + offset)  # Final assignment point
    
    # Dead code branches
    if False:
        final_score *= 1.2
    
    for _ in range(0):  # Never executes
        final_score = 0
        
    return final_score

# Main execution flow
sensor_log = [3.4, -6.7, 8.1, 2.2, -9.3, 7.6, 1.8, -5.2, 6.4]
signal_features = analyze_signal(sensor_log, threshold=6.0)
risk_profile = {'history': [4, 7, 2], 'volatility': 5.6}
baseline_risk = compute_risk(risk_profile)
stability_index = evaluate_stability(signal_features)
feature_set = extract_features(sensor_log)

# Core metrics derived from multiple sources
metrics = [
    len(signal_features),
    stability_index * 10,
    feature_set['paired_product'],
    baseline_risk,
    sum(signal_features) // 1
]

# Weight vector - some weights are red herrings
weights = [1.2, 0.8, 2.1, 0.5, 1.0, 3.3]  # Last weight is unused

# Critical statement
final_score = aggregate_performance(metrics, weights)

print(f"Result: {final_score}")