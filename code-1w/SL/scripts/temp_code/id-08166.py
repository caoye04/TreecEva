import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    offset = 0.05
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant transformation: frequency shifting (dead path)
def shift_frequency(signal, factor=1.5):
    return [math.sin(x * factor) for x in signal]

# Distraction: unused noise injection function
def inject_noise(data, level=0.01):
    import random
    random.seed(42)
    return [x + random.uniform(-level, level) for x in data]

# Real processing begins here
def apply_envelope(signal):
    envelope = []
    for i, x in enumerate(signal):
        # Apply quadratic weighting
        weight = (i + 1) ** 0.5
        envelope.append(x * weight)
    return envelope

# Misleading filter that looks important but is unused
def soft_threshold(data, limit=2.0):
    result = []
    for x in data:
        if abs(x) > limit:
            result.append(x * 0.5)
        else:
            result.append(0.0)
    return result

# Core transformation pipeline
def extract_features(enveloped):
    features = []
    for x in enveloped:
        if x > 5.0:
            features.append(math.log(x) * 2)
        elif x > 2.0:
            features.append(math.sqrt(x) + 1)
        else:
            features.append(x ** 2)
    return features

# Auxiliary diagnostic (distractor)
def compute_entropy(arr):
    total = sum(arr)
    if total == 0:
        return 0.0
    probs = [x / total for x in arr if x > 0]
    return -sum(p * math.log2(p) for p in probs)

# Key analysis logic with lambda abstraction
def analyze_signal(features):
    # Lambda-based transformation: maps feature significance
    score_fn = lambda val: val * 1.5 if val >= 3.0 else val * 0.8
    scores = [score_fn(f) for f in features]
    
    # Secondary adjustment based on position
    adjusted_scores = []
    for idx, s in enumerate(scores):
        if idx % 2 == 0:
            adjusted_scores.append(s * 1.1)
        else:
            adjusted_scores.append(s * 0.95)
    
    # Compute final diagnostic metric
    base_metric = sum(adjusted_scores)
    penalty = len([s for s in scores if s < 2.0]) * 0.5
    final_diagnostic = base_metric - penalty
    
    # Dead code: complex correction never reached due to early exit expectation
    if False:
        correction = math.cos(len(scores))
        final_diagnostic *= correction
    
    return final_diagnostic

# Unused recursive decoy function
def binary_decompose(n, acc=[]):
    if n <= 1:
        return acc + [n]
    return binary_decompose(n // 2, acc + [n % 2])

# Unused character analysis red herring
def count_chars_in_hex(data_list):
    hex_str = ''.join([hex(int(x)) for x in data_list[:5]])
    upper = sum(1 for c in hex_str if c.isupper())
    lower = sum(1 for c in hex_str if c.islower())
    return upper - lower

# Main execution flow
if __name__ == '__main__':
    readings = collect_readings()           # Step 1: Get raw data
    processed_1 = apply_envelope(readings)  # Step 2: Apply envelope
    processed_2 = extract_features(processed_1)  # Step 3: Extract nonlinear features
    
    # Distraction: compute irrelevant metrics
    entropy = compute_entropy(processed_1)
    freq_shifted = shift_frequency(readings, 2.1)
    char_diff = count_chars_in_hex([int(x) for x in readings])
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_2)
    
    # Output target result
    print(f"Result: {final_diagnostic}")