import itertools

# Simulated sensor data processing with noise filtering and mode detection
def analyze_signal_strength(signal):
    magnitude = sum(abs(x) for x in signal)
    average = magnitude / len(signal)
    normalized = [x / (average + 1e-5) for x in signal]
    return [round(x, 3) for x in normalized]

# Legacy function - not used but looks relevant
def calculate_envelope_v1(data):
    envelope = []
    for i in range(len(data)):
        temp_val = (data[i] + data[(i+1)%len(data)]) / 2
        envelope.append(temp_val * 0.9)
    return envelope

# Core transformation: applies threshold logic and counts valid transitions
def count_active_transitions(seq, threshold=0.75):
    if not seq:
        return 0
    count = 0
    for i in range(1, len(seq)):
        if seq[i-1] < threshold <= seq[i]:
            count += 1
    return count

# Data segmentation based on dynamic breakpoints
def split_into_segments(raw, breaks):
    segments = []
    prev = 0
    for b in breaks:
        segments.append(raw[prev:b])
        prev = b
    segments.append(raw[prev:])
    return segments

# Flag analysis - determines processing mode
def evaluate_flags(flag_set):
    mode_bits = 0
    for f in flag_set:
        if f == 'CALIBRATE':
            mode_bits |= 1
        elif f == 'FILTER_NOISE':
            mode_bits |= 2
        elif f == 'ADAPTIVE_GAIN':
            mode_bits |= 4
    return mode_bits

# Main processing pipeline
def process_segments(segments, control_flags):
    mode = evaluate_flags(control_flags)
    results = []

    # Unused intermediate that looks important
    baseline_metrics = {f'segment_{i}': {
        'peak': max(seg) if seg else 0,
        'trough': min(seg) if seg else 0,
        'range': max(seg) - min(seg) if seg else 0
    } for i, seg in enumerate(segments)}

    # Distractor: complex-looking but unused calculation
    spectral_weight = 0.0
    for idx, seg in enumerate(segments):
        weighted_sum = sum((i + 1) * val for i, val in enumerate(seg))
        normalization_factor = sum(i + 1 for i in range(len(seg))) if seg else 1
        segment_spectral = weighted_sum / (normalization_factor + 1e-6)
        spectral_weight += segment_spectral * (idx + 1)

    # Actual relevant logic starts here
    transition_counts = []
    for segment in segments:
        analyzed = analyze_signal_strength(segment)
        transitions = count_active_transitions(analyzed)
        transition_counts.append(transitions)

    # Combine using mode-specific logic
    if mode & 1:
        base_result = sum(transition_counts)
    elif mode & 2:
        base_result = max(transition_counts) * len(transition_counts)
    else:
        base_result = min(transition_counts) + len([t for t in transition_counts if t > 1])

    # Final adjustment using set operations (required feature)
    indices_set = set(range(len(segments)))
    even_indices = {i for i in indices_set if i % 2 == 0}
    odd_indices = indices_set - even_indices
    parity_correction = len(even_indices.intersection(set(range(0, len(transition_counts), 3))))

    final_adjustment = base_result + parity_correction

    # Red herring: another unused path
    if mode > 4:
        backup = 0
        for a, b in itertools.pairwise(transition_counts):
            backup += abs(a - b)
        final_adjustment -= backup  # never reached due to flag configuration

    return final_adjustment

# Simulated input data
raw_signal_data = [
    0.12, -0.35, 0.88, 1.02, -0.15, 0.03, 0.91, -0.77, 0.44, 0.63,
    -0.21, 0.55, 0.89, -0.67, 0.33, 0.71, -0.50, 0.29, 0.94, -0.08
]

segment_breakpoints = [5, 12, 17]
flag_options = ['FILTER_NOISE', 'ADAPTIVE_GAIN']  # No CALIBRATE, so mode = 6

# Split data into segments
segment_data = split_into_segments(raw_signal_data, segment_breakpoints)

# Execute main logic
final_output = process_segments(segment_data, flag_options)
print(f"Result: {final_output}")