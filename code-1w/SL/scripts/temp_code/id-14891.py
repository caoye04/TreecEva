import math

def preprocess_signal(raw_signal):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_signal) for x in raw_signal]
    filtered = [x for x in normalized if x > 0.1]
    return [math.sin(x * math.pi) for x in filtered]

def compute_entropy(sequence):
    # Unused function — red herring
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

def validate_checksum(data):
    # Decoy validation logic (never called in critical path)
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val * (i + 1)) % 256
    return checksum == 42

def generate_symmetry_pattern(n):
    # Distractor: generates symmetric matrix but not used in final result
    pattern = [[(i + j) % n for j in range(n)] for i in range(n)]
    trace = sum(pattern[i][i] for i in range(n))
    return trace  # Dead end

def decode_fragment(fragment):
    # Partial decoding logic with misleading intermediate values
    a = fragment >> 3
    b = (fragment ^ 0xFF) & 0x0F
    c = (a + b) % 17
    if c > 10:
        return c * 2
    else:
        return c * c  # This path is actually irrelevant

def analyze_system_state(signature, logs):
    # Core logic embedded in noise
    key_threshold = 0.75
    aggregate_score = 0
    event_count = len(logs)
    
    # Real signal extraction
    primary_channel = [x for x in signature if x % 3 == 1]
    secondary_channel = [x for x in signature if x % 3 == 2]
    
    # Meaningful computation
    base_magnitude = sum(primary_channel) // len(primary_channel) if primary_channel else 0
    
    # Dictionary-based state tracking (required feature)
    system_state = {
        'status': 'nominal',
        'phase': 'steady',
        'diagnostics': [],
        'flags': {}
    }
    
    for entry in logs:
        log_id, value, severity = entry
        
        # Relevant conditional logic
        if severity > key_threshold and 'ERR' in log_id:
            system_state['diagnostics'].append(value)
            if value > base_magnitude:
                system_state['flags'][log_id] = 'CRITICAL'
    
    # Actual answer derivation (non-obvious)
    diagnostic_sum = sum(system_state['diagnostics'])
    flag_count = len(system_state['flags'])
    
    # Final calculation: uses only specific parts of the data
    adjustment_factor = math.log(flag_count + 2)  # Avoid log(0)
    final_diagnostic = int(diagnostic_sum * adjustment_factor) - 1337
    
    # Dead code branch (misleading)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        system_state['status'] = 'reversed'
    
    return final_diagnostic

# Simulated input data
quantum_signature = [23, 47, 68, 86, 91, 115, 134, 157]
system_logs = [
    ('ERR_POWER', 42, 0.8),
    ('WARN_TEMP', 15, 0.6),
    ('ERR_TIMING', 88, 0.9),
    ('INFO_FLOW', 5, 0.4),
    ('ERR_SIGNAL', 67, 0.85)
]

# Irrelevant precomputations (distractors)
signal_data = preprocess_signal([0.1, 0.3, 0.5, 0.8, 0.9])
symmetry_trace = generate_symmetry_pattern(6)
decoded_parts = [decode_fragment(x) for x in quantum_signature[:3]]

# Critical execution point
final_diagnostic = analyze_system_state(quantum_signature, system_logs)

# Output result as required
print(f"Result: {final_diagnostic}")