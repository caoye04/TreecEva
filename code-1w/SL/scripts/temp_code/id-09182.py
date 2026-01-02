def analyze_readings(readings):
    adjusted = [r * 1.08 for r in readings if r > 0]
    baseline = sum(adjusted) / len(adjusted) if adjusted else 0
    return baseline * 0.92

# Irrelevant signal processing (red herring)
def filter_noise(signal):
    return [s for s in signal if abs(s) > 0.5]

def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Unused complex transformation
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(val - 1)
    return result

# Core logic disguised among distractors
def evaluate_stability(risk_profile):
    score = 0
    modifiers = {'high': -3, 'medium': 0, 'low': 2}
    for key, level in risk_profile.items():
        if key.startswith('neuro'):
            score += modifiers.get(level, 0)
        elif key.endswith('cardio'):
            score += modifiers.get(level, 0) + 1
    return score >= 1

# Main diagnostic pipeline
def process_metrics(data, thresholds):
    # Distractor variables
    temp_cache = {}
    normalization_factor = 1.0
    dummy_list = [1, 1, 2, 3, 5, 8, 13]
    
    # Real computation begins
    primary_keys = ['vital_a', 'vital_b', 'neural_x', 'cardio_y']
    active_metrics = {k: v for k, v in data.items() if k in primary_keys}
    
    # Compute base metric from vital signs
    vital_sum = sum(active_metrics.get(k, 0) for k in ['vital_a', 'vital_b'])
    neural_input = active_metrics.get('neural_x', 0)
    cardio_value = active_metrics.get('cardio_y', 0)
    
    # Conditional expression with meaningful branching
    adjustment = 1.25 if neural_input > thresholds['neural_x'] else 0.88
    boosted_cardio = cardio_value * adjustment if evaluate_stability({'neuro_check': 'high', 'stress_cardio': 'medium'}) else cardio_value
    
    # Use of dictionary operations and conditional logic
    status_flags = {
        'stable': vital_sum > thresholds['vital_a'],
        'responsive': neural_input > 50,
        'perfected': False
    }
    
    # Cascading conditional update
    status_flags['perfected'] = (status_flags['stable'] and 
                                status_flags['responsive'] and 
                                boosted_cardio > 75)
    
    # Final calculation - target result
    base_score = analyze_readings([vital_sum, neural_input, boosted_cardio])
    final_score = base_score + (10 if status_flags['perfected'] else -5)
    
    # Dead code path (never executed due to logic)
    if len(dummy_list) > 100:
        final_score = compute_entropy([int(base_score)])
    
    # Critical answer variable
    final_diagnostic = int(round(final_score * 1.07))
    return final_diagnostic

# Execution setup
if __name__ == '__main__':
    # Input data with plausible medical monitoring context
    health_data = {
        'vital_a': 68,
        'vital_b': 74,
        'neural_x': 58,
        'cardio_y': 63,
        'metabolic_z': 44,  # Irrelevant field
        'aux_signal_1': 0.3 # Noise entry
    }
    
    threshold_map = {
        'vital_a': 120,
        'neural_x': 55
    }
    
    # Trigger main logic
    final_diagnostic = process_metrics(health_data, threshold_map)
    print(f"Result: {final_diagnostic}")