import math

def analyze_signal(strength, noise_floor):
    if strength < noise_floor:
        return 0
    signal_quality = (strength - noise_floor) / strength
    return signal_quality * 100 if signal_quality > 0 else 0

def compute_entropy(data):
    total = sum(data)
    entropy = 0
    for x in data:
        if x > 0:
            p = x / total
            entropy -= p * math.log2(p)
    return entropy

def validate_checksum(record):
    # Irrelevant validation function (dead path)
    checksum = 0
    for c in str(record):
        checksum += ord(c)
    return checksum % 17 == 0

def transform_features(features):
    # Distractor transformation with unused logic
    transformed = []
    scaling_factor = 1.7
    offset = 3
    for f in features:
        adjusted = (f ** 1.5) + offset
        if adjusted > 20:
            adjusted = 20
        transformed.append(round(adjusted * scaling_factor))
    return transformed

def evaluate_stability(readings):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    stability = 1 / (1 + variance) if variance != 0 else 1
    return stability

def process_metrics(data, cfg):
    # Key computation path
    raw_power = data.get('power_levels', [])
    power_sum = sum(raw_power)
    normalized = [p / power_sum for p in raw_power] if power_sum else [0]*len(raw_power)
    
    # Compute primary metrics
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    peak = max(normalized) if normalized else 0
    
    # Irrelevant entropy calculation (distractor)
    _ = compute_entropy([int(p*100) for p in normalized])
    
    # Stability evaluation (partially relevant)
    stability_score = evaluate_stability(raw_power)
    
    # Signal analysis using noise threshold
    main_strength = sum(raw_power)
    noise_level = cfg.get('baseline_noise', 10)
    signal_metric = analyze_signal(main_strength, noise_level)
    
    # Conditional logic with early returns (red herring)
    if signal_metric < 50:
        fallback = cfg.get('use_fallback', False)
        adjustment = 0.85 if fallback else 1.0
        intermediate = (peak * 100) * adjustment
        if intermediate < 20:
            return {'status': 'low', 'score': intermediate}
    
    # Core calculation chain (nested conditions and arithmetic)
    base_score = avg_normalized * 1000
    dynamic_weight = 0.6 if peak > 0.3 else 0.4
    weighted_component = base_score * dynamic_weight + signal_metric * (1 - dynamic_weight)
    
    # Secondary adjustment via conditional expression
    penalty_factor = 0.9 if len(raw_power) < 5 else 1.0
    adjusted_score = weighted_component * penalty_factor
    
    # Tertiary influence from stability
    final_boost = 1 + (stability_score * 0.1)
    boosted_score = adjusted_score * final_boost
    
    # Decoy assignment with similar name
    threshold_limit = cfg.get('limit', 150)
    
    # Actual target variable
    threshold_score = int(round(boosted_score))
    
    # Unused complex unpacking (distractor)
    extras = data.get('auxiliary', [0, 0, 0])
    a, b, c = (x * 2 for x in extras[:3]) if len(extras) >= 3 else (0, 0, 0)
    
    # Fake final processing
    _ = transform_features([a, b, c])
    
    return {
        'status': 'processed',
        'base': base_score,
        'signal': signal_metric,
        'stability': stability_score,
        'threshold_score': threshold_score
    }

# Simulated input data
raw_data = {
    'power_levels': [12, 15, 18, 22, 14],
    'auxiliary': [7, 3, 9, 11]
}

class Config:
    def __get__(self, attr):
        return {'baseline_noise': 8, 'use_fallback': False, 'limit': 150}.get(attr, None)

cfg = Config()

# Main execution
final_output = process_metrics(raw_data, {
    'baseline_noise': 8,
    'use_fallback': False,
    'limit': 150
})

# Extract result
threshold_score = final_output['threshold_score']
print(f"Result: {threshold_score}")