import math

def analyze_signal(pattern):
    if not pattern:
        return 0
    magnitude = sum(x ** 2 for x in pattern)
    threshold = 1024
    normalized = int(math.sqrt(magnitude)) if magnitude > threshold else magnitude // 4
    # Irrelevant transformation
    inverted = [255 - byte for byte in pattern]
    checksum = sum(inverted) % 256
    return normalized + checksum // 10

def encode_sequence(seq):
    encoded = []
    for i, val in enumerate(seq):
        if i % 3 == 0:
            encoded.append((val * 2) ^ 0xAA)
        elif i % 5 == 0:
            encoded.append((val + 17) & 0xFF)
        else:
            encoded.append(val)
    # Dead computation path
    temp_result = [x | 0x0F for x in encoded if x < 100]
    adjustment = len(temp_result) * 3
    return sum(encoded) - adjustment

def evaluate_stability(risk_factors):
    base_score = 100
    penalty = 0
    for factor in risk_factors:
        if factor > 80:
            penalty += 15
        elif factor > 50:
            penalty += 8
    adjusted = base_score - penalty
    # Misleading intermediate
    hypothetical = (base_score * 1.2) - (penalty * 1.5)
    return adjusted if adjusted > 0 else 0

def process_metrics(log_data, system_state):
    # Key execution point
    signal_strength = analyze_signal([x & 0x7F for x in log_data if x > 0])
    sequence_value = encode_sequence([x % 256 for x in log_data])
    stability = evaluate_stability(list(system_state.values()))
    
    # Distractor: complex but unused calculation
    diagnostic_map = {i: (i ** 3) % 97 for i in range(1, 20)}
    metadata_hash = sum(diagnostic_map.keys()) ^ sum(diagnostic_map.values())
    temp_diagnostic = signal_strength * 2 + sequence_value // 100
    
    # Conditional expression with meaningful branching
    fallback_mode = system_state.get('overload', False)
    recovery_offset = 42 if fallback_mode else 17
    
    # Core logic chain
    raw_score = temp_diagnostic + stability * 3 + recovery_offset
    
    # Dictionary-based correction factor
    corrections = {'alpha': 0.95, 'beta': 1.05, 'gamma': 1.1}
    mode = system_state.get('mode', 'alpha')
    corrected_score = raw_score * corrections.get(mode, 1.0)
    
    # Final computation
    final_diagnostic = int(corrected_score) + (metadata_hash % 10)  # Hash only affects by small offset
    
    # Unused red herring function
    def decrypt_payload(data):
        return ''.join(chr(x ^ 0x55) for x in data)[-10:]
    
    # Unused variables
    anomaly_trace = [x for x in log_data if x % 7 == 0 and x > 50]
    threat_level = 'CRITICAL' if len(anomaly_trace) > 5 else 'NORMAL'
    
    return final_diagnostic

# Simulated input data
log_data = [120, -5, 200, 85, 150, 300, 45, 99, 220, 180, 60, 140]
system_state = {
    'mode': 'beta',
    'overload': False,
    'temperature': 68,
    'voltage': 88,
    'cache_hits': 77
}

# Execution point
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")