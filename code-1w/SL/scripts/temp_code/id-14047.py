def preprocess_input(data):
    # Irrelevant preprocessing (dead code path)
    normalized = [x % 7 for x in data if x > 0]
    filtered = [y for y in normalized if y in (1, 3, 5)]
    return sum(filtered) * 2

# Unused helper function (distractor)
def validate_sequence(seq):
    return all(isinstance(x, int) for x in seq) and len(seq) > 3

# Decoy transformation with bit manipulation (misleading intermediate)
def encrypt_key(n):
    shifted = (n << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 1

# Real logic hidden among noise
def build_diagnostic_map(raw):
    history_log = {}
    temp_values = []
    
    for i in raw:
        case_type = 'odd' if i % 2 else 'even'
        if case_type not in history_log:
            history_log[case_type] = 0
        history_log[case_type] += 1
        
        # Meaningful transformation
        transformed = (i ** 2) - (i * 3) + 2
        temp_values.append(transformed)
    
    # Construct actual working map
    diagnostic_map = {
        'base_sum': sum(raw),
        'derived_vals': temp_values,
        'type_count': history_log,
        'meta': {
            'version': 2,
            'active': True
        }
    }
    
    # Red herring: unused complex calculation
    decoy_entropy = 0
    for j in range(len(temp_values)):
        decoy_entropy += temp_values[j] ^ (j * 5)
    diagnostic_map['phantom_entropy'] = decoy_entropy % 1000
    
    return diagnostic_map

# Core analysis function — answer depends on this
def analyze_pattern(diag_map):
    base = diag_map['base_sum']
    derived = diag_map['derived_vals']
    counts = diag_map['type_count']
    
    # Real computation chain
    adjustment = 0
    if 'odd' in counts and counts['odd'] > counts.get('even', 0):
        adjustment += 11
    elif 'even' in counts:
        adjustment -= 7
    
    cumulative = 0
    for val in derived:
        if val > 0:
            cumulative += val // 2
        else:
            cumulative -= abs(val) // 3
    
    # Hidden weighting factor
    multiplier = 3 if diag_map['meta']['version'] == 2 else 1
    
    # Final result obscured by multiple paths
    candidate_a = (cumulative + base) * multiplier + adjustment
    candidate_b = encrypt_key(base)  # Distractor call
    candidate_c = preprocess_input(derived)  # Another red herring
    
    # Critical decision point (non-obvious selection)
    final_score = candidate_a  # Only this matters
    
    # Dead code block (never reached)
    if False:
        fallback = 0
        for x in diag_map.get('phantom_entropy', []):
            fallback ^= x
        final_score = fallback
    
    return final_score

# Setup input (real data source)
sensor_readings = [4, 7, 2, 9, 6]

# Execute real pipeline
intermediate_map = build_diagnostic_map(sensor_readings)
final_diagnostic = analyze_pattern(intermediate_map)

# Output target result
print(f"Result: {final_diagnostic}")