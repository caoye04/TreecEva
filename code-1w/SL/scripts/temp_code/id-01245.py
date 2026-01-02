def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    spike_count = len([x for x in filtered if x > threshold])

    # Core computation path (relevant)
    bit_pattern = 0
    for i, sample in enumerate(raw_samples):
        if sample % 7 == 0:
            bit_pattern ^= (sample & 0xF) << (i % 4)

    # Secondary red herring: frequency analysis (unused)
    freq_map = {}
    for s in raw_samples:
        freq_map[s] = freq_map.get(s, 0) + 1
    dominant_freq = max(freq_map.values()) if freq_map else 0

    return bit_pattern


def validate_calibration_sequence(seq):
    # Dead code path — never called
    checksum = 0
    for ch in seq:
        if ch.isalpha():
            checksum += ord(ch.lower()) - ord('a') + 1
    return checksum % 11 == 0


def transform_diagnostic_key(key_str):
    # Distractor using string methods
    reversed_chunks = []
    for i in range(0, len(key_str), 3):
        chunk = key_str[i:i+3]
        reversed_chunks.append(chunk[::-1])
    scrambled = ''.join(reversed_chunks)
    # This function looks important but only returns length
    return len(scrambled) * 2  # Misleading value

# Simulated sensor data stream (real input)
sensor_readings = [
    42, 87, 119, 203, 35, 77, 91, 14, 63, 21
]

# Auxiliary decoy data
decoys = {
    'calibration': 'XK9ZM2P',
    'version': 'v2.7.1-beta',
    'timestamp': '2023-11-05T14:32:11Z'
}

# Multi-step processing chain with distractions
baseline_shift = sum(x for x in sensor_readings if x < 100) // 4
offset_mask = 0
for idx, val in enumerate(sensor_readings):
    if idx % 3 == 0:
        offset_mask += (val >> 3) & 0x7

# Real work begins here — pattern extraction
sequence_state = 1
for reading in sensor_readings:
    if reading > 50:
        sequence_state *= (reading % 13)
        sequence_state %= 997

# Bit manipulation layer
fusion_key = 0
for i, r in enumerate(sensor_readings):
    if r % 2 == 0:
        fusion_key |= (r ^ (i * 7)) & 0xFF

# Decoy transformation chain (looks complex, unused)
temp_hash = transform_diagnostic_key(decoys['calibration'])
shadow_buffer = [transform_diagnostic_key(decoys['version']) for _ in range(3)]

# Critical diagnostic aggregator
processing_chain = [
    lambda x: x ** 2 % 89,
    lambda x: (x + 17) & 0x3F,
    lambda x: x ^ (x >> 4)
]

diagnostics = [
    analyze_signal_integrity(sensor_readings),
    sequence_state,
    fusion_key,
    baseline_shift,
    offset_mask
]

# Final computation — this is where the answer comes from
def aggregate_metrics(pipeline, metrics):
    result = metrics[0]  # Start with signal integrity
    for op in pipeline:
        result = op(result)
    # Additional interference: irrelevant reductions
    total_diagnostics = sum(metrics)
    avg_diag = total_diagnostics / len(metrics)
    capped_avg = min(avg_diag, 200)
    # But we don't use any of that; final output depends only on transformed metrics[0]
    return int(result)

final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
print(f"Result: {final_diagnostic}")