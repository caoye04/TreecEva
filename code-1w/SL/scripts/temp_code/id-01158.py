import math

# System health monitoring simulation with encoded signal processing

def encode_signal(raw_data, key_offset):
    return [(x ^ key_offset) + 1 for x in raw_data]

def decrypt_profile(token_sequence, mask):
    return [math.floor(t * 0.9) for t in token_sequence if t % 3 == 0]  # Dead-end function (distractor)

def analyze_pattern(seq):
    return sum([seq[i] * (i+1) for i in range(len(seq))])

def shift_window(buffer, shift_by):
    return buffer[-shift_by:] + buffer[:-shift_by]

def validate_checksum(values):
    return sum(values) % 256

# Irrelevant helper (distractor)
def compute_entropy(data):
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    return -sum((freq / len(data)) * math.log2(freq / len(data)) for freq in freq_map.values())

def generate_signature(base, length):
    sig = [base]
    for i in range(1, length):
        sig.append((sig[-1] * 7 + 3) % 101)
    return sig  # Unused in logic path

# Core processing chain
raw_telemetry = [12, 45, 67, 23, 89, 34]
noise_floor = [5, 5, 5, 5, 5, 5]
adjusted_signal = [a - b for a, b in zip(raw_telemetry, noise_floor)]

# Key encoding phase
key = 17
encoded_segments = encode_signal(adjusted_signal, key)

# Misleading intermediate analysis (red herring)
false_indicators = []
for val in encoded_segments:
    if val > 50:
        false_indicators.append(val ** 0.5)
    elif val < 10:
        false_indicators.append(-val)
    else:
        false_indicators.append(val // 3)

# Simulated system state flags (some relevant, some not)
system_state = {
    'active': True,
    'mode': 'diagnostic',
    'version': 2.1,
    'debug_override': False,
    'legacy_mode': False,
    'threshold': 42
}

# Decoy data structure
cached_results = {
    'hash': 'a1b2c3d4',
    'timestamp': 1678886400,
    'data': [99, 88, 77],
    'valid': False
}

# Phantom transformation chain (dead path)
tmp_buffer = [x * 2 for x in raw_telemetry if x < 70]
rotated = shift_window(tmp_buffer, 2)
checksum = validate_checksum(rotated)  # Computed but unused

# Real processing begins: conditional activation based on state
if system_state['active'] and system_state['mode'] == 'diagnostic':
    base_metric = analyze_pattern(encoded_segments)
    
    # Secondary filtering based on threshold
    filtered_values = [v for v in encoded_segments if v > system_state['threshold']]
    
    # Apply corrective scaling using lambda
    scaler = lambda x, ref: round(x * (ref / 100), 2)
    scaled_diagnostics = [scaler(v, base_metric / len(filtered_values)) for v in filtered_values]
    
    # Tertiary validation via string-based rule (using string method as per requirement)
    rule_code = 'verify_final_42'
    if 'verify_final' in rule_code and rule_code.endswith('42'):
        confirmation_flag = True
    else:
        confirmation_flag = False
    
    # Final aggregation only proceeds if confirmation is valid
    if confirmation_flag:
        adjustment_factor = 1.75
        intermediate_scores = [s * adjustment_factor for s in scaled_diagnostics]
        final_diagnostic = int(sum(intermediate_scores))
    else:
        final_diagnostic = -999
else:
    final_diagnostic = -1

# Print result for evaluation
Result: {final_diagnostic}