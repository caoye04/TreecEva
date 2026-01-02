import math

# Simulated quantum telemetry processing with diagnostic validation
def preprocess_signal(raw_data):
    if len(raw_data) == 0:
        return [0]
    processed = []
    for x in raw_data:
        if x % 3 == 0:
            processed.append(x ** 2)
        elif x % 5 == 0:
            processed.append(int(math.sqrt(abs(x))) * (-1 if x < 0 else 1))
        else:
            processed.append(x + 7)
    return processed

# Irrelevant helper - decoy function
def deprecated_normalizer(arr):
    total = sum(abs(v) for v in arr)
    return [v / (total + 1e-9) for v in arr]

# Core transformation: entropy-based modulation
def modulate_entropy(sequence, key_offset=3):
    entropy_mod = 0
    for i, val in enumerate(sequence):
        shifted = val ^ (i + key_offset)
        entropy_mod += (shifted & 7) * ((-1) ** (i % 2))
    return abs(entropy_mod) % 113

# Unused legacy path - dead code branch
def validate_legacy_protocol(token):
    if token < 0:
        return False
    binary_rep = bin(token)[2:]
    return binary_rep.count('1') % 2 == 0

# Main analysis engine with conditional bypasses
def evaluate_threshold_risk(magnitude, mode='strict'):
    if mode == 'relaxed':
        return magnitude < 90
    elif mode == 'strict':
        return 10 < magnitude < 85
    else:
        return False

# Complex state analyzer combining multiple paradigms
def analyze_system_state(signature, buffer):
    # Step 1: unpack critical telemetry
    primary, secondary, *_ = signature  # tuple unpacking
    
    # Step 2: apply modular correction
    corrected_primary = (primary + 37) % 101
    temp_factor = corrected_primary * 2 if corrected_primary > 50 else corrected_primary * 3
    
    # Step 3: bitmask refinement
    masked_input = temp_factor & 0xFF
    
    # Step 4: derive intermediate state using bitwise and arithmetic mix
    intermediate = (masked_input >> 2) ^ (len(buffer) % 17)
    
    # Step 5: conditional override based on heuristic
    if intermediate % 4 == 0:
        intermediate = int(math.log(intermediate + 1) * 10)
    
    # Step 6: inject secondary channel data
    secondary_adjusted = abs(secondary) % 19
    combined_metric = intermediate + secondary_adjusted
    
    # Step 7: apply entropy modulation from earlier computation
    entropy_tuned = modulate_entropy(buffer, key_offset=combined_metric % 7)
    
    # Step 8: final adjustment via conditional expression
    risk_flag = evaluate_threshold_risk(entropy_tuned, mode=('strict' if combined_metric > 40 else 'relaxed'))
    adjustment = -15 if risk_flag else 12
    
    # Step 9: compute final diagnostic score
    final_score = (combined_metric * 3) + entropy_tuned + adjustment
    
    # Distractor: unused derived values
    phantom_index = sum(buffer) // (len(buffer) + 1)
    audit_trace = f"DIAG-{phantom_index:X}"
    validity_check = audit_trace.startswith('DIAG-') and len(audit_trace) > 5
    
    return final_score

# --- Execution context ---

# Real input data stream
sensor_feed = [12, -25, 18, 41, 60, 7]
processed_feed = preprocess_signal(sensor_feed)

# Irrelevant auxiliary array - distractor
baseline_readings = [88, 19, 45, 33, 72, 11, 8]

# Quantum signature constructed from real and dummy sources
quantum_signature = [
    processed_feed[0] * 2,
    processed_feed[-1] + 10,
    sum(processed_feed) % 100  # unused element
]

# Baseline buffer used in actual logic
baseline_buffer = [3, 1, 4, 1, 5, 9, 2, 6]

# Dead assignment - misleading variable
system_verdict = deprecated_normalizer(baseline_readings)

# Key statement
final_diagnostic = analyze_system_state(quantum_signature, baseline_buffer)

# Output result as required
print(f"Target result: {final_diagnostic}")