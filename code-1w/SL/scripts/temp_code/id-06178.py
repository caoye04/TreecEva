import math

def normalize(value, min_val, max_val):
    # Irrelevant normalization function (not used in critical path)
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0.0

def bitwise_blend(a, b, mask):
    # Distractor: complex-looking bit manipulation not central to final result
    return (a ^ mask) & (b | (~mask >> 1))

def accumulate_signal(sequence, factor):
    # Dead-end computation with misleading intermediate signal buildup
    acc = 0
    for i, val in enumerate(sequence):
        acc += val * math.sin(factor * i)
    return acc  # Never used in final chain

def extract_features(data_str):
    # Uses string methods but returns obfuscated, unused features
    tokens = data_str.split(',')
    clean_tokens = [t.strip().upper() for t in tokens if t.isalnum()]
    checksum = sum(ord(c) for c in ''.join(clean_tokens)) % 17
    return [len(clean_tokens), checksum, len(data_str)]  # Diversion

def evaluate_stability(risk_score, history):
    # Decoy logic that looks important but leads nowhere
    if risk_score < 0:
        return False
    trend = sum(1 for h in history if h > risk_score)
    return trend >= 2

def validate_readings(readings):
    # Another red-herring validation that isn't part of main flow
    valid_count = sum(1 for r in readings if 0 <= r <= 1000)
    return valid_count == len(readings)

def compute_entropy(values):
    # Scientific-sounding distraction
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def dynamic_threshold(base, mode):
    # Looks adaptive but only used in non-critical branch
    if mode == 'aggressive':
        return base * 0.75
    elif mode == 'conservative':
        return base * 1.25
    return base * 1.0

def analyze_metrics(vector, thresholds):
    # CORE FUNCTION - actual answer source
    magnitude = sum(x ** 2 for x in vector) ** 0.5
    adjusted = [x / magnitude for x in vector]  # Normalize vector
    
    # Apply threshold filtering based on category
    categories = ['alpha', 'beta', 'gamma', 'delta']
    retained = []
    for i, val in enumerate(adjusted):
        cat = categories[i % 4]
        if abs(val) >= thresholds.get(cat, 0.25):  # Use dynamic threshold map
            retained.append(val)
    
    # Real computation: average of absolute retained values
    if not retained:
        quality_score = 0.0
    else:
        abs_retained = [abs(r) for r in retained]
        quality_score = sum(abs_retained) / len(abs_retained)
    
    # Final transformation using min/max logic
    cap = max(0.5, min(quality_score * 2.0, 1.0))
    penalty = 0.1 if len(retained) < 2 else 0.0
    final_score = (cap - penalty) * 1000  # Scale to integer range
    
    return int(round(final_score))

# Main execution block
if __name__ == "__main__":
    # Input data - realistic sensor readings
    raw_stream = "34, 56, abc, 78, 91"
    parsed_features = extract_features(raw_stream)  # Distractor call
    
    # Irrelevant signal processing
    dummy_sequence = [12, 15, 22, 31, 40]
    phantom_energy = accumulate_signal(dummy_sequence, 0.33)  # Unused
    
    # Fake stability check
    past_risks = [0.4, 0.6, 0.5, 0.7]
    is_stable = evaluate_stability(0.55, past_risks)  # Misleading boolean
    
    # Actual relevant data
    health_vector = [150, -200, 300, -100, 250, -180]
    
    # Threshold map used in core logic
    threshold_map = {
        'alpha': 0.3,
        'beta': 0.25,
        'gamma': 0.35,
        'delta': 0.2
    }
    
    # Noise variables and decoy operations
    temp_buffer = [bitwise_blend(i, 2*i, 0b101) for i in range(5)]  # Bit ops distraction
    validation_passed = validate_readings(health_vector)  # Truthy but unused
    entropy = compute_entropy(health_vector)  # Computed but irrelevant
    
    # Key statement - produces the answer
    final_diagnostic = analyze_metrics(health_vector, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")