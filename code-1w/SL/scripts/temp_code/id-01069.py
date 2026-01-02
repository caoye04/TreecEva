def preprocess_signal(raw_data, threshold=0.5):
    """Filter and normalize signal data (distractor function)"""
    filtered = [x for x in raw_data if abs(x) > threshold]
    total = sum(filtered)
    normalized = [x / total for x in filtered] if total != 0 else []
    return normalized


def encrypt_sequence(seq, key):
    """Apply XOR encryption on sequence with key (red herring)"""
    return [s ^ (key % 256) for s in seq]


def collect_diagnostics(signal_set, mode='full'):
    """Simulate diagnostic collection with irrelevant branching"""
    diagnostics = set()
    temp_log = []
    
    for i in range(len(signal_set)):
        val = signal_set[i]
        if val % 3 == 0:
            diagnostics.add(val * 2)
        elif val % 5 == 0:
            diagnostics.add(val + 10)
        else:
            temp_log.append(val)  # unused
    
    # Dead code path - never executed due to prior logic
    if mode == 'debug_extended':
        for item in temp_log:
            diagnostics.add(item * -1)
    
    return sorted(diagnostics)


def shift_window(data, offset):
    """Rotate list elements (irrelevant transformation)"""
    if not data:
        return data
    offset = offset % len(data)
    return data[offset:] + data[:offset]


def decode_rhythm(pattern):
    """Map rhythm pattern to numeric signature (decoy logic)"""
    rhythm_map = {'S': 1, 'M': 3, 'L': 7}
    return [rhythm_map.get(p, 0) for p in pattern]


def analyze_pattern(signals, key):
    """Core analysis: compute entropy-like metric using bit operations and set differences"""
    # Step 1: Extract high-energy components
    high_energy = {x for x in signals if x > 15}
    
    # Step 2: Generate reference band based on key
    reference_band = {key ^ (i * 7) for i in range(1, 6)}  # e.g., derived from key
    
    # Step 3: Compute overlap and divergence
    common_elements = high_energy & reference_band
    divergent_peaks = high_energy - reference_band
    missing_in_ref = reference_band - high_energy
    
    # Step 4: Bit manipulation chain on aggregated metrics
    base_score = len(common_elements) * 13
    penalty = len(divergent_peaks) * 5
    bonus = len(missing_in_ref) % 4  # minor adjustment
    
    # Step 5: Apply bit shifts and masking
    adjusted = (base_score << 2) - (penalty << 1)
    adjusted = adjusted ^ 0xAA  # XOR mask
    adjusted = (adjusted & 0xFFFF)  # 16-bit truncation
    
    # Step 6: Final adjustment via recursive digit sum (core calculation)
    def digit_sum(n):
        return n if n < 10 else digit_sum(sum(int(d) for d in str(n)))
    
    checksum = digit_sum(adjusted)
    final_value = adjusted + checksum
    
    return final_value

# --- Main Execution with Distractors ---

# Simulated sensor inputs (real input)
sensor_stream = [8, 12, 16, 21, 25, 30, 33, 42]

# Irrelevant preprocessing chains
normalized_stream = preprocess_signal([x * 0.1 for x in sensor_stream])
encrypted_stream = encrypt_sequence([int(x*10) for x in normalized_stream], key=42)

# Signal window shifting (dead-end path)
current_window = shift_window(sensor_stream, offset=3)

# Rhythm decoding with fake pattern (red herring)
rhythm_code = decode_rhythm(['S', 'M', 'L', 'M'])

# Core data collection (used)
collected_signals = collect_diagnostics(sensor_stream)

# Decoy system state variables
system_status = 'STANDBY'
system_status = 'ACTIVE' if sum(collected_signals) > 100 else 'IDLE'
log_entry = f'Status: {system_status}, Signals: {len(collected_signals)}'

# Key derivation with misleading alternate paths
alt_key_source = [3, 6, 9]
primary_key_seed = sum(alt_key_source)  # equals 18
system_key = primary_key_seed * 5  # 90

# Unused alternate key computation (distraction)
temp_key = 0
for i, v in enumerate(alt_key_source):
    temp_key += v << i

# Critical statement
final_diagnostic = analyze_pattern(collected_signals, system_key)

# Print result as required
print(f"Target result: {final_diagnostic}")