def analyze_signal(raw_data, threshold=0.7):
    normalized = [x / max(raw_data) for x in raw_data]
    spikes = [i for i, x in enumerate(normalized) if x > threshold]
    return spikes


def generate_checksum(sequence):
    checksum = 0
    for val in sequence:
        checksum ^= val  # Bitwise XOR across values
    return checksum % 100


def encode_pattern(labels):
    encoded = []
    for label in labels:
        if isinstance(label, str):
            shifted = ''.join(chr(ord(c) + 1) for c in label.lower())
            encoded.append(shifted)
        else:
            encoded.append(str(label))
    return '_'.join(encoded)


def validate_frame(frame_data):
    if not frame_data:
        return False
    total = sum(frame_data)
    parity = bin(total).count('1')
    return parity % 2 == 0


def transform_sequence(seq):
    """
    Applies modular arithmetic and bit shifting to obscure logic path.
    """
    temp_a = [(x * 3 + 7) % 64 for x in seq]  # Affine transformation
    temp_b = [x << 1 for x in temp_a if x & 1]   # Left shift only odd values
    temp_c = [x ^ 15 for x in temp_a[:len(temp_b)]]  # XOR with padding control
    return temp_c


def extract_features(data_stream):
    features = {}
    features['length'] = len(data_stream)
    features['peak'] = max(data_stream)
    features['entropy'] = sum(x > (features['peak'] * 0.5) for x in data_stream)
    features['baseline'] = sum(1 for x in data_stream if x < 10)  # Low-value count
    return features


def aggregate_metrics(seq, config_flags):
    """
    Core computation that produces the answer.
    """
    a = sum(seq)  # Direct contributor
    b = len(seq) ** 2
    c = a * b // (1 if b != 0 else 1)
    d = c & 0xFFFF  # Apply 16-bit mask
    e = d ^ (d >> 4)  # Bit diffusion
    f = e + (e & 0x0F)  # Add lower nibble
    g = f * config_flags[0]  # Scale by first flag
    h = g - config_flags[2]  # Subtract third flag
    final_value = h  # Final result
    return final_value

# --- Main Execution with High Interference ---

# Simulated sensor readings (real input)
primary_readings = [12, 18, 25, 30, 14, 22, 36, 40, 19, 27]

# Irrelevant auxiliary datasets (distraction)
satellite_metadata = ['SAT_X7', 'ORBIT_4B', 'CALIB_NIL']
telemetry_logs = [
    {'time': '12:01', 'status': 'OK', 'power': 98},
    {'time': '12:02', 'status': 'OK', 'power': 99}
]

# Signal processing pipeline
spike_indices = analyze_signal(primary_readings, threshold=0.6)

# Distractor: unused transformation path
buffer_snapshot = [x * 2 for x in primary_readings if x % 3 == 0]
encoded_labels = encode_pattern(satellite_metadata)  # String manipulation red herring

# Feature extraction (partially relevant)
features = extract_features(primary_readings)

# Transform sequence using modular/bit logic (critical path)
tuned_sequence = transform_sequence(primary_readings)

# Checksum validation (looks important but not used in final calc)
frame_valid = validate_frame(tuned_sequence)
checksum_value = generate_checksum(tuned_sequence)

# Configuration flags (only some are used)
flags = [3, 7, 42, 101, 5]  # 3 and 42 are used; others are decoys

# Dead code path (misleading)
if len(tuned_sequence) > 10:
    adjusted = [x + 5 for x in tuned_sequence]
elif checksum_value > 50:
    adjusted = [x - 1 for x in tuned_sequence]
else:
    pass  # No assignment — dead end

# Critical statement: this computes the answer
final_diagnostic = aggregate_metrics(tuned_sequence, flags)

# Output result as required
print(f"Target result: {final_diagnostic}")