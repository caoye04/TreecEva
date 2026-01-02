def analyze_signal(pattern, threshold=0.65):
    if not pattern:
        return 0
    magnitude = sum(p ** 2 for p in pattern) ** 0.5
    normalized = [p / (magnitude + 1e-9) for p in pattern]
    coherence = sum(1 for a, b in zip(normalized, normalized[1:]) if abs(a - b) < 0.1)
    return coherence > len(normalized) * threshold

def extract_features(data_stream):
    features = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            features.append(val * 1.5)
        elif i % 4 == 1:
            features.append(val * 0.7)
        else:
            features.append(val + 2)
    return [f for f in features if f > 3]  

def validate_integrity(check_sequence):
    cumulative = 0
    for idx, item in enumerate(check_sequence):
        if idx % 2 == 0:
            cumulative ^= int(item) & 255
        else:
            cumulative += int(item ** 0.5)
    return cumulative % 17 == 0

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def process_metrics(signature, base):
    temp_buffer = []
    for i, (s, b) in enumerate(zip(signature, base)):
        if s < b:
            temp_buffer.append(s * 1.2)
        elif s > b * 1.1:
            temp_buffer.append(s * 0.85)
        else:
            temp_buffer.append((s + b) / 2)
    
    adjustment_factor = 1.0
    if len(temp_buffer) > 5:
        adjustment_factor = 0.9
    elif any(x > 100 for x in temp_buffer):
        adjustment_factor = 1.1
    
    secondary_check = [x for x in temp_buffer if x > 10]
    if len(secondary_check) < 3:
        adjustment_factor *= 1.05
    
    raw_score = sum(temp_buffer) * adjustment_factor
    
    # Distractor: irrelevant entropy calculation
    _ = compute_entropy([int(x) for x in signature])
    
    # Distractor: unused signal analysis
    _ = analyze_signal(base[:8])
    
    # Distractor: fake validation path
    validation_chain = [raw_score, raw_score * 0.95, raw_score * 1.05]
    _ = validate_integrity(validation_chain)
    
    # Key logic step: final transformation based on feature extraction
    extended_input = [raw_score / 10] * 12
    derived_features = extract_features(extended_input)
    
    # Final computation
    final_diagnostic = int(sum(derived_features) * 10) % 99991
    
    # Dead code path - never executed due to logic above
    if raw_score < 0:
        fallback = 0
        for bit in range(32):
            fallback |= (1 << bit)
        final_diagnostic = fallback & 0xFFFF
    
    return final_diagnostic

# Simulated sensor data
baseline_readings = [23.1, 45.0, 67.3, 34.2, 89.1, 12.0, 44.4, 76.8, 55.5, 61.2]
health_signature = [25.3, 41.2, 70.1, 30.0, 95.0, 10.5, 48.6, 73.0, 54.0, 65.1]

# Trigger key computation
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Result: {final_diagnostic}")