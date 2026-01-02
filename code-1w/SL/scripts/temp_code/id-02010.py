import math

def analyze_signal_integrity(raw_samples, threshold=0.75):
    sample_size = len(raw_samples)
    amplitude_peak = max(raw_samples)
    amplitude_floor = min(raw_samples)
    dynamic_range = amplitude_peak - amplitude_floor

    # Irrelevant signal smoothing (dead path)
    smoothed = [raw_samples[0]]
    for i in range(1, len(raw_samples) - 1):
        smoothed.append((raw_samples[i-1] + raw_samples[i] + raw_samples[i+1]) / 3)
    smoothed.append(raw_samples[-1])

    # Distractor: unused normalization
    normalized = [x / amplitude_peak for x in raw_samples if amplitude_peak != 0]

    valid_count = sum(1 for x in raw_samples if abs(x) > threshold)
    stability_ratio = valid_count / sample_size if sample_size else 0

    return dynamic_range, stability_ratio


def generate_calibration_sequence(seed_offset):
    seq = []
    val = seed_offset
    for i in range(8):
        val = (val * 997 + 11) % 10000
        seq.append(int(val))
    # Decoy transformation
    flipped = [~x & 0xFFFF for x in seq]
    # Unused checksum
    checksum = sum(seq[i] * (i + 1) for i in range(len(seq))) % 65536
    return seq


def decode_timing_frame(frame_data):
    # Simulate parsing a timing frame from embedded system
    binary_str = ''.join(format(b, '08b') for b in frame_data)
    if len(binary_str) < 64:
        binary_str += '0' * (64 - len(binary_str))
    
    # Extract fields (some are red herrings)
    preamble = binary_str[:12]
    timestamp_raw = binary_str[12:36]
    mode_flag = binary_str[36]
    payload_section = binary_str[37:57]
    parity_bits = binary_str[57:]

    timestamp = int(timestamp_raw, 2) % 100000
    mode = 'ACTIVE' if mode_flag == '1' else 'STANDBY'

    # Distractor: simulate legacy compatibility layer
    legacy_map = {i: chr(65 + (i * 7) % 26) for i in range(20)}
    mapped_chars = [legacy_map[i % 20] for i in range(len(payload_section))]
    encoded_tag = ''.join(mapped_chars).lower()

    # Real use: extract bit-weighted score from payload
    weight_sum = 0
    for i, bit in enumerate(payload_section):
        if bit == '1':
            weight_sum += i * (i + 1) // 2  # triangular weighting

    return {
        'timestamp': timestamp,
        'mode': mode,
        'diagnostic_score': weight_sum,
        'tag': encoded_tag
    }


def aggregate_metrics(log_entries, calib_seq):
    base_metric = 0
    adjustment_factor = 0

    # Real logic: analyze calibration sequence using modular arithmetic
    for i, val in enumerate(calib_seq):
        if i % 2 == 0 and val % 3 == 0:
            adjustment_factor += (val % 100) * ((i + 1) ** 0.5)
        elif i % 4 == 3:
            adjustment_factor -= (val % 25)

    # Process log entries
    scores = [entry['diagnostic_score'] for entry in log_entries]
    avg_score = sum(scores) / len(scores) if scores else 0
    peak_score = max(scores) if scores else 0

    # Distractor: string-based version analysis (unused)
    versions = [str(entry['timestamp']) for entry in log_entries]
    version_concat = ''.join(versions)
    unique_digits = len(set(version_concat))
    digit_entropy = sum(version_concat.count(d) * math.log2(len(version_concat) / version_concat.count(d)) for d in set(version_concat)) if version_concat else 0

    # Conditional expression used meaningfully
    scaling_mode = 'AGGRESSIVE' if peak_score > 150 else 'STANDARD'
    multiplier = 2.5 if scaling_mode == 'AGGRESSIVE' else 1.8

    # Tuple unpacking with relevant and irrelevant elements
    (primary, secondary), _ = (scores[:2], scores[2:]) if len(scores) >= 2 else ((0, 0), []), None

    # Core computation
    base_metric = avg_score * 3.7 + primary * 1.3 - secondary * 0.4

    # Final combination
    final_adjusted = base_metric * multiplier + adjustment_factor

    # Key result variable
    final_diagnostic = int(round(final_adjusted))

    # Dead code: simulated logging export
    debug_lines = []
    for entry in log_entries:
        tag_upper = entry['tag'].upper()
        formatted = f"[{entry['timestamp']}] MODE:{entry['mode']} SCORE={entry['diagnostic_score']}"
        if 'X' in tag_upper:
            formatted += " [FLAG]"
        debug_lines.append(formatted.replace(' ', '_'))

    return final_diagnostic

# Main execution
if __name__ == "__main__":
    # Simulated raw signal data (irrelevant to final answer but part of setup)
    signal_data = [0.1, 0.82, 0.63, 0.91, 0.77, 0.54, 0.21, 0.99, 0.45, 0.88]
    _, signal_confidence = analyze_signal_integrity(signal_data, threshold=0.65)

    # Generate real calibration sequence
    calibration_sequence = generate_calibration_sequence(seed_offset=1234)

    # Build timing log (this affects the real answer)
    timing_frames = [
        [0x1A, 0x2B, 0x3C, 0x4D, 0x5E],
        [0x1F, 0x2E, 0x3D, 0x4C, 0x5B],
        [0x1C, 0x2D, 0x3E, 0x4F, 0x5A],
        [0x1B, 0x2C, 0x3D, 0x4E, 0x5F]
    ]
    timing_log = [decode_timing_frame(frame) for frame in timing_frames]

    # Critical statement
    final_diagnostic = aggregate_metrics(timing_log, calibration_sequence)

    print(f"Result: {final_diagnostic}")